#include <iostream>

#include "Utils.hpp"

int main(int argc, char* argv[])
{
    double sum = 0.0;
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