import requests
import json

def fetch_top_models():
    url = "https://huggingface.co/api/models"
    response = requests.get(url)
    models = response.json()
    
    sorted_models = sorted(models, key=lambda x: x.get("downloads", 0), reverse=True)
    top_10_models = sorted_models[:10]
    
    return top_10_models

def generate_report():
    top_models = fetch_top_models()
    report = "Top 10 Hugging Face Models by Downloads:\n"
    for i, model in enumerate(top_models, 1):
        report += f"{i}. {model['modelId']} - {model.get('downloads', 0)} downloads\n"
    
    with open("/reports/top_10_models.txt", "w") as file:
        file.write(report)

if __name__ == "__main__":
    generate_report()
