import pickle
import re
from urllib.parse import unquote,unquote_plus
import numpy as np
import pandas as pd
from keras.api.models import load_model
import html
import tensorflow as tf
from keras.api.saving import register_keras_serializable
from keras.api.layers import Layer
vec_dir = 'fasttext/file/fasttext.pkl'
model_dir = 'fasttext/file/fasttext_bilstm.keras'
def process_words(words):
    if len(words) < 100:
        # 如果元素不足 100，填充到 100 个字符
        return words + ['<pad>'] * (100 - len(words))  # 直接用 $ 填充到列表长度达到 100
    else:
        # 如果元素超过 100，截断到 100 个元素
        return words[:100]

def segment(payload):
    # 将文本转为小写
    payload = payload.lower()
    # 解码 URL 编码
    payload = unquote_plus(unquote(unquote(payload)))
    payload = html.unescape(payload) 
    # 去掉协议和域名部分
    payload = re.sub('^https?://[^/]+','',payload)
    # 特殊符号前后加空格
    symbols = list(r'|&!-@#$%^*()\[\]{};,:\'".<>?/\\+=')
    for symbol in symbols:
        payload = payload.replace(symbol, f' {symbol} ')
    # 将多个连续空格合并为一个
    payload = re.sub(r'\s+', ' ', payload).strip()
    payload = payload.split()
    fuhao = r'|&!-@#$%^*()\[\]{};,:\'".<>?/\\+='
    size = len(payload)
    result = []
    # 词转换
    for i in range(size):
        payload[i] = payload[i].strip() # 去除首尾空格
        if payload[i] != ' ' and payload[i] != '': # 如果不是空或者空格就继
            if payload[i].isnumeric(): # 数字
                result.append('Numbers')
            else:
                result.append(payload[i])
    return process_words(result)
def tonumpy(data,embeddings):
    data = np.array(data)
    data_embed = []
    for d in data:
        if d not in embeddings:
            data_embed.append(embeddings['Unknown'])
        else:
            data_embed.append(embeddings[d])
    return data_embed
def predecit(data):
    data = np.array(data)
    data = np.expand_dims(data, axis=0)
    print(data.shape)
    prediction = model.predict(data)[0][0]  # 预测单个样本
    print("Prediction:", prediction)  # 打印预测结果
    threshold = 0.5
    predict_label = 1 if prediction > threshold else 0
    return str(prediction),predict_label
def process_url(url):
    question_mark_index = url.find('?')
    
    # 如果找到?，返回其后面的部分；否则返回空字符串
    if question_mark_index != -1:
        url =url[question_mark_index + 1:]
    else:
        url = ""
    # 处理URL（例如，发送请求并获取响应）
    payload = segment(url)
    print(payload)
    payload = tonumpy(payload,word2vec["embeddings"])
    prediction,prediction_label = predecit(payload)
    print(url,'-->',prediction,":",prediction_label)
with open(vec_dir, "rb") as f:
    word2vec = pickle.load(f)
model = load_model(model_dir,safe_mode=False)
lines = []
# 使用'with'语句安全地打开文件
with open('fasttext/main/1.txt', 'r', encoding='utf-8') as file:
    # 逐行读取文件并添加到列表中
    for line in file:
        lines.append(line.strip())
for i in range(len(lines)):
    process_url(lines[i])
    
