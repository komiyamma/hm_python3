#pragma once

#include <windows.h>
#include <string>
#include <vector>

// ���̌��ʂ̃o�C�g��(vector.data())�� HmOutputPane.dll��Output�֐��ɂȂ���΁AUnicode�ł��Č��ł���
std::vector<BYTE> EncodeWStringToOriginalEncodeVector(std::wstring original_string);

// �G�ۂ���G�ۓƎ���Star���j�R�[�h�œn���Ă������̂�Decode
std::wstring DecodeOriginalEncodeVector(BYTE *original_encode_string);