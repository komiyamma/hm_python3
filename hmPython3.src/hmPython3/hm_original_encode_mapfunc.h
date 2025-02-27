#pragma once

#include <windows.h>
#include <string>
#include <vector>

// この結果のバイト列(vector.data())を HmOutputPane.dllのOutput関数になげれば、Unicodeでも再現できる
std::vector<BYTE> EncodeWStringToOriginalEncodeVector(std::wstring original_string);

// 秀丸から秀丸独自のStarユニコードで渡ってきたもののDecode
std::wstring DecodeOriginalEncodeVector(BYTE *original_encode_string);

// 秀丸エディタ掲示板でまるを氏が投稿していたアルゴリズム
std::vector<BYTE> EncodeWStringToOriginalEncodeVector2(wstring original_string);
