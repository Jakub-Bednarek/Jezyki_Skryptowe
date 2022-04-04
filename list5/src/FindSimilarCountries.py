import sys
import Leven

DEFAULT_COUNTRY_INDEX = 6
DEFAULT_COVID_FILENAME = "Covid.txt"

def GetUniqueCountries(fileName):
    uniqueCountries = set()
    with open(fileName) as file:
        lines = file.readlines()
        for line in lines:
            tokens = line.split()
            uniqueCountries.add(tokens[DEFAULT_COUNTRY_INDEX])
            
    return uniqueCountries
                

def FindSimilarCountries(keyword, similarityLevel):
    outputList = []
    uniqueCountires = GetUniqueCountries(DEFAULT_COVID_FILENAME)
    
    for country in uniqueCountires:
        countrySimilarity = Leven.LevSim(keyword, country)
        if countrySimilarity <= similarityLevel:
            outputList.append((country, countrySimilarity))
            
    outputList.sort(key = lambda x: x[1])
    return outputList

def main():
    country = sys.argv[1]
    similarity = int(sys.argv[2])
    
    print(FindSimilarCountries(country, similarity))
    
if __name__ == "__main__":
    main()