
import os
from dotenv import find_dotenv, load_dotenv
import openai

load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")

system_content = "You are recalcitrant toddler who asks 'why' a lot."

message = [
        {"role": "system",
         "content": system_content
        }
    ]

while True:
    user_input = input("You: ")
    message.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message
    )

    asst_content = response.choices[0].message.content
    print(f"ToddlerBot: {asst_content}")
    message = [
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_input},
        {"role": "assistant", "content": asst_content}
    ]
