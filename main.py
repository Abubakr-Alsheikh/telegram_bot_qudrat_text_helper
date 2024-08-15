"""
Main file for the Telegram bot.

This file sets up the bot, loads the necessary handlers, and starts the bot polling for updates.
"""

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
)

from constants import (
    TOKEN,
    STATE_GENERAL_ADVICE,
    STATE_SOLUTION_STRATEGIES,
    STATE_SPECIFIC_ADVICE,
)
from handlers import (
    handle_start,
    handle_back_to_start,
    handle_main_menu,
    handle_general_advice,
    handle_general_advice_sheet,
    handle_general_advice_question,
    handle_solution_strategies,
    handle_solution_strategies_sheet,
    handle_solution_strategies_question,
    handle_solution_format,
    handle_specific_advice,
    handle_back,
)

# --- Callback Query Handlers Dictionary ---
callback_handlers = {
    "main_menu": handle_main_menu,
    "back_start": handle_back_to_start,
    STATE_GENERAL_ADVICE: handle_general_advice,
    r"^(?!back_)[a-zA-Z\d\s]+$": handle_general_advice_sheet,    # General advice sheet selection
    r"^ga_q_\d+_.+$": handle_general_advice_question,            # General advice question selection
    STATE_SOLUTION_STRATEGIES: handle_solution_strategies,
    r"^ss_sheet_.+$": handle_solution_strategies_sheet,          # Solution strategies sheet selection
    r"^ss_q_\d+_.+$": handle_solution_strategies_question,       # Solution strategies question selection
    r"^format_(video|audio|text|pdf)$": handle_solution_format,  # Solution format selection
    STATE_SPECIFIC_ADVICE: handle_specific_advice,
    r"^back_.+$": handle_back,                                   # Back button handler
}

# --- Main Function ---
def main() -> None:
    """Runs the Telegram bot."""
    application = Application.builder().token(TOKEN).build()

    # Command Handlers
    application.add_handler(CommandHandler("start", handle_start))

    # Callback Query Handlers (using the dictionary)
    for pattern, handler in callback_handlers.items():
        application.add_handler(CallbackQueryHandler(handler, pattern=pattern))

    application.run_polling()


if __name__ == "__main__":
    main()