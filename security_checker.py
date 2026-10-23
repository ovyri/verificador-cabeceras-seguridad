import requests
from typing import Dict

def check_security_headers(url: str) -> None:
    print(f"\n[+] Analizando cabeceras de seguridad para: {url}")
    
    # Asegurar que la URL tenga esquema HTTP/HTTPS
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    try:
        # Realizamos la petición HTTP ignorando redirecciones si es necesario
        response = requests.get(url, timeout=10)
        headers = response.headers
        
        # Diccionario con las cabeceras críticas de seguridad a evaluar
        security_headers = {
            "Strict-Transport-Security": "HSTS (Fuerza conexiones HTTPS seguras)",
            "Content-Security-Policy": "CSP (Mitiga ataques de XSS e inyección de datos)",
            "X-Frame-Options": "Clickjacking (Evita que la web sea embebida en iframes maliciosos)",
            "X-Content-Type-Options": "MIME-sniffing (Evita la ejecución errónea de tipos de archivos)",
            "Server": "Información del servidor expuesta"
        }

        print("\n--- Resultados del Análisis ---")
        for header, description in security_headers.items():
            if header in headers:
                print(f"  [✓] {header}: Presente")
            else:
                print(f"  [✗] {header}: FALTA -> Recomendación: {description}")

    except requests.exceptions.RequestException as e:
        print(f"  [-] Error al conectar con la URL: {e}")

if __name__ == "__main__":
    print("=== Verificador de Cabeceras HTTP - Seguridad Web ===")
    target = input("Ingresa la URL a escanear (ej: example.com): ").strip()
    if target:
        check_security_headers(target)
    else:
        print("[-] Por favor, ingresa una URL válida.")