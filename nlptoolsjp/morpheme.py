import MeCab 
import pykakasi
from nlptoolsjp.neologd_path import NEOLOGD_PATH

def morpheme(sentence,kind = False,neologd=False):
    """
    MeCabを用いた形態素解析を行う。

    Parameters
    -----------
    sentence : str
        形態素解析対象の文字列
    kind : bool (default=False)
        Trueで形態素の品詞等をまとめた辞書を返す
    neologd : bool (default=False)
        TrueでNeologd辞書に変換する（辞書インストールが必要）

    Returns
    -----------
    morpheme_list : list of str
        分かち書きした結果を格納したリスト
    morpheme_dict : dict 
        keyに分割した形態素、valuesに対象の形態素の品詞、活用、基本形、読み方が
        格納されている
        
    Notes
    -----------
    MeCabのインストールが必要
    標準辞書はIPAの辞書を用いることを前提に作成している
    Neologdの環境Pathをneologd_path.pyに記述して使用してください
    """
    if neologd:
        wakati = MeCab.Tagger(NEOLOGD_PATH)
    else:
        wakati = MeCab.Tagger('-Owakati')
    kks = pykakasi.kakasi()
    if kind:
        morpheme_list = []
        morpheme_dict = {}
        node = wakati.parseToNode(sentence)
        while node:
            word = node.surface
            if word!="":
                morpheme_list.append(word)
            kind_dict = {}
            node_list = node.feature.split(",")
            if neologd:
                if node_list[1] == '数詞':
                    kind_dict = {
                        'speech': node_list[0],
                        'detail_speech': node_list[1]
                        }
                else:
                    reading = kks.convert(node_list[-2])
                    kind_dict = {
                        'speech': node_list[0],
                        'detail_speech': node_list[1:4],
                        'endform': node_list[-3],
                        'reading': reading[0]["hira"] 
                    }
                    if len(node_list) > 5:
                        kind_dict['endform'] = node_list[-3]
                        kind_dict['reading'] = reading[0]["hira"] 
            else:
                kind_dict = {
                    'speech': node_list[0],
                    'detail_speech': node_list[1:4],
                }
                if len(node_list) > 7:
                    kind_dict['inflect'] = node_list[5]
                    kind_dict['endform'] = node_list[7]
                    reading = kks.convert(node_list[-1])
                    kind_dict['reading'] = reading[0]["hira"]  
                else:
                    kind_dict['inflect'] = "*"
                    kind_dict['endform'] = "*"
                    reading = kks.convert(node_list[-1])
                    kind_dict['reading'] = reading[0]["hira"]  
            if word not in morpheme_dict.keys():
                morpheme_dict[word] = kind_dict
            node = node.next
        return morpheme_dict,morpheme_list
    else:
        morpheme_list = wakati.parse(sentence).split()
        return morpheme_list

            
        

def main():   
    s = input()
    a = morpheme(s)
    b = morpheme(s,kind = True)
    print()
    c = morpheme(s,neologd= True)
    d = morpheme(s,kind = True,neologd= True)
    print(a)
    print(b)
    print(c)
    print(d)

if __name__=='__main__':
    main()

