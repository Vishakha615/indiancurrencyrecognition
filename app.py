# pip install pillow

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from tensorflow import keras 
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

st.set_page_config(
    page_title="Indian Currency Recognition",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)


import os
import gdown
from tensorflow.keras.models import load_model

MODEL_PATH = "currency.keras"

if not os.path.exists(MODEL_PATH):
    file_id = "1tqSNF7l0tsgMy0iarqCob_FQgqv4aZNk"
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, MODEL_PATH, quiet=False)

model = load_model(MODEL_PATH)





st.markdown("""
<style>
[data-testid="stSidebar"] {
    background-color: #732C12;
    color:white;
            
}       

</style>
""", unsafe_allow_html=True)


st.markdown(""" <style>
        .stApp{
        background: linear-gradient(to top, #F7C4B2, #FFFFFF);
            }
            
            
  div.stButton > button {
    background-color: #732C12;
    color: white;
    font-size: 20px;
    font-weight: bold;
    width: 145px;
    height: 45px;
    border-radius: 10px;
    border: 2px double white;
    margin-top : 10px;
    margin-bottom : 10px;
    
    
    
}
            </style>
""",unsafe_allow_html=True)





st.title("💰 Indian Currency Recognition")







st.divider()

st.markdown(""" 
            <h5 style="margin-top:20px; color:#421E11; "> Identify Indian Currency Notes using CNN</h5>""",unsafe_allow_html=True)

st.divider()
st.markdown(""" 
            <h3 style="margin-top:20px; color:#000000; text-align:center; "><u> Choose an Input Method</u></h3>""",unsafe_allow_html=True)
st.divider()
st.markdown(""" 
            <h5 style="margin-top:20px; color:#421E11;  "> 1. Upload an Image</h5>""",unsafe_allow_html=True)


# *******************upload image ***********************


uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    st.divider()

    st.markdown("""
        <h5 style="margin-top:20px; color:#421E11;">
        🖼 Image Preview
        </h5>
    """, unsafe_allow_html=True)

    st.image(uploaded_file)

    img = Image.open(uploaded_file)

    img = img.resize((128,128))

    img_array = image.img_to_array(img)

    img_array = img_array / 255.0

    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    class_names = [
        "₹10",
        "₹100",
        "₹20",
        "₹200",
        "₹50",
        "₹500",
        "₹2000"
    ]

    predicted_index = np.argmax(prediction)

    predicted_note = class_names[predicted_index]

    confidence = np.max(prediction) * 100

    st.divider()

    st.markdown("""
        <h4 style="color:#421E11;  margin-top:20px;">
        🎯 Prediction
        </h4>
    """, unsafe_allow_html=True)

    if predicted_note == "Background":

        st.warning("⚠ Background Detected")

    else:

        #st.success(f"💵 Predicted Currency : {predicted_note}")
        st.markdown(f"""
        <div style="
        background:white;
        padding:20px;
        margin-bottom:20px;
        border-radius:15px;
        text-align:center;
        box-shadow:2px 2px 12px rgba(0,0,0,0.2);
        ">

        <h3 style="color:#421E11;">
        💵 Predicted Currency
        </h3>

        <h1 style="color:#0A7D32;">
        {predicted_note}
        </h1>

        </div>
        """, unsafe_allow_html=True)
        st.divider()

        st.markdown(f"""
        <h4 style="color:#421E11;">📊 Confidence</h4>

        <h2 style="color:#1E88E5; margin-top:10px;">
        {confidence:.2f}%
        </h2>
        """, unsafe_allow_html=True)

        st.progress(int(confidence))
    
    
    
st.divider()



#*********************************




if "open_camera" not in st.session_state:
    st.session_state.open_camera = False

st.markdown(""" 
            <h5 style="margin-top:20px; color:#421E11;  "> 2. 📸 Capture Image</h5>""",unsafe_allow_html=True)
    
if st.button("Click Photo"):
    st.session_state.open_camera = True

    #with col2:
        #if st.button("❌ Close Camera"):
            #st.session_state.open_camera = False

