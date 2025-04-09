# Importiere die notwendigen Bibliotheken
from flask import Flask, request, jsonify  # Flask für Webserver und Anfragen
from transformers import AutoTokenizer, AutoModelForCausalLM  # Transformers für GPT-Neo-Modell

# Erstelle eine Flask-App
app = Flask(__name__)

# Lade das GPT-Neo-Modell und den zugehörigen Tokenizer von Hugging Face
# Hier verwenden wir das kleinere Modell (125M) von GPT-Neo
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-125M")
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-125M")

# Route für die POST-Anfrage, um Text mit GPT-Neo zu generieren
@app.route('/generate', methods=['POST'])
def generate():
    # Hole den 'prompt' aus den Formulardaten der Anfrage
    prompt = request.form.get('prompt')

    # Wenn kein Prompt gesendet wurde, gib einen Fehler zurück
    if not prompt:
        return jsonify({"error": "Kein Prompt gesendet"}), 400  # HTTP Statuscode 400 bedeutet Bad Request

    # Tokenisiere den Eingabetext (Prompt)
    # Der Tokenizer wandelt den Text in ein Format um, das das Modell verstehen kann
    inputs = tokenizer(prompt, return_tensors="pt")

    # Generiere Text mit dem GPT-Neo-Modell
    # max_length gibt die maximale Länge des generierten Textes an (hier 150 Zeichen)
    outputs = model.generate(**inputs, max_length=150)

    # Dekodiere den generierten Text zurück in lesbaren Text
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Gib den generierten Text als JSON zurück
    return jsonify({"result": generated_text})

# Wenn das Skript direkt ausgeführt wird, starte den Server
if __name__ == '__main__':
    # Starte die Flask-App und setze den Host und Port
    app.run(debug=True, host="0.0.0.0", port=5002)  # Starte den Server auf Port 5002