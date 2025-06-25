# app.py

import streamlit as st 
import cv2
import numpy as np
from cartoonify_utils import cartoonify_image
from PIL import Image
import io

# Streamlit page setup
st.set_page_config(page_title="Cartoonify Your Image", layout="centered")

# App title
st.title("Cartoonify Your Image")
st.markdown("Upload a photo and transform it into a fun **cartoon-style** image using OpenCV!")

# File uploader
uploaded_file = st.file_uploader("Upload your image", type=["jpg", "jpeg", "png"])

# Sidebar info
with st.sidebar:
    st.header("About")
    st.markdown("""
    This app uses **OpenCV** to apply:
    - Grayscale conversion  
    - Edge detection  
    - Bilateral filtering  
    to give your image a **cartoonified** look!
    """)

# Process uploaded image
if uploaded_file is not None:
    # Load image
    image = Image.open(uploaded_file)
    image_np = np.array(image)

    # Convert RGBA or RGB to BGR for OpenCV
    if image_np.shape[-1] == 4:
        image_np = cv2.cvtColor(image_np, cv2.COLOR_RGBA2BGR)
    else:
        image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    # Resize to 600x400 for faster processing
    #image_np = cv2.resize(image_np, (600, 400))
    image_resized = Image.fromarray(cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB))

    # Display original image
    st.image(image_resized, caption="Uploaded Image", use_container_width=True)

    # Button to apply cartoon filter
    if st.button("Cartoonify Now"):
        cartoon = cartoonify_image(image_np)

        # Convert and display cartoonified image
        cartoon_pil = Image.fromarray(cartoon)
        st.image(cartoon_pil, caption="Cartoonified Image", use_container_width=True)

        # Prepare image for download
        buf = io.BytesIO()
        cartoon_pil.save(buf, format="JPEG")
        byte_im = buf.getvalue()

        # Download button
        st.download_button(
            label="Download Cartoon Image",
            data=byte_im,
            file_name="cartoonified.jpg",
            mime="image/jpeg"
        )

# Footer note
st.markdown("---")
st.markdown("Made with Python & Streamlit")
