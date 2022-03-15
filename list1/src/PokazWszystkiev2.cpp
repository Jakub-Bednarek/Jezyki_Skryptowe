#include <iostream>

int main(int argc, char* argv[], char* env[])
{
    std::cout << "Program arguments:\n";
    for(int i = 0; i < argc; i++)
    {
        std::cout << argv[i] << '\n';
    }

    std::cout << "Program envs:\n";
    while(*env != nullptr)
    {
        std::cout << *env++ << '\n';
    }
    return 0;
}