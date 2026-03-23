# Social Mood Matcher 

**A SmartBridge Product - Let's Bridge the Gap**

Social Mood Matcher is an AI-powered social media content generation platform that delivers personalized, sentiment-aware captions and trending hashtags optimized for different platforms. Creating engaging social media content with appropriate captions and trending hashtags is time-consuming. This application transforms social media content creation into an intelligent, efficient process through smart mood detection and adaptive caption generation.

---

## 🚀 Key Features

* **Image Sentiment Detector:** Analyzes uploaded images to detect visual context and calculates average brightness and RGB values to classify the mood into categories like "happy and energetic," "sad and reflective," "excited and adventurous," or "calm and neutral."
* **Caption Generator:** Creates engaging captions based on the detected sentiment.
* **Hashtag Engine:** Recommends curated hashtags organized by category and sentiment, generating a focused set of relevant tags for each post.
* **Character Limiter:** Intelligently limits captions and hashtags to ensure content fits specific platform limits, including Twitter (280 characters), Instagram (2,200 characters), and LinkedIn (3,000 characters).
* **Gemini AI Layer (Optional):** Integration with Google Gemini 1.5 Flash for enhanced visual intelligence and superior caption quality.

---

## 🏗️ Architecture & Tech Stack

The platform integrates a modular Flask backend with a dynamic web frontend:

* **Frontend UI:** Custom HTML/CSS/JavaScript interface featuring an animated gradient background, drag-and-drop file upload, real-time character count tracking, and clipboard copying.
* **Backend Framework:** Flask (Python) handles image saving, routing, and integrates the individual processing services.
* **Image Processing:** Pillow (PIL) and NumPy for resizing and pixel-level color/brightness extraction.
* **Environment Management:** `python-dotenv` for managing secure API keys.

---

## 📂 Project Structure

```text
Social Mood Matcher/
├── assets/                    # Directory for temporarily storing uploaded images
├── services/
│   ├── caption_service.py     # Database of mood-specific captions and generation logic
│   └── hashtag_service.py     # Database of curated hashtags and generation logic
├── utils/
│   ├── image_utils.py         # Image resizing and NumPy-based mood detection
│   └── text_utils.py          # Smart text truncation for platform limits
├── templates/
│   └── index.html             # Main responsive web interface
├── .env                       # Environment variables (e.g., GEMINI_API_KEY)
├── app.py                     # Main Flask application and API routes
├── requirements.txt           # Python dependencies
└── settings.py                # Configuration for API keys and AI model selection
