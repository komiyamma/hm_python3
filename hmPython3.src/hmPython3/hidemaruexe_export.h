/* 
 * Copyright (c) 2017 Akitsugu Komiyama
 * under the Apache License Version 2.0
 */

#pragma once

#include <windows.h>
#include <string>

using namespace std;

class CHidemaruExeExport {
private:
	static HMODULE hHideExeHandle;
	static wchar_t szHidemaruFullPath[MAX_PATH];

	static HMODULE hHmOutputPaneDLL;
	static HMODULE hHmExplorerPaneDLL;

public:
	//========================================================================
	// �G�ۖ{�̂̃o�[�W�����B
	//-------------------------------------------------------------------------
	// 8.66��3�Ȃ�A�u866.03�v�݂����Ȋ����ɂȂ�B
	//========================================================================
	static double hm_version;
private:
	static double QueryFileVersion(wchar_t* path);

public:
	//========================================================================
	/// �G�ۖ{�̂���Export����Ă��邢�����̊֐��Q
	//========================================================================

	//-------------------------------------------------------------------------
	// ���ݕҏW���̑S�Ẵe�L�X�g�𓾂�
	using PFNGetTotalTextUnicode = HGLOBAL(WINAPI *)(void);
	static PFNGetTotalTextUnicode Hidemaru_GetTotalTextUnicode;

	//-------------------------------------------------------------------------
	// ���ݕҏW���̑I���e�L�X�g�𓾂�(�P���I���̂�)
	using PFNGetSelectedTextUnicode = HGLOBAL(WINAPI *)(void);
	static PFNGetSelectedTextUnicode Hidemaru_GetSelectedTextUnicode;

	//-------------------------------------------------------------------------
	// ���ݕҏW���̃e�L�X�g�̃J�[�\��������s�̃e�L�X�g�𓾂�
	using PFNGetLineTextUnicode = HGLOBAL(WINAPI *)(int nLineNo);
	static PFNGetLineTextUnicode Hidemaru_GetLineTextUnicode;

	// �G�ۂ̃E�B���h�E�n���h��
	using PFNGetCurrentWindowHandle = HWND(WINAPI *)();
	static PFNGetCurrentWindowHandle Hidemaru_GetCurrentWindowHandle;


	//-------------------------------------------------------------------------
	// �w��Ώۂ̃t�@�C���̏G��encode�𓾂�B�G�ێ��̂́u������v-�u�t�@�C���v�[�u�G���R�[�h1�v�̐ݒ�ɏ]���̂Œ��ӁB
	// �ėp�̃G���R�[�h�擾�@�\�ł͂Ȃ��A�g�p�҂��g���Ă���G�ۂ̐ݒ�̌��A���̊Y���̏G�ۂŃt�@�C�����J�����Ƃ�����A
	// ���̃G���R�[�h�ŊJ�����̂����擾����@�\�ƂȂ�B
	using PFNAnalyzeEncoding = int(WINAPI *)(const WCHAR* pwszFileName, DWORD_PTR lParam1, DWORD_PTR lParam2);
	static PFNAnalyzeEncoding Hidemaru_AnalyzeEncoding;

	//-------------------------------------------------------------------------
	// �w��̏G�ۂ�encode���w�肵�āA�t�@�C�����e��ǂݍ���
	using PFNLoadFileUnicode = HGLOBAL (WINAPI *)(const WCHAR* pwszFileName, int nEncode, UINT* pcwchOut, DWORD_PTR lParam1, DWORD_PTR lParam2);
	static PFNLoadFileUnicode Hidemaru_LoadFileUnicode;

	//-------------------------------------------------------------------------
	// ���ݕҏW���̃e�L�X�g�̃J�[�\���̈ʒu���擾����B�}�N����column��lineno����
	using PFNGetCursorPosUnicode = BOOL(WINAPI *)(int* pnLineNo, int* pnColumn);
	static PFNGetCursorPosUnicode Hidemaru_GetCursorPosUnicode;

	using PFNGetCursorPosUnicodeFromMousePos = BOOL(WINAPI *)(POINT* ppt, int* pnLineNo, int* pnColumn);
	static PFNGetCursorPosUnicodeFromMousePos Hidemaru_GetCursorPosUnicodeFromMousePos;

	//-------------------------------------------------------------------------
	// dll�̒�����G�ۃ}�N�������s����
	using PFNEvalMacro = BOOL(WINAPI *)(const wchar_t* pwsz);
	static PFNEvalMacro Hidemaru_EvalMacro;

