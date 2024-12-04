#include "utils.hpp"
#include "os.hpp"
#include "files.hpp"
#include "parser.hpp"

int main(int argc, char** argv)
{
    if (argc > 1) {
        std::pair<int, std::string> res = generate_ast(argv[1]);
        if (res.first != 0) {
            std::cerr << "Error: " << res.second << std::endl;
            exit(EXIT_FAILURE);
        }
        res.second = format_file(res.second);
        Parser parser(res.second);
        Lines lines = parser.lines();
        // write_file("ast.txt", res.second);
    }
    else {
        std::cout << "Usage: pytype <filepath>" << std::endl;
    }
    return 0;
}
