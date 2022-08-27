from hmPython import hm

def _dispatch_method(name, t, *args):
    if t == "fn" or t == "fs":
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


def result(*args): return _dispatch_method("result", "fn", *args);
def version(*args): return _dispatch_method("version", "fn", *args);
def platform(*args): return _dispatch_method("platform", "fn", *args);
def darkmode(*args): return _dispatch_method("darkmode", "fn", *args);
def x(*args): return _dispatch_method("x", "fn", *args);
def y(*args): return _dispatch_method("y", "fn", *args);
def column(*args): return _dispatch_method("column", "fn", *args);
def column_wcs(*args): return _dispatch_method("column_wcs", "fn", *args);
def column_ucs4(*args): return _dispatch_method("column_ucs4", "fn", *args);
def column_cmu(*args): return _dispatch_method("column_cmu", "fn", *args);
def column_gcu(*args): return _dispatch_method("column_gcu", "fn", *args);
def lineno(*args): return _dispatch_method("lineno", "fn", *args);
def tabcolumn(*args): return _dispatch_method("tabcolumn", "fn", *args);
def xview(*args): return _dispatch_method("xview", "fn", *args);
def code(*args): return _dispatch_method("code", "fn", *args);
def unicode(*args): return _dispatch_method("unicode", "fn", *args);
def colorcode(*args): return _dispatch_method("colorcode", "fn", *args);
def marked(*args): return _dispatch_method("marked", "fn", *args);
def lineupdated(*args): return _dispatch_method("lineupdated", "fn", *args);
def xpixel(*args): return _dispatch_method("xpixel", "fn", *args);
def ypixel(*args): return _dispatch_method("ypixel", "fn", *args);
def prevposx(*args): return _dispatch_method("prevposx", "fn", *args);
def prevposy(*args): return _dispatch_method("prevposy", "fn", *args);
def lastupdatedx(*args): return _dispatch_method("lastupdatedx", "fn", *args);
def lastupdatedy(*args): return _dispatch_method("lastupdatedy", "fn", *args);
def mousecolumn(*args): return _dispatch_method("mousecolumn", "fn", *args);
def mouselineno(*args): return _dispatch_method("mouselineno", "fn", *args);
def linecount(*args): return _dispatch_method("linecount", "fn", *args);
def linecount2(*args): return _dispatch_method("linecount2", "fn", *args);
def linelen(*args): return _dispatch_method("linelen", "fn", *args);
def linelen2(*args): return _dispatch_method("linelen2", "fn", *args);
def linelen_wcs(*args): return _dispatch_method("linelen_wcs", "fn", *args);
def linelen_ucs4(*args): return _dispatch_method("linelen_ucs4", "fn", *args);
def linelen_cmu(*args): return _dispatch_method("linelen_cmu", "fn", *args);
def linelen_gcu(*args): return _dispatch_method("linelen_gcu", "fn", *args);
def tabcolumnmax(*args): return _dispatch_method("tabcolumnmax", "fn", *args);
def selecting(*args): return _dispatch_method("selecting", "fn", *args);
def rectselecting(*args): return _dispatch_method("rectselecting", "fn", *args);
def lineselecting(*args): return _dispatch_method("lineselecting", "fn", *args);
def selectionlock(*args): return _dispatch_method("selectionlock", "fn", *args);
def mouseselecting(*args): return _dispatch_method("mouseselecting", "fn", *args);
def multiselecting(*args): return _dispatch_method("multiselecting", "fn", *args);
def multiselectcount(*args): return _dispatch_method("multiselectcount", "fn", *args);
def inselecting(*args): return _dispatch_method("inselecting", "fn", *args);
def seltopx(*args): return _dispatch_method("seltopx", "fn", *args);
def seltopy(*args): return _dispatch_method("seltopy", "fn", *args);
def selendx(*args): return _dispatch_method("selendx", "fn", *args);
def selendy(*args): return _dispatch_method("selendy", "fn", *args);
def seltopcolumn(*args): return _dispatch_method("seltopcolumn", "fn", *args);
def seltoplineno(*args): return _dispatch_method("seltoplineno", "fn", *args);
def selendcolumn(*args): return _dispatch_method("selendcolumn", "fn", *args);
def selendlineno(*args): return _dispatch_method("selendlineno", "fn", *args);
def seltop_wcs(*args): return _dispatch_method("seltop_wcs", "fn", *args);
def seltop_ucs4(*args): return _dispatch_method("seltop_ucs4", "fn", *args);
def seltop_cmu(*args): return _dispatch_method("seltop_cmu", "fn", *args);
def seltop_gcu(*args): return _dispatch_method("seltop_gcu", "fn", *args);
def selend_wcs(*args): return _dispatch_method("selend_wcs", "fn", *args);
def selend_ucs4(*args): return _dispatch_method("selend_ucs4", "fn", *args);
def selend_cmu(*args): return _dispatch_method("selend_cmu", "fn", *args);
def selend_gcu(*args): return _dispatch_method("selend_gcu", "fn", *args);
def selopenx(*args): return _dispatch_method("selopenx", "fn", *args);
def selopeny(*args): return _dispatch_method("selopeny", "fn", *args);
def windowwidth(*args): return _dispatch_method("windowwidth", "fn", *args);
def windowheight(*args): return _dispatch_method("windowheight", "fn", *args);
def windowcx(*args): return _dispatch_method("windowcx", "fn", *args);
def windowcy(*args): return _dispatch_method("windowcy", "fn", *args);
def windowposx(*args): return _dispatch_method("windowposx", "fn", *args);
def windowposy(*args): return _dispatch_method("windowposy", "fn", *args);
def splitstate(*args): return _dispatch_method("splitstate", "fn", *args);
def splitmode(*args): return _dispatch_method("splitmode", "fn", *args);
def splitpos(*args): return _dispatch_method("splitpos", "fn", *args);
def windowstate(*args): return _dispatch_method("windowstate", "fn", *args);
def windowstate2(*args): return _dispatch_method("windowstate2", "fn", *args);
def cxscreen(*args): return _dispatch_method("cxscreen", "fn", *args);
def cyscreen(*args): return _dispatch_method("cyscreen", "fn", *args);
def xworkarea(*args): return _dispatch_method("xworkarea", "fn", *args);
def yworkarea(*args): return _dispatch_method("yworkarea", "fn", *args);
def cxworkarea(*args): return _dispatch_method("cxworkarea", "fn", *args);
def cyworkarea(*args): return _dispatch_method("cyworkarea", "fn", *args);
def monitor(*args): return _dispatch_method("monitor", "fn", *args);
def monitorcount(*args): return _dispatch_method("monitorcount", "fn", *args);
def tabmode(*args): return _dispatch_method("tabmode", "fn", *args);
def tabgroup(*args): return _dispatch_method("tabgroup", "fn", *args);
def tabgrouporder(*args): return _dispatch_method("tabgrouporder", "fn", *args);
def taborder(*args): return _dispatch_method("taborder", "fn", *args);
def tabtotal(*args): return _dispatch_method("tabtotal", "fn", *args);
def tabgrouptotal(*args): return _dispatch_method("tabgrouptotal", "fn", *args);
def screentopy(*args): return _dispatch_method("screentopy", "fn", *args);
def screenleftx(*args): return _dispatch_method("screenleftx", "fn", *args);
def compfilehandle(*args): return _dispatch_method("compfilehandle", "fn", *args);
def scrolllinkhandle(*args): return _dispatch_method("scrolllinkhandle", "fn", *args);
def filehistcount(*args): return _dispatch_method("filehistcount", "fn", *args);
# 分岐あり
def overwrite(*args):
    if len(args)==0:
        return _dispatch_method("overwrite", "fn", *args)
    else:
        return _dispatch_method("overwrite", "st1s", *args)

