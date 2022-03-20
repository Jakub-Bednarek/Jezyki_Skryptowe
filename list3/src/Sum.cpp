#include <iostream>
#include <algorithm>

bool is_number(const std::string& line);

int main(int argc, char* argv[])
{
    double sum = 0;
    std::string input;
    while(std::cin >> input)
    {
        if(is_number(input))
        {
            sum += std::stod(input);
        }
    }

    std::cout << sum << '\n';
    return 0;
}

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