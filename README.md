# 🛡️ Escáner de Cabeceras de Seguridad HTTP

Herramienta en Python diseñada para auditar la postura de seguridad web mediante la inspección de cabeceras HTTP recomendadas por normativas estándar (OWASP).

---

## 🚀 Características
* **Auditoría Automática:** Analiza la presencia de cabeceras clave (`Strict-Transport-Security`, `X-Content-Type-Options`, `Content-Security-Policy`, entre otras).
* **Resiliencia & Timeout:** Control de tiempo de espera (10s) para evitar bloqueos si el servidor objetivo no responde o está caído.
* **Diagnóstico Directo:** Muestra el estado de cada norma e incluye recomendaciones de mitigación en caso de ausencia.

---

## 🛠️ Requisitos e Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/ovyri/verificador-cabeceras-seguridad.git](https://github.com/ovyri/verificador-cabeceras-seguridad.git)
   cd verificador-cabeceras-seguridad