#pragma once

#include "utils.hpp"
#include "os.hpp"

std::string format_file(const std::string& file);
std::pair<int, std::string> generate_ast(const std::string& path);