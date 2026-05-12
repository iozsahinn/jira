import requests
import json

# --- AYARLAR ---
JIRA_BASE_URL = "https://jira.sirketiniz.com" # Şirket Jira URL'si
JSON_FILE = "test_senaryolari.json"
PAT_TOKEN = "BURAYA_PAT_GİRİLECEK"

def upload_to_server_jira():
    url = f"{JIRA_BASE_URL}/rest/api/2/issue"
    
    # PAT Kullanımı için Header yapısı
    headers = {
        "Authorization": f"Bearer {PAT_TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    with open(JSON_FILE, "r", encoding="utf-8") as f:
        issues = json.load(f)

    for issue in issues:
        response = requests.post(url, json=issue, headers=headers, verify=False) 
        # Not: verify=False şirket içi SSL sertifikası hatası alırsanız kullanılır.
        
        if response.status_code == 201:
            print(f"Başarılı: {issue['fields']['summary']}")
        else:
            print(f"Hata ({response.status_code}): {response.text}")

# Çalıştır
upload_to_server_jira()
