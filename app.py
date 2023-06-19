import json
from googletrans import Translator

def translate_text(text):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, src='en', dest='id')
    return translation.text

def translate_json_data(json_data):
    for item in json_data:
        annotations = item.get("annotations", [])
        for annotation in annotations:
            answer = annotation.get("answer", [])
            if isinstance(answer, list):
                translated_answer = []
                for text in answer:
                    translated_text = translate_text(text)
                    translated_answer.append(translated_text)
                annotation["answer"] = translated_answer

        question = item.get("question")
        if question:
            translated_question = translate_text(question)
            item["question"] = translated_question

    return json_data


# Load JSON data from file
with open('data.json', 'r') as json_file:
    json_data = json.load(json_file)

# Translate JSON data
translated_json_data = translate_json_data(json_data)

# Save translated JSON data to a new file
with open('translated_data.json', 'w') as json_file:
    json.dump(translated_json_data, json_file, ensure_ascii=False, indent=4)

