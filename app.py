import requests
import csv
import os
'''These modifications help enhance the security 
of the script by addressing common security concerns
 and ensuring safe handling of data and file operations.'''


def fetch_covid_data():
    url = "https://disease.sh/v3/covid-19/countries/"
    query_countries = ["USA", "India", "Brazil", "Russia", "France", "Germany", "UK", "Italy", "Turkey", "Argentina",
                       "Spain", "Colombia", "Poland", "Iran", "Mexico", "Ukraine", "Peru", "South Africa", "Netherlands", "Indonesia"]

    for country in query_countries:
        try:
            response = requests.get(url + country)
            response.raise_for_status()  # Raise an error for invalid responses
            data = response.json()

            # Validate response data
            if all(key in data for key in ['Date', 'Cases', 'Deaths']):
                # Construct file path with sanitized country name
                country_file_name = ''.join(c for c in country if c.isalnum())  # Remove non-alphanumeric characters
                file_path = os.path.join('/path/to/csvs', f"{country_file_name.lower()}_covid_data.csv")

                # Writing data to CSV file
                with open(file_path, 'w', newline='') as csvfile:
                    fieldnames = data.keys()
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerow(data)
            else:
                print(f"Invalid data received for {country}: {data}")

        except requests.RequestException as e:
            print(f"Error fetching data for {country}: {e}")

if __name__ == "__main__":
    fetch_covid_data()
