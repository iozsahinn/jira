import docx
import json
import re

def word_to_jira_json(docx_file):
    doc = docx.Document(docx_file)
    issues = []
    
    current_case = None
    
    # Varsayalım ki her Test Case "TC_" ile başlıyor
    for para in doc.paragraphs:
        text = para.text.strip()
        
        if text.startswith("TC_"):
            # Önceki case bitmişse listeye ekle
            if current_case:
                issues.append(current_case)
            
            # Yeni case başlat
            current_case = {
                "fields": {
                    "project": {"key": "PROJE_KODUN"}, # Burayı arkadaşın güncellemeli
                    "issuetype": {"name": "Test"},    # Veya "Task"
                    "summary": text,
                    "description": "" # Adımları buraya ekleyeceğiz
                }
            }
        elif current_case and text:
            # Başlık harici metinleri açıklama (description) kısmına ekle
            current_case["fields"]["description"] += text + "\n"

    # Son case'i de ekle
    if current_case:
        issues.append(current_case)

    # Dosyaya yaz
    output_name = docx_file.replace(".docx", ".json")
    with open(output_name, "w", encoding="utf-8") as f:
        json.dump(issues, f, ensure_ascii=False, indent=4)
    
    print(f"Bitti! {output_name} dosyası hazır.")

# Çalıştır
word_to_jira_json("test_senaryolari.docx")
