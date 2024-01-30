from flask import Flask, render_template, request
from PIL import Image
from colorthief import ColorThief
import os
import io


app = Flask(__name__)

temp_directory = 'temp'
os.makedirs(temp_directory, exist_ok=True)


@app.route("/")
def home():
    return render_template('index.html')


def generate_palette(file_path, num_colors=5):

    image = Image.open(file_path).convert('RGB')

    img_buffer = io.BytesIO()
    image.save(img_buffer, format='PNG')
    img_buffer.seek(0)

    color_thief = ColorThief(img_buffer)
    palette = color_thief.get_palette(color_count=num_colors)

    return palette


@app.route("/upload", methods=['POST'])
def upload():

    file = request.files['image-input']
    temp_path = os.path.join(temp_directory, file.filename)
    file.save(temp_path)

    palette = generate_palette(temp_path)
    os.remove(temp_path)
    return render_template('result.html', palette=palette)


if __name__ == "__main__":
    app.run(debug=True)
