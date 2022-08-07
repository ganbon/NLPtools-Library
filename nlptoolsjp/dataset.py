from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader

class NLP_Dataset:
    def __init__(self,tokenizer,
                 enc_max_len = 50,
                 dec_max_len = 100,
                 batch_size = 8):
        self.tokenizer = tokenizer
        self.enc_max_len = enc_max_len
        self.dec_max_len = dec_max_len
        self.batch_size = batch_size
    
    def load_data(self,input_list,output_list):
        x_train,x_test,t_train,t_test=train_test_split(input_list,output_list,test_size=0.2, random_state=42, shuffle=True)
        train_data = [(src, tgt) for src, tgt in zip(x_train, t_train)]
        test_data = [(src, tgt) for src, tgt in zip(x_test, t_test)]
        train,test = self.convert_batch_data(train_data,test_data)
        return train,test
    
    def convert_batch_data(self,train_data, valid_data):
        train_iter = DataLoader(train_data, batch_size=self.batch_size, collate_fn=self.convert_tokenizer)
        valid_iter = DataLoader(valid_data, batch_size=self.batch_size, collate_fn=self.convert_tokenizer)
        return train_iter, valid_iter
    
    def convert_tokenizer(self,data):
        src_list, tgt_list = [], []
        for src, tgt in data:
            src_list.append(src)
            tgt_list.append(tgt)   
        src_list = self.tokenizer(src_list, max_length=self.enc_max_len, truncation=True, padding="max_length", return_tensors="pt")
        if type(tgt_list[0]) is str:
            tgt_list = self.tokenizer(tgt_list, max_length=self.dec_max_len, truncation=True, padding="max_length", return_tensors="pt")
        return src_list, tgt_list

    