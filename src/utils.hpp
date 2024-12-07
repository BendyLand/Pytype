#pragma once

#include <iostream>
#include <fstream>
#include <vector>

std::string read_file(const std::string& path);
void write_file(const std::string& path, const std::string& contents);
std::string gen_indents(int indents);
std::vector<std::string> split(const std::string& str, const std::string& delim);
std::string ltrim(const std::string& str);
std::string rtrim(const std::string& str);
std::string trim(const std::string& str);

template <typename T>
bool contains(std::vector<T> vec, T item)
{
    for (T entry : vec) {
        if (entry == item) return true;
    }
    return false;
}

template <typename T>
std::ostream& operator<<(std::ostream& os, std::vector<T> vec)
{
    for (T entry : vec) {
        std::cout << entry << std::endl;
    }
    return os;
}
