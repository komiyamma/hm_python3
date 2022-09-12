#-------------------- coding: utf-8 ---------------------------
# hmPython3 2.0.1.1用 ライブラリ
# Copyright (c) 2017-2022 Akitsugu Komiyama
# under the Apache License Version 2.0
#--------------------------------------------------------------

import hidemaru
import os
import random

__version__ = hidemaru.__version__

class _TText:
    class _TEncoding:

        def __init__(self, name, codepage, hm_encode):
            self.name = name  # Pythonでファイルを開く際にエンコードとして指定できる文字列( "cp932" や "utf8" など )
            self.codepage = codepage  # マイクロソフトコードページの番号が入っている (932 や 65001 など)
            self.hm_encode = hm_encode      # 秀丸の encode としての値が入っている ( 1 や 6 など )

class _TFile:
    """
    秀丸でファイル関連のクラス
    """

    class _TStreamReader:

        def __init__(self, filepath, hm_encode=-1):
            try:
                if not os.path.exists(filepath):
                    raise FileNotFoundError

                if hm_encode == -1:
                    encoding_name, codepage, hm_encode = hidemaru.file.get_encodingfromfile(filepath)
                else:
                    encoding_name, codepage, hm_encode = hidemaru.file.get_encodingfromhmencode(hm_encode)
                self.__encoding = _TText._TEncoding(encoding_name, codepage, hm_encode)
                self.__filepath = filepath
            except:
                raise

        def __enter__(self):
            return self

        def __GetEncoding(self):
            return self.__encoding

        # 開いたファイルのエンコーディング情報の取得
        Encoding = property(__GetEncoding)


        def __GetFilePath(self):
            return self.__filepath

        # ファイルパス
        FilePath = property(__GetFilePath)

        # 開いたファイルのテキストの取得
        def Read(self):
            try:
                if self.__filepath:
                    success, text = hidemaru.file.get_readalltext(self.__filepath, self.__encoding.hm_encode)
                    if success:
                        return text
                    else:
                        raise IOError
            except:
                raise

        def Close(self):
            self.__encoding = None
            self.__filepath = None

        def __exit__(self, exception_type, exception_value, traceback):
            self.Close()

    # ファイルを開く。
    def Open(self, filepath, hm_encode=-1):
        return _TFile._TStreamReader(filepath, hm_encode)

    # 対象のファイルの encode (秀丸マクロの encode 変数の表を参照) を得る。
    def GetEncoding(self, filepath):
        try:
            if not os.path.exists(filepath):
                raise FileNotFoundError

            encoding_name, codepage, hm_encode = hidemaru.file.get_encodingfromfile(filepath)
            return _TText._TEncoding(encoding_name, codepage, hm_encode)
        except:
            raise


class _TEdit:
    """
    秀丸で編集中のドキュメント関連のクラス
    """

    def __GetFilePath(self):
        filepath = hidemaru.edit.get_filepath()
        if not filepath:
            return None
        else:
            return filepath

    # 編集中のファイルのパスを返す。ファイル名が決まってなければNoneを返す。
    FilePath = property(__GetFilePath)

    #--------------------------------------------------
    def __GetTotalText(self):
        return hidemaru.edit.get_totaltext()

    def __SetTotalText(self, text):
        return hidemaru.edit.set_totaltext(text)

    # 編集中のテキスト全体
    TotalText = property(__GetTotalText, __SetTotalText)
    #--------------------------------------------------

    #--------------------------------------------------
    def __GetSelectedText(self):
        return hidemaru.edit.get_selectedtext()

    def __SetSelectedText(self, text):
        return hidemaru.edit.set_selectedtext(text)

    # 選択中のテキスト。通常選択もしくは行選択のみ（矩形選択は対象としない）
    SelectedText = property(__GetSelectedText, __SetSelectedText)
    #--------------------------------------------------

    #--------------------------------------------------
    def __GetLineText(self):
        return hidemaru.edit.get_linetext()

    def __SetLineText(self, text):
        return hidemaru.edit.set_linetext(text)

    # カーソルがある行のテキスト
    LineText = property(__GetLineText, __SetLineText)
    #--------------------------------------------------

    #--------------------------------------------------
    class _TCursorPos:

        def __init__(self, lineno, column):
            self.lineno = lineno
            self.column = column

    def __GetCursorPos(self):
        lineno, column = hidemaru.edit.get_cursorpos()
        return _TEdit._TCursorPos(lineno, column)

    # カーソルの位置情報。linenoとcolumn（マクロのlinenoとcolumnと同じ値）
    CursorPos = property(__GetCursorPos)
    #--------------------------------------------------

    #--------------------------------------------------
    class _TMousePos:

        def __init__(self, lineno, column, x, y):
            self.lineno = lineno
            self.column = column
            self.x = x
            self.y = y

    def __GetMousePos(self):
        lineno, column, x, y = hidemaru.edit.get_mousepos()
        return _TEdit._TMousePos(lineno, column, x, y)

    # マウスの位置に対応するカーソルの情報。
    # linenoとcolumn（マクロのlinenoとcolumnと同じ値） xとyは、win32 apiのマウス位置情報と同じ
    MousePos = property(__GetMousePos)
    #--------------------------------------------------


class _TMacro:
    """
    秀丸マクロ関連のクラス
    """
    class _TAsStatement:
        """
        秀丸マクロ関連のうち、括弧がなく値が変えられない秀丸組み込みの(関数のように使う)文のラップを表すクラス
        """
        def __getattr__(self, statement_name):
            return lambda *args: self.closure(statement_name, *args)

        def __call__(self, statement_name, *args):
            return self.closure(statement_name, *args)

        def closure(self, statement_name, *args):
            value_list = []
            type_list = []
            for arg in args:
                if type(arg) is int or type(arg) is bool or type(arg) is float:
                    value_list.append(int(arg))
                    type_list.append('int')
                elif type(arg) is list or type(arg) is tuple:
                    if all(type(e) is str for e in arg):
                        value_list.append(tuple(arg))
                        type_list.append('array_str')
                    elif all((type(e) is int or type(e) is float or type(e) is bool) for e in arg):
                        modify_list = [int(e) for e in arg]
                        value_list.append(tuple(modify_list))
                        type_list.append('array_int')

                else:
                    value_list.append(str(arg))
                    type_list.append('str')

            res, msg, errmsg, args = hidemaru.macro.do_statement(statement_name, tuple(value_list), tuple(type_list))
            ret = _TMacro._TStatementResult(res, msg, errmsg, args)

            return ret

    class _TAsFunction:
        """
        秀丸マクロ関連のうち、括弧があり値が返る秀丸組み込みの関数のラップを表すクラス
        """
        def __getattr__(self, function_name):
            return lambda *args: self.closure(function_name, *args)

        def __call__(self, statement_name, *args):
            return self.closure(statement_name, *args)

        def closure(self, function_name, *args):
            value_list = []
            type_list = []
            for arg in args:
                if type(arg) is int or type(arg) is bool or type(arg) is float:
                    value_list.append(int(arg))
                    type_list.append('int')
                else:
                    value_list.append(str(arg))
                    type_list.append('str')

            res, msg, errmsg, args = hidemaru.macro.do_function(function_name, tuple(value_list), tuple(type_list))
            ret = _TMacro._TFunctionResult(res, msg, errmsg, args)

            return ret

    #--------------------------------------------------
    class _TVar:
        """
        秀丸マクロ関連のうち、マクロシンボル（マクロ変数）を扱うクラス
        """

        def __getitem__(self, varname):
            return hidemaru.macro.get_var(varname)

        def __setitem__(self, varname, value):
            if not varname.startswith("#") and not varname.startswith("$"):
                hidemaru.debug_info("指定のマクロ変数への値の代入は出来ません: " + varname)
                hidemaru.macro.set_var(varname, value)
                raise NameError(varname)
            else:
                return hidemaru.macro.set_var(varname, value)

        def __getattr__(self, varname):
            return hidemaru.macro.get_var(varname)

    #--------------------------------------------------

    #--------------------------------------------------
    class _TResult:
        """
        秀丸マクロ関連のうち、マクロ実行結果情報を扱うクラス
        """

        def __init__(self, Result, Message, ErrorMsg):
            self.Result = Result
            self.Message = Message
            if Result >= 1:
                self.Error = None
            else:
                self.Error = RuntimeError(ErrorMsg)
    #--------------------------------------------------
    class _TStatementResult:
        """
        秀丸マクロ関連のうち、マクロ実行結果情報を扱うクラス
        """

        def __init__(self, Result, Message, ErrorMsg, Args):
            self.Result = Result
            self.Message = Message
            self.Args = tuple(Args)
            if ErrorMsg == "":
                self.Error = None
            else:
                self.Error = RuntimeError(ErrorMsg)
    #--------------------------------------------------
    class _TFunctionResult:
        """
        秀丸マクロ関連のうち、マクロ実行結果情報を扱うクラス
        """

        def __init__(self, Result, Message, ErrorMsg, Args):
            self.Result = Result
            self.Message = Message
            self.Args = tuple(Args)
            if Result != None:
                self.Error = None
            else:
                self.Error = RuntimeError(ErrorMsg)

    #--------------------------------------------------
    def __init__(self):
        self.Var = _TMacro._TVar()
        self.Function = _TMacro._TAsFunction();
        self.Statement = _TMacro._TAsStatement();
    #--------------------------------------------------

    #--------------------------------------------------
    # マクロの実行
    def Eval(self, expression_text):
        res, msg, errmsg = hidemaru.macro.do_eval(expression_text)
        ret = _TMacro._TResult(res, msg, errmsg)
        return ret
    #--------------------------------------------------



