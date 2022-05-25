
#include <windows.h>
#include <string>
#include <vector>
#include "convert_string.h"

using namespace std;

bool IsSTARTUNI_inline(DWORD byte4) {
	return (byte4 & 0xF4808000) == 0x04808000;
}

WCHAR inline GetUnicodeInText(char* pchSrc) {
	return MAKEWORD(
		(pchSrc[1] & 0x7F | ((pchSrc[3] & 0x01) << 7)),
		(pchSrc[2] & 0x7F | ((pchSrc[3] & 0x02) << 6))
	);
}


std::wstring DecodeOriginalEncodeVector(BYTE *original_encode_string) {
	try {
		// 独自エンコード
		string str_original_encode = (char *)original_encode_string;

		const char* pstr = str_original_encode.c_str();

		// 最終的な返り値
		wstring result = L"";

		// 一時バッファー用
		string tmp_buffer = "";
		int len = str_original_encode.size();

		int lastcheckindex = len - sizeof(DWORD); // IsSTARTUNI_inline には 4バイト必要
		if (lastcheckindex < 0) {
			lastcheckindex = 0;
		}
		for (int i = 0; i < (int)strlen(pstr); i++) {
			if (i <= lastcheckindex) {
				DWORD* pStarUni = (DWORD*)(&pstr[i]);
				if (IsSTARTUNI_inline(*pStarUni)) {
					if (tmp_buffer.length() > 0) {
						result += cp932_to_utf16(tmp_buffer);
						tmp_buffer.clear();
					}

					char* src = (char *)(&pstr[i]);
					wchar_t wch = GetUnicodeInText(src);
					i = i + 3; // 1バイトではなく4バイト消化したので、計算する
					result += wch;
					continue;
				}
			}
			tmp_buffer += pstr[i];
		}

		if (tmp_buffer.length() > 0) {
			result += cp932_to_utf16(tmp_buffer);
			tmp_buffer.clear();
		}

		return result;
	}
	catch (...) {
		OutputDebugString(L"エラー:\nHmOrignalUnicodeDecodeError");
	}

	return L"";
}