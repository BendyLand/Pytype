#pragma once

#include <iostream>
#include <fstream>

std::string read_file(const std::string& path);
void write_file(const std::string& path, const std::string& contents);
std::string gen_indents(int indents);

template <typename T>
bool contains(std::vector<T> vec, T item)
{
    for (T entry : vec) {
        if (entry == item) return true;
    }
    return false;
}