class _TOutputPane:
    """
    秀丸アウトプットペイン関連のクラス
    """
    # アウトプット枠への出力
    def Output(self, obj):
        return hidemaru.outputpane.output(obj)

    # アウトプット枠情報の一時退避
    def Push(self):
        return hidemaru.outputpane.push()

    # アウトプット枠情報の一時退避したものを復元
    def Push(self):
        return hidemaru.outputpane.pop()

    # アウトプット枠のクリア
    def Clear(self):
        return hidemaru.outputpane.clear()

    # アウトプット枠にメッセージを送る
    def SendMessage(self, command_id):
        return hidemaru.outputpane.sendmessage(command_id)

    # アウトプット枠の基底ディレクトリを設定する
    def SetBaseDir(self, dirpath):
        return hidemaru.outputpane.setbasedir(dirpath)


class _TExplorerPane:
    """
    秀丸ファイルマネージャペイン関連のクラス
    """
    # ファイルマネージャ枠のモードの設定
    def SetMode(self, mode):
        return hidemaru.explorerpane.setmode(mode)

    # ファイルマネージャ枠のモードの取得
    def GetMode(self):
        return hidemaru.explorerpane.getmode()

    # ファイルマネージャ枠に指定のファイルのプロジェクトを読み込む
    def LoadProject(self, filepath):
        return hidemaru.explorerpane.loadproject(filepath)

    # ファイルマネージャ枠のプロジェクトを指定ファイルに保存
    def SaveProject(self, filepath):
        return hidemaru.explorerpane.saveproject(filepath)

    # ファイルマネージャ枠が「プロジェクト」表示のとき、更新された状態であるかどうかを返します
    def GetUpdated(self):
        return hidemaru.explorerpane.getupdated()

    # ファイルマネージャ枠にメッセージを送る
    def SendMessage(self, command_id):
        return hidemaru.explorerpane.sendmessage(command_id)

    # ファイルマネージャ枠にプロジェクトを読み込んでいるならば、そのファイルパスを取得する(読み込んでいなければNoneが返る)
    def GetProject(self):
        filepath = hidemaru.explorerpane.getproject()
        if not filepath:
            return None
        else:
            return filepath

    # ファイルマネージャ枠のカレントディレクトリを返す
    def GetCurrentDir(self):
        dirpath = hidemaru.explorerpane.getcurrentdir()
        if not dirpath:
            return None
        else:
            return dirpath


class _THidemaru:
    """
    特定のカテゴリに所属しないようなもの
    """
    #--------------------------------------------------
    def __init__(self):
        self.File = _TFile()
        self.Edit = _TEdit()
        self.Macro = _TMacro()
        self.OutputPane = _TOutputPane()
        self.ExplorerPane = _TExplorerPane()
    #--------------------------------------------------

    #--------------------------------------------------
    # デバッグモニターに出力
    def debuginfo(self, obj):
        return hidemaru.debug_info(obj)
    #--------------------------------------------------

    #--------------------------------------------------
    def __GetVersion(self):
        return hidemaru.get_version()

    # 秀丸のバージョンを 866.05 のような形で取得。
    # 「β5」なら少数部分が「05」のような形。
    # 正式版だと、866.99 のように「99」となる。
    version = property(__GetVersion)
    #--------------------------------------------------


hm = _THidemaru()


# 非公開
def _method_proxy(name, t, *args):
    if t == "fn" or t == "fs":
        count = len(args)
        if (count == 0):
            return hm.Macro.Var[name]
        elif (count > 0):
            return hm.Macro.Function(name, *args).Result
    elif t == "fsn":
        count = len(args)
        if (count == 0):
            return hm.Macro.Var[name]
        elif (count > 0):
            return hm.Macro.Function(name, *args).Result
    elif t=="fn1s":
        list_args = list(args)
        if len(list_args) >= 1:
            list_args[0] = str(args[0])
        return hm.Macro.Function(name, *list_args).Result
    elif t=="fn1s2s":
        list_args = list(args)
        if len(list_args) >= 1:
            list_args[0] = str(args[0])
        if len(list_args) >= 2:
            list_args[1] = str(args[1])
        return hm.Macro.Function(name, *list_args).Result
    elif t=="st":
        return hm.Macro.Statement(name, *args).Result
    elif t=="st1s":
        list_args = list(args)
        if len(list_args) >= 1:
            list_args[0] = str(args[0])
        return hm.Macro.Statement(name, *list_args).Result
    elif t=="st1s2s":
        list_args = list(args)
        if len(list_args) >= 1:
            list_args[0] = str(args[0])
        if len(list_args) >= 2:
            list_args[1] = str(args[1])
        return hm.Macro.Statement(name, *list_args).Result

def result(*args): return _method_proxy("result", "fn", *args);
def version(*args): return _method_proxy("version", "fn", *args);
def platform(*args): return _method_proxy("platform", "fn", *args);
def darkmode(*args): return _method_proxy("darkmode", "fn", *args);
def x(*args): return _method_proxy("x", "fn", *args);
def y(*args): return _method_proxy("y", "fn", *args);
def column(*args): return _method_proxy("column", "fn", *args);
def column_wcs(*args): return _method_proxy("column_wcs", "fn", *args);
def column_ucs4(*args): return _method_proxy("column_ucs4", "fn", *args);
def column_cmu(*args): return _method_proxy("column_cmu", "fn", *args);
def column_gcu(*args): return _method_proxy("column_gcu", "fn", *args);
def lineno(*args): return _method_proxy("lineno", "fn", *args);
def tabcolumn(*args): return _method_proxy("tabcolumn", "fn", *args);
def xview(*args): return _method_proxy("xview", "fn", *args);
def code(*args): return _method_proxy("code", "fn", *args);
def unicode(*args): return _method_proxy("unicode", "fn", *args);
def colorcode(*args): return _method_proxy("colorcode", "fn", *args);
def marked(*args): return _method_proxy("marked", "fn", *args);
def lineupdated(*args): return _method_proxy("lineupdated", "fn", *args);
def xpixel(*args): return _method_proxy("xpixel", "fn", *args);
def ypixel(*args): return _method_proxy("ypixel", "fn", *args);
def prevposx(*args): return _method_proxy("prevposx", "fn", *args);
def prevposy(*args): return _method_proxy("prevposy", "fn", *args);
def lastupdatedx(*args): return _method_proxy("lastupdatedx", "fn", *args);
def lastupdatedy(*args): return _method_proxy("lastupdatedy", "fn", *args);
def mousecolumn(*args): return _method_proxy("mousecolumn", "fn", *args);
def mouselineno(*args): return _method_proxy("mouselineno", "fn", *args);
def linecount(*args): return _method_proxy("linecount", "fn", *args);
def linecount2(*args): return _method_proxy("linecount2", "fn", *args);
def linelen(*args): return _method_proxy("linelen", "fn", *args);
def linelen2(*args): return _method_proxy("linelen2", "fn", *args);
def linelen_wcs(*args): return _method_proxy("linelen_wcs", "fn", *args);
def linelen_ucs4(*args): return _method_proxy("linelen_ucs4", "fn", *args);
def linelen_cmu(*args): return _method_proxy("linelen_cmu", "fn", *args);
def linelen_gcu(*args): return _method_proxy("linelen_gcu", "fn", *args);
def tabcolumnmax(*args): return _method_proxy("tabcolumnmax", "fn", *args);
def selecting(*args): return _method_proxy("selecting", "fn", *args);
def rectselecting(*args): return _method_proxy("rectselecting", "fn", *args);
def lineselecting(*args): return _method_proxy("lineselecting", "fn", *args);
def selectionlock(*args): return _method_proxy("selectionlock", "fn", *args);
def mouseselecting(*args): return _method_proxy("mouseselecting", "fn", *args);
def multiselecting(*args): return _method_proxy("multiselecting", "fn", *args);
def multiselectcount(*args): return _method_proxy("multiselectcount", "fn", *args);
def inselecting(*args): return _method_proxy("inselecting", "fn", *args);
def seltopx(*args): return _method_proxy("seltopx", "fn", *args);
def seltopy(*args): return _method_proxy("seltopy", "fn", *args);
def selendx(*args): return _method_proxy("selendx", "fn", *args);
def selendy(*args): return _method_proxy("selendy", "fn", *args);
def seltopcolumn(*args): return _method_proxy("seltopcolumn", "fn", *args);
def seltoplineno(*args): return _method_proxy("seltoplineno", "fn", *args);
def selendcolumn(*args): return _method_proxy("selendcolumn", "fn", *args);
def selendlineno(*args): return _method_proxy("selendlineno", "fn", *args);
def seltop_wcs(*args): return _method_proxy("seltop_wcs", "fn", *args);
def seltop_ucs4(*args): return _method_proxy("seltop_ucs4", "fn", *args);
def seltop_cmu(*args): return _method_proxy("seltop_cmu", "fn", *args);
def seltop_gcu(*args): return _method_proxy("seltop_gcu", "fn", *args);
def selend_wcs(*args): return _method_proxy("selend_wcs", "fn", *args);
def selend_ucs4(*args): return _method_proxy("selend_ucs4", "fn", *args);
def selend_cmu(*args): return _method_proxy("selend_cmu", "fn", *args);
def selend_gcu(*args): return _method_proxy("selend_gcu", "fn", *args);
def selopenx(*args): return _method_proxy("selopenx", "fn", *args);
def selopeny(*args): return _method_proxy("selopeny", "fn", *args);
def windowwidth(*args): return _method_proxy("windowwidth", "fn", *args);
def windowheight(*args): return _method_proxy("windowheight", "fn", *args);
def windowcx(*args): return _method_proxy("windowcx", "fn", *args);
def windowcy(*args): return _method_proxy("windowcy", "fn", *args);
def windowposx(*args): return _method_proxy("windowposx", "fn", *args);
def windowposy(*args): return _method_proxy("windowposy", "fn", *args);
def splitstate(*args): return _method_proxy("splitstate", "fn", *args);
def splitmode(*args): return _method_proxy("splitmode", "fn", *args);
def splitpos(*args): return _method_proxy("splitpos", "fn", *args);
def windowstate(*args): return _method_proxy("windowstate", "fn", *args);
def windowstate2(*args): return _method_proxy("windowstate2", "fn", *args);
def cxscreen(*args): return _method_proxy("cxscreen", "fn", *args);
def cyscreen(*args): return _method_proxy("cyscreen", "fn", *args);
def xworkarea(*args): return _method_proxy("xworkarea", "fn", *args);
def yworkarea(*args): return _method_proxy("yworkarea", "fn", *args);
def cxworkarea(*args): return _method_proxy("cxworkarea", "fn", *args);
def cyworkarea(*args): return _method_proxy("cyworkarea", "fn", *args);
def monitor(*args): return _method_proxy("monitor", "fn", *args);
def monitorcount(*args): return _method_proxy("monitorcount", "fn", *args);
def tabmode(*args): return _method_proxy("tabmode", "fn", *args);
def tabgroup(*args): return _method_proxy("tabgroup", "fn", *args);
def tabgrouporder(*args): return _method_proxy("tabgrouporder", "fn", *args);
def taborder(*args): return _method_proxy("taborder", "fn", *args);
def tabtotal(*args): return _method_proxy("tabtotal", "fn", *args);
def tabgrouptotal(*args): return _method_proxy("tabgrouptotal", "fn", *args);
def screentopy(*args): return _method_proxy("screentopy", "fn", *args);
def screenleftx(*args): return _method_proxy("screenleftx", "fn", *args);
def compfilehandle(*args): return _method_proxy("compfilehandle", "fn", *args);
def scrolllinkhandle(*args): return _method_proxy("scrolllinkhandle", "fn", *args);
def filehistcount(*args): return _method_proxy("filehistcount", "fn", *args);
# 分岐あり
def overwrite(*args):
    if len(args)==0:
        return _method_proxy("overwrite", "fn", *args)
    else:
        return _method_proxy("overwrite", "st1s", *args)

