import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

result = requests.get("https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html")

src = result.content
print(src)