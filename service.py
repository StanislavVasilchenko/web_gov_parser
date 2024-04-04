import time

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
}


def get_xml_response(url):
    all_links = []
    for page in range(1, 3):
        response = requests.get(
            f'{url}/epz/order/extendedsearch/results.html?fz44=on&pageNumber={page}',
            headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all(attrs={'class': 'w-space-nowrap ml-auto registry-entry__header-top__icon'})
            for link in links:
                old_str = link.find_all('a')[1].get('href')
                new_str = url + old_str.replace('view.html', 'viewXml.html')
                all_links.append(new_str)
            time.sleep(2)
        else:
            print(f'Connection error. Page - {page}. Status code: {response.status_code}')
    return xml_parsing(all_links)


def xml_parsing(all_links):
    for link in all_links:
        response = requests.get(link, headers=headers)
        if response.status_code == 200:
            content = BeautifulSoup(response.content, features='lxml-xml')
            elements = content.find('publishDTInEIS')
            print(elements.get_text())
        else:
            print(f'Connection error')
