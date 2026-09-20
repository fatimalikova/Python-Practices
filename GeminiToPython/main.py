import os
# pip install google-genai
from google import genai

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("Set the GEMINI_API_KEY environment variable before running.")

client = genai.Client(api_key=api_key)

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )

    print("Gemini:", response.text)