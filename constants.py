"""
Defines constants used in the bot.

This file stores constants like:
- Bot link.
- Bot token.
- Excel file paths.
- State names for user interactions.
"""

BOT_LINK = "https://t.me/QudratTestHelperBot"
TOKEN = open("token.txt", "r").readline()
GENERAL_ADVICE_FILE = "51.xlsx"
SOLUTION_STRATEGIES_FILE = "52.xlsx"

# --- State Constants ---
STATE_START = "start"
STATE_MAIN_MENU = "main_menu"
STATE_GENERAL_ADVICE = "general_advice"
STATE_SOLUTION_STRATEGIES = "solution_strategies"
STATE_SPECIFIC_ADVICE = "specific_advice"
