import requests
import time

# REEMPLAZA ESTO con la URL que copiaste de Discord
DISCORD_WEBHOOK_URL = "url de tu webhook"
URL_APP = "http://localhost:8000/health"

def enviar_alerta(mensaje):
    data = {"content": f"🚨 **ALERTA DE SISTEMA** 🚨\n{mensaje}"}
    try:
        requests.post(DISCORD_WEBHOOK_URL, json=data)
    except Exception as e:
        print(f"Error enviando a Discord: {e}")

def check_system():
    try:
        response = requests.get(URL_APP, timeout=3)
        if response.status_code == 200:
            print("✅ SISTEMA OK")
        else:
            msg = f"El servicio respondió con error {response.status_code}"
            print(f"⚠️ {msg}")
            enviar_alerta(msg)
    except Exception:
        msg = "La aplicación está totalmente CAÍDA (Down)"
        print(f"🚨 {msg}")
        enviar_alerta(msg)

if __name__ == "__main__":
    print("Iniciando monitor con alertas de Discord...")
    while True:
        check_system()
        time.sleep(10)