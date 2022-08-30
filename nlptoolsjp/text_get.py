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
        
if __name__=="__main__":
    url = input()
    scraping(url,f"data/test.txt")