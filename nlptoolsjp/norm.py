from unicodedata import normalize
import re

def remove_str(text,remove_str='[!"#$%&\'\\\\()*+,-./:;<=>?@꒳[\\]^_`{|}~「」〔〕“”〈〉『』【】＆＊・（）＄＃＠。、？！｀＋￥％∀;…]'):
    code_regex = re.compile(remove_str)
    if type(text) is str:
        return code_regex.sub('', text)
    elif type(text) is list:
        return [code_regex.sub('', t) for t in text]
    
def clean_text(text,norm_op=True):
    result = []
    if type(text) is list:
        for t in text:
            try:
                t = re.sub(r'[\n\t\u3000]', '', t).strip(" ")
                if norm_op:
                    t = normalize('NFKC',t)
                result.append(t.lower())    
            except:
                # print(t)
                result.append(t)
                pass
    else:
        result = re.sub(r'[\n\t\u3000]', '',text).strip(" ")
        if norm_op:
            result = normalize('NFKC',text.lower())
    return result

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