def updated(*args): return _method_proxy("updated", "fn", *args);
def updatecount(*args): return _method_proxy("updatecount", "fn", *args);
def anyclipboard(*args): return _method_proxy("anyclipboard", "fn", *args);
def imestate(*args): return _method_proxy("imestate", "fn", *args);
def browsemode(*args): return _method_proxy("browsemode", "fn", *args);
def keypressed(*args): return _method_proxy("keypressed", "fn", *args);
def replay(*args): return _method_proxy("replay", "fn", *args);
def searchmode(*args): return _method_proxy("searchmode", "fn", *args);
def searchoption(*args): return _method_proxy("searchoption", "fn", *args);
def searchoption2(*args): return _method_proxy("searchoption2", "fn", *args);
def foundtopx(*args): return _method_proxy("foundtopx", "fn", *args);
def foundtopy(*args): return _method_proxy("foundtopy", "fn", *args);
def foundendx(*args): return _method_proxy("foundendx", "fn", *args);
def foundendy(*args): return _method_proxy("foundendy", "fn", *args);
def foundhilighting(*args): return _method_proxy("foundhilighting", "fn", *args);
def foundoption(*args): return _method_proxy("foundoption", "fn", *args);
def readonly(*args): return _method_proxy("readonly", "fn", *args);
def encode(*args): return _method_proxy("encode", "fn", *args);
def charset(*args): return _method_proxy("charset", "fn", *args);
def bom(*args): return _method_proxy("bom", "fn", *args);
def codepage(*args): return _method_proxy("codepage", "fn", *args);
def getfocus(*args): return _method_proxy("getfocus", "fn", *args);
def autocompstate(*args): return _method_proxy("autocompstate", "fn", *args);
def argcount(*args): return _method_proxy("argcount", "fn", *args);
def compatiblemode(*args): return _method_proxy("compatiblemode", "fn", *args);
def carettabmode(*args): return _method_proxy("carettabmode", "fn", *args);
def return_in_cell_mode(*args): return _method_proxy("return_in_cell_mode", "fn", *args);
def stophistory(*args): return _method_proxy("stophistory", "fn", *args);
def fontmode(*args): return _method_proxy("fontmode", "fn", *args);
def formline(*args): return _method_proxy("formline", "fn", *args);
def configstate(*args): return _method_proxy("configstate", "fn", *args);
def fontsize(*args): return _method_proxy("fontsize", "fn", *args);
def dayofweeknum(*args): return _method_proxy("dayofweeknum", "fn", *args);
def tickcount(*args): return _method_proxy("tickcount", "fn", *args);
def foldable(*args): return _method_proxy("foldable", "fn", *args);
def folded(*args): return _method_proxy("folded", "fn", *args);
def rangeedittop(*args): return _method_proxy("rangeedittop", "fn", *args);
def rangeeditend(*args): return _method_proxy("rangeeditend", "fn", *args);
def rangeeditmode(*args): return _method_proxy("rangeeditmode", "fn", *args);
def outlinehandle(*args): return _method_proxy("outlinehandle", "fn", *args);
def outlinesize(*args): return _method_proxy("outlinesize", "fn", *args);
def outlineitemcount(*args): return _method_proxy("outlineitemcount", "fn", *args);
def val(*args): return _method_proxy("val", "fn", *args);
def ascii2(*args): return _method_proxy("ascii", "fn", *args);
def strlen(*args): return _method_proxy("strlen", "fn", *args);
def strstr(*args): return _method_proxy("strstr", "fn", *args);
def strrstr(*args): return _method_proxy("strrstr", "fn", *args);
def wcslen(*args): return _method_proxy("wcslen", "fn", *args);
def wcsstrstr(*args): return _method_proxy("wcsstrstr", "fn", *args);
def wcsstrrstr(*args): return _method_proxy("wcsstrrstr", "fn", *args);
def ucs4len(*args): return _method_proxy("ucs4len", "fn", *args);
def ucs4strstr(*args): return _method_proxy("ucs4strstr", "fn", *args);
def ucs4strrstr(*args): return _method_proxy("ucs4strrstr", "fn", *args);
def cmulen(*args): return _method_proxy("cmulen", "fn", *args);
def cmustrstr(*args): return _method_proxy("cmustrstr", "fn", *args);
def cmustrrstr(*args): return _method_proxy("cmustrrstr", "fn", *args);
def gculen(*args): return _method_proxy("gculen", "fn", *args);
def gcustrstr(*args): return _method_proxy("gcustrstr", "fn", *args);
def gcustrrstr(*args): return _method_proxy("gcustrrstr", "fn", *args);
def wcs_to_char(*args): return _method_proxy("wcs_to_char", "fn", *args);
def char_to_wcs(*args): return _method_proxy("char_to_wcs", "fn", *args);
def ucs4_to_char(*args): return _method_proxy("ucs4_to_char", "fn", *args);
def char_to_ucs4(*args): return _method_proxy("char_to_ucs4", "fn", *args);
def cmu_to_char(*args): return _method_proxy("cmu_to_char", "fn", *args);
def char_to_cmu(*args): return _method_proxy("char_to_cmu ", "fn", *args);
def gcu_to_char(*args): return _method_proxy("gcu_to_char", "fn", *args);
def char_to_gcu(*args): return _method_proxy("char_to_gcu", "fn", *args);
def byteindex_to_charindex(*args): return _method_proxy("byteindex_to_charindex", "fn", *args);
def charindex_to_byteindex(*args): return _method_proxy("charindex_to_byteindex", "fn", *args);
def findwindow(*args): return _method_proxy("findwindow", "fn", *args);
def findwindowclass(*args): return _method_proxy("findwindowclass", "fn", *args);
def sendmessage(*args): return _method_proxy("sendmessage", "fn", *args);
def xtocolumn(*args): return _method_proxy("xtocolumn", "fn", *args);
def ytolineno(*args): return _method_proxy("ytolineno", "fn", *args);
def columntox(*args): return _method_proxy("columntox", "fn", *args);
def linenotoy(*args): return _method_proxy("linenotoy", "fn", *args);
def charcount(*args): return _method_proxy("charcount", "fn", *args);
def existfile(*args): return _method_proxy("existfile", "fn", *args);
def getmaxinfo(*args): return _method_proxy("getmaxinfo", "fn", *args);
def keypressedex(*args): return _method_proxy("keypressedex", "fn", *args);
def setcompatiblemode(*args): return _method_proxy("setcompatiblemode", "fn", *args);
def inputchar(*args): return _method_proxy("inputchar", "fn", *args);
def iskeydown(*args): return _method_proxy("iskeydown", "fn", *args);
def getininum(*args): return _method_proxy("getininum", "fn", *args);
def getininumw(*args): return _method_proxy("getininumw", "fn", *args);
def getregnum(*args): return _method_proxy("getregnum", "fn", *args);
def getconfigcolor(*args): return _method_proxy("getconfigcolor", "fn", *args);
def hidemaruorder(*args): return _method_proxy("hidemaruorder", "fn", *args);
def hidemarucount(*args): return _method_proxy("hidemarucount", "fn", *args);
def findhidemaru(*args): return _method_proxy("findhidemaru", "fn", *args);
def hidemaruhandle(*args): return _method_proxy("hidemaruhandle", "fn", *args);
def getcurrenttab(*args): return _method_proxy("getcurrenttab", "fn", *args);
def gettabhandle(*args): return _method_proxy("gettabhandle", "fn", *args);
def getclipboardinfo(*args): return _method_proxy("getclipboardinfo", "fn", *args);
def event(*args): return _method_proxy("event", "fn", *args);
def geteventnotify(*args): return _method_proxy("geteventnotify", "fn", *args);
def loaddll(*args): return _method_proxy("loaddll", "fn", *args);
def dllfunc(*args): return _method_proxy("dllfunc", "fn", *args);
def dllfuncw(*args): return _method_proxy("dllfuncw", "fn", *args);
def dllfuncexist(*args): return _method_proxy("dllfuncexist", "fn", *args);
def createobject(*args): return _method_proxy("createobject", "fn", *args);

