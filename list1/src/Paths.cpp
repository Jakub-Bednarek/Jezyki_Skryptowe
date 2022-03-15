#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

std::vector<std::string> parse(const std::string& path_str);

int main(int argc, char* argv[], char* env[])
{
    std::vector<std::string> args;
    std::string path_string;
    while(*env != nullptr)
    {
        std::string var = *env++;
        if(var.find("PATH") != std::string::npos)
        {
            path_string = var;
        }
    }

    args = parse(path_string);
    if(args.size() == 0)
    {
        std::cout << "\tBRAK\n";
        return 0;
    }

    for(int i = 0; i < args.size(); i++)
    {
        std::cout << args.at(i);

        if(i > 0)
        {
            if(args.at(i) == args.at(i - 1))
            {
                std::cout << "\t DUPLIKAT";
            }
        }

        std::cout << '\n';
    }

    return 0;
}

std::vector<std::string> parse(const std::string& path_str)
{
    auto pos = path_str.find("=") + 1;
    std::vector<std::string> out;
    std::string copy = path_str;
    copy = copy.substr(pos, path_str.length());
    while(pos != std::string::npos)
    {
        pos = copy.find(";");
        out.push_back(copy.substr(0, pos));
        copy = copy.substr(0, pos + 1);
    }
    out.push_back(copy);

    return out;
}