import pickle
import time
from keras.api.models import Sequential
from keras.api.layers import Dense,InputLayer,Dropout,LSTM,GlobalMaxPooling2D, BatchNormalization
from keras.api.callbacks import TensorBoard
from keras.api.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Embedding, InputLayer, Reshape
from keras.api.models import Sequential
import numpy as np
from keras.api.optimizers import Adam
from fasttext_data import build_dataset
from keras.api.models import load_model
from keras.api.callbacks import ReduceLROnPlateau, EarlyStopping, ModelCheckpoint
from sklearn.metrics import precision_score,recall_score,accuracy_score,confusion_matrix
from keras.api.callbacks import EarlyStopping
from keras.api.utils import plot_model
from keras.api.regularizers import l2
vec_dir="file\\fasttext.pkl"
batch_size = 64
epochs_num = 6
pre_datas_train="file\\pre_datas_train.csv"
pre_datas_test="file\\pre_datas_test.csv"
model_dir = "file\\textcnn.keras"

def train(train_generator,train_size, input_num, dims_num,val_generator,val_size):
    print("Start Train Job! ")
    start = time.time()

    model = Sequential()
    model.add(InputLayer(input_shape=(input_num, dims_num.shape[0])))  # 输入形状直接用词向量维度

    model.add(Reshape((input_num, dims_num.shape[0], 1)))  

    
    # 添加卷积层
    model.add(Conv2D(128, kernel_size=(3, dims_num.shape[0]), activation='relu'))  # 使用卷积核
    model.add(MaxPooling2D(pool_size=(input_num - 2, 1)))  # 最大池化
    model.add(Flatten())  # 展平

    # 全连接层
    model.add(Dense(128, activation='relu'))  # 隐藏层
    model.add(Dropout(0.5))  # Dropout
    model.add(Dense(1, activation="sigmoid", name="Output"))
    model.summary()
    optimizer = Adam(learning_rate=0.001)

    model.compile(optimizer=optimizer, loss="binary_crossentropy", metrics=["accuracy", "precision", "recall"])
        # Early stopping to prevent overfitting
    early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
    model_checkpoint = ModelCheckpoint(filepath=model_dir, monitor='val_loss', save_best_only=True)
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=3, verbose=1, min_lr=1e-6)
    model.fit(train_generator, steps_per_epoch=train_size // batch_size, epochs=epochs_num,validation_data=val_generator,
        validation_steps=val_size // batch_size,
        callbacks=[early_stopping, model_checkpoint, reduce_lr])

    #model.save(model_dir)
    end = time.time()
    print("Over train job in %f s" % (end - start))

def test(model_dir, test_generator, test_size, input_num, dims_num):
    model = load_model(model_dir)
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
        #print("Predictions:", predictions[:len(labels)])
        threshold = 0.5
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
    # print(y_true)
    # print(y_pre)
    print(len(y_true))
    print(len(y_pre))
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

if __name__ == "__main__":
    train_generator, test_generator, val_generator, train_size, test_size, val_size,input_num, dims_num = build_dataset(batch_size)
    train(train_generator, train_size, input_num, dims_num,val_generator,val_size)
    test(model_dir, test_generator, test_size, input_num, dims_num)