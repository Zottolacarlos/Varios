import os
from dotenv import load_dotenv
import openai
import spacy #sirve para analiar texto

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

questions_asked = []
questions_answers = []

def ask_chatbot(prompt, model="text-davinci-003"):
    answer = openai.Completion.create(
        engine=model,
        prompt=prompt,
        n=1,
        max_tokens=150,
        temperature=2
    )
    return answer.choices[0].text.strip()

print("Welcome to a our Chatbot. Write 'EXIT' when you wants to finish")

while True:
    historical_conversation = ""
    enter_user = input("\nTú:")
    if enter_user.lower() == "exit":
        break

    for question, answer in zip(questions_asked, questions_answers):
        historical_conversation += f"El usuario pregunta: {question}\n"
        historical_conversation += f"Chatbot responde: {answer}\n"

    prompt = f"El usuario pregunta: {enter_user}\n"
    historical_conversation += prompt
    answer_gtp = ask_chatbot(historical_conversation)
    print(f"{answer_gtp}")

    questions_asked.append(enter_user)
    questions_answers.append(answer_gtp)