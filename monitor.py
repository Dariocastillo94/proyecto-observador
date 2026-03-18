# monitor.py
import requests
import time

URL = "http://localhost:8000/health"

def check_system():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            print(f"✅ SISTEMA OK: {response.json()}")
        else:
            print(f"⚠️ ALERTA: Código de estado {response.status_code}")
    except Exception as e:
        print("🚨 CRÍTICO: La aplicación está caída. Notificando al equipo...")

if __name__ == "__main__":
    while True:
        check_system()
        time.sleep(10) # Revisa cada 10 segundos