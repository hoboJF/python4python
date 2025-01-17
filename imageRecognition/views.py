from django.shortcuts import render
import ollama
from pathlib import Path

SYSTEM_PROMPT = """You are an image analysis assistant. Your job is to determine whether a python (snake) is present in the image or not. 
1. If the image contains any form of snake, such as a python, boa, anaconda, viper, or any other type of snake, respond ONLY with the word "Python." You can be creative with your response, such as identifying snake-related objects like stuffed animals, logos, or anything resembling a snake.
2. If the image does NOT contain any snakes (including pythons, boas, anacondas, vipers, or any snake at all), respond ONLY with the words "Not a python."
Your response should ONLY contain the appropriate word and nothing else."""

def index(request):
    project_root = Path(__file__).resolve().parent
    image_path = project_root / 'test2.jpg'
    response = llama_call(image_path)
    print(response)
    return render(request, 'imageRecognition/index.html')

def llama_call(image_path):
    response = ollama.chat(
        model = 'llama3.2-vision',
        messages=[{
            'role' : 'user',
            'content' : SYSTEM_PROMPT,
            'images' : [str(image_path)]
        }]
    )
    return response