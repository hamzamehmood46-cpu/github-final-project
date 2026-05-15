"""Utilities for emotion detection using the Watson NLP service."""

from __future__ import annotations

import requests


EMOTION_URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
EMOTION_HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}


def _offline_emotion_scores(text_to_analyze: str) -> dict[str, str | float | None]:
    """Return deterministic fallback scores when the remote API is unavailable."""
    text = text_to_analyze.lower()
    emotions = {
        "anger": 0.0,
        "disgust": 0.0,
        "fear": 0.0,
        "joy": 0.0,
        "sadness": 0.0,
    }

    keyword_groups = {
        "joy": ["glad", "happy", "great", "good", "delighted", "joy"],
        "anger": ["mad", "angry", "furious", "annoyed", "rage"],
        "disgust": ["disgust", "disgusted", "gross", "awful", "revolting"],
        "sadness": ["sad", "upset", "depressed", "heartbroken", "unhappy"],
        "fear": ["afraid", "scared", "fear", "terrified", "worried"],
    }

    for emotion, keywords in keyword_groups.items():
        emotions[emotion] = float(
            sum(1 for keyword in keywords if keyword in text)
        )

    if max(emotions.values()) == 0:
        emotions["joy"] = 0.01

    dominant_emotion = max(emotions, key=emotions.get)
    emotions["dominant_emotion"] = dominant_emotion
    return emotions


def emotion_detector(text_to_analyze: str) -> dict[str, str | float | None]:
    """Analyze text and return emotion scores with the dominant emotion."""
    payload = {
        "raw_document": {
            "text": text_to_analyze,
        }
    }

    try:
        response = requests.post(
            EMOTION_URL,
            json=payload,
            headers=EMOTION_HEADERS,
            timeout=10,
        )
    except requests.RequestException:
        return _offline_emotion_scores(text_to_analyze)

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    formatted_response = response.json()
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion,
    }
