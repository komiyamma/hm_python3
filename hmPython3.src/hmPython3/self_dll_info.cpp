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

	// keepdll �̎w�������
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
	// �{�̂���̊֐��̐�������
	CHidemaruExeExport::init();

	// �G��8.66�ȏ�
	if (CHidemaruExeExport::Hidemaru_GetDllFuncCalledType) {
		int dll = CHidemaruExeExport::Hidemaru_GetDllFuncCalledType(-1); // ������dll�̌Ă΂�����`�F�b�N

		// Hidemaru_GetDllFuncCalledType�ɂ��ẮA�ʂ̑��݂ł���Ȃ��琬�藧�����邽�߂ɁA�Ă΂����񂾂��͌��т��Ă��܂��B
		// 0x80000001�݂����ȁA32bit�̍ŏ�ʃr�b�g��������ID�ɂ��Ă��āA�}�N����loaddll��ID�Ɣ��Ȃ��悤�ɂ��Ă��܂��B10�i���ƃ}�C�i�X�l�ł킩��ɂ����ł��ˁB
		if ((dll & 0x80000000) != 0) {
			wstring errmsg = L"�ujsmode�v�́uhidemaru.loadDll(...)�v����̌Ăяo�������m���܂����B\n�ujsmode�v�́uloadDll�o�R�̌Ăяo���v�ɂ͑Ή����Ă��܂���B\n"
				L"�ujsmode�v����Ăяo���ɂ́A�uhidemaruCompat.loaddll(...)�v�𗘗p���Ă��������B\n"
				L"https://�G�ۃ}�N��.net/?page=nobu_tool_hm_jsmode_hidemarucompat\n";
			MessageBox(NULL, errmsg.c_str(), L"�uhmPython3.dll�v�́ujsmode�v����̌Ăяo��", NULL);
			OutputDebugStringW(errmsg.c_str());
			return FALSE;
		}

		CSelfDllInfo::iSelfBindedType = dll;
		SetKeepDll(dll);
		return TRUE;
	}
	else {
		MessageBox(NULL, L"loadll�̃p�^�[�����F���o���܂���ł����B", L"loadll�̃p�^�[�����F���o���܂���ł����B", MB_ICONERROR);
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
