import google.generativeai as genai

genai.configure(api_key ="AIzaSyDpO6vCSyfWTkIXRKyb7NV7gvcwtou8PS0")

for a in genai.list_models():
    print(a.name)