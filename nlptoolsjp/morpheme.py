import MeCab 
import pykakasi


def morpheme(input,kind = False,nelogd = False):
    if nelogd:
        wakati = MeCab.Tagger('-Owakati -d "C:/Program Files/MeCab/dic/ipadic" -u "C:/Program Files/MeCab/dic/NEologd/NEologd.dic"')
    else:
        wakati = MeCab.Tagger('-Owakati')
    kks = pykakasi.kakasi()
    if kind:
        sentence = []
        morpheme_dict = {}
        node = wakati.parseToNode(input)
        while node:
            word = node.surface
            if word!="":
                sentence.append(word)
            kind_dict = {}
            node_list = node.feature.split(",")
            if nelogd:
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
        return morpheme_dict,sentence
    else:
        sentence = wakati.parse(input).split()
        return sentence

            
        

def main():   
    s = input()
    a = morpheme(s)
    b = morpheme(s,kind = True)
    print()
    c = morpheme(s,nelogd = True)
    d = morpheme(s,kind = True,nelogd = True)
    print(a)
    print(b)
    print(c)
    print(d)

if __name__=='__main__':
    main()

