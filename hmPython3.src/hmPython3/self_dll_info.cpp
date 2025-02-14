/* 
 * Copyright (c) 2017 Akitsugu Komiyama
 * under the Apache License Version 2.0
 */

#include <windows.h>
#include <shlwapi.h>

#include "self_dll_info.h"
#include "hidemaruexe_export.h"

#pragma comment(lib, "shlwapi.lib")


HMODULE CSelfDllInfo::hModule = NULL;

wchar_t CSelfDllInfo::szSelfModuleFullPath[MAX_PATH] = L"";
wchar_t CSelfDllInfo::szSelfModuleDirPath[MAX_PATH] = L"";

int CSelfDllInfo::iSelfBindedType = 0;
int CSelfDllInfo::HadSetdKeepDll = false;

void CSelfDllInfo::InitializeHandle(HMODULE hModule) {
	CSelfDllInfo::hModule = hModule;
	GetModuleFileName(hModule, CSelfDllInfo::szSelfModuleFullPath, _countof(CSelfDllInfo::szSelfModuleFullPath));
	wcscpy_s(CSelfDllInfo::szSelfModuleDirPath, CSelfDllInfo::szSelfModuleFullPath);
	PathRemoveFileSpec(CSelfDllInfo::szSelfModuleDirPath);
}

int CSelfDllInfo::GetBindDllType() {
	return iSelfBindedType;
}

void CSelfDllInfo::SetKeepDll(int dll) {
	if (HadSetdKeepDll) {
		return;
	}

	// keepdll の指定をする
	if (CHidemaruExeExport::hm_version >= 898.08) {
		if (dll == -1) {
			wstring keepdll_cmd = L"keepdll " + to_wstring(0) + L", 0";
			CHidemaruExeExport::EvalMacro(keepdll_cmd.c_str());
		}
		else {
			wstring keepdll_cmd = L"keepdll " + to_wstring(dll) + L", 0";
			CHidemaruExeExport::EvalMacro(keepdll_cmd.c_str());
		}

		HadSetdKeepDll = true;
	}
}

void CSelfDllInfo::ClearKeepDll() {
	HadSetdKeepDll = false;
}

BOOL CSelfDllInfo::SetBindDllHandle() {
	// 本体からの関数の生成が先
	CHidemaruExeExport::init();

	// 秀丸8.66以上
	if (CHidemaruExeExport::Hidemaru_GetDllFuncCalledType) {
		int dll = CHidemaruExeExport::Hidemaru_GetDllFuncCalledType(-1); // 自分のdllの呼ばれ方をチェック

		// Hidemaru_GetDllFuncCalledTypeについては、別の存在でありながら成り立たせるために、呼ばれ方情報だけは結びつけています。
		// 0x80000001みたいな、32bitの最上位ビットが立ったIDにしていて、マクロ側loaddllのIDと被らないようにしています。10進だとマイナス値でわかりにくいですね。
		if ((dll & 0x80000000) != 0) {
			wstring errmsg = L"「jsmode」の「hidemaru.loadDll(...)」からの呼び出しを検知しました。\n「jsmode」の「loadDll経由の呼び出し」には対応していません。\n"
				L"「jsmode」から呼び出すには、「hidemaruCompat.loaddll(...)」を利用してください。\n"
				L"https://秀丸マクロ.net/?page=nobu_tool_hm_jsmode_hidemarucompat\n";
			MessageBox(NULL, errmsg.c_str(), L"「hmPython3.dll」の「jsmode」からの呼び出し", NULL);
			OutputDebugStringW(errmsg.c_str());
			return FALSE;
		}

		CSelfDllInfo::iSelfBindedType = dll;
		SetKeepDll(dll);
		return TRUE;
	}
	else {
		MessageBox(NULL, L"loadllのパターンが認識出来ませんでした。", L"loadllのパターンが認識出来ませんでした。", MB_ICONERROR);
	}



	return FALSE;

}

wstring CSelfDllInfo::GetInvocantString() {
	if (iSelfBindedType == -1) {
		return L"";
	}
	else {
		return to_wstring(iSelfBindedType) + L",";
	}
}

wstring CSelfDllInfo::GetSelfModuleFullPath() {
	return szSelfModuleFullPath;
}

wstring CSelfDllInfo::GetSelfModuleDir() {
	return szSelfModuleDirPath;
}
