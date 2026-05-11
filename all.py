from keras.api.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Embedding, InputLayer, Reshape
import gc
import pickle
import random
import sys
from gensim.models import FastText
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.manifold import TSNE
import tensorflow as tf
from fasttext_utils import segment
from fasttext_utils import init_session
from fasttext import process_words
from sklearn.model_selection import train_test_split
import ast

from keras.api.models import Sequential
from keras.api.layers import Dense,InputLayer,Dropout,LSTM,Bidirectional
from keras.api.callbacks import TensorBoard
from keras.api.models import Sequential
import numpy as np
from keras.api.optimizers import Adam
from keras.api.models import load_model
from sklearn.metrics import precision_score,recall_score,accuracy_score,confusion_matrix
from keras.api.callbacks import EarlyStopping
from keras.api.callbacks import ReduceLROnPlateau, EarlyStopping, ModelCheckpoint
def data_generator(file_path):
    def parse_line(line):
        # 分割数据和标签部分
        line = line.strip()  # 去除前后空白
        data_str, label_str = line.split('这是一个分隔符号')
        data = np.array(ast.literal_eval(data_str))
        label = np.array([int(label_str)])
        # print(data)
        # print(label)
        return data, label
    def generator():
        with open(file_path, mode = 'r',errors='ignore',encoding='utf-8') as f:
            for line in f:
                yield parse_line(line)
    return generator()
def batch_generator(datas_dir, datas_size, batch_size, embeddings, train=True, repeat=1):
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
                #print(np.array(batch_data), np.array(batch_label))
                yield (np.array(batch_data), np.array(batch_label))
            except StopIteration:
                generator = data_generator(datas_dir)
def build_dataset(batch_size,fasttext,train,test,val):
    embeddings = fasttext["embeddings"]
    train_size = fasttext["train_size"]
    test_size = fasttext["test_size"]
    val_size = fasttext["val_size"]
    dims_num = fasttext["dims_num"]
    input_num = fasttext["input_num"]
    train_generator = batch_generator(train, train_size, batch_size, embeddings)
    test_generator = batch_generator(test, test_size, batch_size, embeddings, train=False)
    val_generator = batch_generator(val, val_size, batch_size, embeddings)
    return train_generator, test_generator,val_generator,train_size, test_size, val_size,input_num, dims_num
def train_function_cnn(train_generator,train_size, input_num, dims_num,val_generator,val_size,model_dir,layers,output,batch_size,epoch_nums,learning):
    tf.keras.backend.clear_session()
    
    model = Sequential()
    model.add(InputLayer(input_shape=(input_num, dims_num.shape[0])))  # 输入形状直接用词向量维度

    model.add(Reshape((input_num, dims_num.shape[0], 1)))  

    
    # 添加卷积层
    model.add(Conv2D(128, kernel_size=(3, dims_num.shape[0]), activation='relu'))  # 使用卷积核
    model.add(MaxPooling2D(pool_size=(input_num - 2, 1)))  # 最大池化
    model.add(Flatten())  # 展平

    # 全连接层
    model.add(Dense(128, activation='relu'))  # 隐藏层
    model.add(Dropout(output))  # Dropout
    model.add(Dense(1, activation="sigmoid", name="Output"))
    model.summary()
    optimizer = Adam(learning_rate=learning)

    model.compile(optimizer=optimizer, loss="binary_crossentropy", metrics=["accuracy", "precision", "recall"])
        # Early stopping to prevent overfitting
    early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

    # Model checkpoint to save the best model based on validation loss
    model_checkpoint = ModelCheckpoint(filepath=model_dir, monitor='val_loss', save_best_only=True)

    reduce_lr = ReduceLROnPlateau(
    monitor='val_loss',         # 监控验证损失
    factor=0.1,                 # 学习率缩减因子
    patience=5,                 # 在此时间内持续不可改善的指标
    verbose=1,                  # 打印学习率变化信息
    min_lr=1e-6                 # 学习率下限
    )
    # 开始训练，加入回调函数
    model.fit(train_generator,
            steps_per_epoch=train_size // batch_size,
            epochs=epoch_nums,
            validation_data=val_generator,
            validation_steps=val_size // batch_size,
            callbacks=[early_stopping, model_checkpoint,reduce_lr]
            )
    gc.collect()
    del model
