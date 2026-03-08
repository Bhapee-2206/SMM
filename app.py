from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import uuid

from utils.image_utils import analyze_image_mood
from services.caption_service import generate_caption
from services.hashtag_service import generate_hashtags
from utils.text_utils import limit_caption

app = Flask(__name__)

UPLOAD_FOLDER = "assets"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

PLATFORM_LIMITS = {
    "instagram": 2200,
    "twitter": 280,
    "linkedin": 3000
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({"error": "Invalid filename"}), 400

    platform = request.form.get("platform", "instagram")
    hashtag_count = int(request.form.get("hashtags", 5))
    ai_toggle = request.form.get("ai_toggle", "off")

    # safe filename
    ext = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)

    try:

        # 1️⃣ detect mood
        mood = analyze_image_mood(filepath)

        # 2️⃣ generate caption
        caption = generate_caption(mood)

        # 3️⃣ generate hashtags
        hashtags = generate_hashtags(mood)

        hashtag_list = hashtags.split()
        hashtags = " ".join(hashtag_list[:hashtag_count])

        # 4️⃣ combine text
        full_text = caption + " " + hashtags

        limit = PLATFORM_LIMITS.get(platform, 2200)

        limited_text = limit_caption(full_text, limit)

        char_count = len(limited_text)

        return jsonify({
            "mood": mood,
            "caption": caption,
            "hashtags": hashtags,
            "characters": char_count,
            "limit": limit,
            "image": filename
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


@app.route("/assets/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


if __name__ == "__main__":
    app.run(debug=True)