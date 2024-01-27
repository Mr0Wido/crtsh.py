#!/usr/bin/env python3
import argparse
import requests
from bs4 import BeautifulSoup

class CrtShScraper:
    def __init__(self, domain):
        self.domain = domain

    def scrape_crtsh(self):
        url = f"https://crt.sh/?q=%25.{self.domain}"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            tr_tags = soup.find_all("tr")
            crt_subdomains = []
            for tr_tag in tr_tags:
                td_tags = tr_tag.find_all("td")
                if len(td_tags) >= 6:
                    crtsh = td_tags[5].get_text(strip=True)
                    if "." in crtsh:
                        crt_subdomains.append(crtsh)
            return crt_subdomains

def main():
    parser = argparse.ArgumentParser(description="Use the domain name to pull crt.sh data.")
    parser.add_argument("-d", "--domain", required=True, help="Domain name to search in crt.sh.")
    args = parser.parse_args()

    crtsh_scraper = CrtShScraper(args.domain)
    subdomains = crtsh_scraper.scrape_crtsh()

    for subdomain in subdomains:
        print(subdomain)

if __name__ == "__main__":
    main()
