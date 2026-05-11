from fasttext_utils import segment
import pickle,random
import numpy as np
from fasttext import process_words
from sklearn.model_selection import train_test_split
import pandas as pd
import ast
vec_dir="file\\fasttext.pkl"
train= "file\\pre_datas_train.csv"
test="file\\pre_datas_test.csv" 
val="file\\pre_datas_val.csv" 
def pre_process():
    with open(vec_dir, "rb") as f:
        fasttext = pickle.load(f)
        embeddings = fasttext["embeddings"]
    # normal_data = pd.read_csv("data/dmzo_normal.csv", encoding='utf-8',names=['payload'])
    # xss_data = pd.read_csv("data/xss.csv", encoding='utf-8',names=['payload'])
    # sql_data = pd.read_csv("data/sql.csv", encoding='utf-8',names=['payload'])
    normal_data = []
    with open("data/dmzo_normal.csv", mode = 'r',errors='ignore',encoding='utf-8') as f:
        for line in f:
            normal_data.append(line.strip())
    normal_data = pd.DataFrame(normal_data, columns=['payload'])
    normal_data.dropna(inplace=True)
    print(normal_data)

    sql_data = []
    with open("data/sql.csv", mode = 'r',errors='ignore',encoding='utf-8') as f:
        for line in f:
            sql_data.append(line.strip())
    sql_data = pd.DataFrame(sql_data, columns=['payload'])
    sql_data.dropna(inplace=True)
    print(sql_data)

    xss_data = []
    with open("data/xss.csv", mode = 'r',errors='ignore',encoding='utf-8') as f:
        for line in f:
            xss_data.append(line.strip())
    xss_data = pd.DataFrame(xss_data, columns=['payload'])
    xss_data.dropna(inplace=True)
    print(xss_data)
    normal_data['label'] = 0
    xss_data['label'] = 1
    sql_data['label'] = 1

    data = pd.concat([normal_data, xss_data,sql_data])
    data['words'] = data['payload'].map(segment)
    data['processed_words'] = data['words'].apply(process_words)
    all_data = data['processed_words'].tolist()
    label_data = data['label'].tolist()
    random.seed(42)
    rand = random.sample(range(len(all_data)), len(all_data))
    datas = [all_data[index] for index in rand]
    labels = [label_data[index] for index in rand]
    all_data = datas
    label_data = labels
    train_val_datas, test_datas, train_val_labels, test_labels = train_test_split(all_data, label_data, test_size=0.2)
    train_datas, val_datas, train_labels, val_labels = train_test_split(train_val_datas, train_val_labels, test_size=0.25)
    train_size = len(train_labels)
    test_size = len(test_labels)
    val_size = len(val_labels)
    # 保存fasttext信息
    fasttext["train_size"] = train_size
    fasttext["test_size"] = test_size
    fasttext["val_size"] = val_size
    fasttext["input_num"] = len(train_datas[0])
    fasttext["dims_num"] = embeddings["id"]

    with open(vec_dir, "wb") as f:
        pickle.dump(fasttext, f)
    print("Saved fasttext to:", vec_dir)
    print("Write train datas to:", train)
    #print(train_datas)
    with open(train, mode = "w",errors='ignore',encoding='utf-8') as f:
        for i in range(train_size):
            data_line = str(train_datas[i]) + "这是一个分隔符号" + str(train_labels[i]) + "\n"
            f.write(data_line)
    print("Write test datas to:", test)
    with open(test, mode = "w",errors='ignore',encoding='utf-8') as f:
        for i in range(test_size):
            data_line = str(test_datas[i]) + "这是一个分隔符号" + str(test_labels[i]) + "\n"
            f.write(data_line)
    print("Write test datas to:", val)
    with open(val, mode = "w",errors='ignore',encoding='utf-8') as f:
        for i in range(val_size):
            data_line = str(val_datas[i]) + "这是一个分隔符号" + str(val_labels[i]) + "\n"
            f.write(data_line)
    print("Write datas over!")

def data_generator(file_path):
    def parse_line(line):
        # 分割数据和标签部分
        line = line.strip()  # 去除前后空白
        data_str, label_str = line.split('这是一个分隔符号')
        data = np.array(ast.literal_eval(data_str))
        label = np.array([int(label_str)])
        #print(label)
        return data, label
    def generator():
        with open(file_path, mode = 'r',errors='ignore',encoding='utf-8') as f:
            for line in f:
                yield parse_line(line)
    return generator()

def batch_generator(datas_dir, datas_size, batch_size, embeddings, reverse_dictionary, train=True, repeat=1):
    generator = data_generator(datas_dir)
    n = 0
    while True:  # 无限循环以确保持续提供数据
        batch_data = []
        batch_label = []
       # print("来了")
        for _ in range(repeat):
            try:
                for i in range(batch_size):
                    data, label = next(generator)
                    #print(data,label)
                    data_embed = []
                    for d in data:
                        data_embed.append(embeddings[d])
                    batch_data.append(data_embed)
                    batch_label.append(label)
                    n += 1
                    # 对于训练数据条件
                    #print(batch_data,batch_label)
                    if train and n >= datas_size:
                        n = 0  # 重置计数器      
                        generator = data_generator(datas_dir)
                        break
                    if not train and n >= datas_size:
                        yield (np.array(batch_data), np.array(batch_label))
                        return
                yield (np.array(batch_data), np.array(batch_label))
            except StopIteration:
                generator = data_generator(datas_dir)

def build_dataset(batch_size):
    with open(vec_dir, "rb") as f:
        fasttext = pickle.load(f)
    embeddings = fasttext["embeddings"]
    reverse_dictionary = fasttext["reverse_dictionary"]
    train_size = fasttext["train_size"]
    test_size = fasttext["test_size"]
    val_size = fasttext["val_size"]
    dims_num = fasttext["dims_num"]
    input_num = fasttext["input_num"]
    train_generator = batch_generator(train, train_size, batch_size, embeddings, reverse_dictionary)
    test_generator = batch_generator(test, test_size, batch_size, embeddings, reverse_dictionary, train=False)
    val_generator = batch_generator(val, val_size, batch_size, embeddings, reverse_dictionary)
    return train_generator, test_generator,val_generator,train_size, test_size, val_size,input_num, dims_num
if __name__=="__main__":
    pre_process()