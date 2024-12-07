#include "parser.hpp"

std::string Lines::parse_constant_assign_block(size_t current)
{
    while (this->current_pos() < current) this->increment_pos();
    while (this->current_line().value().find("Name(") == std::string::npos) {
        this->increment_pos();
        if (this->current_pos() > this->size()) return "ERROR: Out of valid range of lines.";
    }
    std::string id_line = this->next_line().value();
    size_t start = id_line.find("'");
    size_t end = id_line.find_last_of("'") - 1;
    std::string result = "";
    if (start < end && start != SIZE_T_MAX) {
        result += id_line.substr(start+1, end-start) + "=";
        while (this->current_line().value().find("value=Constant(") == std::string::npos) {
            this->increment_pos();
            if (this->current_pos() > this->size()) return "ERROR: Out of valid range of lines.";
        }
        std::string val_line = this->next_line().value();
        start = val_line.find("=");
        result += val_line.substr(start+1);
    }
    return trim(result);
}

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