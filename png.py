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
plot_only = 200

def run():
    start = time.time()

    normal_data = []
    with open("data/dmzo_normal.csv", mode='r', errors='ignore', encoding='utf-8') as f:
        for line in f:
            normal_data.append(line.strip())
    normal_data = pd.DataFrame(normal_data, columns=['payload'])
    normal_data.dropna(inplace=True)
    
    # 加载 SQL 数据
    sql_data = []
    with open("data/sql.csv", mode='r', errors='ignore', encoding='utf-8') as f:
        for line in f:
            sql_data.append(line.strip())
    sql_data = pd.DataFrame(sql_data, columns=['payload'])
    sql_data.dropna(inplace=True)

    # 加载 XSS 数据
    xss_data = []
    with open("data/xss.csv", mode='r', errors='ignore', encoding='utf-8') as f:
        for line in f:
            xss_data.append(line.strip())
    xss_data = pd.DataFrame(xss_data, columns=['payload'])
    xss_data.dropna(inplace=True)

    Abnormal_data = pd.concat([sql_data, xss_data])  # 合并数据集
    Abnormal_data['words'] = Abnormal_data['payload'].map(segment)
    normal_data['words'] = normal_data['payload'].map(segment)

    # 加载预训练的 FastText 模型
    model_path = "file//fasttext.pkl"  # 替换为你的模型路径
    with open(model_path, "rb") as f:
        fasttext = pickle.load(f)
        embeddings = fasttext["embeddings"]
    
    embeddings_normal = embeddings["embeddings"]

    # 准备特征矩阵

# 在 get_feature_matrix 函数中，添加检查以处理 NaN 或无效值：

    def get_feature_matrix(data):
        feature_matrix = []
        for words in data['words']:
            word_vectors = [embeddings_normal[word] for word in words if word in embeddings_normal]
            if word_vectors:
                feature_matrix.append(np.mean(word_vectors, axis=0))  # 对每条数据取均值
            else:
                feature_matrix.append(np.zeros(embedding_size))  # 如果没有词向量，返回零向量
        feature_matrix = np.array(feature_matrix)
        
        # 检查并替换 NaN 值
        feature_matrix = np.nan_to_num(feature_matrix)  # 将 NaN 替换为 0
        return feature_matrix

    normal_features = get_feature_matrix(normal_data)
    abnormal_features = get_feature_matrix(Abnormal_data)

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
        plt.title("t-SNE visualization of FastText embeddings")
        plt.savefig(filename)
        plt.show()

    # t-SNE 可视化
    tsne = TSNE(perplexity=30, n_components=2, init="pca", max_iter=5000, random_state=0)
    
    # 可视化正常 URL
    low_dim_embs_normal = tsne.fit_transform(normal_features[:plot_only])
    plot_with_labels(low_dim_embs_normal, normal_data['payload'][:plot_only], 'file//normal1_plot.png')
    
    # 可视化异常 URL
    low_dim_embs_abnormal = tsne.fit_transform(abnormal_features[:plot_only])
    plot_with_labels(low_dim_embs_abnormal, Abnormal_data['payload'][:plot_only], 'file//abnormal1_plot.png')

    end = time.time()
    print("Over FastText job in ", end - start)

if __name__ == '__main__':
    run()