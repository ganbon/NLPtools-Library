def generate_text_from_model(input,tokenizer,train_model,
                             max_length_src = 20, max_length_target = 2, num_return_sequences = 3):
    train_model.eval()
    batch = tokenizer([input], max_length = max_length_src, 
                      truncation = True, padding = 'longest', return_tensors = 'pt')
    # 生成処理を行う
    outputs = train_model.generate(input_ids = batch['input_ids'], attention_mask = batch['attention_mask'], 
                                   max_length = max_length_target, repetition_penalty = 8.0, num_return_sequences = num_return_sequences)
    generated_texts = [tokenizer.decode(ids, skip_special_tokens = True, clean_up_tokenization_spaces = False) for ids in outputs]
    return generated_texts