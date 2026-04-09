Školní Kvíz - Linux Master Class

Co projekt dělá
Jedná se o webovou aplikaci určenou pro testování znalostí linuxových příkazů. Obsahuje databázi 50 otázek, odpočet času a počítadlo aktuálního skóre. Hlavním prvkem je integrace umělé inteligence, která v reálném čase analyzuje chybné odpovědi studenta. Funguje jako virtuální učitel, který uživateli vysvětlí, proč udělal chybu a co daný příkaz skutečně provádí.

K čemu je určený
Projekt slouží jako výuková pomůcka pro studenty IT. Pomáhá k efektivnímu procvičování práce v Linuxu a slouží jako příprava k maturitní zkoušce.

Použité technologie

Backend: Python (FastAPI, Uvicorn, Requests)

Frontend: HTML, CSS, Vanilla JS

AI: Lokální LLM model Llama 3.2 (běžící přes Ollama)

Spuštění: Docker

Návod ke spuštění

Ujistěte se, že běží lokální API pro umělou inteligenci (Ollama).

V terminálu ve složce s projektem spusťte tento Docker příkaz:

Bash
docker run -d --name skolni-kviz --network host -v $(pwd):/app -w /app python:3.10-slim sh -c "pip install fastapi uvicorn requests && uvicorn main:app --host 0.0.0.0 --port 8000"
Aplikace bude dostupná v prohlížeči na adrese: http://localhost:8000

Základní příkazy pro správu

Zastavení aplikace: docker stop skolni-kviz

Opětovné spuštění: docker start skolni-kviz

Kontrola stavu: docker ps
