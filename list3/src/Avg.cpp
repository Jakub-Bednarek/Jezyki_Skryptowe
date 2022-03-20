#include <iostream>

#include "Utils.hpp"

int main(int argc, char* argv[])
{
    double sum = 0.0;
    int n_numbers = 0;
    std::string input;
    while(std::cin >> input)
    {
        if(is_number(input))
        {
            sum += std::stod(input);
            n_numbers++;
        }
    }

    std::cout << sum / n_numbers << '\n';
    return 0;
}