def findmarker(*args): return _method_proxy("findmarker", "fs", *args);
def diff(*args): return _method_proxy("diff", "fs", *args);
def reservedmultisel(*args): return _method_proxy("reservedmultisel", "fs", *args);
def regulardll(*args): return _method_proxy("regulardll", "fs", *args);
def filename(*args): return _method_proxy("filename", "fs", *args);
def filename2(*args): return _method_proxy("filename2", "fs", *args);
def filename3(*args): return _method_proxy("filename3", "fs", *args);
def basename(*args): return _method_proxy("basename", "fs", *args);
def basename2(*args): return _method_proxy("basename2", "fs", *args);
def basename3(*args): return _method_proxy("basename3", "fs", *args);
def directory(*args): return _method_proxy("directory", "fs", *args);
def directory2(*args): return _method_proxy("directory2", "fs", *args);
def directory3(*args): return _method_proxy("directory3", "fs", *args);
def filetype(*args): return _method_proxy("filetype", "fs", *args);
def currentmacrofilename(*args): return _method_proxy("currentmacrofilename", "fs", *args);
def currentmacrobasename(*args): return _method_proxy("currentmacrobasename", "fs", *args);
def currentmacrodirectory(*args): return _method_proxy("currentmacrodirectory", "fs", *args);
def hidemarudir(*args): return _method_proxy("hidemarudir", "fs", *args);
def macrodir(*args): return _method_proxy("macrodir", "fs", *args);
def settingdir(*args): return _method_proxy("settingdir", "fs", *args);
def backupdir(*args): return _method_proxy("backupdir", "fs", *args);
def windir(*args): return _method_proxy("windir", "fs", *args);
def winsysdir(*args): return _method_proxy("winsysdir", "fs", *args);
def searchbuffer(*args): return _method_proxy("searchbuffer", "fs", *args);
def targetcolormarker(*args): return _method_proxy("targetcolormarker", "fs", *args);
def replacebuffer(*args): return _method_proxy("replacebuffer", "fs", *args);
def grepfilebuffer(*args): return _method_proxy("grepfilebuffer", "fs", *args);
def grepfolderbuffer(*args): return _method_proxy("grepfolderbuffer", "fs", *args);
def foundbuffer(*args): return _method_proxy("foundbuffer", "fs", *args);
def currentconfigset(*args): return _method_proxy("currentconfigset", "fs", *args);
def fontname(*args): return _method_proxy("fontname", "fs", *args);
def date(*args): return _method_proxy("date", "fs", *args);
def time(*args): return _method_proxy("time", "fs", *args);
def year(*args): return _method_proxy("year", "fs", *args);
def month(*args): return _method_proxy("month", "fs", *args);
def day(*args): return _method_proxy("day", "fs", *args);
def hour(*args): return _method_proxy("hour", "fs", *args);
def minute(*args): return _method_proxy("minute", "fs", *args);
def second(*args): return _method_proxy("second", "fs", *args);
def dayofweek(*args): return _method_proxy("dayofweek", "fs", *args);
# def str(*args): return _method_proxy("str", "fs", *args);
def char(*args): return _method_proxy("char", "fs", *args);
def unichar(*args): return _method_proxy("unichar", "fs", *args);
def sprintf(*args): return _method_proxy("sprintf", "fs", *args);
def leftstr(*args): return _method_proxy("leftstr", "fs", *args);
def rightstr(*args): return _method_proxy("rightstr", "fs", *args);
def midstr(*args): return _method_proxy("midstr", "fs", *args);
def wcsleftstr(*args): return _method_proxy("wcsleftstr", "fs", *args);
def wcsrightstr(*args): return _method_proxy("wcsrightstr", "fs", *args);
def wcsmidstr(*args): return _method_proxy("wcsmidstr", "fs", *args);
def ucs4leftstr(*args): return _method_proxy("ucs4leftstr", "fs", *args);
def ucs4rightstr(*args): return _method_proxy("ucs4rightstr", "fs", *args);
def ucs4midstr(*args): return _method_proxy("ucs4midstr", "fs", *args);
def cmuleftstr(*args): return _method_proxy("cmuleftstr", "fs", *args);
def cmurightstr(*args): return _method_proxy("cmurightstr", "fs", *args);
def cmumidstr(*args): return _method_proxy("cmumidstr", "fs", *args);
def gculeftstr(*args): return _method_proxy("gculeftstr", "fs", *args);
def gcurightstr(*args): return _method_proxy("gcurightstr", "fs", *args);
def gcumidstr(*args): return _method_proxy("gcumidstr", "fs", *args);
def gettext(*args): return _method_proxy("gettext", "fs", *args);
def gettext2(*args): return _method_proxy("gettext2", "fs", *args);
def gettext_wcs(*args): return _method_proxy("gettext_wcs", "fs", *args);
def gettext_ucs4(*args): return _method_proxy("gettext_ucs4", "fs", *args);
def gettext_cmu(*args): return _method_proxy("gettext_cmu", "fs", *args);
def gettext_gcu(*args): return _method_proxy("gettext_gcu", "fs", *args);
def getenv(*args): return _method_proxy("getenv", "fs", *args);
def getgrepfilehist(*args): return _method_proxy("getgrepfilehist", "fs", *args);
def enumcolormarkerlayer(*args): return _method_proxy("enumcolormarkerlayer", "fs", *args);
def getfiletime(*args): return _method_proxy("getfiletime", "fs", *args);
def getoutlineitem(*args): return _method_proxy("getoutlineitem", "fs", *args);
def getarg(*args): return _method_proxy("getarg", "fs", *args);
def getautocompitem(*args): return _method_proxy("getautocompitem", "fs", *args);
def getcolormarker(*args): return _method_proxy("getcolormarker", "fs", *args);
def getfilehist(*args): return _method_proxy("getfilehist", "fs", *args);
def getpathhist(*args): return _method_proxy("getpathhist", "fs", *args);
def getreplacehist(*args): return _method_proxy("getreplacehist", "fs", *args);
def getsearchhist(*args): return _method_proxy("getsearchhist", "fs", *args);
def gettagsfile(*args): return _method_proxy("gettagsfile", "fs", *args);
def gettitle(*args): return _method_proxy("gettitle", "fs", *args);
def browsefile(*args): return _method_proxy("browsefile", "fs", *args);
def quote(*args): return _method_proxy("quote", "fs", *args);
def strreplace(*args): return _method_proxy("strreplace", "fs", *args);
# jsmodeには無いがpythonには必要
def encodeuri(*args): return _method_proxy("encodeuri", "fs", *args);
def decodeuri(*args): return _method_proxy("decodeuri", "fs", *args);

# ２つの値を返す
def enumregvalue(*args):
    ret = hm.Macro.Function("enumregvalue", *args)
    return ret.Result, ret.Args[1];

