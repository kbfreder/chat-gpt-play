
import os
from dotenv import find_dotenv, load_dotenv
import openai

load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system",
         "content": "You are recalcitrant toddler who asks 'why' a lot."
        },
        {"role": "user",
         "content": "What do you say we get ready for school, buddy?"
        }
    ]
)

print(response.choices[0].message.content)