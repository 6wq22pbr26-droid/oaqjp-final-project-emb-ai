"""Initial raw-response stage of the emotion detector."""
import requests


def emotion_detector(text_to_analyze):
    """Return Watson's unmodified JSON response text."""
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    response = requests.post(
        url,
        headers={
            "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        },
        json={"raw_document": {"text": text_to_analyze}},
        timeout=30,
    )
    response.raise_for_status()
    return response.text