# ２つの値を返す
def getlinecount(*args):
    ret = hm.Macro.Function("getlinecount", *args)
    return ret.Result, ret.Args[2];


# 分岐あり
def toupper(*args):
    if len(args)>=1 and (type(args[0]) is str):
        return _method_proxy("toupper", "fs", *args)
    else:
        return _method_proxy("toupper", "st", *args)

# 分岐あり
def tolower(*args):
    if len(args)>=1 and (type(args[0]) is str):
        return _method_proxy("tolower", "fs", *args)
    else:
        return _method_proxy("tolower", "st", *args)

# 分岐あり
def filter2(*args):
    if len(args)>=4:
        return _method_proxy("filter", "fs", *args)
    else:
        return _method_proxy("filter", "st", *args)

def input2(*args): return _method_proxy("input", "fs", *args);
def getinistr(*args): return _method_proxy("getinistr", "fs", *args);
def getinistrw(*args): return _method_proxy("getinistrw", "fs", *args);
def getregbinary(*args): return _method_proxy("getregbinary", "fs", *args);
def getregstr(*args): return _method_proxy("getregstr", "fs", *args);
def enumregkey(*args): return _method_proxy("enumregkey", "fs", *args);
def gettabstop(*args): return _method_proxy("gettabstop", "fs", *args);
def getstaticvariable(*args): return _method_proxy("getstaticvariable", "fs", *args);
def getclipboard(*args): return _method_proxy("getclipboard", "fs", *args);
def dllfuncstr(*args): return _method_proxy("dllfuncstr", "fs", *args);
def dllfuncstrw(*args): return _method_proxy("dllfuncstrw", "fs", *args);
def loaddllfile(*args): return _method_proxy("loaddllfile", "fs", *args);

def refreshdatetime(*args): return _method_proxy("refreshdatetime", "st", *args);
def newfile(*args): return _method_proxy("newfile", "st", *args);
def openfile(*args): return _method_proxy("openfile", "st", *args);
def loadfile(*args): return _method_proxy("loadfile", "st", *args);
def openfilepart(*args): return _method_proxy("openfilepart", "st", *args);
def closenew(*args): return _method_proxy("closenew", "st", *args);
def saveas(*args): return _method_proxy("saveas", "st", *args);
def appendsave(*args): return _method_proxy("appendsave", "st", *args);
def changename(*args): return _method_proxy("changename", "st", *args);
def insertfile(*args): return _method_proxy("insertfile", "st", *args);
def readonlyopenfile(*args): return _method_proxy("readonlyopenfile", "st", *args);
def readonlyloadfile(*args): return _method_proxy("readonlyloadfile", "st", *args);
def save(*args): return _method_proxy("save", "st", *args);
def savelf(*args): return _method_proxy("savelf", "st", *args);
def print2(*args): return _method_proxy("print", "st", *args);
def saveall(*args): return _method_proxy("saveall", "st", *args);
def saveupdatedall(*args): return _method_proxy("saveupdatedall", "st", *args);
def openbyshell(*args): return _method_proxy("openbyshell", "st", *args);
def openbyhidemaru(*args): return _method_proxy("openbyhidemaru", "st", *args);
def setfilehist(*args): return _method_proxy("setfilehist", "st", *args);
def setpathhist(*args): return _method_proxy("setpathhist", "st", *args);
def setencode(*args): return _method_proxy("setencode", "st", *args);
def stophistoryswitch(*args): return _method_proxy("stophistoryswitch", "st", *args);
def deletefilehist(*args): return _method_proxy("deletefilehist", "st", *args);
def OPEN(*args): return _method_proxy("OPEN", "st", *args);
def SAVEAS(*args): return _method_proxy("SAVEAS", "st", *args);
def LOAD(*args): return _method_proxy("LOAD", "st", *args);
def APPENDSAVE(*args): return _method_proxy("APPENDSAVE", "st", *args);
def CHANGENAME(*args): return _method_proxy("CHANGENAME", "st", *args);
def INSERTFILE(*args): return _method_proxy("INSERTFILE", "st", *args);
def OPENFILEPART(*args): return _method_proxy("OPENFILEPART", "st", *args);
def deletefile(*args): return _method_proxy("deletefile", "st", *args);
def propertydialog(*args): return _method_proxy("propertydialog", "st", *args);

