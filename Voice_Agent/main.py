import asyncio

import speech_recognition as sr
from dotenv import load_dotenv
from openai import AsyncOpenAI, OpenAI
from openai.helpers import LocalAudioPlayer

load_dotenv()

client = OpenAI()

openai = AsyncOpenAI()

async def main():
    r = sr.Recognizer()

    SYSTEM_PROMPT = f"""
        You're an expert voice agent. You are given the transcript of
        what the user has spoken. You have to provide an output as if you're a voice agent
        replying to the user queries, whatever you output will be converted back into audio and played to user.
    """

    messages = []

    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            r.pause_threshold = 2

            print("Speak Something...")
            audio = r.listen(source)

            print("Processing Audio (STT)...")
            stt = r.recognize_google(audio)

            print("You said:", stt)

            messages.extend([
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": stt},
            ])

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=messages
            )

            result = response.choices[0].message.content
            print("AI Response:", result)

            messages.append(
                {"role": "assistant", "content": result}
            )

            async with openai.audio.speech.with_streaming_response.create(
                    model="gpt-4o-mini-tts",
                    voice="coral",
                    input=result,
                    instructions="Speak in a cheerful and positive tone.",
                    response_format="pcm",
                ) as response:
                    await LocalAudioPlayer().play(response)

if __name__ == "__main__":
    asyncio.run(main())
