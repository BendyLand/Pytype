#include "utils.hpp"
#include "os.hpp"
#include "files.hpp"

int main(int argc, char** argv)
{
    if (argc > 1) {
        std::pair<int, std::string> res = generate_ast(argv[1]);
        if (res.first != 0) {
            std::cerr << "Error: " << res.second << std::endl;
            exit(EXIT_FAILURE);
        }
        std::string file = read_file("ast.txt");
        file = format_file(file);
        write_file("ast.txt", file);
    }
    else {
        std::cout << "Usage: pytype <filepath>" << std::endl;
    }

    return 0;
}