	//-------------------------------------------------------------------------
	// dll�̌Ă΂ꂩ���A�֐��̌Ă΂��(�Ԃ�l�̗v���^������̗v���^�𔻒�ł���֐�)�B����
	//-------------------------------------------------------------------------
	// dllfunc�����Ă�ł���ԁA�Ō��dllfunc�����Ă񂾓��e�̂ݎ擾�ł��܂��B
	// �Ⴆ��dllfunc�֐�����Hidemaru_EvalMacro�ł����dllfunc���Ăяo���ꍇ�A�擾�ł�����͈̂�ԐV�����Ă񂾂��݂̂̂ł��B
	//-------------------------------------------------------------------------
	using PFNGetDllFuncCalledType = int(WINAPI *)(int n);
	static PFNGetDllFuncCalledType Hidemaru_GetDllFuncCalledType;

	//-------------------------------------------------------------------------
	// n�� - 1���w�肷��ƁAloaddll�̂������Ԃ��܂��B1�ȏ��loaddll�֐��̕Ԃ�l�Ɠ����ł��B - 1�̏ꍇ��loaddll���œǂݍ��܂ꂽDLL�ł��B

	//-------------------------------------------------------------------------
	// n��0���w�肷��ƁAdllfunc / dllfuncw / dllfuncstr / dllfuncstrw�̂ǂ�ŌĂ΂ꂽ���ɂ���āAreturn�ŕԂ��ׂ��l�������܂��B
	// �ȉ��̒l�̂����ꂩ���Ԃ�܂��B
	// dllfunc�����Ă΂�Ă���Ƃ��A�ǂ̂悤�ȌĂ΂�������Ă��邩���擾���܂��B
	enum class DLLFUNCRETURN {
		NOTCALL   = 0,       //�Ă΂�Ă��Ȃ�
		INT       = 0x0001,  //int��Ԃ��ׂ�(dllfunc�܂���dllfuncw)
		CHAR_PTR  = 0x0002,  //char*��Ԃ��ׂ�(dllfuncstr)
		WCHAR_PTR = 0x0003,  //WCHAR*��Ԃ��ׂ�(dllfuncstrw)
		DOUBLE    = 0x0004  //double��Ԃ��ׂ�(dllfunc�܂���dllfuncw�ŕ��������_�����L��)
	};

	//-------------------------------------------------------------------------
	//n��1���琔�������Ԃ̒l���w�肷��ƁA1���琔�����p�����[�^�̎�ނ����l / ������ / Unicode������ / ���������_������Ԃ��܂��B
	// �p�����[�^�̍ő��64�ł��B
	// �ȉ��̒l�̂����ꂩ���Ԃ�܂��B
	enum class DLLFUNCPARAM {
		NOPARAM   = 0,       //�ȍ~�̃p�����[�^�Ȃ�
		INT       = 0x0100,  //int�̃p�����[�^
		CHAR_PTR  = 0x0200,  //char*�̃p�����[�^
		WCHAR_PTR = 0x0300,  //WCHAR*�̃p�����[�^
		DOUBLE    = 0x0400   //double�̃p�����[�^
	};

public:

	//========================================================================
	/// ������
	//========================================================================
	static BOOL init();


	//========================================================================
	/// ���b�v�֐��S
	//========================================================================

	//-------------------------------------------------------------------------
	// Hidemaru_GetTotalTextUnicode�֐��̃��b�v��������
	//-------------------------------------------------------------------------
	static wstring GetTotalText();

	//-------------------------------------------------------------------------
	// Hidemaru_GetSelectedTextUnicode�֐��̃��b�v��������
	//-------------------------------------------------------------------------
	static wstring GetSelectedText();

	//-------------------------------------------------------------------------
	// Hidemaru_GetLineTextUnicode�֐��̃��b�v��������
	//-------------------------------------------------------------------------
	static wstring GetLineText(int lineno = 0);

	//-------------------------------------------------------------------------
	// Hidemaru_AnalyzeEncoding�֐��̃��b�v��������
	//-------------------------------------------------------------------------
	static int AnalyzeEncoding(wstring filename);

	//-------------------------------------------------------------------------
	// Hidemaru_LoadFileUnicode�֐��̃��b�v��������
	//-------------------------------------------------------------------------
	static wstring LoadFileUnicode(wstring filename, int nHmEncode, UINT* pcwchOut, DWORD_PTR lParam1, DWORD_PTR lParam2, bool* success);