def updated(*args): return _dispatch_method("updated", "fn", *args);
def updatecount(*args): return _dispatch_method("updatecount", "fn", *args);
def anyclipboard(*args): return _dispatch_method("anyclipboard", "fn", *args);
def imestate(*args): return _dispatch_method("imestate", "fn", *args);
def browsemode(*args): return _dispatch_method("browsemode", "fn", *args);
def keypressed(*args): return _dispatch_method("keypressed", "fn", *args);
def replay(*args): return _dispatch_method("replay", "fn", *args);
def searchmode(*args): return _dispatch_method("searchmode", "fn", *args);
def searchoption(*args): return _dispatch_method("searchoption", "fn", *args);
def searchoption2(*args): return _dispatch_method("searchoption2", "fn", *args);
def foundtopx(*args): return _dispatch_method("foundtopx", "fn", *args);
def foundtopy(*args): return _dispatch_method("foundtopy", "fn", *args);
def foundendx(*args): return _dispatch_method("foundendx", "fn", *args);
def foundendy(*args): return _dispatch_method("foundendy", "fn", *args);
def foundhilighting(*args): return _dispatch_method("foundhilighting", "fn", *args);
def foundoption(*args): return _dispatch_method("foundoption", "fn", *args);
def readonly(*args): return _dispatch_method("readonly", "fn", *args);
def encode(*args): return _dispatch_method("encode", "fn", *args);
def charset(*args): return _dispatch_method("charset", "fn", *args);
def bom(*args): return _dispatch_method("bom", "fn", *args);
def codepage(*args): return _dispatch_method("codepage", "fn", *args);
def getfocus(*args): return _dispatch_method("getfocus", "fn", *args);
def autocompstate(*args): return _dispatch_method("autocompstate", "fn", *args);
def argcount(*args): return _dispatch_method("argcount", "fn", *args);
def compatiblemode(*args): return _dispatch_method("compatiblemode", "fn", *args);
def carettabmode(*args): return _dispatch_method("carettabmode", "fn", *args);
def return_in_cell_mode(*args): return _dispatch_method("return_in_cell_mode", "fn", *args);
def stophistory(*args): return _dispatch_method("stophistory", "fn", *args);
def fontmode(*args): return _dispatch_method("fontmode", "fn", *args);
def formline(*args): return _dispatch_method("formline", "fn", *args);
def configstate(*args): return _dispatch_method("configstate", "fn", *args);
def fontsize(*args): return _dispatch_method("fontsize", "fn", *args);
def dayofweeknum(*args): return _dispatch_method("dayofweeknum", "fn", *args);
def tickcount(*args): return _dispatch_method("tickcount", "fn", *args);
def foldable(*args): return _dispatch_method("foldable", "fn", *args);
def folded(*args): return _dispatch_method("folded", "fn", *args);
def rangeedittop(*args): return _dispatch_method("rangeedittop", "fn", *args);
def rangeeditend(*args): return _dispatch_method("rangeeditend", "fn", *args);
def rangeeditmode(*args): return _dispatch_method("rangeeditmode", "fn", *args);
def outlinehandle(*args): return _dispatch_method("outlinehandle", "fn", *args);
def outlinesize(*args): return _dispatch_method("outlinesize", "fn", *args);
def outlineitemcount(*args): return _dispatch_method("outlineitemcount", "fn", *args);
def val(*args): return _dispatch_method("val", "fn", *args);
def ascii(*args): return _dispatch_method("ascii", "fn", *args);
def strlen(*args): return _dispatch_method("strlen", "fn", *args);
def strstr(*args): return _dispatch_method("strstr", "fn", *args);
def strrstr(*args): return _dispatch_method("strrstr", "fn", *args);
def wcslen(*args): return _dispatch_method("wcslen", "fn", *args);
def wcsstrstr(*args): return _dispatch_method("wcsstrstr", "fn", *args);
def wcsstrrstr(*args): return _dispatch_method("wcsstrrstr", "fn", *args);
def ucs4len(*args): return _dispatch_method("ucs4len", "fn", *args);
def ucs4strstr(*args): return _dispatch_method("ucs4strstr", "fn", *args);
def ucs4strrstr(*args): return _dispatch_method("ucs4strrstr", "fn", *args);
def cmulen(*args): return _dispatch_method("cmulen", "fn", *args);
def cmustrstr(*args): return _dispatch_method("cmustrstr", "fn", *args);
def cmustrrstr(*args): return _dispatch_method("cmustrrstr", "fn", *args);
def gculen(*args): return _dispatch_method("gculen", "fn", *args);
def gcustrstr(*args): return _dispatch_method("gcustrstr", "fn", *args);
def gcustrrstr(*args): return _dispatch_method("gcustrrstr", "fn", *args);
def wcs_to_char(*args): return _dispatch_method("wcs_to_char", "fn", *args);
def char_to_wcs(*args): return _dispatch_method("char_to_wcs", "fn", *args);
def ucs4_to_char(*args): return _dispatch_method("ucs4_to_char", "fn", *args);
def char_to_ucs4(*args): return _dispatch_method("char_to_ucs4", "fn", *args);
def cmu_to_char(*args): return _dispatch_method("cmu_to_char", "fn", *args);
def char_to_cmu (*args): return _dispatch_method("char_to_cmu ", "fn", *args);
def gcu_to_char(*args): return _dispatch_method("gcu_to_char", "fn", *args);
def char_to_gcu(*args): return _dispatch_method("char_to_gcu", "fn", *args);
def byteindex_to_charindex(*args): return _dispatch_method("byteindex_to_charindex", "fn", *args);
def charindex_to_byteindex(*args): return _dispatch_method("charindex_to_byteindex", "fn", *args);
def findwindow(*args): return _dispatch_method("findwindow", "fn", *args);
def findwindowclass(*args): return _dispatch_method("findwindowclass", "fn", *args);
def sendmessage(*args): return _dispatch_method("sendmessage", "fn", *args);
def xtocolumn(*args): return _dispatch_method("xtocolumn", "fn", *args);
def ytolineno(*args): return _dispatch_method("ytolineno", "fn", *args);
def columntox(*args): return _dispatch_method("columntox", "fn", *args);
def linenotoy(*args): return _dispatch_method("linenotoy", "fn", *args);
def charcount(*args): return _dispatch_method("charcount", "fn", *args);
def existfile(*args): return _dispatch_method("existfile", "fn", *args);
def getmaxinfo(*args): return _dispatch_method("getmaxinfo", "fn", *args);
def keypressedex(*args): return _dispatch_method("keypressedex", "fn", *args);
def setcompatiblemode(*args): return _dispatch_method("setcompatiblemode", "fn", *args);
def inputchar(*args): return _dispatch_method("inputchar", "fn", *args);
def iskeydown(*args): return _dispatch_method("iskeydown", "fn", *args);
def getininum(*args): return _dispatch_method("getininum", "fn", *args);
def getininumw(*args): return _dispatch_method("getininumw", "fn", *args);
def getregnum(*args): return _dispatch_method("getregnum", "fn", *args);
def getconfigcolor(*args): return _dispatch_method("getconfigcolor", "fn", *args);
def hidemaruorder(*args): return _dispatch_method("hidemaruorder", "fn", *args);
def hidemarucount(*args): return _dispatch_method("hidemarucount", "fn", *args);
def findhidemaru(*args): return _dispatch_method("findhidemaru", "fn", *args);
def hidemaruhandle(*args): return _dispatch_method("hidemaruhandle", "fn", *args);
def getcurrenttab(*args): return _dispatch_method("getcurrenttab", "fn", *args);
def gettabhandle(*args): return _dispatch_method("gettabhandle", "fn", *args);
def getclipboardinfo(*args): return _dispatch_method("getclipboardinfo", "fn", *args);
def event(*args): return _dispatch_method("event", "fn", *args);
def geteventnotify(*args): return _dispatch_method("geteventnotify", "fn", *args);
def loaddll(*args): return _dispatch_method("loaddll", "fn", *args);
def dllfunc(*args): return _dispatch_method("dllfunc", "fn", *args);
def dllfuncw(*args): return _dispatch_method("dllfuncw", "fn", *args);
def dllfuncexist(*args): return _dispatch_method("dllfuncexist", "fn", *args);
def createobject(*args): return _dispatch_method("createobject", "fn", *args);
def releaseobject(*args): return _dispatch_method("releaseobject", "fn", *args);
# def member_rnum(*args): return _dispatch_method("member_rnum", "fn", *args);

