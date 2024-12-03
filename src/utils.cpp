#include "utils.hpp"

std::string read_file(const std::string& path)
{
    std::string result = "";
    std::fstream file(path);
    if (!file.is_open()) {
        std::cerr << "Unable to open file: " << path << std::endl;
        exit(EXIT_FAILURE);
    }
    char buf;
    while (file.get(buf)) result += buf;
    file.close();
    return result;
}

void write_file(const std::string& path, const std::string& contents)
{
    std::fstream file(path);
    if (!file.is_open()) {
        std::cerr << "Unable to open file: " << path << std::endl;
        exit(EXIT_FAILURE);
    }
    for (char c : contents) file << c;
    file.close();
}

std::string gen_indents(int indents)
{
    std::string result = "";
    for (int i = 0; i < indents; i++) result += "\t";
    return result;
}