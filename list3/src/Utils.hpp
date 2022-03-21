#ifndef UTILS_HPP
#define UTILS_HPP

#include <algorithm>
#include <string>

bool is_number(const std::string& line)
{
    int found_commas = 0;
    return std::all_of(line.begin(), line.end(), [&found_commas](const auto& c) -> bool {
        if(c == '.')
        {
            return ++found_commas < 2;
        }

        return std::isdigit(c);
    });
}

#endif // UTILS_HPP