def findmarker(*args): return _dispatch_method("findmarker", "fs", *args);
def diff(*args): return _dispatch_method("diff", "fs", *args);
def reservedmultisel(*args): return _dispatch_method("reservedmultisel", "fs", *args);
def regulardll(*args): return _dispatch_method("regulardll", "fs", *args);
def filename(*args): return _dispatch_method("filename", "fs", *args);
def filename2(*args): return _dispatch_method("filename2", "fs", *args);
def filename3(*args): return _dispatch_method("filename3", "fs", *args);
def basename(*args): return _dispatch_method("basename", "fs", *args);
def basename2(*args): return _dispatch_method("basename2", "fs", *args);
def basename3(*args): return _dispatch_method("basename3", "fs", *args);
def directory(*args): return _dispatch_method("directory", "fs", *args);
def directory2(*args): return _dispatch_method("directory2", "fs", *args);
def directory3(*args): return _dispatch_method("directory3", "fs", *args);
def filetype(*args): return _dispatch_method("filetype", "fs", *args);
def currentmacrofilename(*args): return _dispatch_method("currentmacrofilename", "fs", *args);
def currentmacrobasename(*args): return _dispatch_method("currentmacrobasename", "fs", *args);
def currentmacrodirectory(*args): return _dispatch_method("currentmacrodirectory", "fs", *args);
def hidemarudir(*args): return _dispatch_method("hidemarudir", "fs", *args);
def macrodir(*args): return _dispatch_method("macrodir", "fs", *args);
def settingdir(*args): return _dispatch_method("settingdir", "fs", *args);
def backupdir(*args): return _dispatch_method("backupdir", "fs", *args);
def windir(*args): return _dispatch_method("windir", "fs", *args);
def winsysdir(*args): return _dispatch_method("winsysdir", "fs", *args);
def searchbuffer(*args): return _dispatch_method("searchbuffer", "fs", *args);
def targetcolormarker(*args): return _dispatch_method("targetcolormarker", "fs", *args);
def replacebuffer(*args): return _dispatch_method("replacebuffer", "fs", *args);
def grepfilebuffer(*args): return _dispatch_method("grepfilebuffer", "fs", *args);
def grepfolderbuffer(*args): return _dispatch_method("grepfolderbuffer", "fs", *args);
def foundbuffer(*args): return _dispatch_method("foundbuffer", "fs", *args);
def currentconfigset(*args): return _dispatch_method("currentconfigset", "fs", *args);
def fontname(*args): return _dispatch_method("fontname", "fs", *args);
def date(*args): return _dispatch_method("date", "fs", *args);
def time(*args): return _dispatch_method("time", "fs", *args);
def year(*args): return _dispatch_method("year", "fs", *args);
def month(*args): return _dispatch_method("month", "fs", *args);
def day(*args): return _dispatch_method("day", "fs", *args);
def hour(*args): return _dispatch_method("hour", "fs", *args);
def minute(*args): return _dispatch_method("minute", "fs", *args);
def second(*args): return _dispatch_method("second", "fs", *args);
def dayofweek(*args): return _dispatch_method("dayofweek", "fs", *args);
# def str(*args): return _dispatch_method("str", "fs", *args);
def char(*args): return _dispatch_method("char", "fs", *args);
def unichar(*args): return _dispatch_method("unichar", "fs", *args);
def hex(*args): return _dispatch_method("hex", "fs", *args);
def sprintf(*args): return _dispatch_method("sprintf", "fs", *args);
def leftstr(*args): return _dispatch_method("leftstr", "fs", *args);
def rightstr(*args): return _dispatch_method("rightstr", "fs", *args);
def midstr(*args): return _dispatch_method("midstr", "fs", *args);
def wcsleftstr(*args): return _dispatch_method("wcsleftstr", "fs", *args);
def wcsrightstr(*args): return _dispatch_method("wcsrightstr", "fs", *args);
def wcsmidstr(*args): return _dispatch_method("wcsmidstr", "fs", *args);
def ucs4leftstr(*args): return _dispatch_method("ucs4leftstr", "fs", *args);
def ucs4rightstr(*args): return _dispatch_method("ucs4rightstr", "fs", *args);
def ucs4midstr(*args): return _dispatch_method("ucs4midstr", "fs", *args);
def cmuleftstr(*args): return _dispatch_method("cmuleftstr", "fs", *args);
def cmurightstr(*args): return _dispatch_method("cmurightstr", "fs", *args);
def cmumidstr(*args): return _dispatch_method("cmumidstr", "fs", *args);
def gculeftstr(*args): return _dispatch_method("gculeftstr", "fs", *args);
def gcurightstr(*args): return _dispatch_method("gcurightstr", "fs", *args);
def gcumidstr(*args): return _dispatch_method("gcumidstr", "fs", *args);
def gettext(*args): return _dispatch_method("gettext", "fs", *args);
def gettext2(*args): return _dispatch_method("gettext2", "fs", *args);
def gettext_wcs(*args): return _dispatch_method("gettext_wcs", "fs", *args);
def gettext_ucs4(*args): return _dispatch_method("gettext_ucs4", "fs", *args);
def gettext_cmu(*args): return _dispatch_method("gettext_cmu", "fs", *args);
def gettext_gcu(*args): return _dispatch_method("gettext_gcu", "fs", *args);
def getenv(*args): return _dispatch_method("getenv", "fs", *args);
def getgrepfilehist(*args): return _dispatch_method("getgrepfilehist", "fs", *args);
def enumcolormarkerlayer(*args): return _dispatch_method("enumcolormarkerlayer", "fs", *args);
def getfiletime(*args): return _dispatch_method("getfiletime", "fs", *args);
def getoutlineitem(*args): return _dispatch_method("getoutlineitem", "fs", *args);
def getarg(*args): return _dispatch_method("getarg", "fs", *args);
def getautocompitem(*args): return _dispatch_method("getautocompitem", "fs", *args);
def getcolormarker(*args): return _dispatch_method("getcolormarker", "fs", *args);
def getfilehist(*args): return _dispatch_method("getfilehist", "fs", *args);
def getpathhist(*args): return _dispatch_method("getpathhist", "fs", *args);
def getreplacehist(*args): return _dispatch_method("getreplacehist", "fs", *args);
def getresultex(*args): return _dispatch_method("getresultex", "fs", *args);
def getsearchhist(*args): return _dispatch_method("getsearchhist", "fs", *args);
def gettagsfile(*args): return _dispatch_method("gettagsfile", "fs", *args);
def gettitle(*args): return _dispatch_method("gettitle", "fs", *args);
def browsefile(*args): return _dispatch_method("browsefile", "fs", *args);
def quote(*args): return _dispatch_method("quote", "fs", *args);
def strreplace(*args): return _dispatch_method("strreplace", "fs", *args);
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
        return _dispatch_method("toupper", "fs", *args)
    else:
        return _dispatch_method("toupper", "st", *args)

