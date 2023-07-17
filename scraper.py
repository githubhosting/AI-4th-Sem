import bs4 as beautifulsoup4
import requests

url = "https://www.branch.io/customers/"

response = requests.get(url)
soup = beautifulsoup4.BeautifulSoup(response.text, "html.parser")
print(soup.prettify())