from unicodedata import normalize
import re

def remove_str(sentence,remove_str='[!"#$%&\'\\\\()*+,-./:;<=>?@꒳[\\]^_`{|}~「」〔〕“”〈〉『』【】＆＊・（）＄＃＠。、？！｀＋￥％∀;…]'):
    """
    不要な文字を削除する

    Parameters
    ----------
    setnence: str
        除去元の文字列
    remove_str : str (default=[!"#$%&\'\\\\()*+,-./:;<=>?@꒳[\\]^_`{|}~「」〔〕“”〈〉『』【】＆＊・（）＄＃＠。、？！｀＋￥％∀;…])
        除去したい文字列、正規表現でも可

    Returns
    ----------
    除去済みの文字列

    Notes
    --------
    特殊文字を消す回数が多いためライブラリとしてまとめた。
    """
    code_regex = re.compile(remove_str)
    if type(sentence) is str:
        return code_regex.sub('', sentence)
    elif type(sentence) is list:
        return [code_regex.sub('', t) for t in sentence]
    
def clean_text(sentence,norm_op=True):
    """
    改行、半角等を取り除く。
    また、norm_opがTrueのときnormalizeで正規化を行う

    Parameters
    ----------
    setnence: str
        正規化したい文字列
    norm_op : bool (default=True)
        normalizeで正規化する

    Returns
    ----------
    result : str
        正規化済みの文字列

    Notes
    --------
    よく使うためライブラリとしてまとめた。
    """
    result = []
    if type(sentence) is list:
        for t in sentence:
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
        result = re.sub(r'[\n\t\u3000]', '',sentence).strip(" ")
        if norm_op:
            result = normalize('NFKC',sentence.lower())
    return result


if __name__=='__main__':
    data = '　固い地べたの感触を顔面に味わい、\n\n彼は自分がうつ伏せに倒れたのだと気付いた。\n\n全身に力が入らず、手先の感覚はすでにない。\n\n\nただ、喉をかきむしりたくなるほどの熱が体の真ん中を支配している。'
    clean_data = clean_text(data)
    print(clean_data)