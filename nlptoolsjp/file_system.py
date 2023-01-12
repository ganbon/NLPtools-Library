import csv
import json
import pandas as pd
import pickle


def file_create(data,file_path,mode='w'):
    if '.txt' in file_path or '.html' in file_path:
        with open(file_path,mode = mode,encoding = 'utf-8') as f:
            if type(data) is str:
                f.write(data)
            elif type(data) is list:
                for d in data:
                    f.write(d+"\n")
    elif '.json' in file_path:
        with open(file_path, mode = "wt", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii = False) 
    elif '.pkl' in file_path:
        with open(file_path,'wb') as tf:
            pickle.dump(file_path,tf)
    elif '.csv' in file_path:
        with open(file_path, mode = mode, encoding="utf-8") as f:
            if type(data) is list:
                writer = csv.writer(f)
                writer.writerows(data)
            elif type(data) is pd.DataFrame:
                 data.to_csv(file_path,index = False)
    

def file_load(file_path):
    if '.json' in file_path:
        with open(file_path, mode = 'r', encoding="utf-8") as f:
           data = json.load(f) 
    elif '.csv' in file_path:
            data = pd.read_csv(file_path)
    elif '.pkl' in file_path:
        with open(file_path,mode = 'rb') as tf:
            data = pickle.load(tf)
    else:
        with open(file_path, mode = 'r', encoding='utf-8') as f:
            lines = f.read()
            data = [l for l in lines.split('\n')]
    return data
    
            