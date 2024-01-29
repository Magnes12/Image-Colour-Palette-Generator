from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/generate_palette", methods=['POST'])
def generate_palette():
    pass


if __name__ == "__main__":
    app.run(debug=True)
