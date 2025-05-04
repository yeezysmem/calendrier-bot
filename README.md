# Telegram Bot with ChatGPT and Schedule Features

This is a Python-based Telegram bot that integrates the Telegram API and the OpenAI ChatGPT API. The bot has two main functionalities:

1. **Show Current Schedule**: Retrieves and displays the current schedule stored in the database.
2. **Create a Joke with Participants**: Generates a custom joke involving participants using the ChatGPT API.

## Requirements

* Python 3.8+
* `python-telegram-bot` for interacting with the Telegram API
* `openai` for ChatGPT integration
* A database (e.g., SQLite, PostgreSQL) to store schedules
* Telegram Bot Token (from [BotFather](https://core.telegram.org/bots#botfather))
* OpenAI API Key (from [OpenAI](https://platform.openai.com/))

## Setup

### 1. Install Dependencies

To get started, first install the required dependencies:

```bash
pip install python-telegram-bot openai
```

### 2. Set Up API Keys

* Get your **Telegram Bot Token** from BotFather.
* Obtain your **OpenAI API Key** from OpenAI.

Set up the keys in your project either as environment variables or in the configuration file.

```bash
export TELEGRAM_BOT_TOKEN="your_telegram_bot_token"
export OPENAI_API_KEY="your_openai_api_key"
```

### 3. Database Setup

Ensure you have a database to store the schedule data. The bot will fetch the current schedule from the database when requested by the user.

### 4. Running the Bot

After configuring your bot and the API keys, you can run the bot with the following command:

```bash
python bot.py
```

The bot will start listening for messages on Telegram.

## Features

### Show Current Schedule

To view the current schedule, simply type the `/schedule` command in the bot chat. The bot will respond with the schedule fetched from the database.

### Create a Joke with Participants

The bot allows users to create a personalized joke involving participants. To generate a joke, type the `/joke [participant1] [participant2] ...` command. The bot will use the ChatGPT API to generate a funny story or joke with the participants' names.

Example:

```
/joke Alice Bob Charlie
```

The bot will respond with a custom joke that includes Alice, Bob, and Charlie.

## Contributing

Feel free to fork this repository and submit issues or pull requests for improvements and bug fixes.

## License

This project is open-source and available under the [MIT License](LICENSE).

