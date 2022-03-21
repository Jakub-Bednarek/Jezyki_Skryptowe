#include <iostream>
#include <algorithm>
#include <fstream>
#include <string>
#include <vector>
#include <stdio.h>
#include <sstream>
#include <conio.h>

struct Record {
    std::string date;
    int deaths;
    std::string country;
};

std::vector<Record> read_file(const std::string& path);
void save_file(const std::string& path, const std::vector<Record> values);

int main(int argc, char* argv[])
{
    std::string path = "temp.txt";
    std::string output_name = "sorted_temp.txt";
    std::cout << argv[0] << '\n';

    if (argc > 1)
    {
        path = argv[1];
    }

    auto records = read_file(path);
    std::sort(records.begin(), records.end(), [](const auto& v1, const auto& v2) { return v1.deaths < v2.deaths;  });
    save_file(output_name, records);

    return 0;
}

std::vector<Record> read_file(const std::string& path)
{
    std::ifstream input(path);

    if(!input.is_open())
    {
        return {};
    }

    std::string line;
    std::vector<Record> records;
    std::stringstream ss;
    while(std::getline(input, line))
    {
        ss << line;
        std::string date;
        std::string country;
        int deaths;

        ss >> deaths >> date >> country;
        records.push_back({date, deaths, country});
    }

    return records;
}

void save_file(const std::string& path, const std::vector<Record> values)
{
    std::ofstream output(path);

    if(!output.is_open())
    {
        return;
    }

    for(const auto& rec : values)
    {
        output << rec.country << '\t' << rec.date << '\t' << rec.deaths << '\n';
    }
}