	//-------------------------------------------------------------------------
	// Hidemaru_GetCursorPosUnicode�֐��̃��b�v��������
	//-------------------------------------------------------------------------
	// ���W�^�BPoint�^�ł́ASystem.Drawing��ǂݍ��܂Ȃ��ƃ_���Ȃ̂ŕ��ׂ�����B�܂��Ax, y�͏G�ۂɕʒl�Ƃ��đ��݂���̂ŁA
	// �����܂ł��A�}�N����column��lineno�ƈ�v���Ă���Ƃ����咣�B
	// column��lineno�̓G�f�B�^�I�ȍ��W�ł���B
	struct HmCursurPos
	{
	public:
		int lineno;
		int column;
		HmCursurPos(int _lineno, int _column)
		{
			this->lineno = _lineno;
			this->column = _column;
		}
	};
	static HmCursurPos GetCursorPos();


	//-------------------------------------------------------------------------
	// Hidemaru_GetCursorPosUnicodeFromMousePos�֐��̃��b�v��������
	// (�G��8.73�ȏ�)
	//-------------------------------------------------------------------------
	struct HmMousePos
	{
	public:
		int x;
		int y;
		int lineno;
		int column;
		HmMousePos(int _x, int _y, int _lineno, int _column)
		{
			this->x = _x;
			this->y = _y;
			this->lineno = _lineno;
			this->column = _column;
		}
	};
	static HmMousePos GetCursorPosFromMousePos();

	//-------------------------------------------------------------------------
	// Hidemaru_EvalMacro�֐��̃��b�v��������
	//-------------------------------------------------------------------------
	static BOOL EvalMacro(wstring);



	//-------------------------------------------------------------------------
	// �A�E�g�v�b�g�p�l��
	//-------------------------------------------------------------------------
	using PFNHmOutputPane_Output = int(_cdecl*)(HWND hwnd, BYTE *);
	static PFNHmOutputPane_Output HmOutputPane_Output;
	using PFNHmOutputPane_OutputW = int(_cdecl*)(HWND hwnd, wchar_t* message);
	static PFNHmOutputPane_OutputW HmOutputPane_OutputW;
	using PFNHmOutputPane_Push = int(_cdecl*)(HWND hwnd);
	static PFNHmOutputPane_Push HmOutputPane_Push;
	using PFNHmOutputPane_Pop = int(_cdecl*)(HWND hwnd);
	static PFNHmOutputPane_Pop HmOutputPane_Pop;
	using PFNHmOutputPane_GetWindowHandle = HWND(_cdecl*)(HWND hwnd);
	static PFNHmOutputPane_GetWindowHandle HmOutputPane_GetWindowHandle;
	using PFNHmOutputPane_SetBaseDir = int(_cdecl*)(HWND hwnd, BYTE *);
	static PFNHmOutputPane_SetBaseDir HmOutputPane_SetBaseDir;


	//-------------------------------------------------------------------------
	// �t�@�C���}�l�[�W���p�l��
	//-------------------------------------------------------------------------
	using PFNHmExplorerPane_SetMode = int(_cdecl*)(HWND hwnd, intptr_t);
	static PFNHmExplorerPane_SetMode HmExplorerPane_SetMode;
	using PFNHmExplorerPane_GetMode = int(_cdecl*)(HWND hwnd);
	static PFNHmExplorerPane_GetMode HmExplorerPane_GetMode;
	using PFNHmExplorerPane_LoadProject = int(_cdecl*)(HWND hwnd, BYTE *);
	static PFNHmExplorerPane_LoadProject HmExplorerPane_LoadProject;
	using PFNHmExplorerPane_SaveProject = int(_cdecl*)(HWND hwnd, BYTE *);
	static PFNHmExplorerPane_SaveProject HmExplorerPane_SaveProject;
	using PFNHmExplorerPane_GetProject = BYTE* (_cdecl*)(HWND hwnd);
	static PFNHmExplorerPane_GetProject HmExplorerPane_GetProject;
	using PFNHmExplorerPane_GetWindowHandle = HWND(_cdecl*)(HWND hwnd);
	static PFNHmExplorerPane_GetWindowHandle HmExplorerPane_GetWindowHandle;
	using PFNHmExplorerPane_GetUpdated = int(_cdecl*)(HWND hwnd);
	static PFNHmExplorerPane_GetUpdated HmExplorerPane_GetUpdated;
	using PFNHmExplorerPane_GetCurrentDir = BYTE* (_cdecl*)(HWND hwnd);
	static PFNHmExplorerPane_GetCurrentDir HmExplorerPane_GetCurrentDir;
};

