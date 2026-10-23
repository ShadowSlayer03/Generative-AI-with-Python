from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "which ducati bike is there in this image?"},
                {
                    "type": "input_image",
                    "image_url": "https://images.ctfassets.net/x7j9qwvpvr5s/4K6UfbNTM0JC14I1lRkDqW/b9190b47890450bfc63cc6856901f294/Supersport-950-overview-hero-1600x1000.jpg?fm=webp&q=90",
                },
            ],
        }
    ],
)

print(response.output_text)
