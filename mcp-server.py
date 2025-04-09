# Importiere die notwendigen Bibliotheken
from flask import Flask, request, jsonify  # Flask für Webserver und Anfragen
import requests  # Zum Senden von HTTP-Anfragen an den GPT-Neo-Server
from flask_cors import CORS  # Flask-CORS, um Cross-Origin Requests zu erlauben

# Erstelle eine Flask-App
app = Flask(__name__)

# Ermögliche Cross-Origin Resource Sharing (CORS) für alle Ursprünge
CORS(app)

# URL des GPT-Neo Flask Servers, auf dem das Modell läuft
GPT_NEO_SERVER_URL = "http://127.0.0.1:5002/generate"  # Dies ist die URL des GPT-Neo Servers

# Route für die POST-Anfrage vom Frontend
@app.route('/mcp_request', methods=['POST'])
def mcp_request():
    # Hole den 'prompt' aus der Anfrage, die der Benutzer gesendet hat
    prompt = request.form.get('prompt')

    # Wenn kein Prompt gesendet wurde, gib einen Fehler zurück
    if not prompt:
        return "Kein Prompt gesendet", 400  # HTTP Statuscode 400 bedeutet Bad Request

    # Leite die Anfrage an den GPT-Neo-Server weiter
    response = requests.post(GPT_NEO_SERVER_URL, data={'prompt': prompt})

    # Wenn der GPT-Neo-Server einen Fehler zurückgibt, gib einen Fehler aus
    if response.status_code != 200:
        return "Fehler beim GPT-Neo-Server", 500  # HTTP Statuscode 500 bedeutet Serverfehler

    # Extrahiere das Ergebnis aus der JSON-Antwort des GPT-Neo-Servers
    result = response.json().get('result', '')  # Hol dir das 'result' aus der Antwort

    # Analysiere den Text, um den Button zu finden, der basierend auf dem Prompt geklickt werden soll
    button_color = ""  # Standardwert, falls kein Button erwähnt wird
    if "roten Button" in result:
        button_color = "red"  # Der Benutzer möchte den roten Button klicken
    elif "blauen Button" in result:
        button_color = "blue"  # Der Benutzer möchte den blauen Button klicken
    elif "grünen Button" in result:
        button_color = "green"  # Der Benutzer möchte den grünen Button klicken
    elif "gelben Button" in result:
        button_color = "yellow"  # Der Benutzer möchte den gelben Button klicken
    
    # Gebe die Farbe des Buttons zurück, der geklickt werden soll, und das Ergebnis
    return jsonify({'button_color': button_color, 'response': result})

# Wenn das Skript direkt ausgeführt wird, starte den Server
if __name__ == "__main__":
    print("Starte MCP-Server...")  # Zeige eine Nachricht, dass der Server gestartet wird
    app.run(debug=True, host="0.0.0.0", port=5001)  # Starte den Flask-Server auf allen Netzwerkinterfaces, Port 5001