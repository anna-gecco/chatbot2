import os
from openai import OpenAI

# API-Key von Render kommt automatisch aus den Environment Variables
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Beispiel-FAQ (kannst du später erweitern oder aus Datei laden)
FAQ = {
    "Wie kann ich mein Passwort zurücksetzen?": "Du kannst dein Passwort über die 'Passwort vergessen'-Funktion zurücksetzen.",
    "Welche Zahlungsmethoden gibt es?": "Wir akzeptieren Kreditkarte, PayPal und Sofortüberweisung.",
    "Wie kontaktiere ich den Support?": "Du erreichst unseren Support per E-Mail an support@example.com.",
    "Wo finde ich meine Rechnungen?": "Deine Rechnungen findest du im Benutzerkonto unter 'Rechnungen'.",
    "Kann ich mein Abo kündigen?": "Ja, dein Abo kannst du jederzeit in den Kontoeinstellungen kündigen."
}

def search_faq(question: str):
    """FAQ-Suche (sehr einfache Version mit Keywords)"""
    for key, value in FAQ.items():
        if key.lower() in question.lower():
            return value
    return None

def get_ai_answer(question: str) -> str:
    """Wenn keine FAQ gefunden → KI-Antwort"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": question}],
        max_tokens=200
    )
    return response.choices[0].message.content.strip()

def chatbot_response(user_input: str) -> str:
    faq_answer = search_faq(user_input)
    if faq_answer:
        return faq_answer
    return get_ai_answer(user_input)