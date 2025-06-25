# app.py

import streamlit as st
import cv2
import numpy as np
from cartoonify_utils import cartoonify_image
from PIL import Image
import io

# Set up the app page
st.set_page_config(page_title="Cartoonify Your Image", layout="centered")

# App title and instructions
st.title("🎨 Cartoonify Your Image")
st.write("Upload a photo and see it transformed into a cartoon!")

# File uploader component
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Load image with PIL and convert to NumPy array
    image = Image.open(uploaded_file)
    image_np = np.array(image)

    # Handle transparency (RGBA) if present
    if image_np.shape[-1] == 4:
        image_np = cv2.cvtColor(image_np, cv2.COLOR_RGBA2BGR)
    else:
        image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    # Show the original image
    st.image(image, caption='Uploaded Image', use_container_width=True)

    # Process image on button click
    if st.button("Cartoonify"):
        cartoon = cartoonify_image(image_np)

        # Show the cartoonified image
        st.image(cartoon, caption='Cartoonified Image', use_container_width=True)

        # Convert to PIL and allow download
        result = Image.fromarray(cartoon)
        buf = io.BytesIO()
        result.save(buf, format="JPEG")
        byte_im = buf.getvalue()

        # Download button
        st.download_button("📥 Download Cartoon Image", data=byte_im,
                           file_name="cartoonified.jpg", mime="image/jpeg")