def train_function_bilstm(train_generator,train_size, input_num, dims_num,val_generator,val_size,model_dir,layers,output,batch_size,epoch_nums,learning):
    tf.keras.backend.clear_session()
    
    model = Sequential()
    model.add(InputLayer(input_shape=(input_num, dims_num.shape[0]), batch_size=batch_size))
    model.add(Bidirectional(LSTM(layers, return_sequences=False)))
    model.add(Dropout(output))
    # model.add(LSTM(64))
    # model.add(Dropout(0.5))
    model.add(Dense(1, activation="sigmoid", name="Output"))
    model.summary()
    optimizer = Adam(learning_rate=learning)#0.001

    model.compile(optimizer=optimizer, loss="binary_crossentropy", metrics=["accuracy", "precision", "recall"])
        # Early stopping to prevent overfitting
    early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

    # Model checkpoint to save the best model based on validation loss
    model_checkpoint = ModelCheckpoint(filepath=model_dir, monitor='val_loss', save_best_only=True)

    reduce_lr = ReduceLROnPlateau(
    monitor='val_loss',         # 监控验证损失
    factor=0.1,                 # 学习率缩减因子
    patience=5,                 # 在此时间内持续不可改善的指标
    verbose=1,                  # 打印学习率变化信息
    min_lr=1e-6                 # 学习率下限
    )
    # 开始训练，加入回调函数
    model.fit(train_generator,
            steps_per_epoch=train_size // batch_size,
            epochs=epoch_nums,
            validation_data=val_generator,
            validation_steps=val_size // batch_size,
            callbacks=[early_stopping, model_checkpoint,reduce_lr]
            )
    gc.collect()
    del model
def test_function(model_dir, test_generator, test_size, input_num, dims_num, batch_size):
    model = load_model(model_dir)
    labels_pre = []
    labels_true = []
    batch_num = test_size // batch_size + 1
    steps = 0
    for batch, labels in test_generator:
        #print(len(labels))
        # 在模型中处理预测，确保每个批次都有固定的大小
        if len(labels) < batch_size:
            # 填充至 batch_size
            padding_size = batch_size - len(labels)
            padding_array = np.zeros((padding_size, input_num, dims_num.shape[0]))
            batch = np.concatenate((batch, padding_array))

        # 进行预测
        predictions = model.predict_on_batch(batch)
        #print("Predictions:", predictions[:len(labels)])
        threshold = 0.5
        predicted_labels = (predictions[:len(labels)] > threshold).astype(int).flatten()
        labels_true.extend(labels)
        labels_pre.extend(predicted_labels)
        steps += 1
        #print(f"{steps}/{batch_num} batch")
        
        if steps >= batch_num:
            break
    y_true = labels_true
    y_true = [int(label) for arr in y_true for label in arr]
    y_pre = labels_pre
    # print(y_true)
    # print(y_pre)
    # print(len(y_true))
    # print(len(y_pre))
    accuracy = accuracy_score(y_true, y_pre)
    precision = precision_score(y_true, y_pre)
    recall = recall_score(y_true, y_pre)
    tn, fp, fn, tp = confusion_matrix(y_true, y_pre).ravel()
    # 计算误报率
    fpr = fp / (fp + tn)
    print("Accuracy score is :", accuracy)
    print("Precision score is :", precision)
    print("Recall score is :", recall)
    print("fpr score is :", fpr)
    gc.collect() 
    del model
    return [accuracy,precision,recall,fpr]