# 分岐あり
def tolower(*args):
    if len(args)>=1 and (type(args[0]) is str):
        return _dispatch_method("tolower", "fs", *args)
    else:
        return _dispatch_method("tolower", "st", *args)

# 分岐あり
def filter(*args):
    if len(args)>=4:
        return _dispatch_method("filter", "fs", *args)
    else:
        return _dispatch_method("filter", "st", *args)

def input(*args): return _dispatch_method("input", "fs", *args);
def getinistr(*args): return _dispatch_method("getinistr", "fs", *args);
def getinistrw(*args): return _dispatch_method("getinistrw", "fs", *args);
def getregbinary(*args): return _dispatch_method("getregbinary", "fs", *args);
def getregstr(*args): return _dispatch_method("getregstr", "fs", *args);
def enumregkey(*args): return _dispatch_method("enumregkey", "fs", *args);
def enumregvalue(*args): return _dispatch_method("enumregvalue", "fs", *args);
def getconfig(*args): return _dispatch_method("getconfig", "fs", *args);
def gettabstop(*args): return _dispatch_method("gettabstop", "fs", *args);
def getstaticvariable(*args): return _dispatch_method("getstaticvariable", "fs", *args);
def getclipboard(*args): return _dispatch_method("getclipboard", "fs", *args);
def geteventparam(*args): return _dispatch_method("geteventparam", "fs", *args);
def dllfuncstr(*args): return _dispatch_method("dllfuncstr", "fs", *args);
def dllfuncstrw(*args): return _dispatch_method("dllfuncstrw", "fs", *args);
def loaddllfile(*args): return _dispatch_method("loaddllfile", "fs", *args);
# def member_rstr(*args): return _dispatch_method("member", "fs", *args);

