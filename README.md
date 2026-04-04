# 🎓 Školní Kvíz - Linux Master Class

## 📖 Co projekt dělá
Jedná se o interaktivní e-learningovou webovou aplikaci pro testování znalostí linuxových příkazů. Obsahuje 50 otázek, odpočet času a počítadlo skóre. Hlavní inovací je integrace umělé inteligence, která v reálném čase analyzuje chybné odpovědi studenta a jako virtuální učitel mu vysvětluje, proč udělal chybu.

## 🎯 K čemu je určený
Projekt slouží jako výuková pomůcka pro studenty IT k efektivnímu procvičování práce v Linuxu a k přípravě na maturitu.

## 🛠️ Použité technologie
* **Backend:** Python (FastAPI, Uvicorn, Requests)
* **Frontend:** HTML, CSS, Vanilla JS
* **AI:** Lokální LLM model Llama 3.2 (Ollama)
* **Spuštění:** Docker

## 🚀 Návod ke spuštění
1. Musí běžet lokální API umělé inteligence (Ollama).
2. Ve složce s projektem spusťte tento Docker příkaz:
`docker run -d --name skolni-kviz --network host -v $(pwd):/app -w /app python:3.10-slim sh -c "pip install fastapi uvicorn requests && uvicorn main:app --host 0.0.0.0 --port 8000"`
3. Web poběží na `http://localhost:8000`