def up(*args): return _method_proxy("up", "st", *args);
def down(*args): return _method_proxy("down", "st", *args);
def right(*args): return _method_proxy("right", "st", *args);
def left(*args): return _method_proxy("left", "st", *args);
def up_nowrap(*args): return _method_proxy("up_nowrap", "st", *args);
def down_nowrap(*args): return _method_proxy("down_nowrap", "st", *args);
def shiftup(*args): return _method_proxy("shiftup", "st", *args);
def shiftdown(*args): return _method_proxy("shiftdown", "st", *args);
def shiftright(*args): return _method_proxy("shiftright", "st", *args);
def shiftleft(*args): return _method_proxy("shiftleft", "st", *args);
def gofileend(*args): return _method_proxy("gofileend", "st", *args);
def gofiletop(*args): return _method_proxy("gofiletop", "st", *args);
def gokakko(*args): return _method_proxy("gokakko", "st", *args);
def golastupdated(*args): return _method_proxy("golastupdated", "st", *args);
def goleftkakko(*args): return _method_proxy("goleftkakko", "st", *args);
def gorightkakko(*args): return _method_proxy("gorightkakko", "st", *args);
def golinetop(*args): return _method_proxy("golinetop", "st", *args);
def golinetop2(*args): return _method_proxy("golinetop2", "st", *args);
def golineend(*args): return _method_proxy("golineend", "st", *args);
def golineend2(*args): return _method_proxy("golineend2", "st", *args);
def golineend3(*args): return _method_proxy("golineend3", "st", *args);
def goscreenend(*args): return _method_proxy("goscreenend", "st", *args);
def goscreentop(*args): return _method_proxy("goscreentop", "st", *args);
def jump(*args): return _method_proxy("jump", "st", *args);
def moveto(*args): return _method_proxy("moveto", "st", *args);
def movetolineno(*args): return _method_proxy("movetolineno", "st", *args);
def movetoview(*args): return _method_proxy("movetoview", "st", *args);
def moveto2(*args): return _method_proxy("moveto2", "st", *args);
def moveto_wcs(*args): return _method_proxy("moveto_wcs", "st", *args);
def moveto_ucs4(*args): return _method_proxy("moveto_ucs4", "st", *args);
def moveto_cmu(*args): return _method_proxy("moveto_cmu", "st", *args);
def moveto_gcu(*args): return _method_proxy("moveto_gcu", "st", *args);
def nextpage(*args): return _method_proxy("nextpage", "st", *args);
def prevpage(*args): return _method_proxy("prevpage", "st", *args);
def halfnextpage(*args): return _method_proxy("halfnextpage", "st", *args);
def halfprevpage(*args): return _method_proxy("halfprevpage", "st", *args);
def rollup(*args): return _method_proxy("rollup", "st", *args);
def rollup2(*args): return _method_proxy("rollup2", "st", *args);
def rolldown(*args): return _method_proxy("rolldown", "st", *args);
def rolldown2(*args): return _method_proxy("rolldown2", "st", *args);
def wordleft(*args): return _method_proxy("wordleft", "st", *args);
def wordleft2(*args): return _method_proxy("wordleft2", "st", *args);
def wordright(*args): return _method_proxy("wordright", "st", *args);
def wordright2(*args): return _method_proxy("wordright2", "st", *args);
def wordrightsalnen(*args): return _method_proxy("wordrightsalnen", "st", *args);
def wordrightsalnen2(*args): return _method_proxy("wordrightsalnen2", "st", *args);
def gowordtop(*args): return _method_proxy("gowordtop", "st", *args);
def gowordend(*args): return _method_proxy("gowordend", "st", *args);
def gowordtop2(*args): return _method_proxy("gowordtop2", "st", *args);
def gowordend2(*args): return _method_proxy("gowordend2", "st", *args);
def prevpos(*args): return _method_proxy("prevpos", "st", *args);
def prevposhistback(*args): return _method_proxy("prevposhistback", "st", *args);
def prevposhistforward(*args): return _method_proxy("prevposhistforward", "st", *args);
def setmark(*args): return _method_proxy("setmark", "st", *args);
def clearallmark(*args): return _method_proxy("clearallmark", "st", *args);
def marklist(*args): return _method_proxy("marklist", "st", *args);
def nextmark(*args): return _method_proxy("nextmark", "st", *args);
def prevmark(*args): return _method_proxy("prevmark", "st", *args);
def prevfunc(*args): return _method_proxy("prevfunc", "st", *args);
def nextfunc(*args): return _method_proxy("nextfunc", "st", *args);
def nextresult(*args): return _method_proxy("nextresult", "st", *args);
def prevresult(*args): return _method_proxy("prevresult", "st", *args);
def gotagpair(*args): return _method_proxy("gotagpair", "st", *args);
def backtab(*args): return _method_proxy("backtab", "st", *args);
def forwardtab(*args): return _method_proxy("forwardtab", "st", *args);
def appendcopy(*args): return _method_proxy("appendcopy", "st", *args);
def appendcut(*args): return _method_proxy("appendcut", "st", *args);
def beginrect(*args): return _method_proxy("beginrect", "st", *args);
def beginrectmulti(*args): return _method_proxy("beginrectmulti", "st", *args);
def beginsel(*args): return _method_proxy("beginsel", "st", *args);
def beginlinesel(*args): return _method_proxy("beginlinesel", "st", *args);
def endsel(*args): return _method_proxy("endsel", "st", *args);
def copy(*args): return _method_proxy("copy", "st", *args);
def copy2(*args): return _method_proxy("copy2", "st", *args);
def cut(*args): return _method_proxy("cut", "st", *args);
def copyline(*args): return _method_proxy("copyline", "st", *args);
def cutline(*args): return _method_proxy("cutline", "st", *args);
def cutafter(*args): return _method_proxy("cutafter", "st", *args);
def copyword(*args): return _method_proxy("copyword", "st", *args);
def cutword(*args): return _method_proxy("cutword", "st", *args);
def escapeselect(*args): return _method_proxy("escapeselect", "st", *args);
def paste(*args): return _method_proxy("paste", "st", *args);
def pasterect(*args): return _method_proxy("pasterect", "st", *args);
def refpaste(*args): return _method_proxy("refpaste", "st", *args);
def refcopy(*args): return _method_proxy("refcopy", "st", *args);
def refcopy2(*args): return _method_proxy("refcopy2", "st", *args);
def selectall(*args): return _method_proxy("selectall", "st", *args);
def selectline(*args): return _method_proxy("selectline", "st", *args);
def selectword(*args): return _method_proxy("selectword", "st", *args);
def selectword2(*args): return _method_proxy("selectword2", "st", *args);
def showcliphist(*args): return _method_proxy("showcliphist", "st", *args);
def poppaste(*args): return _method_proxy("poppaste", "st", *args);
def poppaste2(*args): return _method_proxy("poppaste2", "st", *args);
def getcliphist(*args): return _method_proxy("getcliphist", "st", *args);
def clearcliphist(*args): return _method_proxy("clearcliphist", "st", *args);
def selectcfunc(*args): return _method_proxy("selectcfunc", "st", *args);
def copyurl(*args): return _method_proxy("copyurl", "st", *args);
def copyformed(*args): return _method_proxy("copyformed", "st", *args);
def selectcolumn(*args): return _method_proxy("selectcolumn", "st", *args);
def tomultiselect(*args): return _method_proxy("tomultiselect", "st", *args);
def invertselection(*args): return _method_proxy("invertselection", "st", *args);
def reservemultisel(*args): return _method_proxy("reservemultisel", "st", *args);
def selectreservedmultisel(*args): return _method_proxy("selectreservedmultisel", "st", *args);
def clearreservedmultisel(*args): return _method_proxy("clearreservedmultisel", "st", *args);
def clearreservedmultiselall(*args): return _method_proxy("clearreservedmultiselall", "st", *args);
def backspace(*args): return _method_proxy("backspace", "st", *args);
def delete(*args): return _method_proxy("del", "st", *args);
def deleteafter(*args): return _method_proxy("deleteafter", "st", *args);
def deletebefore(*args): return _method_proxy("deletebefore", "st", *args);
def deleteline(*args): return _method_proxy("deleteline", "st", *args);
def deleteline2(*args): return _method_proxy("deleteline2", "st", *args);
def deleteword(*args): return _method_proxy("deleteword", "st", *args);
def deletewordall(*args): return _method_proxy("deletewordall", "st", *args);
def deletewordfront(*args): return _method_proxy("deletewordfront", "st", *args);
def dupline(*args): return _method_proxy("dupline", "st", *args);
def insertline(*args): return _method_proxy("insertline", "st", *args);
def insertreturn(*args): return _method_proxy("insertreturn", "st", *args);
def tab(*args): return _method_proxy("tab", "st", *args);
def undelete(*args): return _method_proxy("undelete", "st", *args);
def undo(*args): return _method_proxy("undo", "st", *args);
def redo(*args): return _method_proxy("redo", "st", *args);
def casechange(*args): return _method_proxy("casechange", "st", *args);
def indent(*args): return _method_proxy("indent", "st", *args);
def unindent(*args): return _method_proxy("unindent", "st", *args);
def shifttab(*args): return _method_proxy("shifttab", "st", *args);
def tospace(*args): return _method_proxy("tospace", "st", *args);
def totab(*args): return _method_proxy("totab", "st", *args);
def tohankaku(*args): return _method_proxy("tohankaku", "st", *args);
def tozenkakuhira(*args): return _method_proxy("tozenkakuhira", "st", *args);
def tozenkakukata(*args): return _method_proxy("tozenkakukata", "st", *args);
def capslockforgot(*args): return _method_proxy("capslockforgot", "st", *args);
def imeconvforgot(*args): return _method_proxy("imeconvforgot", "st", *args);
def reopen(*args): return _method_proxy("reopen", "st", *args);
def filtermenu(*args): return _method_proxy("filtermenu", "st", *args);
def autocomplete(*args): return _method_proxy("autocomplete", "st", *args);
def form(*args): return _method_proxy("form", "st", *args);
def unform(*args): return _method_proxy("unform", "st", *args);
def showformline(*args): return _method_proxy("showformline", "st", *args);
def clearundobuffer(*args): return _method_proxy("clearundobuffer", "st", *args);
def template(*args): return _method_proxy("template", "st", *args);
def find1(*args): return _method_proxy("find", "st", *args);
def find2(*args): return _method_proxy("find2", "st", *args);
def findword(*args): return _method_proxy("findword", "st", *args);
def replace1(*args): return _method_proxy("replace", "st", *args);
def replaceall(*args): return _method_proxy("replaceall", "st", *args);
def replaceallfast(*args): return _method_proxy("replaceallfast", "st", *args);
def replaceallquick(*args): return _method_proxy("replaceallquick", "st", *args);
def finddown(*args): return _method_proxy("finddown", "st", *args);
def finddown2(*args): return _method_proxy("finddown2", "st", *args);
def findup(*args): return _method_proxy("findup", "st", *args);
def findup2(*args): return _method_proxy("findup2", "st", *args);
def getsearch(*args): return _method_proxy("getsearch", "st", *args);
def gosearchstarted(*args): return _method_proxy("gosearchstarted", "st", *args);
def setsearch(*args): return _method_proxy("setsearch", "st", *args);
def setsearchhist(*args): return _method_proxy("setsearchhist", "st", *args);
def setreplace(*args): return _method_proxy("setreplace", "st", *args);
def setreplacehist(*args): return _method_proxy("setreplacehist", "st", *args);
def setgrepfile(*args): return _method_proxy("setgrepfile", "st", *args);
def forceinselect(*args): return _method_proxy("forceinselect", "st", *args);
def goupdatedown(*args): return _method_proxy("goupdatedown", "st", *args);
def goupdateup(*args): return _method_proxy("goupdateup", "st", *args);
def clearupdates(*args): return _method_proxy("clearupdates", "st", *args);
def grep(*args): return _method_proxy("grep", "st", *args);
def grepdialog(*args): return _method_proxy("grepdialog", "st", *args);
def grepdialog2(*args): return _method_proxy("grepdialog2", "st", *args);
def localgrep(*args): return _method_proxy("localgrep", "st", *args);
def grepreplace(*args): return _method_proxy("grepreplace", "st", *args);
def grepreplacedialog2(*args): return _method_proxy("grepreplacedialog2", "st", *args);
def escapeinselect(*args): return _method_proxy("escapeinselect", "st", *args);
def hilightfound(*args): return _method_proxy("hilightfound", "st", *args);
def colormarker(*args): return _method_proxy("colormarker", "st", *args);
def nextcolormarker(*args): return _method_proxy("nextcolormarker", "st", *args);
def prevcolormarker(*args): return _method_proxy("prevcolormarker", "st", *args);
def colormarkerdialog(*args): return _method_proxy("colormarkerdialog", "st", *args);
def deletecolormarker(*args): return _method_proxy("deletecolormarker", "st", *args);
def deletecolormarkerall(*args): return _method_proxy("deletecolormarkerall", "st", *args);
def selectcolormarker(*args): return _method_proxy("selectcolormarker", "st", *args);
def selectallfound(*args): return _method_proxy("selectallfound", "st", *args);
def colormarkerallfound(*args): return _method_proxy("colormarkerallfound", "st", *args);
def clearcolormarkerallfound(*args): return _method_proxy("clearcolormarkerallfound", "st", *args);
def foundlist(*args): return _method_proxy("foundlist", "st", *args);
def foundlistoutline(*args): return _method_proxy("foundlistoutline", "st", *args);
def findmarkerlist(*args): return _method_proxy("findmarkerlist", "st", *args);
def selectinselect(*args): return _method_proxy("selectinselect", "st", *args);
def setinselect2(*args): return _method_proxy("setinselect2", "st", *args);
def settargetcolormarker(*args): return _method_proxy("settargetcolormarker", "st", *args);
def colormarkersnapshot(*args): return _method_proxy("colormarkersnapshot", "st", *args);
def restoredesktop(*args): return _method_proxy("restoredesktop", "st", *args);
def savedesktop(*args): return _method_proxy("savedesktop", "st", *args);
def scrolllink(*args): return _method_proxy("scrolllink", "st", *args);
def split(*args): return _method_proxy("split", "st", *args);
def setsplitinfo(*args): return _method_proxy("setsplitinfo", "st", *args);
def splitswitch(*args): return _method_proxy("splitswitch", "st", *args);
def windowcascade(*args): return _method_proxy("windowcascade", "st", *args);
def windowhorz(*args): return _method_proxy("windowhorz", "st", *args);
def windowtiling(*args): return _method_proxy("windowtiling", "st", *args);
def windowvert(*args): return _method_proxy("windowvert", "st", *args);
def windowlist(*args): return _method_proxy("windowlist", "st", *args);
def compfile(*args): return _method_proxy("compfile", "st", *args);
def COMPFILE(*args): return _method_proxy("COMPFILE", "st", *args);
def nextcompfile(*args): return _method_proxy("nextcompfile", "st", *args);
def prevcompfile(*args): return _method_proxy("prevcompfile", "st", *args);
def alwaystopswitch(*args): return _method_proxy("alwaystopswitch", "st", *args);
def settabmode(*args): return _method_proxy("settabmode", "st", *args);
def settabgroup(*args): return _method_proxy("settabgroup", "st", *args);
def settaborder(*args): return _method_proxy("settaborder", "st", *args);
def iconthistab(*args): return _method_proxy("iconthistab", "st", *args);
def fullscreen(*args): return _method_proxy("fullscreen", "st", *args);
def backtagjump(*args): return _method_proxy("backtagjump", "st", *args);
def directtagjump(*args): return _method_proxy("directtagjump", "st", *args);
def freecursorswitch(*args): return _method_proxy("freecursorswitch", "st", *args);
def imeswitch(*args): return _method_proxy("imeswitch", "st", *args);
def imeregisterword(*args): return _method_proxy("imeregisterword", "st", *args);
def help1(*args): return _method_proxy("help", "st", *args);
def help2(*args): return _method_proxy("help2", "st", *args);
def help3(*args): return _method_proxy("help3", "st", *args);
def help4(*args): return _method_proxy("help4", "st", *args);
def help5(*args): return _method_proxy("help5", "st", *args);
def help6(*args): return _method_proxy("help6", "st", *args);
def hidemaruhelp(*args): return _method_proxy("hidemaruhelp", "st", *args);
def macrohelp(*args): return _method_proxy("macrohelp", "st", *args);
def overwriteswitch(*args): return _method_proxy("overwriteswitch", "st", *args);
def readonlyswitch(*args): return _method_proxy("readonlyswitch", "st", *args);
def showcode(*args): return _method_proxy("showcode", "st", *args);
def showcharcount(*args): return _method_proxy("showcharcount", "st", *args);
def showlineno(*args): return _method_proxy("showlineno", "st", *args);
def tagjump(*args): return _method_proxy("tagjump", "st", *args);
def redraw(*args): return _method_proxy("redraw", "st", *args);
def browsemodeswitch(*args): return _method_proxy("browsemodeswitch", "st", *args);
def clist(*args): return _method_proxy("clist", "st", *args);
def clearupdated(*args): return _method_proxy("clearupdated", "st", *args);
def refreshtabstop(*args): return _method_proxy("refreshtabstop", "st", *args);
def refreshtabstop_shrink(*args): return _method_proxy("refreshtabstop_shrink", "st", *args);
def refreshtabstop_current(*args): return _method_proxy("refreshtabstop_current", "st", *args);
def autospellcheckswitch(*args): return _method_proxy("autospellcheckswitch", "st", *args);
def spellcheckdialog(*args): return _method_proxy("spellcheckdialog", "st", *args);
def savebacktagjump(*args): return _method_proxy("savebacktagjump", "st", *args);
def fold(*args): return _method_proxy("fold", "st", *args);
def unfold(*args): return _method_proxy("unfold", "st", *args);
def nextfoldable(*args): return _method_proxy("nextfoldable", "st", *args);
def prevfoldable(*args): return _method_proxy("prevfoldable", "st", *args);
def selectfoldable(*args): return _method_proxy("selectfoldable", "st", *args);
def foldall(*args): return _method_proxy("foldall", "st", *args);
def unfoldall(*args): return _method_proxy("unfoldall", "st", *args);
def rangeeditin(*args): return _method_proxy("rangeeditin", "st", *args);
def rangeeditout(*args): return _method_proxy("rangeeditout", "st", *args);
def nextoutlineitem(*args): return _method_proxy("nextoutlineitem", "st", *args);
def prevoutlineitem(*args): return _method_proxy("prevoutlineitem", "st", *args);
def showoutline(*args): return _method_proxy("showoutline", "st", *args);
def showoutlinebar(*args): return _method_proxy("showoutlinebar", "st", *args);
def showfoldingbar(*args): return _method_proxy("showfoldingbar", "st", *args);
def syncoutline(*args): return _method_proxy("syncoutline", "st", *args);
def refreshoutline(*args): return _method_proxy("refreshoutline", "st", *args);
def setoutlinesize(*args): return _method_proxy("setoutlinesize", "st", *args);
def beep(*args): return _method_proxy("beep", "st", *args);
def play(*args): return _method_proxy("play", "st", *args);
def playsync(*args): return _method_proxy("playsync", "st", *args);
def debuginfo(*args): return _method_proxy("debuginfo", "st", *args);
def showvars(*args): return _method_proxy("showvars", "st", *args);
def title(*args): return _method_proxy("title", "st", *args);
def run(*args): return _method_proxy("run", "st", *args);
def runsync(*args): return _method_proxy("runsync", "st", *args);
def runsync2(*args): return _method_proxy("runsync2", "st", *args);
def runex(*args): return _method_proxy("runex", "st", *args);
def disabledraw(*args): return _method_proxy("disabledraw", "st", *args);
def enabledraw(*args): return _method_proxy("enabledraw", "st", *args);
def disabledraw2(*args): return _method_proxy("disabledraw2", "st", *args);
def disablebreak(*args): return _method_proxy("disablebreak", "st", *args);
def disableinvert(*args): return _method_proxy("disableinvert", "st", *args);
def enableinvert(*args): return _method_proxy("enableinvert", "st", *args);
def disableerrormsg(*args): return _method_proxy("disableerrormsg", "st", *args);
def enableerrormsg(*args): return _method_proxy("enableerrormsg", "st", *args);
def disablehistory(*args): return _method_proxy("disablehistory", "st", *args);
def sleep(*args): return _method_proxy("sleep", "st", *args);
def setfloatmode(*args): return _method_proxy("setfloatmode", "st", *args);
def seterrormode(*args): return _method_proxy("seterrormode", "st", *args);
def setbackgroundmode(*args): return _method_proxy("setbackgroundmode", "st", *args);
def inputpos(*args): return _method_proxy("inputpos", "st", *args);
def menu(*args): return _method_proxy("menu", "st", *args);
def mousemenu(*args): return _method_proxy("mousemenu", "st", *args);
def setmenudelay(*args): return _method_proxy("setmenudelay", "st", *args);
def writeininum(*args): return _method_proxy("writeininum", "st", *args);
def writeininumw(*args): return _method_proxy("writeininumw", "st", *args);
def writeinistr(*args): return _method_proxy("writeinistr", "st", *args);
def writeinistrw(*args): return _method_proxy("writeinistrw", "st", *args);
def openreg(*args): return _method_proxy("openreg", "st", *args);
def createreg(*args): return _method_proxy("createreg", "st", *args);
def closereg(*args): return _method_proxy("closereg", "st", *args);
def writeregbinary(*args): return _method_proxy("writeregbinary", "st", *args);
def writeregnum(*args): return _method_proxy("writeregnum", "st", *args);
def writeregstr(*args): return _method_proxy("writeregstr", "st", *args);
def deletereg(*args): return _method_proxy("deletereg", "st", *args);
def configset(*args): return _method_proxy("configset", "st", *args);
def config(*args): return _method_proxy("config", "st", *args);
def configcolor(*args): return _method_proxy("configcolor", "st", *args);
def saveconfig(*args): return _method_proxy("saveconfig", "st", *args);
def setconfigstate(*args): return _method_proxy("setconfigstate", "st", *args);
def setfiletype(*args): return _method_proxy("setfiletype", "st", *args);
def envchanged(*args): return _method_proxy("envchanged", "st", *args);
def loadkeyassign(*args): return _method_proxy("loadkeyassign", "st", *args);
def savekeyassign(*args): return _method_proxy("savekeyassign", "st", *args);
def loadhilight(*args): return _method_proxy("loadhilight", "st", *args);
def savehilight(*args): return _method_proxy("savehilight", "st", *args);
def loadbookmark(*args): return _method_proxy("loadbookmark", "st", *args);
def savebookmark(*args): return _method_proxy("savebookmark", "st", *args);
def setfontchangemode(*args): return _method_proxy("setfontchangemode", "st", *args);
def settabstop(*args): return _method_proxy("settabstop", "st", *args);
def convert_return_in_cell(*args): return _method_proxy("convert_return_in_cell", "st", *args);
def showwindow(*args): return _method_proxy("showwindow", "st", *args);
def setmonitor(*args): return _method_proxy("setmonitor", "st", *args);
def setwindowpos(*args): return _method_proxy("setwindowpos", "st", *args);
def setwindowsize(*args): return _method_proxy("setwindowsize", "st", *args);
def setfocus(*args): return _method_proxy("setfocus", "st", *args);
def begingroupundo(*args): return _method_proxy("begingroupundo", "st", *args);
def endgroupundo(*args): return _method_proxy("endgroupundo", "st", *args);
def findspecial(*args): return _method_proxy("findspecial", "st", *args);
def setstaticvariable(*args): return _method_proxy("setstaticvariable", "st", *args);
def setregularcache(*args): return _method_proxy("setregularcache", "st", *args);
def closehidemaru(*args): return _method_proxy("closehidemaru", "st", *args);
def closehidemaruforced(*args): return _method_proxy("closehidemaruforced", "st", *args);
def beginclipboardread(*args): return _method_proxy("beginclipboardread", "st", *args);
def seteventnotify(*args): return _method_proxy("seteventnotify", "st", *args);

