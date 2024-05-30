import streamlit as st
import tensorflow as tf
from tensorflow import keras
from keras import datasets, models
#from tensorflow.keras.models import model_from_json
import numpy as np
import random
import cv2

# Set Streamlit page configuration
st.set_page_config(page_title="Nhận dạng chữ số mnist", page_icon="🔢")

# Define page background styling
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1444080748397-f442aa95c3e5?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8Mnx8fGVufDB8fHx8fA%3D%3D");
    background-size: 100% 100%;
}
[data-testid="stHeader"]{
    background: rgba(0,0,0,0);
}
[data-testid="stToolbar"]{
    right:2rem;
}
[data-testid="stForm"]{
    background-color: #77777745;
    backdrop-filter: blur(20px);
}
.st-emotion-cache-lrlib{
    padding-top: 44px;
}
[data-testid="stSidebar"] {
    background-color: #77777745;
    border-radius: 10px;
    margin-top: 115px;
    margin-left: 58px;
    backdrop-filter: blur(10px);
}
.header{
    background-color: rgb(113 104 119 / 10%);
    padding: 20px;
    border-radius: 6px;
    box-shadow: 17px 11px 53px -48px rgba(147,0,255,0.45);
    backdrop-filter: blur(20px);
}
.header img{
    width: 100%;
    height: 250px;
    border-radius: 4px;
    box-shadow: 17px 11px 118px -38px rgba(147,0,255,0.45);
    object-fit: cover;
}
.header-title{
    font-size: 44px;
    font-weight: 700;
    text-align: center;
    margin-top: 18px;
}
.header-malop{
    font-size: 32px;
    font-weight: 700;
    text-align: center;
}
.st-emotion-cache-1hdbmx1{
    border: 1px solid #fff;
}
.st-bv{
    background-color: transparent;
}
.st-emotion-cache-1hgxyac{
    background-color: #fff;
}
.st-emotion-cache-1hgxyac svg{
    fill: #333;
}
.st-emotion-cache-1hgxyac:hover:enabled, .st-emotion-cache-1hgxyac:focus:enabled{
    background-color: rgb(242 242 242);
}
[data-testid="baseButton-secondaryFormSubmit"]{
    width: 100px;
    background-color: #ffffff33;
}
.st-emotion-cache-19rxjzo .ef3psqc6{
    float:right;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Tiêu đề ứng dụng Streamlit
st.title("NHẬN DIỆN CHỮ VIẾT TAY")

# Hàm tạo ảnh ngẫu nhiên
def tao_anh_ngau_nhien():
    image = np.zeros((10 * 28, 10 * 28), np.uint8)
    data = np.zeros((100, 28, 28, 1), np.uint8)

    for i in range(100):
        n = random.randint(0, 9999)
        sample = st.session_state.X_test[n]
        data[i] = sample
        x = i // 10
        y = i % 10
        image[x * 28:(x + 1) * 28, y * 28:(y + 1) * 28] = sample[:, :, 0]

    return image, data

# Kiểm tra xem mô hình và dữ liệu đã được tải chưa
if 'is_load' not in st.session_state:
    # Tải mô hình
    model_architecture = "D:/Nam3/Ki_2/XuLyAnhSo/XLA/ImageProcessing-project-main/model/digit_config.json"
    model_weights = 'D:/Nam3/Ki_2/XuLyAnhSo/XLA/ImageProcessing-project-main/model/digit_weight.h5'
    
    with open(model_architecture, 'r',encoding='utf-8') as json_file:
        model = models.model_from_json(json_file.read())
    model.load_weights(model_weights)

    OPTIMIZER = tf.keras.optimizers.Adam()
    model.compile(loss="categorical_crossentropy", optimizer=OPTIMIZER, metrics=["accuracy"])
    st.session_state.model = model

    # Tải dữ liệu
    (_, _), (X_test, y_test) = datasets.mnist.load_data()
    X_test = X_test.reshape((10000, 28, 28, 1))
    st.session_state.X_test = X_test

    st.session_state.is_load = True
    print('Lần đầu load model và data')
else:
    print('Đã load model và data rồi')

# Nút tạo ảnh ngẫu nhiên
if st.button('Tạo ảnh'):
    image, data = tao_anh_ngau_nhien()
    st.session_state.image = image
    st.session_state.data = data

# Hiển thị ảnh được tạo
if 'image' in st.session_state:
    image = st.session_state.image
    st.image(image, caption='Generated Image', use_column_width=True)

    # Nút nhận dạng chữ số
    if st.button('Nhận dạng'):
        data = st.session_state.data
        data = data / 255.0
        data = data.astype('float32')
        ket_qua = st.session_state.model.predict(data)
        dem = 0
        s = ''
        for x in ket_qua:
            s = s + '%d ' % (np.argmax(x))
            dem = dem + 1
            if (dem % 10 == 0) and (dem < 100):
                s = s + '\n'
        st.text(s)