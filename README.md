# Emotion Detector

This repository contains the final project for an AI-based web application
named Emotion Detector. The application uses the Watson NLP emotion prediction
service to analyze text and identify the dominant emotion in the given
statement.

## Project Features

- Detects `anger`, `disgust`, `fear`, `joy`, and `sadness`
- Returns the dominant emotion from the analyzed text
- Exposes the functionality through a Flask web interface
- Includes unit tests for the emotion detection logic
- Includes error handling for invalid or blank input
- Supports static code analysis with `pylint`

## Project Structure

- `EmotionDetection/` contains the emotion detection package
- `server.py` runs the Flask web application
- `test_emotion_detection.py` contains the unit tests
- `templates/` contains the HTML page for the web app
- `static/` contains the JavaScript used by the interface

## Run the Application

```bash
python server.py
```

Then open `http://127.0.0.1:5000/` in a browser.
