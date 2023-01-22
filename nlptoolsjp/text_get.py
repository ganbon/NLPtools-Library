from bs4 import BeautifulSoup
import requests 
from urllib.request import urlopen
import time
from nlptoolsjp.file_system import file_create

def scraping_obj(url,open=False):
    """
    requestsにより指定したURLをスクレイピングし、要素を返す

    Parameters
    ----------
    url: str
        スクレイピング先のURL
    open : bool (default=False)
        Trueでurlopenでスクレイピングする

    Returns
    ----------
        soup : BuautifulSoupオブジェクト
    """
    if open:
        responses = urlopen(url)
        soup = BeautifulSoup(responses,'html.parser')
    else:
        responses = requests.get(url)
        soup = BeautifulSoup(responses.text, 'html.parser')
    time.sleep(10)
    return soup

def scraping(url, file_path = None):
    """
    requestsにより指定したURLをスクレイピングし、結果のテキスト部分のみ返す

    Parameters
    ----------
    url: str
        スクレイピング先のURL
    file_path : str (default=None)
        保存先を指定する

    Returns
    ----------
    text.split('\n') : list of str
        スクレイピングのテキスト部分を改行部分で区切ったリストを返す
    """
    responses = requests.get(url)
    soup = BeautifulSoup(responses.content, 'html.parser')
    text_list = soup.get_text().splitlines()
    text_list = list(dict.fromkeys(text_list))
    text_list = [text.replace('\u3000', '') for text in text_list]
    text = '\n'.join(text_list)
    if file_path is not None:
        file_create(text,file_path)
    time.sleep(10)
    return text.split('\n')

def scraping_url(soup=None,url=None,class_name=None,file_path = None):
    """
    requestsにより指定したURLをスクレイピングし、aタグのURLのみを取得する

    Parameters
    ----------
    soup : BeautifulSoupオブジェクト (default=None)
        スクレイピングのhtml要素をそのまま渡す
    url: str (default=None)
        スクレイピング先のURL
    class_name : str (default=None)
        htmlのタグのクラス名を指定する
    file_path : str (default=None)
        保存先を指定する

    Returns
    ----------
    url_list : list of str
        取得したURLをリストに格納して返す    
    title_list : list of str
        取得したURLタイトルをリストに格納して返す
    """
    if soup is None:
        try:
            responses = requests.get(url)
            soup = BeautifulSoup(responses.text, 'html.parser')
            time.sleep(10)
        except:
            return []
    if class_name is None:
        class_context = soup.find_all("a")
    else:
        class_context = soup.find_all("a",class_=class_name)
    title_list = [con_text.text for con_text in class_context]
    url_list = [con_text.get("href") for con_text in class_context]
    if file_path is not None:
        file_create(class_context,file_path)
    return url_list,title_list

if __name__=="__main__":
    url = input()
    scraping(url)