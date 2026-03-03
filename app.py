from flask import Flask, request, abort, send_from_directory
from handlers.text_analyzer import analyze_text
from flask_cors import CORS

app = Flask(__name__, static_folder="static")
CORS(app)


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    if "text" not in data:
        abort(422, description="Missing 'text' field")

    res = analyze_text(data["text"])

    return {
        "word_count": res["word_count"],
        "char_count_with_spaces": res["char_count_with_spaces"],
        "char_count_without_spaces": res["char_count_without_spaces"],
        "sentence_count": res["sentence_count"],
        "top_words": res["top_words"],
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
