import MeCab 
import jaconv


def morpheme(input,kind = False,nelogd = False):
    if nelogd:
        wakati = MeCab.Tagger('-Owakati -d "C:/Program Files/MeCab/dic/ipadic" -u "C:/Program Files/MeCab/dic/NEologd/NEologd.20200910-u.dic"')
    else:
        wakati = MeCab.Tagger('-Owakati')
    if kind:
        sentence = wakati.parse(input).split()
        node = wakati.parseToNode(input)
        kind_list = []
        while node:
            kind_dict = {}
            node_list = node.feature.split(",")
            if node_list[0]!="BOS/EOS":
                if nelogd:
                    if node_list[1] == '数詞':
                        kind_dict = {
                            'speech': node_list[0],
                            'detail_speech': node_list[1]
                            }
                    else:
                        kind_dict = {
                            'speech': node_list[0],
                            'detail_speech': node_list[1:4],
                            'endform': node_list[-3],
                            'reading': jaconv.kata2hira(node_list[-2])
                        }
                        if len(node_list) > 5:
                            kind_dict['endform'] = node_list[-3]
                            kind_dict['reading'] = jaconv.kata2hira(node_list[-2])
                else:
                    kind_dict = {
                        'speech': node_list[0],
                        'detail_speech': node_list[1:4],
                    }
                    if len(node_list) > 7:
                        kind_dict['inflect'] = node_list[5]
                        kind_dict['endform'] = node_list[7]
                        kind_dict['reading'] = jaconv.kata2hira(node_list[-1])     
                kind_list.append(kind_dict)
            node = node.next
        morpheme_dict = dict(zip(sentence,kind_list))
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

