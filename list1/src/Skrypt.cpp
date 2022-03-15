#include <iostream>
#include <vector>
#include <bitset>
#include <unordered_map>

#define MAX_ARGUMENTS_NUMBER 7

void process_error_code(const std::bitset<MAX_ARGUMENTS_NUMBER>& error_code, const std::vector<std::string>& values);

//Jako argumenty podajemy kolejno kod bledu a nastepnie wszystkie czesci w kolejnosci malejacej
int main(int argc, char* argv[], char* env[])
{
    std::bitset<MAX_ARGUMENTS_NUMBER> error_code;
    std::vector<std::string> arguments;

    try
    {;
        error_code = std::bitset<MAX_ARGUMENTS_NUMBER>(argv[1]);
        std::cout << "\nerror_code: " << error_code << '\n';
    }
    catch(const std::exception& e)
    {
        std::cout << "Invalid argument for error code!" << '\n';
        return -1;
    }
    
    for(int i = 2; i < argc; i++)
    {
        arguments.push_back(argv[i]);
    }

    process_error_code(error_code, arguments);

    return 0;
}

void process_error_code(const std::bitset<MAX_ARGUMENTS_NUMBER>& error_code, const std::vector<std::string>& values)
{
    bool found_error = false;
    int current_index = values.size() - 1;
    for(const auto& val : values)
    {
        if(error_code[current_index--])
        {
            if(!found_error)
            {
                std::cout << "Znalezione uszkodzone czesci:\n";
                found_error = true;
            }
            std::cout << '\t' << val << '\n'; 
        }
    }

    if(!found_error)
    {
        std::cout << "Brak znalezionych uszkodzonych czesci!\n";
    }
}