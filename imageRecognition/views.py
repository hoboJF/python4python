from django.shortcuts import render
import ollama
import os
from pathlib import Path

def index(request):
    project_root = Path(__file__).resolve().parent
    image_path = project_root / 'test.jpg'
    response = ollama.chat(
        model = 'llama3.2-vision',
        messages=[{
            'role' : 'user',
            'content' : 'What is in this image?',
            'images' : [str(image_path)]
        }]
    )
    print(response)
    return render(request, 'imageRecognition/index.html')