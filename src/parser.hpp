#pragma once

#include <string>
#include <vector>
#include <optional>
#include "utils.hpp"

class Lines
{
public:
    size_t size() const;
    std::optional<std::string> next_line() const;
    std::optional<std::string> prev_line() const;
    std::optional<std::string> current_line() const;
    size_t increment_pos();
    size_t decrement_pos();
    size_t current_pos();
    std::string step_down();
    std::string step_up();
    std::string parse_constant_assign_block(size_t current);
    Lines(const std::string& text) 
        : _current(0), _lines(split(text, "\n")) 
    {}
private:
    size_t _current;
    std::vector<std::string> _lines;
};

class Parser
{
public:
    std::string ast;
    Lines lines();
    Parser(const std::string& ast) 
        : ast(ast) 
    {}
};