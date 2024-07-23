import asyncio
import streamlit as st
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Load secrets from Streamlit's secrets management
TOKEN = st.secrets['orgiamidino']['TOKEN']
BOT_USERNAME = st.secrets['orgiamidino']['BOT_USERNAME']

# Define a simple command handler to reply with 'YES'
async def simple_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('YES')

# Main function to start the bot
async def start_bot():
    print('Starting bot...')

    # Create the application and set up handlers
    app = Application.builder().token(TOKEN).build()

    # Add handler for any text message to reply with 'YES'
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), simple_reply))

    # Initialize the application
    await app.initialize()

    # Start polling
    await app.start()
    await app.run_polling()

# Streamlit Interface
st.title("Simple Telegram Bot on Streamlit")
st.write("The bot is running. Interact with it on Telegram.")

# Ensure the bot is started only once
if 'bot_started' not in st.session_state:
    st.session_state['bot_started'] = True
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_bot())
