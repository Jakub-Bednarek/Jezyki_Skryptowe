#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

#define DEFAULT_COVID_FILENAME "Covid.txt"
#define DEFAULT_COUNTRY "Poland"
#define DEFAULT_MONTH "1"
#define DEFAULT_MONTH_INDEX 2
#define DEFAULT_COUNTRY_INDEX 6
#define DEFAULT_CASES_INDEX 4
#define EXPECTED_ARGUMENTS_SIZE 3
#define EXPECTED_TOKENS_IN_LINE 12

int get_total_cases(const std::string& month, const std::string& country);
std::string get_month_from_arguments(char* argv[], int argv_size, int& pos);
int extract_cases_for_month_and_country(const std::vector<std::string>& tokens, const std::string& month, const std::string& country);
std::vector<std::string> split_line_to_tokens(const std::string& line);
std::pair<std::string, std::string> get_month_and_country_args(char* argv[], int argv_size);

int main(int argc, char* argv[])
{
    const auto month_and_country = get_month_and_country_args(argv, argc);

    std::cout << get_total_cases(month_and_country.first, month_and_country.second) << '\n';

    return 0;
}

int get_total_cases(const std::string& month, const std::string& country)
{
    std::ifstream input(DEFAULT_COVID_FILENAME);
    unsigned int sum = 0;

    std::string line;
    while(std::getline(input, line))
    {
        const auto tokens = split_line_to_tokens(line);

        sum += extract_cases_for_month_and_country(tokens, month, country);
        // std::cout << sum << '\n';
    }

    return sum;
}

std::string get_month_from_arguments(char* argv[], int argv_size, int& pos)
{
    int month = 0;
    for(int i = 1; i < argv_size; i++)
    {
        try
        {
            int temp = std::stoi(argv[i]);
            pos = i;
            return argv[i];
        }
        catch(const std::exception& e) {}
    }

    return "";
}

int extract_cases_for_month_and_country(const std::vector<std::string>& tokens, const std::string& month, const std::string& country)
{
    if(tokens.size() != EXPECTED_TOKENS_IN_LINE)
    {
        return 0;
    }

    int cases = 0;
    if(tokens.at(DEFAULT_MONTH_INDEX) == month && tokens.at(DEFAULT_COUNTRY_INDEX) == country)
    {
        try
        {
            cases = std::stoi(tokens.at(DEFAULT_CASES_INDEX));
        }
        catch(const std::exception& e) {}
    }

    return cases;
}

std::vector<std::string> split_line_to_tokens(const std::string& line)
{
    std::vector<std::string> output;
    std::stringstream ss;
    ss << line;

    std::string token;
    while(ss >> token)
    {
        output.push_back(token);
    }

    return output;
}

std::pair<std::string, std::string> get_month_and_country_args(char* argv[], int argv_size)
{
    if(argv_size == 1)
    {
        return std::make_pair(DEFAULT_MONTH, DEFAULT_COUNTRY);
    }

    int month_pos = 0;
    std::string month = get_month_from_arguments(argv, argv_size, month_pos);
    if(month_pos == 0)
    {
        return std::make_pair(DEFAULT_MONTH, argv[1]);
    }

    return std::make_pair(month, argv[EXPECTED_ARGUMENTS_SIZE - month_pos]);
}