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

Gemini said
Here is the complete README.md in a single block so you can easily copy and paste it into your project.

Markdown
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
💡 Use Case Scenarios
Food Photography: Upload a cozy photo of a homemade soup. The system detects the mood and generates a warm caption with relevant food hashtags.

Travel Content: Upload a sunset beach photo. The platform detects a peaceful mood, generates an aesthetic caption, and provides platform-optimized travel hashtags.

Brand Content: Ensure your marketing copy fits perfectly within Twitter's strict 280-character limit without cutting off the primary message.

⚙️ Pre-requisites & Installation
Python 3.10+: Download from python.org

System Requirements: 4GB+ RAM for AI model inference

Internet Connection: For optional Gemini API usage

Setup Instructions:

Clone the repository and navigate into the project folder.

Install the required dependencies:

Bash
pip install -r requirements.txt
(Optional) Set up Google Gemini API for enhanced features:

Create a .env file in the root directory.

Add your API key: GEMINI_API_KEY=your_api_key_here

Run the Flask application:

Bash
python app.py
Open your browser and navigate to http://127.0.0.1:5000.

🔮 Future Enhancements
Support for video content analysis

Multi-language caption generation

A/B testing for caption variants

Social media analytics integration

Batch processing for multiple images

Direct posting to social media platform