if st.session_state.open_camera:

    camera_image = st.camera_input("")

    if camera_image is not None:

        st.divider()

        st.markdown("""
        <h5 style="margin-top:20px; color:#421E11;">
        🖼 Image Preview
        </h5>
        """, unsafe_allow_html=True)

        st.image(camera_image)

        img = Image.open(camera_image)

        img = img.resize((128,128))

        img_array = image.img_to_array(img)

        img_array = img_array / 255.0

        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)

        class_names = [
        "₹10",
        "₹100",
        "₹20",
        "₹200",
        "₹50",
        "₹500",
        ]

        predicted_index = np.argmax(prediction)

        predicted_note = class_names[predicted_index]

        confidence = np.max(prediction) * 100

        st.divider()

        st.markdown("""
        <h4 style="color:#421E11; margin-top:20px;">
        🎯 Prediction
        </h4>
        """, unsafe_allow_html=True)

        if predicted_note == "Background":

            st.warning("⚠️ Background Detected")

        else:

            #st.success(f"💵 Predicted Currency : {predicted_note}")
            st.markdown(f"""
            <div style="
            background:white;
            margin-bottom:20px;
            padding:20px;
            border-radius:15px;
            text-align:center;
            box-shadow:2px 2px 12px rgba(0,0,0,0.2);
            ">

            <h3 style="color:#421E11;">
            💵 Predicted Currency
            </h3>

            <h1 style="color:#0A7D32;">
            {predicted_note}
            </h1>

            </div>
            """, unsafe_allow_html=True)
            
            
        st.divider()

    
        st.markdown(f"""
        <h4 style="color:#421E11;">📊 Confidence</h4>

        <h2 style="color:#1E88E5; margin-top:10px;">
        {confidence:.2f}%
        </h2>
        """, unsafe_allow_html=True)

        st.progress(int(confidence))
    

        st.session_state.open_camera = False
        
#************************************
st.divider()
st.markdown(""" 
            <h3 style="margin-top:20px; color:#421E11; text-align:center; "> 📋 <u>Currency Model Information</u></h3>""",unsafe_allow_html=True)
    
st.divider()
col1, col2, col3 = st.columns(3)



    
with col1:
    st.markdown("""
    <div style="
        background:#945948;
        padding:22px;
        margin-top :20px;
        width:300px;
        height:100px;
        border-radius:15px;
        text-align:center;
        box-shadow:2px 2px 10px rgba(0,0,0,0.15);
        border-left:6px solid #732C12;
    ">
        <h5 style="color:#FFFFFF; margin-top:12px;">🏛&nbsp;&nbsp;&nbsp; Country India</h5>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
        background:#945948;
        padding:22px;
        width:300px;
        margin-top :20px;
        height:100px;
        border-radius:15px;
        text-align:center;
        box-shadow:2px 2px 10px rgba(0,0,0,0.15);
        border-left:6px solid #732C12;
    ">
        <h5 style="color:#FFFFFF;  margin-top:12px;">📌 In 7 Classes</h5>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
        background:#945948;
        padding:22px;
        margin-top :20px;
        width:300px;
        height:100px;
        border-radius:15px;
        text-align:center;
        box-shadow:2px 2px 10px rgba(0,0,0,0.15);
        border-left:6px solid #732C12;
    ">
        <h5 style="color:#FFFFFF;  text-align:center; margin-top:5px;">📏 Image size <br>128 × 128</h5>
    </div>
    """, unsafe_allow_html=True)
    
    


col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="
        background:#945948;
        padding:22px;
        width:300px;
        height:100px;
        margin-top :20px;
        border-radius:15px;
        margin-bottom :20px;
        text-align:center;
        box-shadow:2px 2px 10px rgba(0,0,0,0.15);
        border-left:6px solid #732C12;
    ">
        <h5 style="color:#FFFFFF; margin-top:12px;"> 🧠 CNN Model</h5>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
        background:#945948;
        padding:22px;
        width:300px;
        margin-top :20px;
        height:100px;
        margin-bottom :20px;
        border-radius:15px;
        text-align:center;
        box-shadow:2px 2px 10px rgba(0,0,0,0.15);
        border-left:6px solid #732C12;
    ">
        <h5 style="color:#FFFFFF;  margin-top:12px;">🎯 Accuracy Above 50%</h5>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
        background:#945948;
        padding:22px;
        width:300px;
        height:100px;
        margin-top :20px;
        margin-bottom :20px;
        border-radius:15px;
        text-align:center;
        box-shadow:2px 2px 10px rgba(0,0,0,0.15);
        border-left:6px solid #732C12;
    ">
        <h5 style="color:#FFFFFF;  margin-top:5px;">⚙️ Tensorflow  &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;Framework</h5>
    </div>
    """, unsafe_allow_html=True)
    
       
st.divider()
st.markdown(
    """
    <div style="text-align:center; color:#A87262; font-size:17px;">
        Developed using TensorFlow, Keras and Streamlit 
        
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style="text-align:center; color:#A87262; font-size:17px;">
        Developed by 
        
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style="text-align:center; color:#A87262; font-size:17px;">
        Vishakha Nikam
        
    </div>
    """,
    unsafe_allow_html=True
)

