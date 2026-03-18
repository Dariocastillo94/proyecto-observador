# Resilient API & Monitoring System (Ops Project)

Este proyecto simula un entorno de producción donde la disponibilidad es crítica. 
No es solo una API, es un ecosistema de despliegue y vigilancia.

### 🚀 Tecnologías
* **Backend:** FastAPI (Python)
* **Infraestructura:** Docker & Docker Compose
* **CI/CD:** GitHub Actions (Validación automática)
* **Observabilidad:** Script de monitoreo con alertas vía Webhooks (Discord)

### 🛠️ Cómo ejecutarlo
1. `docker build -t mi-api-ops .`
2. `docker run -d -p 8000:8000 --name api-contenedor mi-api-ops`
3. `python monitor.py` (Configura tu WEBHOOK_URL primero)

### 📈 Conceptos de Operations Aplicados
* **Contenerización:** Aislamiento de dependencias y portabilidad.
* **Health Checks:** Endpoint específico para que los balanceadores de carga sepan el estado del servicio.
* **Alerting:** Notificaciones proactivas antes de que el usuario reporte el error.

### Como se vería el mensaje en Discord al tener una incidencia
<img width="473" height="448" alt="image" src="https://github.com/user-attachments/assets/d1e916cf-b735-4bd1-b225-a43e9f0c74b5" />
