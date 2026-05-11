import ast
import pickle
import numpy as np
import json
import csv
from fasttext_utils import segment
from fasttext_data import build_dataset
from fasttext_utils import init_session
import pandas as pd
from keras.api.models import load_model
import re
from sklearn.metrics import precision_score,recall_score,accuracy_score,confusion_matrix
from fasttext import process_words
pre_datas_test="file\\textpre.csv"
output="file\\out.csv"
init_session()
vec_dir = "file\\fasttext.pkl"
model_dir = "file\\fasttext_bilstm.keras"
#model_dir = "file\\fasttext_bilstm__第14次.keras"
batch_size = 64
epochs_num = 1

def pre_process_unlabeled(input_num):
    with open(vec_dir, "rb") as f:
        fasttext = pickle.load(f)
        dictionary = fasttext["dictionary"]
    unlabeled_data = pd.read_csv("data/test.csv", encoding='utf-8',names=['payload'])
    unlabeled_data['label'] = 1
    pre_size = len(unlabeled_data['label'])
    unlabeled_data['words'] = unlabeled_data['payload'].map(segment)
    unlabeled_data['processed_words'] = unlabeled_data['words'].apply(process_words)
    test_datas = unlabeled_data['processed_words'].tolist()
    # 保存处理后的数据为 CSV 文件
    with open(pre_datas_test, "w",errors='ignore',encoding='utf-8') as f:
        for i in range(pre_size):
            data_line = str(test_datas[i]) + "这是一个分隔符号1\n"
            f.write(data_line)
    print("Processed unlabeled data saved to:", pre_datas_test)
    return pre_datas_test, pre_size  # 返回处理后的数据路径

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
        with open(file_path, 'r',encoding='utf-8') as f:
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
def build(batch_size,test_size):
    with open(vec_dir, "rb") as f:
        fasttext = pickle.load(f)
    embeddings = fasttext["embeddings"]
    reverse_dictionary = fasttext["reverse_dictionary"]
    dims_num = fasttext["dims_num"]
    input_num = fasttext["input_num"]
    pre_generator = batch_generator(pre_datas_test,test_size,batch_size,embeddings,reverse_dictionary,train=False)
    return pre_generator,test_size,input_num,dims_num

def test(model_dir, input_file, test_generator, test_size, input_num, dims_num, batch_size):
    model = load_model(model_dir,safe_mode=False)
    labels_pre = []
    labels_true = []
    batch_num = test_size // batch_size + 1
    steps = 0
    for batch, labels in test_generator:
        print(len(labels))
        # 在模型中处理预测，确保每个批次都有固定的大小
        if len(labels) < batch_size:
            # 填充至 batch_size
            padding_size = batch_size - len(labels)
            padding_array = np.zeros((padding_size, input_num, dims_num.shape[0]))
            batch = np.concatenate((batch, padding_array))

        # 进行预测
        predictions = model.predict_on_batch(batch)
        print("Predictions:", predictions[:len(labels)])
        threshold = 0.55
        predicted_labels = (predictions[:len(labels)] > threshold).astype(int).flatten()
        labels_true.extend(labels)
        labels_pre.extend(predicted_labels)
        steps += 1
        print(f"{steps}/{batch_num} batch")
        
        if steps >= batch_num:
            break
    y_true = labels_true
    y_true = [int(label) for arr in y_true for label in arr]
    y_pre = labels_pre
    print(y_true)
    print(y_pre)
    print(len(y_true))
    print(len(y_pre))
    for i in range(len(y_true)):
        if y_true[i]!=y_pre[i]:
            print(f'{i+1},',end='')
    print("")
    accuracy = accuracy_score(y_true, y_pre)
    precision = precision_score(y_true, y_pre)
    recall = recall_score(y_true, y_pre)
    print("Accuracy score is :", accuracy)
    print("Precision score is :", precision)
    print("Recall score is :", recall)

