# 🎨 Cartoonify Your Image

A simple yet powerful application built using **Python**, **OpenCV**, and **Streamlit** that converts normal photographs into cartoon-like images. This project includes both a **Jupyter notebook** for explanation and a **Streamlit web app** for interactive use.

---

## 🧠 How Cartoonification Works
The cartoonify algorithm uses classical image processing steps:

1. Grayscale Conversion – simplifies color complexity
2. Median Blurring – reduces image noise
3. Adaptive Thresholding – extracts edges (sketch effect)
4. Bilateral Filtering – smooths regions while preserving edges
5. Bitwise AND – overlays filtered image with edges to produce final cartoon

These steps are applied in cartoonify_utils.py.
The final result is an image that looks hand-drawn or illustrated, giving it a fun cartoon-like effect.

---

## 📂 Repository Structure

```plaintext
cartoonify-app/
├── app.py                         # Streamlit web app for cartoonifying images
├── cartoonify_utils.py           # Utility functions for image processing
├── Cartooning_an_Image_using_OpenCV.ipynb  # Jupyter notebook with step-by-step explanation
├── requirements.txt              # Python dependencies (optional for deployment)
└── README.md                     # Project documentation
```

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
## 📒 Explore via Jupyter Notebook
If you'd like to understand the logic in a more educational format, open:

```bash
Cartooning_an_Image_using_OpenCV.ipynb
You can run this notebook in Google Colab or your local Jupyter environment.
```


## 🖼️ Sample Output
Original Image	Cartoonified Image
![input_img](https://github.com/user-attachments/assets/c4fc3ddd-a303-45f6-8945-706961d5dbb5)
![cartoonified](https://github.com/user-attachments/assets/343611bf-4b38-4aab-bf05-0628d1ce7895)



## 🛠 Tech Stack
  🐍 Python 3
  📦 OpenCV
  📊 NumPy
  🖼️ Pillow
  🌐 Streamlit

##💡 Future Improvements
  - Add more filter styles (e.g., sketch, oil painting, pencil sketch)
  - Enable webcam integration
  - Deploy to Streamlit Cloud or Render
  - Add option to view and save all transformation stages
  - Optimize for mobile devices

