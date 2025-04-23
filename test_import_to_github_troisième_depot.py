import requests
import base64
import os
from dotenv import load_dotenv

# Charger les variables depuis le fichier .env
load_dotenv()

# Récupérer le token GitHub
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    print("⛔ ERREUR : Le token GITHUB_TOKEN n’est pas défini.")
    exit()

# Infos du repo (⚠️ Remplace avec ton nom d'utilisateur et ton dépôt)
OWNER = "Grego92"
REPO = "mon-premier-depot"
BRANCH = "main"
FILE_PATH = "test_import_to_github_troisième_depot.py"  # Nom du fichier à envoyer
LOCAL_FILE = "C:\\Users\\Administrateur\\Documents\\Mon-projet-github\\Script-test\\test_import_to_github_troisième_depot.py"

# Lire le contenu du fichier et l'encoder en Base64
with open(LOCAL_FILE, "rb") as file:
    content = base64.b64encode(file.read()).decode("utf-8")

# URL de l'API pour créer/modifier un fichier
url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{FILE_PATH}"

# Message de commit
data = {
    "message": "Ajout du fichier fichier test_import_to_github_deuxieme_depot.py",
    "content": content,
    "branch": BRANCH
}

# Headers avec l'authentification
headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}

# Envoyer la requête PUT à GitHub
response = requests.put(url, json=data, headers=headers)

# Vérifier la réponse
if response.status_code == 201:
    print("✅ Fichier ajouté avec succès !")
elif response.status_code == 200:
    print("⚠️ Fichier mis à jour !")
else:
    print(f"❌ Erreur {response.status_code} : {response.json()}")