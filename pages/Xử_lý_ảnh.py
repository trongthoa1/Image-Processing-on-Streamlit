import streamlit as st
import time
import numpy as np
import ThucHanhXuLyAnh.Chapter03 as c3
import ThucHanhXuLyAnh.Chapter04 as c4
import ThucHanhXuLyAnh.Chapter05 as c5
import ThucHanhXuLyAnh.Chapter09 as c9


import sys
import tkinter
from tkinter import Frame, Tk, BOTH, Text, Menu, END
from tkinter.filedialog import Open, SaveAs
import cv2


from PIL import Image

st.set_page_config(page_title="Xử lý ảnh số", page_icon="✨")
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1444080748397-f442aa95c3e5?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8Mnx8fGVufDB8fHx8fA%3D%3D");
    background-size: 100% 100%;
    # background-color: #333
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
    # background-image: url("https://images.unsplash.com/photo-1444080748397-f442aa95c3e5?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8Mnx8fGVufDB8fHx8fA%3D%3D");
   # background-position: center;
   # object-fit: contain;
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
st.markdown(page_bg_img,unsafe_allow_html=True)
st.markdown("# Xử lý ảnh")
st.write()

image_file = st._main.file_uploader("Upload Your Image", type=[
                                  'jpg', 'png', 'jpeg', 'tif'])

global imgin
if image_file is not None:
    file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
    imgin = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE) 

    chapter_options = ["Chapter 3", "Chapter 4", "Chapter 5", "Chapter 9"]
    selected_chapter = st.sidebar.selectbox("Select an option", chapter_options)


    if selected_chapter == "Chapter 3":
        chapter3_options = ["Negative", "Logarit", "Power", "PiecewiseLinear", "Histogram", "HistogramEqualization",
                                                "HistogramEqualizationColor", "LocalHistogram", "HistogramStatistics", 
                                                "BoxFilter", "GaussFilter","Threshold", "MedianFilter", "Sharpen", "Gradient"]
        
        chapter3_selected = st.sidebar.selectbox("Select an option", chapter3_options)    
        if chapter3_selected  == "Negative":
            processed_image = c3.Negative(imgin)
        elif chapter3_selected  == "Logarit":
            processed_image = c3.Logarit(imgin)
        elif chapter3_selected  == "Power":
            processed_image = c3.Power(imgin)
        elif chapter3_selected  == "PiecewiseLinear":
            processed_image = c3.PiecewiseLinear(imgin)
        elif chapter3_selected  == "Histogram":
            processed_image = c3.Histogram(imgin)
        elif chapter3_selected  == "HistogramEqualization":
            processed_image = c3.HistEqual(imgin)
        elif chapter3_selected == "HistogramEqualizationColor":
            imgin = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
            processed_image = c3.HistEqualColor(imgin)
        elif chapter3_selected  == "LocalHistogram":
            processed_image = c3.LocalHist(imgin)
        elif chapter3_selected  == "HistogramStatistics":
            processed_image = c3.HistStat(imgin)
        elif chapter3_selected  == "BoxFilter":
            processed_image = c3.BoxFilter(imgin)
        elif chapter3_selected  == "GaussFilter":
            processed_image = c3.GaussFilter(imgin)
        elif chapter3_selected  == "Threshold":
            processed_image = c3.Threshold(imgin)
        elif chapter3_selected  == "MedianFilter":
            processed_image = c3.MedianFilter(imgin)
        elif chapter3_selected  == "Sharpen":
            processed_image = c3.Sharpen(imgin)
        elif chapter3_selected  == "Gradient":
            processed_image = c3.Gradient(imgin) 
            
                      
    elif selected_chapter == "Chapter 4":
        
        chapter4_options = ["Spectrum", "FrequencyFilter", "DrawFilter", "RemoveMoire"]
        
        chapter4_selected = st.sidebar.selectbox("Select an option", chapter4_options)   
        
        
        if chapter4_selected == "Spectrum":
            processed_image = c4.Spectrum(imgin)
        elif chapter4_selected == "FrequencyFilter":
            processed_image = c4.FrequencyFilter(imgin)
        elif chapter4_selected == "DrawFilter":
            imgin = Image.new('RGB', (5, 5),  st.get_option("theme.backgroundColor"))
            processed_image = c4.DrawNotchRejectFilter()
        elif chapter4_selected == "RemoveMoire":
            processed_image = c4.RemoveMoire(imgin)
            

    elif selected_chapter == "Chapter 5":
        
        chapter5_options = ["CreateMotionNoise", "DenoiseMotion", "DenoisestMotion"]
        chapter5_selected = st.sidebar.selectbox("Select an option", chapter5_options)   
        
        if chapter5_selected == "CreateMotionNoise":
            processed_image = c5.CreateMotionNoise(imgin)
        elif chapter5_selected == "DenoiseMotion":
            processed_image = c5.DenoiseMotion(imgin)
        elif chapter5_selected == "DenoisestMotion":
            temp = cv2.medianBlur(imgin, 7)
            processed_image = c5.DenoiseMotion(temp)   
            
                 
    elif selected_chapter == "Chapter 9":
        
        chapter9_options = ["ConnectedComponent", "CountRice"]
        chapter9_selected = st.sidebar.selectbox("Select an option", chapter9_options)   
        
        if chapter9_selected  == "ConnectedComponent":
            processed_image = c9.ConnectedComponent(imgin)    
        elif chapter9_selected  == "CountRice":
            processed_image = c9.CountRice(imgin)
    

    st.subheader("Original Image and Processed Image")
    st.image([imgin, processed_image], width = 350)
st.button("Re-run")
