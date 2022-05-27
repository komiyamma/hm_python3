
#include <windows.h>
#include <string>
#include <vector>
#include "convert_string.h"

static int nZenkaku(wchar_t wch) {
	wstring wstr = L"";
	wstr += wch;
	string u8 = utf16_to_utf8(wstr);

	WORD* pu8 = (WORD*)u8.c_str();
	WORD vu8 = *pu8;
	if (0x00 <= vu8 && vu8 <= 0x80) {
		return 0;
	}
	if (vu8 == 0xf8f0) {
		return 0;
	}
	if (0xff61 <= vu8 == vu8 <= 0xff9f) {
		return 0;
	}
	if (0xf8f1 <= vu8 == vu8 <= 0xf8f3) {
		return 0;
	}
	return 8;
}



static vector<BYTE> ToOriginalHmStarUnicode(wchar_t wch) {

	vector<BYTE> ret;
	ret.push_back(0x1A);
	ret.push_back(0x80 + LOBYTE(wch));
	ret.push_back(0x80 + HIBYTE(wch));
	BYTE byte4ix = ((wch & 0x80) >> 7) + ((wch & 0x8000) >> 14) + 4 + nZenkaku(wch);
	ret.push_back(byte4ix);

	return ret;
}


vector<BYTE> EncodeWStringToOriginalEncodeVector2(wstring original_string) {
	vector<BYTE> r;
	for (wchar_t wch : original_string) {

		wstring wstr = L"";
		wstr += wch;
		string str = utf16_to_cp932(wstr);
		wstring wstr2 = cp932_to_utf16(str);

		// 同じならCP932に存在するコード
		if (wstr == wstr2) {
			for (char ch : str) {
				r.push_back(ch);
			}
		}

		else {

			// 異なるならCP932には存在しないコード
			vector<BYTE> byte4 = ToOriginalHmStarUnicode(wch);
			for (BYTE b : byte4) {
				r.push_back(b);
			}
		}
	}

	// 最後にNULL相当ついイア
	r.push_back(0);
	return r;
}
