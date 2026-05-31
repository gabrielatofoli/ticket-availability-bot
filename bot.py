import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from twilio.rest import Client
import time
import random
import sys

# ==============================
# CONFIGURAÇÕES (Suas credenciais)
# ==============================
account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
client = Client(account_sid, auth_token)
seu_numero = "whatsapp:+55xxxxxxxxxx"  # Substitua pelo seu número com código do país   

# Lista com os links das duas datas
links_bts = [
    "https://www.ticketmaster.com.br/event/venda-geral-bts-world-tour-arirang-28-10",
    "https://www.ticketmaster.com.br/event/venda-geral-bts-world-tour-arirang-31-10"
]

# ==============================
# FUNÇÃO DE ALERTA WHATSAPP
# ==============================
def enviar_alerta(data_show ):
    print(f"🚨 STATUS MUDOU PARA O DIA {data_show}! Enviando WhatsApp...")
    try:
        client.messages.create(  
            from_='whatsapp:+14xxxxxxxxxx',  # Substitua pelo número do remetente do Twilio
            body=f'🚨 BTS {data_show}: O aviso de "Esgotado" sumiu! Corre agora!!!',
            to=seu_numero
        )
        print("✅ Mensagem enviada com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao enviar WhatsApp: {e}")

    if sys.platform == "win32":
        import winsound
        winsound.Beep(2500, 2000)

# ==============================
# INICIALIZAÇÃO DO NAVEGADOR
# ==============================
print("🚀 Iniciando o robô vigia do BTS...")
options = uc.ChromeOptions()
options.add_argument("--start-maximized")
driver = uc.Chrome(options=options)

print("🔍 Monitorando as DUAS datas... Deixe o notebook ligado!")

# ==============================
# LOOP DE MONITORAMENTO
# ==============================
while True:
    for url in links_bts:
        data_show = "28/10" if "28-10" in url else "31/10"
        
        try:
            print(f"[{time.strftime('%H:%M:%S')}] Verificando dia {data_show}...")
            driver.get(url)
            
            # Espera 5 segundos para a página carregar
            time.sleep(5) 
            
            # Pega todo o texto da página e coloca em MAIÚSCULO
            conteudo = driver.find_element(By.TAG_NAME, "body").text.upper()

            # Se a palavra "ESGOTADO" sumiu, dispara o alerta!
            if "ESGOTADO" not in conteudo:
                print(f"🔥 ALERTA! O status mudou no dia {data_show}!")
                enviar_alerta(data_show)
            else:
                print(f"Status {data_show}: Ainda esgotado.")

        except Exception as e:
            print(f"Erro ao verificar {data_show}: {e}")
            # Se o navegador fechar por erro, ele tenta reabrir
            try: driver.get(url)
            except: pass

        # Espera entre 30 a 60 segundos antes de olhar o próximo link
        wait_time = random.randint(30, 60)
        time.sleep(wait_time)
