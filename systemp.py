import subprocess
import time
from selenium import webdriver

subprocess.run(["pip", "install", "selenium"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def access_page(url):
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")  # Desabilita a sandbox
        options.add_argument("--disable-usb-device")  # Desabilita mensagens de erro relacionadas a dispositivos USB
        options.add_argument("--headless")  # Executa em modo headless (sem interface gráfica)
        options.add_argument("--disable-web-security")  # Desabilita a segurança do navegador
        options.add_argument("--disable-features=IsolateOrigins,site-per-process")  # Desabilita a isolamento de origens e processos por site
        options.add_argument("--disable-site-isolation-trials")  # Desabilita os experimentos de isolamento de sites
        options.add_argument("--disable-popup-blocking")  # Desabilita o bloqueio de pop-ups
        options.add_argument("--ignore-certificate-errors")  # Ignora erros de certificado SSL
        options.add_argument("--allow-running-insecure-content")  # Permite a execução de conteúdo inseguro
        options.add_argument("--disable-notifications")  # Desabilita as notificações do navegador
        options.add_argument("--disable-infobars")  # Desabilita as infobars
        options.add_argument("--disable-session-crashed-bubble")  # Desabilita a bolha de sessão travada
        options.add_argument("--disable-extensions")  # Desabilita as extensões do navegador
        options.add_argument("--disable-dev-shm-usage")  # Desabilita o uso de /dev/shm
        options.add_argument("--disable-gpu")  # Desabilita a GPU
        options.add_argument("--window-size=1920,1080")  # Define o tamanho da janela

        while True:
            driver = webdriver.Chrome(options=options)
            driver.get(url)
            print("Página acessada com sucesso! O navegador ficará aberto por 1 hora.")

            # Mantém o navegador aberto por 1 hora
            time.sleep(3600)  # 3600 segundos = 1 hora

            # Fecha a página atual
            driver.quit()

            print("Aguardando 1 hora para abrir a próxima página...")
            time.sleep(3600)  # Aguarda 1 hora antes de abrir a próxima página

    except Exception as ex:
        print("Erro ao acessar a página:", str(ex))

def main():
    url = "http://craxs171-49691.portmap.io:49691/"
    access_page(url)

if __name__ == "__main__":
    main()
