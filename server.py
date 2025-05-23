from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"
    
    return f"""For the given statement, the system response is 'anger': {response.get('anger')},\
    'disgust': {response.get('disgust')}, 'fear': {response.get('fear')},\
    'joy': {response.get('joy')}, and 'sadness': {response.get('sadness')}.\
    The dominant emotion is {response.get('dominant_emotion')}."""

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000)