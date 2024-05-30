import cv2
import streamlit as st
import numpy as np
from cvzone.HandTrackingModule import HandDetector
st.set_page_config(page_title="PHÓNG TO THU NHỎ", page_icon="🔍")
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
    # background-image: url("https://images.unsplash.com/photo-1617550523898-600c24418b75?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
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


def main():
    st.title("PHÓNG TO - THU NHỎ HÌNH ẢNH")

    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    detector = HandDetector(detectionCon=0.75)
    startDist = None
    scale = 0
    cx, cy = 500, 500

    img1 = cv2.imread("D:/Nam3/Ki_2/XuLyAnhSo/XLA/ImageProcessing-project-main/pages/test/test.jpg")

    # Vùng hiển thị hình ảnh trong ứng dụng Streamlit
    image_placeholder = st.empty()

    while True:
        success, img = cap.read()
        hands, img = detector.findHands(img)

        if len(hands) == 2:
            if detector.fingersUp(hands[0]) == [1, 1, 0, 0, 0] and \
                    detector.fingersUp(hands[1]) == [1, 1, 0, 0, 0]:
                lmList1 = hands[0]["lmList"]
                lmList2 = hands[1]["lmList"]

                if startDist is None:
                    length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
                    startDist = length

                length, info, img = detector.findDistance(hands[0]["center"], hands[1]["center"], img)
                scale = int((length - startDist) // 2)
                cx, cy = info[4:]

        else:
            startDist = None

        try:
            h1, w1, _ = img1.shape
            newH, newW = ((h1+scale)//2)*2, ((w1+scale)//2)*2
            img1_resized = cv2.resize(img1, (newW, newH))

            img[cy-newH//2:cy+ newH//2, cx-newW//2:cx+ newW//2] = img1_resized

        except:
            pass

        # Chuyển đổi hình ảnh từ NumPy array sang định dạng dữ liệu cho Streamlit
        image_streamlit = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Hiển thị hình ảnh trong ứng dụng Streamlit
        image_placeholder.image(image_streamlit, channels="RGB", use_column_width=True)

if __name__ == "__main__":
    main()
