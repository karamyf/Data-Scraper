import requests
import csv
from bs4 import BeautifulSoup

url = "https://www.upwork.com/hire/java-developers/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

freelancers = soup.find_all("div", {"class": "o-card"})

with open("freelancers.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Freelancer Name", "Freelancer Title", "Freelancer Description"])
    for freelancer in freelancers:

        #h4 ellipsis no-modal mb-0
        name = soup.find("div", {"class": "h4 ellipsis no-modal mb-0"}).text
        title = freelancer.find("p", {"class": "o-card__subtitle"}).text
        description = freelancer.find("p", {"class": "o-card__description"}).text
        writer.writerow([name, title, description])

print("Done!")


'''
        price = soup.find("p", {"class": "price_color"}).text
        availability = soup.find("p", {"class": ...
'''
