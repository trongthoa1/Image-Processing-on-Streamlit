import streamlit as st
import numpy as np
import cv2 as cv
import joblib
import argparse

st.set_page_config(page_title="NHẬN DẠNG KHUÔN MẶT", page_icon="🧭")

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
st.markdown("# NHẬN DẠNG KHUÔN MẶT")
FRAME_WINDOW = st.image([])

def str2bool(v):
    if v.lower() in ['on', 'yes', 'true', 'y', 't']:
        return True
    elif v.lower() in ['off', 'no', 'false', 'n', 'f']:
        return False
    else:
        raise NotImplementedError

parser = argparse.ArgumentParser()
parser.add_argument('--image1', '-i1', type=str, help='Path to the input image1. Omit for detecting on default camera.')
parser.add_argument('--image2', '-i2', type=str, help='Path to the input image2. When image1 and image2 parameters given then the program try to find a face on both images and runs face recognition algorithm.')
parser.add_argument('--video', '-v', type=str, help='Path to the input video.')
parser.add_argument('--scale', '-sc', type=float, default=1.0, help='Scale factor used to resize input video frames.')
parser.add_argument('--face_detection_model', '-fd', type=str, default="D:/Nam3/Ki_2/XuLyAnhSo/XLA/ImageProcessing-project-main/model/face_detection_yunet_2023mar.onnx", help='Path to the face detection model. Download the model at https://github.com/opencv/opencv_zoo/tree/master/models/face_detection_yunet')
parser.add_argument('--face_recognition_model', '-fr', type=str, default="D:/Nam3/Ki_2/XuLyAnhSo/XLA/ImageProcessing-project-main/model/face_recognition_sface_2021dec.onnx", help='Path to the face recognition model. Download the model at https://github.com/opencv/opencv_zoo/tree/master/models/face_recognition_sface')
parser.add_argument('--score_threshold', type=float, default=0.9, help='Filtering out faces of score < score_threshold.')
parser.add_argument('--nms_threshold', type=float, default=0.3, help='Suppress bounding boxes of iou >= nms_threshold.')
parser.add_argument('--top_k', type=int, default=5000, help='Keep top_k bounding boxes before NMS.')
parser.add_argument('--save', '-s', type=str2bool, default=False, help='Set true to save results. This flag is invalid when using camera.')
args = parser.parse_args()

svc = joblib.load("D:/Nam3/Ki_2/XuLyAnhSo/XLA/ImageProcessing-project-main/model/svc.pkl")
mydict = ['PhanQuoc', 'ThayDuc', 'TheBin', 'ThuyLinh', 'TrongThoai']

def visualize(input, faces, fps, thickness=2):
    if faces[1] is not None:
        for idx, face in enumerate(faces[1]):
            print('Face {}, top-left coordinates: ({:.0f}, {:.0f}), box width: {:.0f}, box height {:.0f}, score: {:.2f}'.format(idx, face[0], face[1], face[2], face[3], face[-1]))

            coords = face[:-1].astype(np.int32)
            cv.rectangle(input, (coords[0], coords[1]), (coords[0]+coords[2], coords[1]+coords[3]), (0, 255, 0), thickness)
            cv.circle(input, (coords[4], coords[5]), 2, (255, 0, 0), thickness)
            cv.circle(input, (coords[6], coords[7]), 2, (0, 0, 255), thickness)
            cv.circle(input, (coords[8], coords[9]), 2, (0, 255, 0), thickness)
            cv.circle(input, (coords[10], coords[11]), 2, (255, 0, 255), thickness)
            cv.circle(input, (coords[12], coords[13]), 2, (0, 255, 255), thickness)
    cv.putText(input, 'FPS: {:.2f}'.format(fps), (1, 16), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


if __name__ == '__main__':
    detector = cv.FaceDetectorYN.create(
        args.face_detection_model,
        "",
        (320, 320),
        args.score_threshold,
        args.nms_threshold,
        args.top_k
    )
    recognizer = cv.FaceRecognizerSF.create(
    args.face_recognition_model,"")

    tm = cv.TickMeter()

    cap = cv.VideoCapture(0)
    frameWidth = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    detector.setInputSize([frameWidth, frameHeight])

    dem = 0
    while True:
        hasFrame, frame = cap.read()
        if not hasFrame:
            print('No frames grabbed!')
            break

        # Inference
        tm.start()
        faces = detector.detect(frame) # faces is a tuple
        tm.stop()
        y = 50
        key = cv.waitKey(1)
        if key == 27:
            break
        if faces[1] is not None:
            for face_info in faces[1]:
                face_align = recognizer.alignCrop(frame, face_info)
                face_feature = recognizer.feature(face_align)
                test_predict = svc.predict(face_feature)
                result = mydict[test_predict[0]]
                # Vẽ văn bản lên khung hình
                cv.putText(frame, result, (1, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                y = y + 20
        # """if faces[1] is not None:
        #     face_align = recognizer.alignCrop(frame, faces[1][0])
        #     face_feature = recognizer.feature(face_align)
        #     test_predict = svc.predict(face_feature)
        #     result = mydict[test_predict[0]]
            
        #     # vẽ văn bản lên khung hình 
        #     cv.putText(frame,result,(1,50),cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)"""
        # Draw results on the input image
        visualize(frame, faces, tm.getFPS())

        FRAME_WINDOW.image(frame, channels='BGR')
    cv.destroyAllWindows()