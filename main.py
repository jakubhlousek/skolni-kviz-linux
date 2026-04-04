from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import requests
import random

app = FastAPI()

class Data(BaseModel):
    otazka: str
    odpoved: str
    spravna: str

OTAZKY = [
    {"otazka": "Jakým příkazem vypíšeš obsah aktuální složky?", "moznosti": ["cd", "pwd", "ls", "rm"], "spravna": "ls"},
    {"otazka": "Jak změníš aktuální složku o jednu úroveň výš?", "moznosti": ["cd /", "cd ..", "cd ~", "cd -"], "spravna": "cd .."},
    {"otazka": "Jakým příkazem zjistíš svou aktuální cestu (kde se nacházíš)?", "moznosti": ["path", "pwd", "dir", "here"], "spravna": "pwd"},
    {"otazka": "Jak vytvoříš novou složku?", "moznosti": ["mkdir", "newdir", "md", "create"], "spravna": "mkdir"},
    {"otazka": "Kterým příkazem zkopíruješ soubor?", "moznosti": ["mv", "copy", "cp", "duplicate"], "spravna": "cp"},
    {"otazka": "Jakým příkazem přesuneš nebo přejmenuješ soubor?", "moznosti": ["mv", "move", "ren", "cp"], "spravna": "mv"},
    {"otazka": "Jaký příkaz slouží k vyhledávání textu uvnitř souboru?", "moznosti": ["find", "search", "grep", "match"], "spravna": "grep"},
    {"otazka": "Jakým příkazem trvale smažeš soubor?", "moznosti": ["del", "remove", "rm", "erase"], "spravna": "rm"},
    {"otazka": "Jak smažeš složku včetně veškerého jejího obsahu?", "moznosti": ["rm -r", "rmdir", "del -a", "remove all"], "spravna": "rm -r"},
    {"otazka": "Jak spustíš příkaz s právy administrátora?", "moznosti": ["root", "admin", "sudo", "su"], "spravna": "sudo"},
    {"otazka": "Jakým příkazem změníš přístupová práva k souboru?", "moznosti": ["chown", "chmod", "perms", "attrib"], "spravna": "chmod"},
    {"otazka": "Jakým příkazem v Ubuntu nainstaluješ nový balíček?", "moznosti": ["apt install", "get-pack", "yum install", "pkg add"], "spravna": "apt install"},
    {"otazka": "Kterým příkazem si vypíšeš historii zadaných příkazů?", "moznosti": ["log", "past", "history", "cmd"], "spravna": "history"},
    {"otazka": "Jak vyčistíš obrazovku terminálu?", "moznosti": ["cls", "wipe", "clean", "clear"], "spravna": "clear"},
    {"otazka": "Jaký příkaz stáhne soubor z internetu přes URL?", "moznosti": ["wget", "download", "get", "fetch"], "spravna": "wget"},
    {"otazka": "Kterým příkazem vypíšeš posledních 10 řádků souboru?", "moznosti": ["end", "tail", "bottom", "last"], "spravna": "tail"},
    {"otazka": "Kterým příkazem vypíšeš běžící procesy a zátěž CPU v reálném čase?", "moznosti": ["top", "taskmgr", "ps", "proc"], "spravna": "top"},
    {"otazka": "Jak ukončíš proces podle jeho PID?", "moznosti": ["stop", "end", "kill", "terminate"], "spravna": "kill"},
    {"otazka": "Jakým příkazem ověříš spojení s jiným počítačem v síti?", "moznosti": ["netstat", "ping", "test", "connect"], "spravna": "ping"},
    {"otazka": "Kterým příkazem zabalíš složku do archivu typu .tar?", "moznosti": ["zip", "compress", "tar", "rar"], "spravna": "tar"},
    {"otazka": "Jak zjistíš volné místo na pevných discích?", "moznosti": ["du", "df -h", "diskfree", "storage"], "spravna": "df -h"},
    {"otazka": "Jakým příkazem zjistíš aktuální využití paměti RAM?", "moznosti": ["ram", "memory", "free", "sysinfo"], "spravna": "free"},
    {"otazka": "Jak zjistíš IP adresu svého síťového rozhraní?", "moznosti": ["ip a", "netstat", "ping", "route"], "spravna": "ip a"},
    {"otazka": "Kterým příkazem změníš vlastníka souboru?", "moznosti": ["chmod", "chown", "useradd", "usermod"], "spravna": "chown"},
    {"otazka": "Jak vypíšeš prvních 10 řádků textového souboru?", "moznosti": ["head", "start", "top", "begin"], "spravna": "head"},
    {"otazka": "Jakým příkazem restartuješ systém z terminálu?", "moznosti": ["reboot", "restart", "reload", "init 0"], "spravna": "reboot"},
    {"otazka": "Jak okamžitě vypneš počítač z terminálu?", "moznosti": ["halt", "shutdown now", "poweroff", "kill all"], "spravna": "shutdown now"},
    {"otazka": "Který příkaz vypíše uživatele, kteří jsou právě přihlášeni?", "moznosti": ["who", "users", "logins", "id"], "spravna": "who"},
    {"otazka": "Jakým příkazem zjistíš verzi jádra (kernelu) Linuxu?", "moznosti": ["kernel", "uname -r", "os-ver", "system"], "spravna": "uname -r"},
    {"otazka": "Jakým příkazem vyhledáš soubory podle názvu v celém systému?", "moznosti": ["search", "locate", "find", "grep"], "spravna": "find"},
    {"otazka": "Kterým příkazem vytvoříš prázdnou složku?", "moznosti": ["touch", "create", "new", "mkdir"], "spravna": "mkdir"},
    {"otazka": "Jak si zobrazíš nápovědu (manuál) k určitému příkazu?", "moznosti": ["help", "info", "man", "guide"], "spravna": "man"},
    {"otazka": "Jak vypíšeš obsah souboru přímo do terminálu (bez editoru)?", "moznosti": ["cat", "show", "print", "echo"], "spravna": "cat"},
    {"otazka": "Kterým příkazem zjistíš, pod jakým jménem jsi přihlášený?", "moznosti": ["whoami", "myid", "user", "name"], "spravna": "whoami"},
    {"otazka": "Jakým příkazem změníš heslo uživatele?", "moznosti": ["password", "passwd", "chpass", "key"], "spravna": "passwd"},
    {"otazka": "Jaký příkaz vypíše seznam všech připojených USB zařízení?", "moznosti": ["usb-list", "lsusb", "devices", "hwinfo"], "spravna": "lsusb"},
    {"otazka": "Jak zjistíš, kolik vteřin běží systém od posledního zapnutí?", "moznosti": ["runtime", "uptime", "time", "alive"], "spravna": "uptime"},
    {"otazka": "Jak vypíšeš kalendář na aktuální měsíc?", "moznosti": ["date", "month", "cal", "calendar"], "spravna": "cal"},
    {"otazka": "Jak vytvoříš symbolický odkaz (zástupce) na soubor?", "moznosti": ["ln -s", "link", "shortcut", "alias"], "spravna": "ln -s"},
    {"otazka": "Který příkaz slouží k aktualizaci seznamu balíčků v Ubuntu?", "moznosti": ["apt update", "apt upgrade", "apt fetch", "apt refresh"], "spravna": "apt update"},
    {"otazka": "Kterým příkazem provedeš upgrade všech nainstalovaných balíčků?", "moznosti": ["apt update", "apt upgrade", "apt install", "apt new"], "spravna": "apt upgrade"},
    {"otazka": "Jakým příkazem vypíšeš pouze unikátní (neopakující se) řádky ze souboru?", "moznosti": ["uniq", "single", "sort", "filter"], "spravna": "uniq"},
    {"otazka": "Jak zjistíš velikost konkrétní složky na disku?", "moznosti": ["df", "du -sh", "size", "measure"], "spravna": "du -sh"},
    {"otazka": "Jak vytvoříš nového uživatele v systému?", "moznosti": ["adduser", "newuser", "createuser", "mkuser"], "spravna": "adduser"},
    {"otazka": "Jakým příkazem seřadíš řádky v souboru podle abecedy?", "moznosti": ["order", "arrange", "sort", "align"], "spravna": "sort"},
    {"otazka": "Jak vypíšeš všechny běžící procesy (statický seznam)?", "moznosti": ["ps aux", "top", "htop", "procs"], "spravna": "ps aux"},
    {"otazka": "Jak zjistíš název svého počítače?", "moznosti": ["pcname", "hostname", "sysname", "device"], "spravna": "hostname"},
    {"otazka": "Jakým příkazem odstraníš prázdnou složku?", "moznosti": ["rm", "rmdir", "deldir", "erasedir"], "spravna": "rmdir"},
    {"otazka": "Jak zjistíš, který příkaz nebo program je spojený s daným slovem?", "moznosti": ["whereis", "find", "locate", "search"], "spravna": "whereis"},
    {"otazka": "Jak se odpojíš ze vzdáleného SSH serveru nebo zavřeš terminál?", "moznosti": ["close", "quit", "exit", "leave"], "spravna": "exit"}
]

