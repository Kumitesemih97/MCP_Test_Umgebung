# GPT-Neo Button Interaktionssystem

Dies ist eine Test Umgebung, die es ermöglicht mit einem lokal ausgeführten GPT-Neo-Modell verschiedene Buttons in einer HTML-Datei zu klicken.

## Voraussetzungen

- Python 3.x
- pip
- PyTorch
- Flask
- Transformers

## Installation

### 1. Repository klonen

Einfach das Repo klonen oder als ZIP-Datei downloaden:

### 2. GPT-Neo Modell herunterladen

Damit alles klappt, müsste das GPT-Neo 125M Modell lokal vorhanden sein.

Damit das alles automatisiert abläuft, stelle ich zusätzlich noch eine `download_gpt_neo_model.py` zur Verfügung.

Diese dann bitte vorher ausführen, um Funktionalität zu garantieren.

### 3. Server starten

Zuerst starten wir den GPT-Neo-Server über das Terminal (macOS) bzw. dem CMD (Windows):

```bash
python3 gpt-neo-server.py
```

Und dann den MCP-Server:

```bash
python3 mcp-server.py
```

**Hinweis**: Bitte zwei seperate Instanzen vom Terminal bzw. CMD verwenden.


### 4. HTML-Seite öffnen

Einfach mit einem Doppelklick die `index.html`-Datei öffnen.

## Wie es funktioniert

1. **Benutzereingabe**: Der User gibt einen Prompt in das Eingabefeld ein (z.B. „Klicke den roten Button“).
2. **MCP-Server**: Die Eingabe wird an den MCP-Server gesendet, der ihn an den GPT-Neo-Server weiterleitet.
3. **GPT-Neo-Modell**: Das Modell verarbeitet den Prompt und gibt die Aktion zurück (z.B. "roter Button").
4. **Frontend**: Die HTML-Seite ändert die Farbe des geklickten Buttons und gibt eine Bestätigung aus.

## FYI

- Bitte sicher stellen, dass sowohl der GPT-Neo- als auch der MCP-Server korrekt laufen.
- Wenn die Eingabe nicht erkannt wird, einfach überprüfen, ob der richtige Button im Prompt erwähnt wird.
