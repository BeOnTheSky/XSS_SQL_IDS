import time
from keras.api.models import Sequential
from keras.api.layers import Dense,InputLayer,Dropout,LSTM,Bidirectional
from keras.api.callbacks import TensorBoard
from keras.api.models import Sequential
import numpy as np
from keras.api.optimizers import Adam
from fasttext_data import build_dataset
from fasttext_utils import init_session
from keras.api.models import load_model
from sklearn.metrics import precision_score,recall_score,accuracy_score,confusion_matrix
from keras.api.callbacks import EarlyStopping
from keras.api.callbacks import ReduceLROnPlateau, EarlyStopping, ModelCheckpoint
vec_dir="file\\fasttext.pkl"
init_session()
batch_size = 64
epochs_num = 6
pre_datas_train="file\\pre_datas_train.csv"
pre_datas_test="file\\pre_datas_test.csv"
#model_dir = "file\\fasttext_bilstm.keras"
model_dir = "file\\bilstm.keras"


def train(train_generator,train_size, input_num, dims_num,val_generator,val_size):
    
    
    '''
    print("Start Train Job! ")
    start = time.time()
    model = Sequential()
    model.add(InputLayer(input_shape=(input_num, dims_num.shape[0]), batch_size=batch_size))
    model.add(LSTM(128, return_sequences=True))
    model.add(Dropout(0.5))
    model.add(LSTM(64))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation="sigmoid", name="Output"))
    optimizer = Adam()
    model.compile(optimizer, loss="binary_crossentropy", metrics=["accuracy","precision","recall"])
    model.fit(train_generator, steps_per_epoch=train_size // batch_size, epochs=epochs_num)

    model.save(model_dir)
    end = time.time()
    print("Over train job in %f s" % (end - start))
    '''
    print("Start Train Job! ")
    start = time.time()

    model = Sequential()
    model.add(InputLayer(input_shape=(input_num, dims_num.shape[0]), batch_size=batch_size))
    model.add(Bidirectional(LSTM(128, return_sequences=False)))
    #model.add(LSTM(128, return_sequences=False))
    model.add(Dropout(0.5))
    # model.add(LSTM(64))
    # model.add(Dropout(0.5))
    model.add(Dense(1, activation="sigmoid", name="Output"))
    model.summary()
    optimizer = Adam(learning_rate=0.001)

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
              epochs=epochs_num,
              validation_data=val_generator,
            validation_steps=val_size // batch_size,
            callbacks=[early_stopping, model_checkpoint,reduce_lr]
             )

    #model.save(model_dir)  #
    end = time.time()
    print("Over train job in %f s" % (end - start))
def test(model_dir, test_generator, test_size, input_num, dims_num, batch_size):
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
    train_generator, test_generator, val_generator,train_size, test_size, val_size,input_num, dims_num = build_dataset(batch_size)
    train(train_generator, train_size, input_num, dims_num,val_generator,val_size)
    test(model_dir, test_generator, test_size, input_num, dims_num, batch_size)