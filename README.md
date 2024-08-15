# Telegram Qudrat Test Helper Bot

This is a Telegram bot designed to help users prepare for the Qudrat Test. It provides general advice, solution strategies, and access to resources like videos, audio recordings, text documents, and PDFs.

## Features

* **General Advice:** Offers general tips and advice on different aspects of the Qudrat Test.
* **Solution Strategies:** Provides specific strategies for solving different types of questions.
* **Resource Access:** Allows users to access relevant videos, audio recordings, text documents, and PDFs.
* **User-Friendly Navigation:** Features a simple menu-based navigation system with back buttons.

## How to Use

1. Add the bot to your Telegram: [Bot Link](BOT_LINK) (Replace `BOT_LINK` with the actual link to your bot)
2. Start the bot by sending the `/start` command.
3. Follow the on-screen instructions to navigate through the menus and access the information you need.

## File Structure

* **`main.py`:** Main file that sets up the bot and handles user interactions.
* **`excel_handler.py`:** Contains the `ExcelHandler` class for interacting with Excel files.
* **`general_advice_model.py`:** Defines the `GeneralAdviceModel` for handling general advice data.
* **`solution_strategies_model.py`:** Defines the `SolutionStrategiesModel` for handling solution strategies data.
* **`handlers.py`:** Contains the handler functions for different bot commands and callbacks.
* **`keyboards.py`:** Defines the functions for creating inline keyboards.
* **`constants.py`:** Stores constants used throughout the project.

## Dependencies

* **Python Telegram Bot:** `pip install python-telegram-bot`
* **openpyxl:** `pip install openpyxl`

## Configuration

1. Create a `token.txt` file in the same directory as the other files and paste your bot token inside it.
2. Make sure the Excel files (`51.xlsx` and `52.xlsx`) are in the same directory and contain the necessary data in the correct format.
