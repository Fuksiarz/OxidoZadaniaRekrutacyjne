
import os
from openai import OpenAI
from dotenv import load_dotenv

#load variables
load_dotenv()

def generate_html_from_article(article_content):
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key = OPENAI_API_KEY)
    
    #adding instructions
    prompt = f"""
Poniżej znajduje się artykuł. Przetwórz treść i zwróć ją w formacie HTML z odpowiednią strukturą.
- Użyj odpowiednich znaczników HTML do organizacji treści.
- Niech znaczniki nagłówków będą w jednej koncepcji, preferowany to h2.
- Zidentyfikuj odpowiednie miejsca, w których obrazy wzbogacą artykuł, i umieść tam znaczniki <img>.
- Myślę, że zdjęcie poniżej nagłówków przedstawiających wizualizację treści do kolejnego nagłówka będzie odpowiednim miejscem ale zdecyduj co będzie lepsze.
- Użyj znacznika <img> z src="image_placeholder.jpg" i dodaj atrybut alt z opisem obrazu. Tekst alt powinien być jasnym opisem koncepcji obrazu, który odpowiada kontekstowi artykułu.
- Dodaj podpisy pod obrazami, używając odpowiednich znaczników HTML, takich jak <figcaption>.
- chciałbym aby figcaption i img były zamknięte w tagach figure.
- Nie dołączaj kodu CSS ani JavaScript, wyłącznie treść do umieszczenia pomiędzy znacznikami <body> i </body>.
- nie dodawaj znaczników <html>, <body>, <head>. 
- zamknij cały artykuł w znacznikach <div>.
Artykuł:
{article_content}
"""

    # configuring chatbot model
    completion = client.chat.completions.create(
        model="gpt-4",  
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return completion.choices[0].message.content

def main():
    # Read article content from file
    with open("trescArtykulu.txt", "r", encoding="utf-8") as file:
        content = file.read()

    # Get HTML from OpenAI
    html_content = generate_html_from_article(content)
    
    # Save the resulting HTML to a file
    with open("artykul.html", "w", encoding="utf-8") as html_file:
        html_file.write(html_content)
    print("HTML content saved to artykul.html")

if __name__ == "__main__":
    main()