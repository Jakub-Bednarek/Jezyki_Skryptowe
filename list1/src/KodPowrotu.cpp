#include <iostream>
#include <vector>
#include <bitset>
#include <algorithm>
#include <unordered_map>
#include <iterator>

#define MAX_ARGUMENTS_SIZE 7

std::bitset<MAX_ARGUMENTS_SIZE> get_error_code(const std::unordered_map<std::string, unsigned int>& mapped_values, 
                              const std::vector<std::string>& user_input);

//Jako argumenty przekazujemy maksymalnie 7 czesci wg malejacej waznosci
int main(int argc, char* argv[], char* env[])
{
    std::unordered_map<std::string, unsigned int> mapped_args;
    unsigned int value = 0;
    for(int i = argc - 1; i > 0; i--, value++)
    {
        mapped_args.insert({argv[i], value});
    }
    
    std::vector<std::string> user_input;
    std::string input_line;
    while(std::cin >> input_line)
    {
        user_input.push_back(input_line);
    }

    auto code =  get_error_code(mapped_args, user_input);
    std::cout << code;

    return (int)code.to_ulong();
}

std::bitset<MAX_ARGUMENTS_SIZE> get_error_code(const std::unordered_map<std::string, unsigned int>& mapped_values, 
                              const std::vector<std::string>& user_input)
{
    std::bitset<MAX_ARGUMENTS_SIZE> error_code = {0};

    std::for_each(user_input.begin(), user_input.end(), [&mapped_values, &error_code](const auto& user_line) {
            if(mapped_values.find(user_line) != mapped_values.end())
            {
                error_code.set(mapped_values.at(user_line), true);
            }
    });

    return error_code;
}