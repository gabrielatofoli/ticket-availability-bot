# 🎫 Ticket Monitor Bot | Bot Monitor de Ingressos

## 🇺🇸 English

Ticket Monitor Bot is a Python automation project created to monitor ticket availability on Ticketmaster event pages.

The bot periodically checks selected event pages and detects when the "SOLD OUT" status is no longer displayed. When a change is detected, it automatically sends a WhatsApp notification using the Twilio API.

### Features

- Automated ticket availability monitoring
- Support for multiple event dates
- Detection of status changes on the page
- WhatsApp notifications using Twilio API
- Randomized checking intervals
- Automated browser navigation with Selenium

### Technologies

- Python
- Selenium
- Undetected ChromeDriver
- Twilio API
- WhatsApp Sandbox
- Python Dotenv

### Validation

Since tickets were unavailable during development, the bot was validated by simulating the removal of the "SOLD OUT" text through browser developer tools. The test successfully triggered the WhatsApp notification, confirming that the monitoring logic works as expected.

---

## 🇧🇷 Português

O Ticket Monitor Bot é um projeto de automação desenvolvido em Python para monitorar a disponibilidade de ingressos em páginas de eventos da Ticketmaster.

O sistema verifica periodicamente as páginas monitoradas e identifica quando o aviso de "ESGOTADO" deixa de aparecer. Quando essa alteração é detectada, uma mensagem é enviada automaticamente pelo WhatsApp utilizando a API do Twilio.

### Funcionalidades

- Monitoramento automático de disponibilidade de ingressos
- Suporte para múltiplas datas de evento
- Detecção de mudança de status na página
- Notificações via WhatsApp utilizando a API do Twilio
- Intervalos aleatórios entre verificações
- Navegação automatizada com Selenium

### Tecnologias Utilizadas

- Python
- Selenium
- Undetected ChromeDriver
- Twilio API
- WhatsApp Sandbox
- Python Dotenv

### Validação

Como não havia ingressos disponíveis durante o desenvolvimento, a validação foi realizada simulando a remoção do texto "ESGOTADO" através das ferramentas de desenvolvedor do navegador. O teste acionou corretamente a notificação via WhatsApp, confirmando o funcionamento da lógica de monitoramento.


---

## How to run | Como executar'

1. Clone the repository:

```bash
git clone https://github.com/your-username/ticket-monitor-bot.git