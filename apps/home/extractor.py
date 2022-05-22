from bs4 import BeautifulSoup
import requests

def get_css_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for link in soup.find_all('link'):
        href = link.get('href')
        if href and 'css' in href:
            if url in href:
                links.append(href)
            else:
                links.append(url+href)
    return links


def get_js_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for link in soup.find_all('script'):
        src = link.get('src')
        if  src and 'js' in src:
            if url in src:
                links.append(src)
            else:
                links.append(url+src)
    return links

def get_link_data(file_url):
    try:
        r = requests.get(file_url, stream = True)
        data = ""
        for line in r.iter_lines():
            data += line.decode('utf-8')
        return data
    except:
        return None

if __name__ == '__main__':
    url = 'https://github.com/ANSHULKO/design_extractor'
    css_links = get_css_links(url)
    js_links = get_js_links(url)
    print(css_links)
    print(js_links)
