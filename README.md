# Cartoonify_App
A Streamlit app to convert images into cartoon-style using OpenCV

# 🎨 Cartoonify Your Image

A simple web app built with **Streamlit** and **OpenCV** that transforms your uploaded images into a cartoon-like version using edge detection and filtering techniques.

---

## 🧠 How It Works

This app uses OpenCV to apply the following steps to an image:
1. Convert the image to grayscale
2. Apply median blur for noise reduction
3. Detect edges using adaptive thresholding
4. Apply bilateral filtering to preserve edges while smoothing colors
5. Combine edges with filtered image for a cartoon effect

---

## 🚀 Try It Locally

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/cartoonify-app.git
cd cartoonify-app
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
3. Run the App
```bash
streamlit run app.py
```
📂 Project Structure
```bash
cartoonify-app/
├── app.py                # Streamlit app code
├── cartoonify_utils.py   # Image processing functions
├── requirements.txt      # Project dependencies
└── README.md             # Project overview and setup instructions
```
🖼️ Sample Output
Original Image	Cartoonified Image
(Insert image)	(Insert image)

You can include example inputs and outputs by placing them in an examples/ folder and linking them here.

🛠️ Tech Stack
Python

Streamlit

OpenCV

NumPy

Pillow (PIL)

💡 Future Improvements
Add more filter styles (e.g., sketch, oil painting, pencil sketch)

Enable webcam integration

Deploy to Streamlit Cloud or Render

Add option to view and save all transformation stages

Optimize for mobile devices

