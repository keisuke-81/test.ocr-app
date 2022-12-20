import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing 


#タイトル
st.title("Hello! OCR ")

"""
### 〜 画像からテキスト抽出〜
（光学式文字認識）`英語、日本語対応`
"""

#写真をアップロード
st.sidebar.write("# Image Uploader")
st.sidebar.write("# `英語、日本語対応`")
image = st.sidebar.file_uploader(label = "この下へドラグアンドドロップもしくはクリックしてファイル選択で画像をアップロード",type=['png','jpg','jpeg'])
#image_dog = Image.open('dog.png')

@st.cache
def load_text(): #ocr読み取りの
    text_reader = ocr.Reader(['en','ja'],model_storage_directory='.')
    return text_reader 

text_reader = load_text() #load model 空っぽの入れ物にデータを入れる　インスタンス化　変数変えても

if image is not None:

    input_image = Image.open(image) #read image 画像の読み込み
    st.image(input_image) #display image 画像の表示
    # 進捗表示用のプレースホルダー
    status_text = st.empty()
    # プログレスバー
    # progress_bar = st.progress(0)

    # for i in range(100):
    #     # 進捗表示の文字列を更新
    #     status_text.text(f'Progress: {i}%')
    #     # for ループ内でプログレスバーの状態を更新する
    #     progress_bar.progress(i + 1)
    #     sleep(0.1)
    

    with st.spinner("ただいま画像読み取り中! "):
        
        
        #ocr処理
        result = text_reader.readtext(np.array(input_image)) #抽出したテキストをnp.arrayによってnumpyの配列に変換(Supporting format = string(file path or url), bytes, numpy array)
        text_word = np.stack(result) #numpyの配列をstrackによって結合して表に変換する
        st.markdown("## 🌟`読み取り結果`🌟 ")
        st.write(text_word[:,1]) #表の中で文章が表示されている列のみを([:,1])表示させる
        st.snow() #完了した時に雪を降らせる
else:
    st.write("サイドバー画像をアップロードしてください(200MBまで)")
    st.write("アップロードした画像と抽出されたテキストはここに表示されます")
    #st.image(image_dog,width=150)






