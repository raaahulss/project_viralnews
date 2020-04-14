import requests as r

def get_content(url):
    response = r.get(url)
    print(url)
    if response is not None:
        return response.text
    else:
        return "Error_404"