import streamlit as st
import numpy as np
from PIL import Image
import cv2

st.set_page_config(page_title="Nhận dạng 5 phương tiện", page_icon="🚲")
st.title("Nhận dạng 5 loại đối tượng (phương tiện)")
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
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


try:
    if st.session_state["LoadModel"] == True:
        print('Đã load model rồi')
except KeyError:
    st.session_state["LoadModel"] = True
    st.session_state["Net"] = cv2.dnn.readNet(r"D:\Nam3\Ki_2\XuLyAnhSo\XLA\ImageProcessing-project-main\model\yolo5_5_xe.onnx")
    print(st.session_state["LoadModel"])
    print('Load model lần đầu')


# Constants.
INPUT_WIDTH = 640
INPUT_HEIGHT = 640
SCORE_THRESHOLD = 0.5
NMS_THRESHOLD = 0.45
CONFIDENCE_THRESHOLD = 0.45
 
# Text parameters.
FONT_FACE = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.7
THICKNESS = 1
 
# Colors.
BLACK  = (0,0,0)
BLUE   = (255,178,50)
YELLOW = (0,255,255)

def draw_label(im, label, x, y):
    """Draw text onto image at location."""
    # Get text size.
    text_size = cv2.getTextSize(label, FONT_FACE, FONT_SCALE, THICKNESS)
    dim, baseline = text_size[0], text_size[1]
    # Use text size to create a BLACK rectangle.
    cv2.rectangle(im, (x,y), (x + dim[0], y + dim[1] + baseline), (0,0,0), cv2.FILLED);
    # Display text inside the rectangle.
    cv2.putText(im, label, (x, y + dim[1]), FONT_FACE, FONT_SCALE, YELLOW, THICKNESS, cv2.LINE_AA)

def pre_process(input_image, net):
    # Create a 4D blob from a frame.
    blob = cv2.dnn.blobFromImage(input_image, 1/255,  (INPUT_WIDTH, INPUT_HEIGHT), [0,0,0], 1, crop=False)

    # Sets the input to the network.
    net.setInput(blob)

    # Run the forward pass to get output of the output layers.
    outputs = net.forward(net.getUnconnectedOutLayersNames())
    return outputs

def post_process(input_image, outputs):
    # Print the shape of outputs for debugging
    print("Outputs shape:", outputs[0].shape)
    # Lists to hold respective values while unwrapping.
    class_ids = []
    confidences = []
    boxes = []
    # Rows.
    rows = outputs[0].shape[1]
    image_height, image_width = input_image.shape[:2]
    # Resizing factor.
    x_factor = image_width / INPUT_WIDTH
    y_factor =  image_height / INPUT_HEIGHT
    # Iterate through detections.
    for r in range(rows):
        row = outputs[0][0][r]
        # Print the row for debugging
        print("Row:", row)
        confidence = row[4]
        # Discard bad detections and continue.
        if confidence >= CONFIDENCE_THRESHOLD:
                classes_scores = row[5:]
                # Get the index of max class score.
                class_id = np.argmax(classes_scores)
                #  Continue if the class score is above threshold.
                if (classes_scores[class_id] > SCORE_THRESHOLD):
                    confidences.append(confidence)
                    class_ids.append(class_id)
                    cx, cy, w, h = row[0], row[1], row[2], row[3]
                    left = int((cx - w/2) * x_factor)
                    top = int((cy - h/2) * y_factor)
                    width = int(w * x_factor)
                    height = int(h * y_factor)
                    box = np.array([left, top, width, height])
                    boxes.append(box)

    # Perform non maximum suppression to eliminate redundant, overlapping boxes with lower confidences.
    indices = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
    for i in indices:
        box = boxes[i]
        left = box[0]
        top = box[1]
        width = box[2]
        height = box[3]             
        # Draw bounding box.             
        cv2.rectangle(input_image, (left, top), (left + width, top + height), BLUE, 3*THICKNESS)
        # Class label.                      
        label = "{}:{:.2f}".format(classes[class_ids[i]], confidences[i])             
        # Draw label.             
        draw_label(input_image, label, left, top)
    return input_image

img_file_buffer = st.file_uploader("Upload an image", type=["bmp", "png", "jpg", "jpeg"])

if img_file_buffer is not None:
    image = Image.open(img_file_buffer)
    # Chuyển sang cv2 để dùng sau này
    frame = np.array(image)
    frame = frame[:, :, [2, 1, 0]] # BGR -> RGB

    st.image(image)
    if st.button('Predict'):
        classes = ['xe_buyt', 'xe_hoi', 'xe_may', 'xe_canh_sat', 'xe_cuu_thuong']
        # Process image.
        detections = pre_process(frame, st.session_state["Net"])
        img = post_process(frame.copy(), detections)
        """
        Kết quả dự đoán:
        """
        t, _ = st.session_state["Net"].getPerfProfile()
        label = 'Inference time: %.2f ms' % (t * 1000.0 /  cv2.getTickFrequency())
        print(label)
        cv2.putText(img, label, (20, 40), FONT_FACE, FONT_SCALE,  (0, 0, 255), THICKNESS, cv2.LINE_AA)
        st.image(img)
