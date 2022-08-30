from unicodedata import normalize
import re

def remove_str(text,remove_str='[!"#$%&\'\\\\()*+,-./:;<=>?@[\\]^_`{|}~「」〔〕“”〈〉『』【】＆＊・（）＄＃＠。、？！｀＋￥％]'):
    code_regex = re.compile(remove_str)
    return code_regex.sub('', text)
    
def clean_text(text):
    result = []
    if type(text) is list:
        for t in text:
            t = re.sub(r'[\n \u3000]', '', t) 
            t = normalize('NFKC',t)
            result.append(t.lower())    
        return text
    else:
        text = re.sub(r'[\n \u3000]', '',text)
        return normalize('NFKC',text.lower())

def japan_textline(text):
    result = ''
    for t in text:
        if t=='。':
            result+='。\n'
        else:
            result += t
    return result

if __name__=='__main__':
    data = '　固い地べたの感触を顔面に味わい、\n\n彼は自分がうつ伏せに倒れたのだと気付いた。\n\n全身に力が入らず、手先の感覚はすでにない。\n\n\nただ、喉をかきむしりたくなるほどの熱が体の真ん中を支配している。'
    clean_data1 = clean_text(data)
    clean_data2 = japan_textline(clean_data1)
    print(clean_data2)