def refreshdatetime(*args): return _dispatch_method("refreshdatetime", "st", *args);
def newfile(*args): return _dispatch_method("newfile", "st", *args);
def openfile(*args): return _dispatch_method("openfile", "st", *args);
def loadfile(*args): return _dispatch_method("loadfile", "st", *args);
def openfilepart(*args): return _dispatch_method("openfilepart", "st", *args);
def closenew(*args): return _dispatch_method("closenew", "st", *args);
def saveas(*args): return _dispatch_method("saveas", "st", *args);
def appendsave(*args): return _dispatch_method("appendsave", "st", *args);
def changename(*args): return _dispatch_method("changename", "st", *args);
def insertfile(*args): return _dispatch_method("insertfile", "st", *args);
def readonlyopenfile(*args): return _dispatch_method("readonlyopenfile", "st", *args);
def readonlyloadfile(*args): return _dispatch_method("readonlyloadfile", "st", *args);
def save(*args): return _dispatch_method("save", "st", *args);
def savelf(*args): return _dispatch_method("savelf", "st", *args);
def print(*args): return _dispatch_method("print", "st", *args);
def saveall(*args): return _dispatch_method("saveall", "st", *args);
def saveupdatedall(*args): return _dispatch_method("saveupdatedall", "st", *args);
def openbyshell(*args): return _dispatch_method("openbyshell", "st", *args);
def openbyhidemaru(*args): return _dispatch_method("openbyhidemaru", "st", *args);
def setfilehist(*args): return _dispatch_method("setfilehist", "st", *args);
def setpathhist(*args): return _dispatch_method("setpathhist", "st", *args);
def setencode(*args): return _dispatch_method("setencode", "st", *args);
def stophistoryswitch(*args): return _dispatch_method("stophistoryswitch", "st", *args);
def deletefilehist(*args): return _dispatch_method("deletefilehist", "st", *args);
def OPEN(*args): return _dispatch_method("OPEN", "st", *args);
def SAVEAS(*args): return _dispatch_method("SAVEAS", "st", *args);
def LOAD(*args): return _dispatch_method("LOAD", "st", *args);
def APPENDSAVE(*args): return _dispatch_method("APPENDSAVE", "st", *args);
def CHANGENAME(*args): return _dispatch_method("CHANGENAME", "st", *args);
def INSERTFILE(*args): return _dispatch_method("INSERTFILE", "st", *args);
def OPENFILEPART(*args): return _dispatch_method("OPENFILEPART", "st", *args);
def deletefile(*args): return _dispatch_method("deletefile", "st", *args);
def propertydialog(*args): return _dispatch_method("propertydialog", "st", *args);
# def exit(*args): return _dispatch_method("exit", "st", *args);
# def exitall(*args): return _dispatch_method("exitall", "st", *args);
# def saveexit(*args): return _dispatch_method("saveexit", "st", *args);
# def saveexitall(*args): return _dispatch_method("saveexitall", "st", *args);
# def quit(*args): return _dispatch_method("quit", "st", *args);
# def quitall(*args): return _dispatch_method("quitall", "st", *args);
def up(*args): return _dispatch_method("up", "st", *args);
def down(*args): return _dispatch_method("down", "st", *args);
def right(*args): return _dispatch_method("right", "st", *args);
def left(*args): return _dispatch_method("left", "st", *args);
def up_nowrap(*args): return _dispatch_method("up_nowrap", "st", *args);
def down_nowrap(*args): return _dispatch_method("down_nowrap", "st", *args);
def shiftup(*args): return _dispatch_method("shiftup", "st", *args);
def shiftdown(*args): return _dispatch_method("shiftdown", "st", *args);
def shiftright(*args): return _dispatch_method("shiftright", "st", *args);
def shiftleft(*args): return _dispatch_method("shiftleft", "st", *args);
def gofileend(*args): return _dispatch_method("gofileend", "st", *args);
def gofiletop(*args): return _dispatch_method("gofiletop", "st", *args);
def gokakko(*args): return _dispatch_method("gokakko", "st", *args);
def golastupdated(*args): return _dispatch_method("golastupdated", "st", *args);
def goleftkakko(*args): return _dispatch_method("goleftkakko", "st", *args);
def gorightkakko(*args): return _dispatch_method("gorightkakko", "st", *args);
def golinetop(*args): return _dispatch_method("golinetop", "st", *args);
def golinetop2(*args): return _dispatch_method("golinetop2", "st", *args);
def golineend(*args): return _dispatch_method("golineend", "st", *args);
def golineend2(*args): return _dispatch_method("golineend2", "st", *args);
def golineend3(*args): return _dispatch_method("golineend3", "st", *args);
def goscreenend(*args): return _dispatch_method("goscreenend", "st", *args);
def goscreentop(*args): return _dispatch_method("goscreentop", "st", *args);
def jump(*args): return _dispatch_method("jump", "st", *args);
def moveto(*args): return _dispatch_method("moveto", "st", *args);
def movetolineno(*args): return _dispatch_method("movetolineno", "st", *args);
def movetoview(*args): return _dispatch_method("movetoview", "st", *args);
def moveto2(*args): return _dispatch_method("moveto2", "st", *args);
def moveto_wcs(*args): return _dispatch_method("moveto_wcs", "st", *args);
def moveto_ucs4(*args): return _dispatch_method("moveto_ucs4", "st", *args);
def moveto_cmu(*args): return _dispatch_method("moveto_cmu", "st", *args);
def moveto_gcu(*args): return _dispatch_method("moveto_gcu", "st", *args);
def nextpage(*args): return _dispatch_method("nextpage", "st", *args);
def prevpage(*args): return _dispatch_method("prevpage", "st", *args);
def halfnextpage(*args): return _dispatch_method("halfnextpage", "st", *args);
def halfprevpage(*args): return _dispatch_method("halfprevpage", "st", *args);
def rollup(*args): return _dispatch_method("rollup", "st", *args);
def rollup2(*args): return _dispatch_method("rollup2", "st", *args);
def rolldown(*args): return _dispatch_method("rolldown", "st", *args);
def rolldown2(*args): return _dispatch_method("rolldown2", "st", *args);
def wordleft(*args): return _dispatch_method("wordleft", "st", *args);
def wordleft2(*args): return _dispatch_method("wordleft2", "st", *args);
def wordright(*args): return _dispatch_method("wordright", "st", *args);
def wordright2(*args): return _dispatch_method("wordright2", "st", *args);
def wordrightsalnen(*args): return _dispatch_method("wordrightsalnen", "st", *args);
def wordrightsalnen2(*args): return _dispatch_method("wordrightsalnen2", "st", *args);
def gowordtop(*args): return _dispatch_method("gowordtop", "st", *args);
def gowordend(*args): return _dispatch_method("gowordend", "st", *args);
def gowordtop2(*args): return _dispatch_method("gowordtop2", "st", *args);
def gowordend2(*args): return _dispatch_method("gowordend2", "st", *args);
def prevpos(*args): return _dispatch_method("prevpos", "st", *args);
def prevposhistback(*args): return _dispatch_method("prevposhistback", "st", *args);
def prevposhistforward(*args): return _dispatch_method("prevposhistforward", "st", *args);
def setmark(*args): return _dispatch_method("setmark", "st", *args);
def clearallmark(*args): return _dispatch_method("clearallmark", "st", *args);
def marklist(*args): return _dispatch_method("marklist", "st", *args);
def nextmark(*args): return _dispatch_method("nextmark", "st", *args);
def prevmark(*args): return _dispatch_method("prevmark", "st", *args);
def prevfunc(*args): return _dispatch_method("prevfunc", "st", *args);
def nextfunc(*args): return _dispatch_method("nextfunc", "st", *args);
def nextresult(*args): return _dispatch_method("nextresult", "st", *args);
def prevresult(*args): return _dispatch_method("prevresult", "st", *args);
def gotagpair(*args): return _dispatch_method("gotagpair", "st", *args);
def backtab(*args): return _dispatch_method("backtab", "st", *args);
def forwardtab(*args): return _dispatch_method("forwardtab", "st", *args);
def appendcopy(*args): return _dispatch_method("appendcopy", "st", *args);
def appendcut(*args): return _dispatch_method("appendcut", "st", *args);
def beginrect(*args): return _dispatch_method("beginrect", "st", *args);
def beginrectmulti(*args): return _dispatch_method("beginrectmulti", "st", *args);
def beginsel(*args): return _dispatch_method("beginsel", "st", *args);
def beginlinesel(*args): return _dispatch_method("beginlinesel", "st", *args);
def endsel(*args): return _dispatch_method("endsel", "st", *args);
def copy(*args): return _dispatch_method("copy", "st", *args);
def copy2(*args): return _dispatch_method("copy2", "st", *args);
def cut(*args): return _dispatch_method("cut", "st", *args);
def copyline(*args): return _dispatch_method("copyline", "st", *args);
def cutline(*args): return _dispatch_method("cutline", "st", *args);
def cutafter(*args): return _dispatch_method("cutafter", "st", *args);
def copyword(*args): return _dispatch_method("copyword", "st", *args);
def cutword(*args): return _dispatch_method("cutword", "st", *args);
def escapeselect(*args): return _dispatch_method("escapeselect", "st", *args);
def paste(*args): return _dispatch_method("paste", "st", *args);
def pasterect(*args): return _dispatch_method("pasterect", "st", *args);
def refpaste(*args): return _dispatch_method("refpaste", "st", *args);
def refcopy(*args): return _dispatch_method("refcopy", "st", *args);
def refcopy2(*args): return _dispatch_method("refcopy2", "st", *args);
def selectall(*args): return _dispatch_method("selectall", "st", *args);
def selectline(*args): return _dispatch_method("selectline", "st", *args);
def selectword(*args): return _dispatch_method("selectword", "st", *args);
def selectword2(*args): return _dispatch_method("selectword2", "st", *args);
def showcliphist(*args): return _dispatch_method("showcliphist", "st", *args);
def poppaste(*args): return _dispatch_method("poppaste", "st", *args);
def poppaste2(*args): return _dispatch_method("poppaste2", "st", *args);
def getcliphist(*args): return _dispatch_method("getcliphist", "st", *args);
def clearcliphist(*args): return _dispatch_method("clearcliphist", "st", *args);
def selectcfunc(*args): return _dispatch_method("selectcfunc", "st", *args);
def copyurl(*args): return _dispatch_method("copyurl", "st", *args);
def copyformed(*args): return _dispatch_method("copyformed", "st", *args);
def selectcolumn(*args): return _dispatch_method("selectcolumn", "st", *args);
def tomultiselect(*args): return _dispatch_method("tomultiselect", "st", *args);
def invertselection(*args): return _dispatch_method("invertselection", "st", *args);
def reservemultisel(*args): return _dispatch_method("reservemultisel", "st", *args);
def selectreservedmultisel(*args): return _dispatch_method("selectreservedmultisel", "st", *args);
def clearreservedmultisel(*args): return _dispatch_method("clearreservedmultisel", "st", *args);
def clearreservedmultiselall(*args): return _dispatch_method("clearreservedmultiselall", "st", *args);
def backspace(*args): return _dispatch_method("backspace", "st", *args);
def delete(*args): return _dispatch_method("del", "st", *args);
def deleteafter(*args): return _dispatch_method("deleteafter", "st", *args);
def deletebefore(*args): return _dispatch_method("deletebefore", "st", *args);
def deleteline(*args): return _dispatch_method("deleteline", "st", *args);
def deleteline2(*args): return _dispatch_method("deleteline2", "st", *args);
def deleteword(*args): return _dispatch_method("deleteword", "st", *args);
def deletewordall(*args): return _dispatch_method("deletewordall", "st", *args);
def deletewordfront(*args): return _dispatch_method("deletewordfront", "st", *args);
def dupline(*args): return _dispatch_method("dupline", "st", *args);
def insertline(*args): return _dispatch_method("insertline", "st", *args);
def insertreturn(*args): return _dispatch_method("insertreturn", "st", *args);
def tab(*args): return _dispatch_method("tab", "st", *args);
def undelete(*args): return _dispatch_method("undelete", "st", *args);
def undo(*args): return _dispatch_method("undo", "st", *args);
def redo(*args): return _dispatch_method("redo", "st", *args);
def casechange(*args): return _dispatch_method("casechange", "st", *args);
def indent(*args): return _dispatch_method("indent", "st", *args);
def unindent(*args): return _dispatch_method("unindent", "st", *args);
def shifttab(*args): return _dispatch_method("shifttab", "st", *args);
def tospace(*args): return _dispatch_method("tospace", "st", *args);
def totab(*args): return _dispatch_method("totab", "st", *args);
def tohankaku(*args): return _dispatch_method("tohankaku", "st", *args);
def tozenkakuhira(*args): return _dispatch_method("tozenkakuhira", "st", *args);
def tozenkakukata(*args): return _dispatch_method("tozenkakukata", "st", *args);
def capslockforgot(*args): return _dispatch_method("capslockforgot", "st", *args);
def imeconvforgot(*args): return _dispatch_method("imeconvforgot", "st", *args);
def reopen(*args): return _dispatch_method("reopen", "st", *args);
def filtermenu(*args): return _dispatch_method("filtermenu", "st", *args);
def autocomplete(*args): return _dispatch_method("autocomplete", "st", *args);
def form(*args): return _dispatch_method("form", "st", *args);
def unform(*args): return _dispatch_method("unform", "st", *args);
def showformline(*args): return _dispatch_method("showformline", "st", *args);
def clearundobuffer(*args): return _dispatch_method("clearundobuffer", "st", *args);
def template(*args): return _dispatch_method("template", "st", *args);
def find1(*args): return _dispatch_method("find1", "st", *args);
def find2(*args): return _dispatch_method("find2", "st", *args);
def findword(*args): return _dispatch_method("findword", "st", *args);
def replace1(*args): return _dispatch_method("replace1", "st", *args);
def replaceall(*args): return _dispatch_method("replaceall", "st", *args);
def replaceallfast(*args): return _dispatch_method("replaceallfast", "st", *args);
def replaceallquick(*args): return _dispatch_method("replaceallquick", "st", *args);
def finddown(*args): return _dispatch_method("finddown", "st", *args);
def finddown2(*args): return _dispatch_method("finddown2", "st", *args);
def findup(*args): return _dispatch_method("findup", "st", *args);
def findup2(*args): return _dispatch_method("findup2", "st", *args);
def getsearch(*args): return _dispatch_method("getsearch", "st", *args);
def gosearchstarted(*args): return _dispatch_method("gosearchstarted", "st", *args);
def setsearch(*args): return _dispatch_method("setsearch", "st", *args);
def setsearchhist(*args): return _dispatch_method("setsearchhist", "st", *args);
def setreplace(*args): return _dispatch_method("setreplace", "st", *args);
def setreplacehist(*args): return _dispatch_method("setreplacehist", "st", *args);
def setgrepfile(*args): return _dispatch_method("setgrepfile", "st", *args);
def forceinselect(*args): return _dispatch_method("forceinselect", "st", *args);
def goupdatedown(*args): return _dispatch_method("goupdatedown", "st", *args);
def goupdateup(*args): return _dispatch_method("goupdateup", "st", *args);
def clearupdates(*args): return _dispatch_method("clearupdates", "st", *args);
def grep(*args): return _dispatch_method("grep", "st", *args);
def grepdialog(*args): return _dispatch_method("grepdialog", "st", *args);
def grepdialog2(*args): return _dispatch_method("grepdialog2", "st", *args);
def localgrep(*args): return _dispatch_method("localgrep", "st", *args);
def grepreplace(*args): return _dispatch_method("grepreplace", "st", *args);
def grepreplacedialog2(*args): return _dispatch_method("grepreplacedialog2", "st", *args);
def escapeinselect(*args): return _dispatch_method("escapeinselect", "st", *args);
def hilightfound(*args): return _dispatch_method("hilightfound", "st", *args);
def colormarker(*args): return _dispatch_method("colormarker", "st", *args);
def nextcolormarker(*args): return _dispatch_method("nextcolormarker", "st", *args);
def prevcolormarker(*args): return _dispatch_method("prevcolormarker", "st", *args);
def colormarkerdialog(*args): return _dispatch_method("colormarkerdialog", "st", *args);
def deletecolormarker(*args): return _dispatch_method("deletecolormarker", "st", *args);
def deletecolormarkerall(*args): return _dispatch_method("deletecolormarkerall", "st", *args);
def selectcolormarker(*args): return _dispatch_method("selectcolormarker", "st", *args);
def selectallfound(*args): return _dispatch_method("selectallfound", "st", *args);
def colormarkerallfound(*args): return _dispatch_method("colormarkerallfound", "st", *args);
def clearcolormarkerallfound(*args): return _dispatch_method("clearcolormarkerallfound", "st", *args);
def foundlist(*args): return _dispatch_method("foundlist", "st", *args);
def foundlistoutline(*args): return _dispatch_method("foundlistoutline", "st", *args);
def findmarkerlist(*args): return _dispatch_method("findmarkerlist", "st", *args);
def selectinselect(*args): return _dispatch_method("selectinselect", "st", *args);
def setinselect2(*args): return _dispatch_method("setinselect2", "st", *args);
def settargetcolormarker(*args): return _dispatch_method("settargetcolormarker", "st", *args);
def colormarkersnapshot(*args): return _dispatch_method("colormarkersnapshot", "st", *args);
def restoredesktop(*args): return _dispatch_method("restoredesktop", "st", *args);
def savedesktop(*args): return _dispatch_method("savedesktop", "st", *args);
def scrolllink(*args): return _dispatch_method("scrolllink", "st", *args);
def split(*args): return _dispatch_method("split", "st", *args);
def setsplitinfo(*args): return _dispatch_method("setsplitinfo", "st", *args);
def splitswitch(*args): return _dispatch_method("splitswitch", "st", *args);
def windowcascade(*args): return _dispatch_method("windowcascade", "st", *args);
def windowhorz(*args): return _dispatch_method("windowhorz", "st", *args);
def windowtiling(*args): return _dispatch_method("windowtiling", "st", *args);
def windowvert(*args): return _dispatch_method("windowvert", "st", *args);
def windowlist(*args): return _dispatch_method("windowlist", "st", *args);
def compfile(*args): return _dispatch_method("compfile", "st", *args);
def COMPFILE(*args): return _dispatch_method("COMPFILE", "st", *args);
def nextcompfile(*args): return _dispatch_method("nextcompfile", "st", *args);
def prevcompfile(*args): return _dispatch_method("prevcompfile", "st", *args);
def alwaystopswitch(*args): return _dispatch_method("alwaystopswitch", "st", *args);
def settabmode(*args): return _dispatch_method("settabmode", "st", *args);
def settabgroup(*args): return _dispatch_method("settabgroup", "st", *args);
def settaborder(*args): return _dispatch_method("settaborder", "st", *args);
def iconthistab(*args): return _dispatch_method("iconthistab", "st", *args);
def fullscreen(*args): return _dispatch_method("fullscreen", "st", *args);
def backtagjump(*args): return _dispatch_method("backtagjump", "st", *args);
def directtagjump(*args): return _dispatch_method("directtagjump", "st", *args);
def freecursorswitch(*args): return _dispatch_method("freecursorswitch", "st", *args);
def imeswitch(*args): return _dispatch_method("imeswitch", "st", *args);
def imeregisterword(*args): return _dispatch_method("imeregisterword", "st", *args);
def help(*args): return _dispatch_method("help", "st", *args);
def help2(*args): return _dispatch_method("help2", "st", *args);
def help3(*args): return _dispatch_method("help3", "st", *args);
def help4(*args): return _dispatch_method("help4", "st", *args);
def help5(*args): return _dispatch_method("help5", "st", *args);
def help6(*args): return _dispatch_method("help6", "st", *args);
def hidemaruhelp(*args): return _dispatch_method("hidemaruhelp", "st", *args);
def macrohelp(*args): return _dispatch_method("macrohelp", "st", *args);
def overwriteswitch(*args): return _dispatch_method("overwriteswitch", "st", *args);
def readonlyswitch(*args): return _dispatch_method("readonlyswitch", "st", *args);
def showcode(*args): return _dispatch_method("showcode", "st", *args);
def showcharcount(*args): return _dispatch_method("showcharcount", "st", *args);
def showlineno(*args): return _dispatch_method("showlineno", "st", *args);
def tagjump(*args): return _dispatch_method("tagjump", "st", *args);
def redraw(*args): return _dispatch_method("redraw", "st", *args);
def browsemodeswitch(*args): return _dispatch_method("browsemodeswitch", "st", *args);
def clist(*args): return _dispatch_method("clist", "st", *args);
def clearupdated(*args): return _dispatch_method("clearupdated", "st", *args);
def refreshtabstop(*args): return _dispatch_method("refreshtabstop", "st", *args);
def refreshtabstop_shrink(*args): return _dispatch_method("refreshtabstop_shrink", "st", *args);
def refreshtabstop_current(*args): return _dispatch_method("refreshtabstop_current", "st", *args);
def autospellcheckswitch(*args): return _dispatch_method("autospellcheckswitch", "st", *args);
def spellcheckdialog(*args): return _dispatch_method("spellcheckdialog", "st", *args);
def savebacktagjump(*args): return _dispatch_method("savebacktagjump", "st", *args);
def fold(*args): return _dispatch_method("fold", "st", *args);
def unfold(*args): return _dispatch_method("unfold", "st", *args);
def nextfoldable(*args): return _dispatch_method("nextfoldable", "st", *args);
def prevfoldable(*args): return _dispatch_method("prevfoldable", "st", *args);
def selectfoldable(*args): return _dispatch_method("selectfoldable", "st", *args);
def foldall(*args): return _dispatch_method("foldall", "st", *args);
def unfoldall(*args): return _dispatch_method("unfoldall", "st", *args);
def rangeeditin(*args): return _dispatch_method("rangeeditin", "st", *args);
def rangeeditout(*args): return _dispatch_method("rangeeditout", "st", *args);
def nextoutlineitem(*args): return _dispatch_method("nextoutlineitem", "st", *args);
def prevoutlineitem(*args): return _dispatch_method("prevoutlineitem", "st", *args);
def showoutline(*args): return _dispatch_method("showoutline", "st", *args);
def showoutlinebar(*args): return _dispatch_method("showoutlinebar", "st", *args);
def showfoldingbar(*args): return _dispatch_method("showfoldingbar", "st", *args);
def syncoutline(*args): return _dispatch_method("syncoutline", "st", *args);
def refreshoutline(*args): return _dispatch_method("refreshoutline", "st", *args);
def setoutlinesize(*args): return _dispatch_method("setoutlinesize", "st", *args);
def beep(*args): return _dispatch_method("beep", "st", *args);
def play(*args): return _dispatch_method("play", "st", *args);
def playsync(*args): return _dispatch_method("playsync", "st", *args);
def debuginfo(*args): return _dispatch_method("debuginfo", "st", *args);
def showvars(*args): return _dispatch_method("showvars", "st", *args);
def title(*args): return _dispatch_method("title", "st", *args);
def run(*args): return _dispatch_method("run", "st", *args);
def runsync(*args): return _dispatch_method("runsync", "st", *args);
def runsync2(*args): return _dispatch_method("runsync2", "st", *args);
def runex(*args): return _dispatch_method("runex", "st", *args);
def disabledraw(*args): return _dispatch_method("disabledraw", "st", *args);
def enabledraw(*args): return _dispatch_method("enabledraw", "st", *args);
def disabledraw2(*args): return _dispatch_method("disabledraw2", "st", *args);
def disablebreak(*args): return _dispatch_method("disablebreak", "st", *args);
def disableinvert(*args): return _dispatch_method("disableinvert", "st", *args);
def enableinvert(*args): return _dispatch_method("enableinvert", "st", *args);
def disableerrormsg(*args): return _dispatch_method("disableerrormsg", "st", *args);
def enableerrormsg(*args): return _dispatch_method("enableerrormsg", "st", *args);
def disablehistory(*args): return _dispatch_method("disablehistory", "st", *args);
def sleep(*args): return _dispatch_method("sleep", "st", *args);
def setfloatmode(*args): return _dispatch_method("setfloatmode", "st", *args);
def seterrormode(*args): return _dispatch_method("seterrormode", "st", *args);
def setbackgroundmode(*args): return _dispatch_method("setbackgroundmode", "st", *args);
def inputpos(*args): return _dispatch_method("inputpos", "st", *args);
def menu(*args): return _dispatch_method("menu", "st", *args);
def mousemenu(*args): return _dispatch_method("mousemenu", "st", *args);
def setmenudelay(*args): return _dispatch_method("setmenudelay", "st", *args);
def writeininum(*args): return _dispatch_method("writeininum", "st", *args);
def writeininumw(*args): return _dispatch_method("writeininumw", "st", *args);
def writeinistr(*args): return _dispatch_method("writeinistr", "st", *args);
def writeinistrw(*args): return _dispatch_method("writeinistrw", "st", *args);
def openreg(*args): return _dispatch_method("openreg", "st", *args);
def createreg(*args): return _dispatch_method("createreg", "st", *args);
def closereg(*args): return _dispatch_method("closereg", "st", *args);
def writeregbinary(*args): return _dispatch_method("writeregbinary", "st", *args);
def writeregnum(*args): return _dispatch_method("writeregnum", "st", *args);
def writeregstr(*args): return _dispatch_method("writeregstr", "st", *args);
def deletereg(*args): return _dispatch_method("deletereg", "st", *args);
def configset(*args): return _dispatch_method("configset", "st", *args);
def config(*args): return _dispatch_method("config", "st", *args);
def configcolor(*args): return _dispatch_method("configcolor", "st", *args);
def saveconfig(*args): return _dispatch_method("saveconfig", "st", *args);
def setconfigstate(*args): return _dispatch_method("setconfigstate", "st", *args);
def setfiletype(*args): return _dispatch_method("setfiletype", "st", *args);
def envchanged(*args): return _dispatch_method("envchanged", "st", *args);
def loadkeyassign(*args): return _dispatch_method("loadkeyassign", "st", *args);
def savekeyassign(*args): return _dispatch_method("savekeyassign", "st", *args);
def loadhilight(*args): return _dispatch_method("loadhilight", "st", *args);
def savehilight(*args): return _dispatch_method("savehilight", "st", *args);
def loadbookmark(*args): return _dispatch_method("loadbookmark", "st", *args);
def savebookmark(*args): return _dispatch_method("savebookmark", "st", *args);
def setfontchangemode(*args): return _dispatch_method("setfontchangemode", "st", *args);
def settabstop(*args): return _dispatch_method("settabstop", "st", *args);
def convert_return_in_cell(*args): return _dispatch_method("convert_return_in_cell", "st", *args);
def showwindow(*args): return _dispatch_method("showwindow", "st", *args);
def setmonitor(*args): return _dispatch_method("setmonitor", "st", *args);
def setwindowpos(*args): return _dispatch_method("setwindowpos", "st", *args);
def setwindowsize(*args): return _dispatch_method("setwindowsize", "st", *args);
def setfocus(*args): return _dispatch_method("setfocus", "st", *args);
def begingroupundo(*args): return _dispatch_method("begingroupundo", "st", *args);
def endgroupundo(*args): return _dispatch_method("endgroupundo", "st", *args);
def findspecial(*args): return _dispatch_method("findspecial", "st", *args);
def setstaticvariable(*args): return _dispatch_method("setstaticvariable", "st", *args);
def setregularcache(*args): return _dispatch_method("setregularcache", "st", *args);
def closehidemaru(*args): return _dispatch_method("closehidemaru", "st", *args);
def closehidemaruforced(*args): return _dispatch_method("closehidemaruforced", "st", *args);
def beginclipboardread(*args): return _dispatch_method("beginclipboardread", "st", *args);
def seteventnotify(*args): return _dispatch_method("seteventnotify", "st", *args);

