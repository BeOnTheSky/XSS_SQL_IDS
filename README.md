# 基于语义的 Web 攻击检测

## 1. 项目简介

本项目面向 Web 请求中的 XSS 与 SQL 注入攻击检测任务，基于请求载荷（payload）的语义表示进行恶意流量识别。项目将原始 HTTP 日志、正常请求样本、XSS 攻击样本和 SQL 注入攻击样本整理为可训练的数据集，并通过 fastText 语义向量、LSTM、TextCNN 等文本分类模型学习请求参数、URL、payload 中的上下文语义特征，从而判断输入请求是否属于正常访问、XSS 攻击或 SQL 注入攻击。

项目适用于 Web 安全实验、入侵检测课程实验、攻击 payload 分类研究和语义化恶意请求检测原型验证。

## 2. 核心功能

- **HTTP 请求日志清洗**：从原始 HTTP 访问日志或 SQL 格式日志中提取请求内容，形成可训练的文本样本。
- **攻击样本构建**：支持正常请求、XSS 攻击请求、SQL 注入攻击请求等数据集组织。
- **语义特征建模**：利用 fastText 思路对 Web payload 进行词级/子词级语义表示，缓解传统关键词规则对变形攻击泛化不足的问题。
- **深度学习分类检测**：提供 fastText、LSTM、TextCNN 等检测模型，用于 Web 攻击二分类或多分类实验。
- **实验评估与可视化**：支持对训练过程、检测结果或统计信息进行分析和图形化展示。

## 3. 技术路线

```text
原始 HTTP 日志 / 攻击 payload 数据
        │
        ▼
数据清洗与样本整理
        │
        ▼
payload 分词 / token 化 / 序列化
        │
        ▼
语义向量表示：fastText / embedding
        │
        ▼
检测模型：fastText、LSTM、TextCNN
        │
        ▼
输出检测结果：正常 / XSS / SQL 注入
```

## 4. 项目目录结构

```text
.
├── all.py                         # 综合实验或统一运行入口
├── fasttext.py                    # fastText 相关模型实现或训练脚本
├── fasttext_data.py               # fastText 数据读取、样本构建、数据集处理
├── fasttext_LSTM.py               # 基于 fastText 表示与 LSTM 的检测模型
├── fasttext_text.py               # 基于 fastText/文本语义表示的检测实验脚本
├── fasttext_utils.py              # fastText 相关工具函数
├── textcnn.py                     # TextCNN 文本分类检测模型
├── png.py                         # 实验结果或统计图生成脚本
├── scpng.py                       # 图表生成/结果可视化脚本
├── data/
│   ├── payload_full.csv           # 综合 payload 数据集
│   ├── xss.csv                    # XSS 攻击样本数据
│   ├── sql.csv                    # SQL 注入攻击样本数据
│   ├── dmzo_normal.csv            # 正常请求样本数据
│   ├── test.csv                   # 测试集样本
│   ├── test2.csv                  # 测试集样本
│   └── 1.csv                      # 辅助样本/中间数据
├── log/
│   ├── http_data.txt              # HTTP 请求日志数据
│   ├── normal_data.txt            # 正常请求日志
│   ├── abnormal_data.txt          # 异常请求日志
│   ├── 正常http_data.sql          # 正常 HTTP 日志 SQL 数据
│   ├── 正常normal_data.sql        # 正常样本 SQL 数据
│   ├── xss攻击http_data.sql       # XSS 攻击 HTTP 日志 SQL 数据
│   ├── xss攻击normal_data.sql     # XSS 正常对照 SQL 数据
│   ├── xss攻击abnormal_data.sql   # XSS 异常样本 SQL 数据
│   ├── sql注入攻击http_data.sql   # SQL 注入 HTTP 日志 SQL 数据
│   ├── sql注入攻击normal_data.sql # SQL 注入正常对照 SQL 数据
│   └── sql注入攻击abnormal_data.sql # SQL 注入异常样本 SQL 数据
└── main/
    ├── main.py                    # 主流程入口或日志处理入口
    ├── rawData.py                 # 原始数据读取与解析
    ├── datacleaning.py            # 数据清洗脚本
    ├── computer1.py               # 统计/计算辅助脚本
    ├── computer2.py               # 统计/计算辅助脚本
    ├── computer3.py               # 统计/计算辅助脚本
    ├── test1.py                   # 测试脚本
    ├── test2.py                   # 测试脚本
    └── 1.txt                      # 辅助文本/中间结果
```


