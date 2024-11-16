
import google.generativeai as genai
model = genai.Model(model="text-bison")
def chat():
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        response = model.generate_text(prompt=user_input, temperature=0.7)
        print("Bot:", response.text)
import google.generativeai as genai

def chat():
    model = genai.Model(model="text-bison")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        response = model.generate_text(prompt=user_input, temperature=0.7)
        print("Bot:", response.text)

if __name__ == "__main__":
    chat() 