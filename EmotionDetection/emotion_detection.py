import requests, json

def emotion_detector(text_to_analyse):
    #URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    #Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    #Input json: { "raw_document": { "text": text_to_analyse } }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers = header)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)

    emotions = formatted_response['emotionPredictions'][0]['emotion']
   
    dominant_emotion = 'none'
    for emotion in emotions:
        if emotions.get(emotion) == max(emotions.values()):
            dominant_emotion = emotion
    
    return {
        'anger': emotions.get('anger'),
        'disgust': emotions.get('disgust'),
        'fear': emotions.get('fear'),
        'joy': emotions.get('joy'),
        'sadness': emotions.get('sadness'),
        'dominant_emotion': dominant_emotion
    }