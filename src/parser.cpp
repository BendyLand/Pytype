#include "parser.hpp"

std::string Lines::step_down()
{
    return this->_lines[this->increment_pos()];
}

std::string Lines::step_up()
{
    return this->_lines[this->decrement_pos()];
}

size_t Lines::increment_pos()
{
    return ++this->_current;
}

size_t Lines::decrement_pos()
{
    return --this->_current;
}

size_t Lines::current_pos()
{
    return this->_current;
}

std::optional<std::string> Lines::next_line() const
{
    if (this->_current < this->_lines.size()-2) return this->_lines[this->_current+1];
    else return std::nullopt;
}
std::optional<std::string> Lines::prev_line() const
{
    if (this->_current > 0) return this->_lines[this->_current-1];
    else return std::nullopt;
}

std::optional<std::string> Lines::current_line() const
{
    if (this->_lines.size() > 0) return this->_lines[this->_current];
    else return std::nullopt;
}

size_t Lines::size() const
{
    return this->_lines.size();
}

Lines Parser::lines()
{
    Lines result(this->ast);
    return result;
}