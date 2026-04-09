Školní Kvíz: Linuxové příkazy
O čem to je
Udělal jsem webovou aplikaci na procvičování příkazů v Linuxu. Je tam databáze 50 otázek, které se náhodně generují, běží tam časový limit a počítá se skóre (včetně streaků za správné odpovědi za sebou). Hlavní věc je, že jsem tam zapojil umělou inteligenci, která funguje jako učitel – když dá někdo špatnou odpověď, AI mu hned vysvětlí, co ten jeho špatný příkaz vlastně dělá a proč tam nepatří.

Pro koho to je
Dělal jsem to jako pomůcku pro nás do školy, abychom se líp naučili na maturitu z operačních systémů a nemuseli si příkazy jen pamatovat, ale hned viděli souvislosti.

Technologie

Backend: Python (FastAPI). Vybral jsem ho, protože je jednoduchý na nastavení API a hodně rychlý.

Frontend: Čisté HTML, CSS a JavaScript (psal jsem to bez frameworků, aby to bylo lehké).

AI: Používám lokální model Llama 3.2 (1B verze), který běží přes Ollamu, takže data nejdou nikam na internet.

Nasazení: Projekt je v Dockeru pro snadné spuštění kdekoli.

Příkazy pro ovládání
Tady jsou příkazy, které se budou hodit v terminálu:

1. Přechod do složky s projektem:

Bash
cd ~/projekt
2. Zapnutí kvízu (vytvoření a spuštění kontejneru):

Bash
docker run -d --name skolni-kviz --network host -v $(pwd):/app -w /app python:3.10-slim sh -c "pip install fastapi uvicorn requests && uvicorn main:app --host 0.0.0.0 --port 8000"
Po spuštění stačí otevřít prohlížeč na adrese: http://localhost:8000

3. Kontrola běžících služeb:

Bash
docker ps
4. Vypnutí aplikace:

Bash
docker stop skolni-kviz
5. Smazání kontejneru (pro čistý restart):

Bash
docker rm skolni-kviz
6. Restartování AI modelu (pokud by neběžel):

Bash
ollama serve
# (v druhém okně terminálu:)
ollama run llama3.2:1b
