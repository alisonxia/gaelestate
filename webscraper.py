from bs4 import BeautifulSoup
import requests

url = 'https://www.facebook.com/marketplace/kingston-ca/propertyrentals?exact=false'

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

links = soup.findAll("div", class_="a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7")
print(links)
for link in links:
    print("div")


