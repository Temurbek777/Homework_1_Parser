import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import re

"""Function for extracting all external links"""


def getExternalLinks(url):
    external_links = []

    res = requests.get(url)

    soup = BeautifulSoup(res.text, "html.parser")

    links = soup.find_all('a', href=True)

    base_url = urlparse(url).netloc

    for link in links:
        href = link['href']
        parsed_href = urlparse(href)
        # print(parsed_href)

        if parsed_href.scheme in ('http', 'https') and parsed_href.netloc != base_url:
            external_links.append(href)

    while True:
        try:
            a = int(input("Choose\n 1.Print to terminal \n 2.Save to file\n"))
            if a == 1:
                print("External links of the ", url)
                for i in external_links:
                    print(i)
                break
            elif a == 2:
                f = open("External_links.txt", "w")
                f.write(f"External links of the {url}")
                for i in external_links:
                    f.write(i)
                    f.write("\n")
                f.close()
                break
        except  ValueError:
            print("Only integers are allowed")

    # print("New Links")
    # for i in external_links:
    #     return getExternalLinks(i)


getExternalLinks("https://www.askpython.com/")  # Calling function
