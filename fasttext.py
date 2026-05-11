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
plt_dir = "file//fasttext_plot.png" # 保存图像的路径
vec_dir = "file//fasttext.pkl"     # 保存词向量的路径
def process_words(words):
    if len(words) < 100:
        # 如果元素不足 100，填充到 100 个字符
        return words + ['<pad>'] * (100 - len(words))  # 直接用  填充到列表长度达到 100
    else:
        # 如果元素超过 100，截断到 100 个元素
        return words[:100]
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
    # # 设置标签
    # sql_data['label'] = 1  # 假设 SQL 注入为 1
    # xss_data['label'] = 1  # 假设 XSS 为 1
    data = pd.concat([normal_data,sql_data, xss_data])  # 合并数据集
    print(data['payload'])
    data['words'] = data['payload'].map(segment)
    print(data['words'])
    # 创建 FastText 模型
    # 将 text 直接传递给 FastText
    model = FastText(sentences=data['words'].tolist(),vector_size=embedding_size, window=skip_window, negative=num_sampled,min_count=1, workers=4, epochs=num_iter,seed=1)

    embeddings = model.wv

    # 绘图函数
    def plot_with_labels(low_dim_embs, labels, filename=plt_dir):
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
    tsne = TSNE(perplexity=30, n_components=2, init="pca", n_iter=5000, random_state=0)
    plot_words = embeddings.index_to_key[:plot_only]  # 只绘制前200个单词
    plot_embeddings = np.array([embeddings[word] for word in plot_words])
    low_dim_embs = tsne.fit_transform(plot_embeddings)
    plot_with_labels(low_dim_embs, plot_words)

    # 保存模型
    def save(embeddings):
        dictionary = {word: i for i, word in enumerate(embeddings.index_to_key)}
        reverse_dictionary = {i: word for word, i in dictionary.items()}
        fasttext_model = {"dictionary": dictionary, "embeddings": embeddings, "reverse_dictionary": reverse_dictionary}
        with open(vec_dir, "wb") as f:
            pickle.dump(fasttext_model, f)

    save(embeddings)

    end = time.time()
    print("Over FastText job in ", end - start)
    print("Saved words vec to", vec_dir)


if __name__ == '__main__':
    run()