## 5. 环境要求

建议使用 Python 3.8 及以上版本。

```txt
numpy
pandas
scikit-learn
torch
matplotlib
tqdm
```


## 6. 数据准备

项目默认数据目录为 `data/`，日志目录为 `log/`。主要数据包括：

| 文件                      | 说明                      |
| ------------------------- | ------------------------- |
| `data/dmzo_normal.csv`    | 正常 Web 请求样本         |
| `data/xss.csv`            | XSS 攻击 payload 样本     |
| `data/sql.csv`            | SQL 注入攻击 payload 样本 |
| `data/payload_full.csv`   | 综合 payload 数据集       |
| `log/*.sql` / `log/*.txt` | 原始或中间 HTTP 日志数据  |

如需重新生成训练数据，可先运行数据清洗脚本：

```bash
python main/datacleaning.py
```

## 7. 运行方式

### 7.1 数据清洗

```bash
python main/datacleaning.py
```

### 7.2 运行 fastText 检测模型

```bash
python fasttext_text.py
```

或：

```bash
python fasttext.py
```

### 7.3 运行 LSTM 检测模型

```bash
python fasttext_LSTM.py
```

### 7.4 运行 TextCNN 检测模型

```bash
python textcnn.py
```

### 7.5 运行综合实验入口

```bash
python all.py
```

不同脚本可能对应不同实验设置，例如二分类检测、多分类检测、模型对比或可视化。建议首次运行时先检查脚本顶部的数据路径、类别标签、训练轮数、batch size、学习率等参数。

## 8. 输出结果

项目运行后通常可得到以下结果：

- Web 请求是否异常的分类结果；
- XSS 攻击与 SQL 注入攻击的识别结果；
- 模型训练过程中的准确率、损失值等指标；
- 检测结果统计图或实验可视化图表。

## 9. 应用场景

- Web 应用防火墙（WAF）检测规则的机器学习补充；
- XSS 与 SQL 注入攻击 payload 分类实验；
- 网络空间安全课程设计或实验教学；
- 基于文本语义建模的恶意请求检测研究；
- Web 日志安全审计与异常请求分析原型。

## 10. 与传统规则检测的区别

传统 Web 攻击检测通常依赖关键词、正则表达式或专家规则，对编码变形、混淆 payload、拼接语句等变体攻击的泛化能力有限。本项目将请求内容视为语义序列，通过 embedding、fastText、LSTM、TextCNN 等模型学习 token 之间的上下文关系，能够在一定程度上识别与已知攻击语义相近但表面形式不同的攻击样本。
## 11. 实验示例
1. 以下两图分别为正常URL和异常URL的特征图
<img width="799" height="498" alt="image" src="https://github.com/user-attachments/assets/d88c73eb-c8da-4f55-aa1b-65982157dc6b" />
<img width="744" height="558" alt="image" src="https://github.com/user-attachments/assets/694a703d-89f9-4035-9889-feca41b48f22" />
2. 以下分别为服务端运行界面和检测系统运行界面
<img width="1005" height="528" alt="image" src="https://github.com/user-attachments/assets/3e19644f-6455-4e24-8903-729973ef2f84" />
<img width="1033" height="445" alt="image" src="https://github.com/user-attachments/assets/fc66e527-46fa-4317-8709-aa9fab1cc281" />
3. 使用xsstrike模拟xss攻击，分别是正常URL和异常URL日志图
<img width="1030" height="152" alt="image" src="https://github.com/user-attachments/assets/837bc364-94c3-4f9b-aa3d-21c5655e5ce9" />
<img width="1017" height="446" alt="image" src="https://github.com/user-attachments/assets/c47170c6-26ec-4f1a-89d5-b37a72a89b17" />


## 12. 作者与单位声明
本项目作者及单位
```text 
项目名称：Semantic based Web Attack Detection
项目作者：Jianhui Qiu，Hong Deng, Chang Ding, Shengrui Gao, Zhiquan Liu
作者单位：暨南大学网络空间安全学院