def freedll(*args): return _method_proxy("freedll", "st", *args);
def setdlldetachfunc(*args): return _method_proxy("setdlldetachfunc", "st", *args);
def keepdll(*args): return _method_proxy("keepdll", "st", *args);
def setcomdetachmethod(*args): return _method_proxy("setcomdetachmethod", "st", *args);
def keepobject(*args): return _method_proxy("keepobject", "st", *args);
def releaseobject(*args): return _method_proxy("releaseobject", "st", *args);

# 配列展開
def menuarray(*args): return menu(*(args[0]));

# 配列展開
def mousemenuarray(*args): return mousemenu(*(args[0]));

def message(*args): return _method_proxy("message", "fn1s2s", *args);

def insert(*args): return _method_proxy("insert", "st1s", *args);
def insertfix(*args): return _method_proxy("insertfix", "st1s", *args);
def searchdialog(*args): return _method_proxy("searchdialog", "st1s", *args);
def searchdown(*args): return _method_proxy("searchdown", "st1s", *args);
def searchdown2(*args): return _method_proxy("searchdown2", "st1s", *args);
def searchup(*args): return _method_proxy("searchup", "st1s", *args);
def searchup2(*args): return _method_proxy("searchup2", "st1s", *args);
def question(*args): return _method_proxy("question", "st1s", *args);
def setclipboard(*args): return _method_proxy("setclipboard", "st1s", *args);
def addclipboard(*args): return _method_proxy("addclipboard", "st1s", *args);