@app.get("/")
def domov():
    with open("index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.get("/nova-otazka")
def get_otazka():
    q = random.choice(OTAZKY)
    zamichane = q["moznosti"].copy()
    random.shuffle(zamichane)
    return {
        "otazka": q["otazka"],
        "moznosti": zamichane,
        "spravna": q["spravna"]
    }

@app.post("/kontrola")
def kontrola(data: Data):
    if data.odpoved == "TIME_OUT":
        prompt = f"The student ran out of time on the question: '{data.otazka}'. The correct answer was '{data.spravna}'. Tell them to be faster next time and state what the command '{data.spravna}' does in English. Max 2 sentences."
    elif data.odpoved == data.spravna:
        prompt = f"The student correctly answered '{data.otazka}' with the command '{data.odpoved}'. Congratulate them in English as an IT mentor. Keep it to 1 short sentence."
    else:
        prompt = f"The student chose the WRONG command '{data.odpoved}' for the question: '{data.otazka}'. The CORRECT command is '{data.spravna}'. As an IT teacher, explain in English what '{data.odpoved}' actually does, and why '{data.spravna}' is the correct choice. Keep it short, max 3 sentences."
        
    try:
        res = requests.post("http://127.0.0.1:11434/api/generate", json={"model": "llama3.2:1b", "prompt": prompt, "stream": False})
        return {"hodnotenie": res.json()["response"].strip()}
    except:
        return {"hodnotenie": "Spojení s AI selhalo. Zkontroluj, zda běží Llama."}
