from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY non définie dans .env")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "llama-3.3-70b-versatile"

def zero_shot_classification(email : str) -> str:
    prompt = f"""
    Classify the following email into one of the following categories: "Work", "Personal", "Spam","Sport" "Other". 
    Email: {email}
    Category:

    mails can be in french or english.
    """
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=10,
        temperature=0.0,
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":    
    while True:
        print("\nEntrez un email à classifier (ou 'exit' pour quitter):")
        user_email = input("> ").strip()
        
        if user_email.lower() == 'exit':
            print("Au revoir!")
            break
        
        if not user_email:
            print("Veuillez entrer un email valide.")
            continue
        
        print("\nClassification en cours...")
        category = zero_shot_classification(user_email)
        print(f"\nEmail: {user_email}")
        print(f"Catégorie: {category}")
        print("-" * 60)
        print(f"Category: {category}\n")