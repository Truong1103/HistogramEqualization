from flask import Flask, render_template, request, jsonify
from PIL import Image
import cv2
import numpy as np
import base64

app = Flask(__name__)

# Hàm để cân bằng histogram
def equalize_histogram(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    equalized_image = cv2.equalizeHist(gray_image)
    return cv2.cvtColor(equalized_image, cv2.COLOR_GRAY2BGR)

# Hàm để tính histogram của ảnh Greyscale
def calculate_greyscale_histogram(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    hist = hist.flatten()
    return hist

# Hàm để tăng độ sáng
def increase_brightness(image, brightness=50):
    brightness_array = np.full_like(image, brightness, dtype=np.uint8)
    return cv2.add(image, brightness_array)

# Hàm để lấy ảnh gốc dưới dạng dữ liệu Base64
def get_image_base64(image):
    _, img_encoded = cv2.imencode('.png', cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    img_base64 = base64.b64encode(img_encoded).decode('utf-8')
    return img_base64

# Trang chính
@app.route('/')
def home():
    return render_template('index.html')

# Trang xử lý khi tải lên và biến đổi hình ảnh
@app.route('/process', methods=['POST'])
def process_image():
    uploaded_image = request.files['image']
    if not uploaded_image:
        return "Hãy chọn một hình ảnh."

    image = Image.open(uploaded_image)
    image_cv2 = np.array(image)

    # Cân bằng histogram và tăng độ sáng tự động
    processed_image = equalize_histogram(image_cv2)

    # Lấy giá trị độ sáng từ request
    increased_brightness_image = increase_brightness(processed_image, brightness=int(request.form['brightness']))

    # Chuyển các ảnh thành dạng dữ liệu Base64
    original_image_base64 = get_image_base64(image_cv2)
    processed_image_base64 = get_image_base64(processed_image)
    increased_brightness_image_base64 = get_image_base64(increased_brightness_image)

     # Tính histogram cho ảnh Greyscale và ảnh tăng độ sáng
    greyscale_histogram = calculate_greyscale_histogram(image_cv2)
    increased_brightness_histogram = calculate_greyscale_histogram(increased_brightness_image)

    # Chuyển histogram thành dạng JSON
    greyscale_histogram = greyscale_histogram.tolist()
    increased_brightness_histogram = increased_brightness_histogram.tolist()

    return jsonify({
        'original_image': original_image_base64,
        'processed_image': processed_image_base64,
        'increased_brightness_image': increased_brightness_image_base64,
        'greyscale_histogram': greyscale_histogram,
        'increased_brightness_histogram': increased_brightness_histogram
    })

if __name__ == '__main__':
    app.run(debug=True)
