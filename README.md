
# 🎂 Bot de Aniversários para Discord

Este é um bot desenvolvido com Python que envia mensagens automáticas no Discord para parabenizar usuários pelo aniversário. Os aniversários são registrados pelos próprios usuários e salvos em um arquivo JSON. O bot verifica diariamente se é aniversário de alguém e envia uma mensagem personalizada.

## 🚀 Funcionalidades

- 📅 Cadastro de aniversários com comando `.aniversario DD-MM-AAAA`
- 🔔 Envio automático de felicitações no dia do aniversário
- 💾 Armazenamento persistente em `birthdays.json`
- 🌎 Suporte a fuso horário brasileiro (America/Sao_Paulo)
- 🤖 Baseado em `discord.py` e `APScheduler`

## 🧠 Como funciona

1. O bot escuta o comando `.aniversario` para registrar a data de nascimento do usuário.
2. Os dados são armazenados no arquivo `birthdays.json`.
3. Todos os dias, à meia-noite (fuso de São Paulo), o bot verifica se alguém está fazendo aniversário.
4. Se houver, ele envia uma mensagem mencionando a pessoa e indicando sua idade atual.

## 💡 Funcionalidades futuras

- 🔍 Comando para consultar a data de aniversário de qualquer usuário
- ❌ Comando para excluir sua data de nascimento do sistema

## 🛠️ Requisitos

- Python 3.8+
- Um bot configurado no Discord com token
- As bibliotecas abaixo (instale com `pip install -r requirements.txt`):

```txt
discord.py
apscheduler
python-dotenv
pytz
```

## 📁 Estrutura dos arquivos

```
.
├── bot.py              # Código principal do bot
├── birthdays.json      # Arquivo que armazena os aniversários
├── .env                # Arquivo com o TOKEN do bot
```

## 📦 Como usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/discord-birthday-bot.git
   cd discord-birthday-bot
   ```

2. Crie um arquivo `.env` com seu token do Discord:
   ```env
   TOKEN=seu_token_do_bot
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o bot:
   ```bash
   python bot.py
   ```

5. No Discord, use:
   ```
   .aniversario 22-07-2000
   ```

## 📝 Exemplo de mensagem

> @everyone 🎉 Hoje é aniversário de @usuario! Está completando 20 anos! 🎂

## 📌 Observações

- O `channel_id` precisa ser atualizado com o ID do canal onde as mensagens devem ser enviadas.
- Apenas datas válidas no formato `DD-MM-AAAA` são aceitas.
- O bot deve estar com as permissões corretas para enviar mensagens e ler membros.