if __name__ == "__main__":
    _, _, _, _,_,_,input_num, dims_num = build_dataset(batch_size)
    _, pre_size=pre_process_unlabeled(input_num)
    pre_generator,_,_,_=build(batch_size,pre_size)
    labels = test(model_dir, output,pre_generator, pre_size, input_num, dims_num, batch_size)
'''
import pickle  # 导入pickle模块，用于序列化和反序列化对象
import numpy as np  # 导入NumPy库，用于处理数组和矩阵
import json  # 导入json模块，用于处理JSON格式数据
import csv  # 导入csv模块，用于读取和写入CSV文件
from keras.models import load_model  # 从Keras库中导入load_model函数，用于加载模型
from keras.preprocessing.sequence import pad_sequences  # 导入pad_sequences函数，用于对序列进行填充
from utils import segment  # 从utils模块导入segment函数，用于文本分词
from process_ import build_dataset  # 从process_模块导入build_dataset函数，用于构建数据集
from utils import init_session  # 从utils模块导入init_session函数，用于初始化会话
import pandas as pd  # 导入Pandas库，用于数据处理
import urllib.parse  # 导入urllib.parse模块，用于处理URL编码和解码
import re  # 导入re模块，用于处理正则表达式

# 定义一些路径和参数
pre_datas_test = "file\\textpre.csv"  # 预处理后的数据文件路径
output = "file\\out.csv"  # 输出预测结果的文件路径
init_session()  # 初始化会话
vec_dir = "file\\fasttext.pickle"  # 词向量模型文件路径
model_dir = "file\\model.keras"  # 已训练模型文件路径
batch_size = 64  # 定义批量大小
epochs_num = 1  # 定义训练轮数

# 预处理未标注数据的函数
def pre_process_unlabeled(input_num):
    # 加载词向量模型
    with open(vec_dir, "rb") as f:
        fasttext = pickle.load(f)  # 反序列化词向量模型
        dictionary = fasttext["dictionary"]  # 获取词典

    unlabeled_data = []  # 用于存储未标注的文本数据
    # 打开未标注数据文件并进行读取
    with open("data\\text.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, fieldnames=["payload"])  # 创建CSV文件阅读器，指定列名为“payload”
        for row in reader:
            payload = row["payload"]  # 获取payload列中的数据
            word = segment(payload)  # 对payload进行分词
            unlabeled_data.append(word)  # 将分词后的结果添加到unlabeled_data列表中

    unlabeled_num = len(unlabeled_data)  # 获取未标注数据的数量
    unlabeled_label = [-1] * unlabeled_num  # 初始化未标注数据的标签为-1
    pre_size = len(unlabeled_label)  # 记录未标注数据的数量

    # 将文本转换为对应的索引序列
    def to_index(data):
        d_index = []
        for word in data:
            if word in dictionary.keys():  # 如果单词存在于词典中
                d_index.append(dictionary[word])  # 将单词转换为词典中的索引
            else:
                d_index.append(dictionary["UNK"])  # 对于未知单词，使用“UNK”表示
        return d_index

    datas_index = [to_index(data) for data in unlabeled_data]  # 将所有未标注数据转换为索引序列
    # 输出长度超过100的索引序列
    for i in datas_index:
        if len(i) > 100:  # 如果索引序列长度大于100
            print(1, len(i))  # 输出长度信息

    # 对索引序列进行填充，使其长度固定为input_num
    datas_index = pad_sequences(datas_index, maxlen=input_num, value=-1)

    # 将处理后的数据保存为CSV文件
    with open(pre_datas_test, "w", newline='', encoding="utf-8") as f:
        for row in datas_index:
            data_line = str(row.tolist()) + "|[-1]\n"  # 组合数据和标签
            f.write(data_line)  # 将组合后的数据写入文件

    print("Processed unlabeled data saved to:", pre_datas_test)  # 输出保存文件路径
    return pre_datas_test, pre_size  # 返回处理后的数据文件路径和数据数量

# 定义一个数据生成器，用于从CSV文件中读取数据
def data_generator(file_path):
    # 解析CSV文件中的每一行数据
    def parse_line(line):
        line = line.strip()  # 去除行的前后空白字符
        data_str, label_str = line.split('|')  # 将数据和标签部分分开
        data = np.array(json.loads(data_str))  # 将数据部分转换为数组
        label = np.array(json.loads(label_str))  # 将标签部分转换为数组
        return data, label  # 返回数据和标签

    # 定义生成器函数，逐行读取文件
    def generator():
        with open(file_path, 'r') as f:
            for line in f:
                yield parse_line(line)  # 返回解析后的数据和标签
    return generator()  # 返回生成器对象

# 批量生成数据的生成器函数
def batch_generator(datas_dir, datas_size, batch_size, embeddings, reverse_dictionary, train=True, repeat=1):
    batch_data = []  # 存储当前批次的数据
    batch_label = []  # 存储当前批次的标签
    generator = data_generator(datas_dir)  # 获取数据生成器
    n = 0  # 计数器，用于记录当前生成的数据量

    # 无限循环生成数据
    while True:
        for _ in range(repeat):
            try:
                for i in range(batch_size):
                    data, label = next(generator)  # 获取一条数据
                    data_embed = []  # 用于存储嵌入后的数据
                    for d in data:
                        if d != -1:  # 如果数据有效
                            data_embed.append(embeddings[reverse_dictionary[d]])  # 将索引转换为词嵌入
                        else:
                            data_embed.append([0.0] * len(embeddings["UNK"]))  # 对于无效数据，使用零向量填充
                    batch_data.append(data_embed)  # 将嵌入后的数据添加到当前批次中
                    batch_label.append(label)  # 将标签添加到当前批次中
                    n += 1  # 更新计数器
                    # 如果是测试模式且生成的数据数量超过了数据集大小
                    if not train and n >= datas_size:
                        yield (np.array(batch_data), np.array(batch_label))  # 返回当前批次数据
                        return  # 结束生成器
                yield (np.array(batch_data), np.array(batch_label))  # 返回当前批次数据
                batch_data = []  # 清空批次数据
                batch_label = []  # 清空批次标签
            except StopIteration:  # 如果生成器结束
                if batch_data:  # 如果还有剩余的数据
                    yield (np.array(batch_data), np.array(batch_label))  # 返回剩余的数据
                return  # 结束生成器

# 构建数据生成器和相关参数的函数
def build(batch_size, test_size):
    # 加载词向量模型
    with open(vec_dir, "rb") as f:
        fasttext = pickle.load(f)  # 加载词向量模型
    embeddings = fasttext["embeddings"]  # 提取词向量
    reverse_dictionary = fasttext["reverse_dictionary"]  # 提取反向词典
    dims_num = fasttext["dims_num"]  # 获取词向量的维度
    input_num = fasttext["input_num"]  # 获取输入数据的长度

    # 创建批量数据生成器，用于生成测试数据
    pre_generator = batch_generator(pre_datas_test, test_size, batch_size, embeddings, reverse_dictionary, train=False)
    return pre_generator, test_size, input_num, dims_num  # 返回生成器和相关参数

# 模型测试函数，进行预测并保存结果
def test(model_dir, input_file, test_generator, test_size, input_num, dims_num, batch_size):
    model = load_model(model_dir)  # 加载已训练好的模型
    labels_pre = []  # 用于存储预测结果
    batch_num = test_size // batch_size + 1  # 计算批次数量
    steps = 0  # 步数计数器

    # 逐批次进行预测
    for batch, labels in test_generator:
        if len(labels) == batch_size:  # 如果批次大小与设定的batch_size相等
            predictions = model.predict_on_batch(batch)  # 进行预测
        else:  # 如果批次大小小于batch_size，则需要对数据进行填充
            batch = np.concatenate(
                (batch, np.zeros((batch_size - len(labels), input_num, dims_num.shape[0]))))  # 填充
            predictions = model.predict_on_batch(batch)[0:len(labels)]  # 进行预测
'''