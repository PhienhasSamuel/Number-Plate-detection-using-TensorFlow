import os
import cv2
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from ocr_utils import extract_text_from_image, translate_to_english

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Capture image from webcam
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        if not ret:
            return "Failed to capture image from webcam", 500

        # Save captured image
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"captured_{timestamp}.jpg"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        cv2.imwrite(filepath, frame)

        # OCR and translate
        original_text = extract_text_from_image(filepath)
        translated_text = translate_to_english(original_text)

        time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return render_template('index.html',
                               image_file=filename,
                               original_text=original_text,
                               translated_text=translated_text,
                               time=time_str)
    else:
        # GET request, just show the page without image or text
        return render_template('index.html',
                               image_file=None,
                               original_text=None,
                               translated_text=None,
                               time=None)

if __name__ == '__main__':
    app.run(debug=True)