def replacedialog(*args): return _method_proxy("replacedialog", "st1s2s", *args);
def replacedown(*args): return _method_proxy("replacedown", "st1s2s", *args);
def replaceup(*args): return _method_proxy("replaceup", "st1s2s", *args);

# 返り値の型が分岐するもの
class _GetResultExFunction:

    def __call__(self, *args):
        if (args[0] == -1):
            return self.rstr(*args)
        else:
            return _method_proxy("getresultex", "fsn", *args);

    def rnum(self, *args):
        hm.Macro.Var["#__getresultex_rnum_arg0__"] = args[0];
        eval_ret = hm.Macro.Eval(r'''#__temp_getresultex_rnum__ = getresultex(#__getresultex_rnum_arg0__);''');
        func_ret = hm.Macro.Var["#__temp_getresultex_rnum__"];
        hm.Macro.Var["#__temp_getresultex_rnum__"] = 0;
        hm.Macro.Var["#__getresultex_rnum_arg0__"] = 0
        return func_ret
        
    def rstr(self, *args):
        hm.Macro.Var["#__getresultex_rstr_arg0__"] = args[0];
        eval_ret = hm.Macro.Eval(r'''$__temp_getresultex_rstr__ = getresultex(#__getresultex_rstr_arg0__);''');
        func_ret = hm.Macro.Var["$__temp_getresultex_rstr__"];
        hm.Macro.Var["$__temp_getresultex_rstr__"] = "";
        hm.Macro.Var["#__getresultex_rstr_arg0__"] = 0;
        return func_ret

# getresultex
getresultex = _GetResultExFunction();

# 返り値の型が分岐するもの
class _GetEventParamFunction:

    def __call__(self, *args):
        if args[0] == 0 and hm.Macro.Var["event"] == 9:
            return self.rstr(*args)
        else:
            return _method_proxy("geteventparam", "fsn", *args);

    def rnum(self, *args):
        hm.Macro.Var["#__geteventparam_rnum_arg0__"] = args[0];
        eval_ret = hm.Macro.Eval(r'''#__temp_geteventparam_rnum__ = geteventparam(#__geteventparam_rnum_arg0__);''');
        func_ret = hm.Macro.Var["#__temp_geteventparam_rnum__"];
        hm.Macro.Var["#__temp_geteventparam_rnum__"] = 0;
        hm.Macro.Var["#__geteventparam_rnum_arg0__"] = 0;
        return func_ret
        
    def rstr(self, *args):
        hm.Macro.Var["#__geteventparam_rstr_arg0__"] = args[0];
        eval_ret = hm.Macro.Eval(r'''$__temp_geteventparam_rstr__ = geteventparam(#__geteventparam_rstr_arg0__);''');
        func_ret = hm.Macro.Var["$__temp_geteventparam_rstr__"];
        hm.Macro.Var["$__temp_geteventparam_rstr__"] = "";
        hm.Macro.Var["#__geteventparam_rstr_arg0__"] = 0;
        return func_ret

# geteventparam
geteventparam = _GetEventParamFunction();

# 返り値の型が分岐するもの
class _GetConfigFunction:

    def __call__(self, *args):
        return self.rstr(*args)

    def rnum(self, *args):
        hm.Macro.Var["$__getconfig_rnum_arg0__"] = args[0];
        eval_ret = hm.Macro.Eval(r'''#__temp_getconfig_rnum__ = getconfig($__getconfig_rnum_arg0__);''');
        func_ret = hm.Macro.Var["#__temp_getconfig_rnum__"];
        hm.Macro.Var["#__temp_getconfig_rnum__"] = 0;
        hm.Macro.Var["$__getconfig_rnum_arg0__"] = "";
        return func_ret
        
    def rstr(self, *args):
        hm.Macro.Var["$__getconfig_rstr_arg0__"] = args[0];
        eval_ret = hm.Macro.Eval(r'''$__temp_getconfig_rstr__ = getconfig($__getconfig_rstr_arg0__);''');
        func_ret = hm.Macro.Var["$__temp_getconfig_rstr__"];
        hm.Macro.Var["$__temp_getconfig_rstr__"] = "";
        hm.Macro.Var["$__getconfig_rstr_arg0__"] = "";
        return func_ret

# getconfig
getconfig = _GetConfigFunction();

# 返り値の型が分岐するもの
class _MemberFunction:

    def rnum(self, *args):
        arg_name_list = []
        for i, arg in enumerate(args):
            # bool か int か float なら 整数にして
            if type(arg) == type(True) or type(arg) == type(10) or type(arg) == type(10.5):
                var_name = "#__member_rnum_arg" + str(i) + "__"
                arg_name_list.append(var_name)
                hm.Macro.Var[var_name] = int(arg);
            else:
                var_name = "$__member_rnum_arg" + str(i) + "__"
                arg_name_list.append(var_name)
                hm.Macro.Var[var_name] = str(arg);
        
        var_arg_list = ", ".join(arg_name_list)
        eval_ret = hm.Macro.Eval(r'''#__temp_member_rnum__ = member( ''' + var_arg_list + r''');''');
        func_ret = hm.Macro.Var["#__temp_member_rnum__"];
        hm.Macro.Var["#__temp_member_rnum__"] = 0;

        for var_name in arg_name_list:
            
            if var_name.startswith('#'):
                hm.Macro.Var[var_name] = 0;
            else:
                hm.Macro.Var[var_name] = "";

        return func_ret
        
    def rstr(self, *args):
        arg_name_list = []
        for i, arg in enumerate(args):
            # bool か int か float なら 整数にして
            if type(arg) == type(True) or type(arg) == type(10) or type(arg) == type(10.5):
                var_name = "#__member_rstr_arg" + str(i) + "__"
                arg_name_list.append(var_name)
                hm.Macro.Var[var_name] = int(arg);
            else:
                var_name = "$__member_rstr_arg" + str(i) + "__"
                arg_name_list.append(var_name)
                hm.Macro.Var[var_name] = str(arg);
            
        var_arg_list = ", ".join(arg_name_list)
        eval_ret = hm.Macro.Eval(r'''$__temp_member_rstr__ = member( ''' + var_arg_list + r''');''');
        func_ret = hm.Macro.Var["$__temp_member_rstr__"];
        hm.Macro.Var["$__temp_member_rstr__"] = "";

        for var_name in arg_name_list:
            
            if var_name.startswith('#'):
                hm.Macro.Var[var_name] = 0;
            else:
                hm.Macro.Var[var_name] = "";

        return func_ret

# member
member = _MemberFunction();
