from operator import ne
from nlptoolsjp.morpheme import morpheme 

def bleu(test_text,pre_text,n=5,nelogd=False):
    test_mor = morpheme(test_text,nelogd = nelogd)
    pre_mor = morpheme(pre_text,nelogd = nelogd)
    p_list = []
