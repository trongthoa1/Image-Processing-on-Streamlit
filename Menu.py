import streamlit as st
#import lib.common as tools

st.set_page_config(
    page_title="ĐỒ ÁN CUỐI KỲ MÔN XỬ LÝ ẢNH SỐ",
    page_icon="📸",
)

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

.st-emotion-cache-lrlib{
    padding-top: 44px;
}

[data-testid="stSidebar"] {
    # background-image: url("https://images.pexels.com/photos/1257860/pexels-photo-1257860.jpeg?cs=srgb&dl=pexels-philippedonn-1257860.jpg&fm=jpg");
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
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)


st.write('<div class="header">'
            '<img src="https://images.unsplash.com/photo-1444080748397-f442aa95c3e5?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxleHBsb3JlLWZlZWR8Mnx8fGVufDB8fHx8fA%3D%3D" alt="">'
            '<p class="header-title">ĐỒ ÁN CUỐI KỲ XỬ LÝ ẢNH SỐ</p>'
            '<p class="header-malop">(DIPR430685_23_2_01)</p>'
        '</div>',
          unsafe_allow_html=True)
# st.write("# Mã lớp : DIPR430685_23_2_01")
st.write('## 21133084 - Trần Trọng Thoại')
st.write('## 21133108 - Trần Phan Quốc')


st.markdown(
    """
    
    ## Sản phẩm
    Project cuối kỳ cho môn học XỬ LÝ ẢNH SỐ (DIPR430685).
    Trường Đại Học Sư Phạm Kỹ Thuật TP.HCM do Th.S Trần Tiến Đức hướng dẫn. 

    ### Đồ án gồm 5 chức năng cơ bản
    - 📖 Giải phương trình bậc 2
    - 📖 Nhận dạng khuôn mặt
    - 📖 Nhận diện chữ viết tay mnist
    - 📖 Nhận dạng 5 loại đối tượng (xe buýt, xe cảnh sát, xe cứu thương, xe hơi, xe máy)
    - 📖 Xử lý ảnh

    ### Chúng em đã thêm các chức năng:
    - 📝 Phát hiện đối tượng bằng yolov4
    - 📝 Nhận dạng chuyển động
    - 📝 Nhận dạng bàn tay
    - 📝 Phóng to - thu nhỏ hình ảnh


    Đề tài và bài báo cáo được chúng em thực hiện trong khoảng thời gian ngắn, với những kiến thức còn hạn chế cùng nhiều hạn chế khác về mặt kĩ thuật và kinh nghiệm trong việc thực hiện một dự án. Do đó, trong quá trình làm nên đề tài có những thiếu sót là điều không thể tránh khỏi nên chúng em rất mong nhận được những ý kiến đóng góp quý báu của thầy để kiến thức của chúng em được hoàn thiện hơn và chúng em có thể làm tốt hơn nữa trong những lần sau. Chúng em xin chân thành cảm ơn. 
    """
)