def freedll(*args): return _dispatch_method("freedll", "st", *args);
def setdlldetachfunc(*args): return _dispatch_method("setdlldetachfunc", "st", *args);
def keepdll(*args): return _dispatch_method("keepdll", "st", *args);
def setcomdetachmethod(*args): return _dispatch_method("setcomdetachmethod", "st", *args);
def keepobject(*args): return _dispatch_method("keepobject", "st", *args);

# 配列展開
def menuarray(*args): return menu(*(args[0]));

# 配列展開
def mousemenuarray(*args):  return mousemenu(*(args[0]));


def message(*args): return _dispatch_method("message", "fn1s2s", *args);

def insert(*args): return _dispatch_method("insert", "st1s", *args);
def insertfix(*args): return _dispatch_method("insertfix", "st1s", *args);
def searchdialog(*args): return _dispatch_method("searchdialog", "st1s", *args);
def searchdown(*args): return _dispatch_method("searchdown", "st1s", *args);
def searchdown2(*args): return _dispatch_method("searchdown2", "st1s", *args);
def searchup(*args): return _dispatch_method("searchup", "st1s", *args);
def searchup2(*args): return _dispatch_method("searchup2", "st1s", *args);
def replacedialog(*args): return _dispatch_method("replacedialog", "st1s", *args);
def replacedown(*args): return _dispatch_method("replacedown", "st1s", *args);
def replaceup(*args): return _dispatch_method("replaceup", "st1s", *args);
def question(*args): return _dispatch_method("question", "st1s", *args);
def setclipboard(*args): return _dispatch_method("setclipboard", "st1s", *args);
def addclipboard(*args): return _dispatch_method("addclipboard", "st1s", *args);


def replacedialog(*args): return _dispatch_method("replacedialog", "st1s2s", *args);
def replacedown(*args): return _dispatch_method("replacedown", "st1s2s", *args);
def replaceup(*args): return _dispatch_method("replaceup", "st1s2s", *args);
