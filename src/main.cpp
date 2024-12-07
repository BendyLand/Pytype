#include "files.hpp"
#include "os.hpp"
#include "parser.hpp"
#include "utils.hpp"

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
        std::vector<std::string> const_assignments;
        for (size_t i = 0; i < lines.size(); i++) {
            std::string assign_block = lines.parse_constant_assign_block(i);
            if (assign_block.find("ERROR") != std::string::npos) continue;
            const_assignments.emplace_back(assign_block);
        }
        //todo: maybe integrate python's "typing" module for inference
        const_assignments = filter_empty(const_assignments);
        std::cout << const_assignments << std::endl;
		write_file("ast.txt", res.second);
	}
	else {
		std::cout << "Usage: pytype <filepath>" << std::endl;
	}
	return 0;
}
