import requests as r
from bs4 import BeautifulSoup
import json

from ..constants import SCRAPPING_KEY, SCRAPPING_URL
def get_content(url):
    response = get_data_embedly(url)['content']
    # response = r.get(url)
    # print(url)
    if response is not None:
        return response
    else:
        return "Error_404"

def get_data_embedly(url):
    url = SCRAPPING_URL + url
    print("Getting information from ",url)
    page = r.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    if soup is None or soup.pre is None:
        return None
    # print(soup.pre.text)
    json_text = html_decode(soup.pre.text)
    # print("text",json_text,"end2")
    row = json.loads(json_text)
    # print(row)
    if row['content'] is None and row['description'] is None:
        print("Skipping link : ",url)
        return None
    if row['content'] is None and row['description'] is not None :
        row['content'] = row['description']
    row['content']= BeautifulSoup(row['content'], "lxml").text
    row['provider_display'] = row['provider_display'].replace('www.','')
    return row


def html_decode(s):
    """
    Returns the ASCII decoded version of the given HTML string. This does
    NOT remove normal HTML tags like <p>.
    """
    htmlCodes = (
            ("'", '&#39;'),
            ('"', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            ('&', '&amp;')
        )
    for code in htmlCodes:
        s = s.replace(code[1], code[0])
    return s