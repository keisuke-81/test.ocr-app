import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing 

#title
st.title("OCRアプリ - 画像からテキスト抽出")

#subtitle
st.markdown("## 光学式文字認識 - 使用 `easyocr`, `streamlit`")

st.markdown("")

#写真をアップロード
image = st.file_uploader(label = "ここへドラグアンドドロップもしくはクリックしてファイル選択で画像をアップロード",type=['png','jpg','jpeg'])


@st.cache
def load_model(): 
    reader = ocr.Reader(['en','ja'],model_storage_directory='.')
    return reader 

reader = load_model() #load model

if image is not None:

    input_image = Image.open(image) #read image
    st.image(input_image) #display image

    with st.spinner("ただいま画像読み取り中! "):
        

        result = reader.readtext(np.array(input_image))

        result_text = [] #empty list for results


        for text in result:
            result_text.append(text[1])

        st.write(result_text)
    #st.success("Here you go!")
    st.balloons()
else:
    st.write("Upload an Image")

#st.caption("Made with ❤️ by @1littlecoder")





