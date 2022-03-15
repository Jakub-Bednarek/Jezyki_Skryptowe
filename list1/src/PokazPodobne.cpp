#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>

#ifdef __WIN32
    #include <sysinfoapi.h>
#endif //__Win32

std::vector<std::string> process_envs(const std::vector<std::string>& args,
                                      const std::vector<std::string>& envs);
std::string process_line(size_t name_pos, const std::string& line);

int main(int argc, char* argv[], char* env[])
{
    std::vector<std::string> envs;
    std::vector<std::string> args;

    for(int i = 0; i < argc; i++)
    {
        args.push_back(argv[i]);
    }

    while(*env != nullptr)
    {
        envs.push_back(*env++);
    }

    if(!envs.empty())
    {
        envs = process_envs(args, envs);
        std::sort(envs.rbegin(), envs.rend());
        std::copy(envs.begin(), envs.end(), std::ostream_iterator<std::string>(std::cout, "\n"));
    }
#ifdef __WIN32
    else
    {
        OSVERSIONINFOEX osinfo;
        osinfo.dwOSVersionInfoSize = sizeof(osinfo);
        osinfo.szCSDVersion[0] = L'\0';

        if(GetOSVersion(&osinfo))
        {
            DWORD dwProductType = 0;
            if(GetProductInfo(osinfo.dwMajorVersion, osinfo.dwMinorVersion, 0, 0, &dwProductType)
            {
                if(dwProductType == PRODUCT_CLOUD || dwProductType == PRODUCT_CLOUDN)
                {
                    std::cout << "parametr = NONE\n";
                }
            }
        }
    }
#else
    else
    {
        std::cout << "parametr = NONE\n";
    }
#endif //__WIN32

    return 0;
}

std::vector<std::string> process_envs(const std::vector<std::string>& args,
                                      const std::vector<std::string>& envs)
{
    std::vector<std::string> output;
    for(auto& str : envs)
    {
        auto pos = str.find("=");
        if(pos != std::string::npos)
        {
            std::string name = str.substr(0, pos);
            if(std::any_of(args.begin(), args.end(), [&name](const auto& line) { return line == name; }))
            {
                std::string processed_line = process_line(pos, str);
                output.push_back(processed_line);
            }
        }
    }

    return output;
}

std::string process_line(size_t name_pos, const std::string& line)
{
    std::string out_line;
    std::string values = line.substr(name_pos + 1, line.length());

    out_line += line.substr(0, name_pos);
    out_line += "\n=\n";
    
    bool found_multiple_entries = false;
    size_t next_value_pos = values.find(";");
    while(next_value_pos != std::string::npos)
    {
        out_line += ("\t" + values.substr(0, next_value_pos) + "\n");
        values = values.substr(next_value_pos + 1, values.length());
        next_value_pos = values.find(";");
        found_multiple_entries = true;
    }

    if(found_multiple_entries)
    {
        out_line += "\t";
    }

    out_line += values.substr(0, values.length());

    return out_line;
}