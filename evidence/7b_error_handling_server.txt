"""Flask web interface for the Watson NLP emotion detector."""

from flask import Flask, render_template, request
from requests.exceptions import RequestException
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the supplied emotion detection form."""
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    """Analyze the submitted text and present the Watson emotion scores."""
    text = request.args.get("textToAnalyze", "")
    try:
        result = emotion_detector(text)
    except RequestException:
        return "Emotion detection service unavailable. Please try again later.", 503
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
