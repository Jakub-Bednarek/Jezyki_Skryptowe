#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <iterator>

int main(int argc, char* argv[])
{
    bool silent_mode_enabled = false;
    int  lines_to_output = -1;
    int current_arg = 1;
    if (strcmp(argv[current_arg], "/S") == 0)
    {
        silent_mode_enabled = true;
        current_arg++;
    }

    try
    {
        lines_to_output = std::stoi(argv[current_arg++]);
    }
    catch (const std::exception& e)
    {
        std::cout << "Invalid number of lines\n";
        return 2;
    }

    std::ifstream input(argv[current_arg]);
    if (!input.is_open())
    {
        return 1;
    }

    std::vector<std::string> output;
    int count = 0;
    std::string line;
    while (std::getline(input, line))
    {
        if (count < lines_to_output)
        {
            output.push_back(line);
            count++;
        }
        else
        {
            output.erase(output.begin());
            output.push_back(line);
        }
    }

    std::copy(output.begin(), output.end(), std::ostream_iterator<std::string>(std::cout, "\n"));
    return 0;
}