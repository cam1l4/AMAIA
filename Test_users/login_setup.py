from playwright.sync_api import sync_playwright

def save_auth_state(user_type):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Cambia a True si no necesitas ver la UI
        context = browser.new_context()  
        page = context.new_page()
        
        print(f"🔹 Iniciando sesión para: {user_type}")  # Debugging

        # 🔹 Determina credenciales según el usuario
        if user_type == "investor":
            username = "NasirXpro"
            password = "12345678"
            file_name = "auth_investor.json"

        elif user_type == "newUser":
            username = "camila"
            password = "Test123*"
            file_name = "auth_newUser.json"

        else:
            print(f"⚠ Usuario desconocido: {user_type}")
            return  # Sale si el usuario no está definido

        # 🔹 Navega a la página de login
        page.goto("https://app.amaia.io/login")

        # 🔹 Ingresa credenciales y hace login
        page.get_by_role("textbox", name="JohnDoe").fill(username)
        page.get_by_role("textbox", name="Enter your password").fill(password)
        page.get_by_role("textbox", name="Enter your password").click(timeout=2000)
        page.get_by_role("button", name="Login").click(timeout=3000)
        page.wait_for_timeout(3000)
        
        # 🔹 Espera a que el login sea exitoso
        page.wait_for_selector("text=Dashboard", timeout=15000)  # Ajusta según la UI

        # 🔹 Guarda el estado de autenticación en un archivo separado por usuario
        context.storage_state(path=file_name)
        print(f"✅ Estado de autenticación guardado en '{file_name}'")

        browser.close()

# 🔹 Ejecuta para múltiples usuarios
if __name__ == "__main__":
    usuarios = ["investor", "newUser"]  # Lista de usuarios
    for user in usuarios:
        print(f"🔄 Ejecutando login para: {user}")  # Debugging
        save_auth_state(user)