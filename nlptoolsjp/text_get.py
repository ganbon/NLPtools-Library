from bs4 import BeautifulSoup
import requests
import time
from nlptoolsjp.file_system import file_create


def scraping(url, file_path = None):
    responses = requests.get(url)
    soup = BeautifulSoup(responses.content, 'html.parser')
    text_list = soup.get_text().splitlines()
    text_list = list(dict.fromkeys(text_list))
    text_list = [text.replace('\u3000', '') for text in text_list]
    text = '\n'.join(text_list)
    if file_path is not None:
        file_create(text,file_path)
    time.sleep(1)
    return text.split('\n')

def scraping_obj(url):
    responses = requests.get(url)
    soup = BeautifulSoup(responses.text, 'html.parser')
    return soup

def scraping_url(url,class_name,file_path = None):
    try:
        responses = requests.get(url)
        soup = BeautifulSoup(responses.text, 'html.parser')
    except:
        return []
    class_context = soup.find_all("a",class_=class_name)
    title_list = [con_text.text for con_text in class_context]
    url_list = [con_text.get("href") for con_text in class_context]
    if file_path is not None:
        file_create(class_context,file_path)
    return url_list,title_list

if __name__=="__main__":
    url = input()
    scraping(url)