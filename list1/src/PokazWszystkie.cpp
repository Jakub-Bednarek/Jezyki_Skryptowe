#include <iostream>
#include <algorithm>
#include <vector>
#include <iterator>

int main(int argc, char* argv[], char* env[])
{
    std::vector<std::string> args;
    std::vector<std::string> envs;

    for(int i = 0; i < argc; i++)
    {
        args.push_back(argv[i]);
    }

    while(*env != nullptr)
    {
        envs.push_back(*env++);
    }

    std::cout << "Argumenty programu:\n";
    std::copy(args.begin(), args.end(), std::ostream_iterator<std::string>(std::cout, "\n"));

    std::cout << "\nZmienne srodowiskowe\n";
    std::copy(envs.begin(), envs.end(), std::ostream_iterator<std::string>(std::cout, "\n"));

    return 0;
}