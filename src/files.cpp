#include "files.hpp"

std::string format_file(const std::string& file)
{
    std::string result = "";
    std::vector<char> openings = {'[', '{', '('};
    std::vector<char> closings = {']', '}', ')'};
    int indents = 0;
    int quotes = 0;
    bool skip = false;
    for (size_t i = 0; i < file.size(); i++) {
        if (skip) {
            skip = false;
            continue;
        }
        if (i < file.size()-2) {
            if (file[i] == '\'' || file[i] == '"') {
                if (quotes > 0) quotes--;
                else quotes++;
            }
            if (contains(openings, file[i]) && !contains(closings, file[i+1])) {
                result += file[i];
                result += "\n";
                indents++;
                result += gen_indents(indents);
                continue;
            }
            if (file[i] == ',' && quotes == 0) {
                result += file[i];
                result += "\n";
                result += gen_indents(indents);
                if (file[i+1] == ' ') skip = true;
                continue;
            }
            if (i > 0) {
                if (contains(closings, file[i]) && !contains(openings, file[i-1])) {
                    result += "\n";
                    indents--;
                    result += gen_indents(indents);
                    result += file[i];
                    continue;
                }
            }
        }
        if (i >= file.size()-2) {
            if (contains(closings, file[i]) && !contains(openings, file[i-1])) {
                indents--;
                result += "\n";
                result += gen_indents(indents);
            }
        }
        result += file[i];
    }
    return result;
}

std::pair<int, std::string> generate_ast(const std::string& path)
{
    std::string command;
#if OS_UNIX_LIKE_DEFINED
    command = "./python3 ast_parser.py " + path;  
#else
    command = "python3.exe " + path;  
#endif
    std::pair<int, std::string> res = OS::run_command(command);
    return res;
}
