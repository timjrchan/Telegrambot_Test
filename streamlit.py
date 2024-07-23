import asyncio
import streamlit as st
from telegram import Update 
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# secrets and credentials
TOKEN = st.secrets['orgiamidino']['TOKEN']
BOT_USERNAME = st.secrets['orgiamidino']['BOT_USERNAME']

# Define a simple command handler to reply with 'YES'
async def simple_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('YES')

# Main function to start the bot
def start_bot():
    print('Starting bot...')

    # Create the application and set up handlers
    app = Application.builder().token(TOKEN).build()

    # Add handler for any text message to reply with 'YES'
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), simple_reply))

    # Run the bot within the event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(app.initialize())
    loop.create_task(app.start_polling())
    return loop

# Streamlit Interface
st.title("Simple Telegram Bot on Streamlit")
st.write("The bot is running. Interact with it on Telegram.")

# Ensure the bot is started only once
if 'bot_started' not in st.session_state:
    st.session_state['bot_started'] = True
    loop = start_bot()
    st.session_state['bot_loop'] = loop