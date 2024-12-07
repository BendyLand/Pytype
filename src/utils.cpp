#include "utils.hpp"

std::vector<std::string> filter_empty(const std::vector<std::string>& vec)
{
    std::vector<std::string> result;
    result.reserve(vec.size());
    for (const std::string& entry : vec) {
        if (entry.empty()) continue;
        result.emplace_back(entry);
    }
    result.resize(result.size());
    return result;
}

std::string ltrim(const std::string& str)
{
    size_t start = str.find_first_not_of("\t");
    if (start == 0) start = str.find_first_not_of(" ");
    return str.substr(start);
}

std::string rtrim(const std::string& str)
{
    size_t end = str.find_last_not_of(" ");
    return str.substr(0, end+1);
}

std::string trim(const std::string& str)
{
    std::string result = str;
    result = ltrim(result);
    result = rtrim(result);
    return result;
}

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
    file.clear();
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
