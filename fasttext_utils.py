import base64
import nltk
import re
from urllib.parse import unquote,unquote_plus
import pandas as pd
import tensorflow as tf
from urllib.parse import urlparse
import html
# Oracle, MySQL, SQL Server, PostgreSQL, OceanBase, TIDB, MongoDB, GaussDB, GBase
def is_base64_encoded(s):
    """判断一个字符串是否是有效的Base64编码"""
    if isinstance(s, str):
        # Base64编码后的字符串长度必须是4的倍数
        if len(s) % 4 == 0:
            try:
                # 尝试解码并验证
                base64.b64decode(s, validate=True)
                return True
            except (base64.binascii.Error, ValueError):
                return False
    return False

def decode_base64(encoded_str):
    """解码Base64编码字符串"""
    if is_base64_encoded(encoded_str):
        decoded_bytes = base64.b64decode(encoded_str)
        return decoded_bytes.decode('utf-8', errors='replace')
    else:
        return encoded_str
def segment(payload):
    """
    收集html语言，js语言，sql语言的关键字
    同样可以收集其他敏感字符比如admin等（未做）
    对输入文本进行分词处理，包括：
    1.小写化
    2.URL解码和html解码
    3.去掉协议和域名
    4.在特殊符号前后加空格
    5.根据特殊符号进行分词
    6.对每一个分词做词转换（比如数字转换成Numbers,十六进制数转换成HexString，涉及以上三种语言的关键字则不做处理）
    """
    payload = unquote(payload)
    if is_base64_encoded(payload):
        payload = decode_base64(payload)
    # 将文本转为小写
    payload = payload.lower()
    # 解码 URL 编码
    payload = unquote_plus(unquote(unquote(payload)))
    payload = html.unescape(payload) 
    # 去掉协议和域名部分
    payload = re.sub('^https?://[^/]+','',payload)
    payload = payload.replace("\x00","")
    #print(payload)
    # 特殊符号前后加空格
    symbols = list(r'|&!-@#$%^*()\[\]{};,:\'".<>?/\\+=')
    for symbol in symbols:
        payload = payload.replace(symbol, f' {symbol} ')
    #print(payload)
    # 将多个连续空格合并为一个
    payload = re.sub(r'\s+', ' ', payload).strip()
    # 分词处理
    payload = payload.split()
    #print(payload)
    size = len(payload)
    result = []
    # 词转换
    for i in range(size):
        payload[i] = payload[i].strip() # 去除首尾空格
        if payload[i] != ' ' and payload[i] != '': # 如果不是空或者空格就继续
            if payload[i].isnumeric(): # 数字
                result.append('Numbers')
            else:
                result.append(payload[i])
    return result
    
def init_session():
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        try:
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
        except RuntimeError as e:
            print(f"RuntimeError: {e}")
# 调用 init_session 来初始化 TensorFlow 会话并配置 GPU
init_session()

