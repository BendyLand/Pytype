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

std::vector<std::string> split(const std::string& str, const std::string& delim)
{
    std::vector<std::string> result;
    std::string temp = str;
    while (temp.find(delim) != std::string::npos) {
        std::string token = temp.substr(0, temp.find(delim));
        result.emplace_back(token);
        temp.erase(0, temp.find(delim)+delim.length());
    }
    if (temp.size() > 0) result.emplace_back(temp);
    return result;
}
