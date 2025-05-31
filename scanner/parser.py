import json

def parse_log(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    # Простий парсинг: шукаємо ключові слова
    results = []
    for line in lines:
        if any(x in line for x in ['SubGHz', 'NFC', 'RFID']):
            results.append(line.strip())
    return results

def load_known_devices():
    with open('scanner/device_db.json', 'r') as f:
        return json.load(f)
