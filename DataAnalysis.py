# This program analyzes life expectancy data from a CSV file.
# It finds the lowest and highest life expectancy overall and allows the user to query specific years and countries.

# Define the file path
fileName = 'life-expectancy.csv'
filePath = 'C:/Users/USER/Downloads/'
fullFilePath = filePath + fileName

# Function to load the data from the CSV file
def load_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip().split(',') for line in lines[1:]]  # Skip the header

# Load the data
data = load_data(fullFilePath)

# Print the first few rows to check the data (optional)
for row in data[:5]:  # Display first 5 rows of data
    print(row)

def find_min_max_life_expectancy(data):
    min_life = float('inf')
    max_life = float('-inf')
    min_year = max_year = ''
    min_country = max_country = ''

    for row in data:
        year = row[0]
        country = row[1]
        life_expectancy = float(row[2])  # Corrected variable name
        
        if life_expectancy < min_life:
            min_life = life_expectancy
            min_year = year
            min_country = country
        
        if life_expectancy > max_life:
            max_life = life_expectancy
            max_year = year
            max_country = country

    return (min_year, min_country, min_life), (max_year, max_country, max_life)

def average_life_expectancy_for_year(data, year):
    total_life_expectancy = 0
    count = 0
    min_life = float('inf')
    max_life = float('-inf')
    min_country = max_country = ''

    for row in data:
        if row[0] == year:
            country = row[1]
            life_expectancy = float(row[2])  # Corrected variable name
            total_life_expectancy += life_expectancy
            count += 1
            
            if life_expectancy < min_life:
                min_life = life_expectancy
                min_country = country
            
            if life_expectancy > max_life:
                max_life = life_expectancy
                max_country = country

    average = total_life_expectancy / count if count > 0 else 0
    return average, (min_country, min_life), (max_country, max_life)

def main():
    data = load_data(fullFilePath)

    (min_year, min_country, min_life), (max_year, max_country, max_life) = find_min_max_life_expectancy(data)
    print(f"The overall max life expectancy is: {max_life} from {max_country} in {max_year}")
    print(f"The overall min life expectancy is: {min_life} from {min_country} in {min_year}")

    year_of_interest = input("Enter the year of interest: ")
    average, (min_country_year, min_life_year), (max_country_year, max_life_year) = average_life_expectancy_for_year(data, year_of_interest)

    print(f"For the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was {average:.2f}")
    print(f"The max life expectancy was in {max_country_year} with {max_life_year:.2f}")
    print(f"The min life expectancy was in {min_country_year} with {min_life_year:.3f}")

    # Additional feature: country-specific analysis
    country_of_interest = input("Enter a country to analyze life expectancy: ")
    total_life_expectancy = 0
    count = 0
    min_life_country = float('inf')
    max_life_country = float('-inf')

    for row in data:
        if row[1] == country_of_interest:
            life_expectancy = float(row[2])  # Corrected variable name
            total_life_expectancy += life_expectancy
            count += 1
            
            if life_expectancy < min_life_country:
                min_life_country = life_expectancy
            
            if life_expectancy > max_life_country:
                max_life_country = life_expectancy

    average_country = total_life_expectancy / count if count > 0 else 0
    print(f"For {country_of_interest}:")
    print(f"Average life expectancy: {average_country:.2f}")
    print(f"Max life expectancy: {max_life_country:.2f}")
    print(f"Min life expectancy: {min_life_country:.2f}")

if __name__ == "__main__":
    main()


import pandas as pd
import numpy as py

fileName = 'life-expectancy.csv'
filePath = 'C:/Users/USER/Downloads/'
fullFilePath = filePath + fileName

print(fullFilePath)

df = pd.read_csv(fullFilePath)

df