def predi(model_dir, test_generator, test_size, input_num, dims_num, batch_size):
    model = load_model(model_dir,safe_mode=False)
    labels_pre = []
    labels_true = []
    batch_num = test_size // batch_size + 1
    steps = 0
    for batch, labels in test_generator:
        # print(len(labels))
        # 在模型中处理预测，确保每个批次都有固定的大小
        if len(labels) < batch_size:
            # 填充至 batch_size
            padding_size = batch_size - len(labels)
            padding_array = np.zeros((padding_size, input_num, dims_num.shape[0]))
            batch = np.concatenate((batch, padding_array))

        # 进行预测
        predictions = model.predict_on_batch(batch)
        #print("Predictions:", predictions[:len(labels)])
        threshold = 0.5
        predicted_labels = (predictions[:len(labels)] > threshold).astype(int).flatten()
        labels_true.extend(labels)
        labels_pre.extend(predicted_labels)
        steps += 1
        #print(f"{steps}/{batch_num} batch")
        
        if steps >= batch_num:
            break
    y_true = labels_true
    y_true = [int(label) for arr in y_true for label in arr]
    y_pre = labels_pre
    # print(y_true)
    # print(y_pre)
    # print(len(y_true))
    # print(len(y_pre))
    result = []
    for i in range(len(y_true)):
        if y_true[i]!=y_pre[i]:
            result.append(i+1)
            print(f'{i+1},',end='')
    print("")
    accuracy = accuracy_score(y_true, y_pre)
    precision = precision_score(y_true, y_pre)
    recall = recall_score(y_true, y_pre)
    print("Accuracy score is :", accuracy)
    print("Precision score is :", precision)
    print("Recall score is :", recall)
    gc.collect() 
    del model
    return result,accuracy

vec_dir = 'file//fasttext.pkl'
def run():
    init_session()
    # dual_output = DualOutput('file//output.txt')
    # sys.stdout = dual_output
    finish = {'rule':[],'accuracy':[],'precision':[],'recall':[],'fpr':[],'predict':[],'result':[]}
    with open(vec_dir, "rb") as f:
        fasttext = pickle.load(f)
    train= "file\\pre_datas_train.csv"
    test="file\\pre_datas_test.csv" 
    val="file\\pre_datas_val.csv" 
    leanrning_=[0.1,0.01,0.001,0.0001]
    #model = "bilstm"
    model = "cnn"
    for i in leanrning_:
        for h_ in range(3):
            batch_size=64
            epoch_nums=6
            model_dir = f"file//fasttext_{model}__第{h_}次_{i}.keras"
            train_generator, test_generator, val_generator,train_size, test_size, val_size,input_num, dims_num = build_dataset(batch_size,fasttext,train,test,val)
            if model == "bilstm":
                train_function_bilstm(train_generator, train_size, input_num, dims_num,val_generator,val_size,model_dir,128,0.5,batch_size,epoch_nums,i)
            else:
                train_function_cnn(train_generator, train_size, input_num, dims_num,val_generator,val_size,model_dir,128,0.5,batch_size,epoch_nums,i)
            fs = test_function(model_dir, test_generator, test_size, input_num, dims_num, batch_size)

            pre_datas_test="file//textpre.csv"
            pre_generator = batch_generator(pre_datas_test,133,batch_size,fasttext['embeddings'],train=False)

            fp1,fp2 = predi(model_dir,pre_generator, 133, input_num, dims_num, batch_size)
            print(f'{model}_第{h_}次')
            finish['rule'].append(f'{model}__第{h_}次')
            finish['accuracy'].append(fs[0])
            finish['precision'].append(fs[1])
            finish['recall'].append(fs[2])
            finish['fpr'].append(fs[3])
            finish['result'].append(','.join(map(str, fp1)))
            finish['predict'].append(fp2)
            gc.collect
    for i in range(len(finish['rule'])):
        print(f"{finish['rule'][i]}->{finish['accuracy'][i]}->{finish['precision'][i]}->{finish['recall'][i]}->{finish['fpr'][i]}->{finish['predict'][i]}->{finish['result'][i]}")
    df = pd.DataFrame(finish)
    df.to_excel(f'file//{model}_result.xlsx',index=False)
    print('成功写入')
    # sys.stdout = sys.__stdout__
    # dual_output.file.close()    
if __name__=="__main__":
    run()