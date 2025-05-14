# Telegram to Discord Webhook Bot

A simple and efficient Telegram bot that forwards your messages to a Discord channel using a webhook, instantly and with customization options.

### Features
- Instantly forwards messages from Telegram to Discord
- Easy-to-use interface with a button-based menu
- Fully customizable settings:
  - Webhook URL for Discord integration
  - Option to send messages as embeds
  - Custom embed color (`#RRGGBB`)
  - Sender’s name and avatar
- Ideal for bridging Telegram and Discord for quick communication, updates, or notifications.

### Why Use This?
This bot is perfect for:
- Instant message forwarding between Telegram and Discord.
- Real-time communication in Discord channels.
- Creating lightweight integrations or bridges for your community, team, or projects.

### Setup
1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/tg-ds-webhook-sender.git
   ```
   
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
   
3. Configure the bot by opening `config.py` and inserting your Telegram bot token:

   ```python
   BOT_TOKEN = "your_bot_token_here"
   ```
   
4. Run the bot:
 
   ```bash
   python main.py
   ```

### Files Overview

* **`main.py`**: The main entry point of the bot, handles bot initialization and event loops.
* **`config.py`**: Contains configuration variables, such as the bot token.
* **`handlers.py`**: Handles Telegram UI and interactions with the user.
* **`utils.py`**: Contains utility functions for sending messages to Discord and managing user data.

### License

This project is licensed under the **MIT License**.
