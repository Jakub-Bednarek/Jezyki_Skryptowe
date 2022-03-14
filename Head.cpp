#include <iostream>
#include <vector>
#include <cstring>

int main(int argc, char* argv[], char* env[])
{
    bool silent_mode_enabled = false;
    int  lines_to_output = -1;
    for(int i = 1; i < argc; i++)
    {
        if(strcmp(argv[i], "/S") == 0)
        {
            silent_mode_enabled = true;
        }
        else if(lines_to_output == -1)
        {
            try
            {
               lines_to_output = std::stoi(argv[i]); 
            }
            catch(const std::exception& e)
            {
                if(!silent_mode_enabled)
                {
                    std::cout << "Niepoprawna liczba linii lub jej brak!\n";
                }
                return 2;
            }
            
        }
    }

    if(lines_to_output == -1)
    {
        if(!silent_mode_enabled)
        {
            std::cout << "Niepoprawna liczba linii lub jej brak!";
            return 2;
        }
    }

    std::vector<std::string> stored_lines;
    std::string current_line;
    while(std::cin >> current_line)
    {
        stored_lines.push_back(current_line);
    }

    bool not_enough_lines_for_output = false;
    int number_of_missing_lines = stored_lines.size() - lines_to_output;
    if((not_enough_lines_for_output = (number_of_missing_lines < 0)))
    {
        lines_to_output = stored_lines.size();
    }
    else
    {
        lines_to_output = number_of_missing_lines;
    }

    for(int i = lines_to_output; i < stored_lines.size(); i++)
    {
        std::cout << stored_lines.at(i) << '\n';
    }

    if(not_enough_lines_for_output && !silent_mode_enabled)
    {
        std::cout << "Za malo linii na wejsciu: " << std::abs(number_of_missing_lines) << '\n';
        return 2;
    }

    return 0;
}