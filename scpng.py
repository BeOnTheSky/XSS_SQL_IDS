import time
import pandas as pd
import numpy as np
from gensim.models import FastText
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import pickle
from fasttext_utils import segment

# 参数配置
embedding_size = 200
skip_window = 6
num_sampled = 64
num_iter = 10
plot_only = 200

def run():
    start = time.time()

    normal_data = []
    with open("data/dmzo_normal.csv", mode = 'r',errors='ignore',encoding='utf-8') as f:
        for line in f:
            normal_data.append(line.strip())
    normal_data = pd.DataFrame(normal_data, columns=['payload'])
    normal_data.dropna(inplace=True)
    print(normal_data)

    # 加载 SQL 数据
    sql_data = []
    with open("data/sql.csv", mode='r', errors='ignore', encoding='utf-8') as f:
        for line in f:
            sql_data.append(line.strip())
    sql_data = pd.DataFrame(sql_data, columns=['payload'])
    sql_data.dropna(inplace=True)
    print(sql_data)
    # 加载 XSS 数据
    xss_data = []
    with open("data/xss.csv", mode='r', errors='ignore', encoding='utf-8') as f:
        for line in f:
            xss_data.append(line.strip())
    xss_data = pd.DataFrame(xss_data, columns=['payload'])
    xss_data.dropna(inplace=True)
    print(xss_data)

    Abnormal_data = pd.concat([sql_data, xss_data])  # 合并数据集
    Abnormal_data['words'] = Abnormal_data['payload'].map(segment)
    normal_data['words'] = normal_data['payload'].map(segment)
    print(Abnormal_data['words'])
    print(normal_data['words'])
    # 创建 FastText 模型
    # 将 text 直接传递给 FastText
    model_normal = FastText(sentences=normal_data['words'].tolist(),vector_size=embedding_size, window=skip_window, negative=num_sampled,min_count=1, workers=4, epochs=num_iter,seed=1)
    model_Abnormal = FastText(sentences=Abnormal_data['words'].tolist(),vector_size=embedding_size, window=skip_window, negative=num_sampled,min_count=1, workers=4, epochs=num_iter,seed=1)
    
    embeddings_normal = model_normal.wv
    embeddings_Abnormal = model_Abnormal.wv

    # 绘图函数
    def plot_with_labels(low_dim_embs, labels, filename):
        plt.figure(figsize=(10, 10))
        for i, label in enumerate(labels):
            x, y = low_dim_embs[i, :]
            plt.scatter(x, y, marker='o')
            plt.annotate(label, xy=(x, y), xytext=(5, 2),
                         textcoords="offset points",
                         ha="right",
                         va="bottom")
        plt.savefig(filename)
        plt.show()

    tsne = TSNE(perplexity=30, n_components=2, init="pca", n_iter=5000, random_state=0)
    plot_words = embeddings_normal.index_to_key[:plot_only]  # 只绘制前200个单词
    plot_embeddings = np.array([embeddings_normal[word] for word in plot_words])
    low_dim_embs = tsne.fit_transform(plot_embeddings)
    plot_with_labels(low_dim_embs, plot_words,'file//normal_plot.png')
    # t-SNE 可视化
    tsne = TSNE(perplexity=30, n_components=2, init="pca", n_iter=5000, random_state=0)
    plot_words = embeddings_Abnormal.index_to_key[:plot_only]  # 只绘制前200个单词
    plot_embeddings = np.array([embeddings_Abnormal[word] for word in plot_words])
    low_dim_embs = tsne.fit_transform(plot_embeddings)
    plot_with_labels(low_dim_embs, plot_words,'file//Abnormal_plot.png')

    end = time.time()
    print("Over FastText job in ", end - start)


if __name__ == '__main__':
    run()