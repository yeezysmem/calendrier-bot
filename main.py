from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ConversationHandler
from datetime import datetime
from g4f.client import Client
import g4f
import nest_asyncio
import os

nest_asyncio.apply()

TOKEN = os.environ["SECRET_TOKEN"]
ASK_FOR_PROMPT = range(1)
client = Client()
schedules = {
    'this_week': {
        'url': 'https://imgur.com/a/7vWOosw',
    },
    'next_week': {
        'url': 'https://imgur.com/a/sPFpRNu',
    },
}

def create_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🗓 Current schedule", callback_data='this_week')],
        [InlineKeyboardButton("🗓 Next week", callback_data='next_week')]
    ])

async def start(update: Update, context):
    user = update.message.from_user
    username = user.username
    await update.message.reply_text(
        text="Choose one of the options below:",
        reply_markup=create_menu()
    )

async def get_schedule(update: Update, context):
    photo_url = schedules['this_week']['url']
    await update.message.reply_photo(photo=photo_url, reply_markup=create_menu())

async def get_comingweek(update: Update, context):
    photo_url = schedules['next_week']['url']
    await update.message.reply_photo(photo=photo_url, reply_markup=create_menu())

async def send_anekdot(update: Update, context):
    query = update.callback_query
    user = query.from_user
    username = user.username
    await query.answer()
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Make up a short joke or anecdote including one or more of the following characters, not necessarily all of them, but use them for anecdotes: Danya, Vika (who is in love with Nikita, she is a psychologist, she loves to answer like “se bon, se bien, se drolle” because she is learning French), Dima (he is a very satirical 17-year-old boy), Nikita (he is gay, he doesn't go to school, he is always looking for excuses), Nestor (he is very calm always), and Ananas (his name is Ananas, he is an Arab and he only speaks Arabic or French). The joke should be funny and creative, but not all characters should be in every joke, make sure that the joke is complete and funny."}],
    )
    anekdot = response.choices[0].message.content 
    await query.message.reply_text(f"Анекдот для {username}:\n{anekdot}", reply_markup=create_menu())

async def send_fanfik(update: Update, context):
    query = update.callback_query
    user = query.from_user
    username = user.username
    await query.answer()
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "create a fanfik."}],
    )
    fanfik = response.choices[0].message.content 
    await query.message.reply_text(f"Fanfik for @AkameGaNick :\n{fanfik}", reply_markup=create_menu())

async def send_polska(update: Update, context):
    query = update.callback_query
    user = query.from_user
    username = user.username
    await query.answer()
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Napisz Nestorowi coś miłego po polsku."}],
    )
    polska = response.choices[0].message.content 
    await query.message.reply_text(f"цитата для @h3llacious :\n{polska}", reply_markup=create_menu())

async def customize_anekdot(update: Update, context):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("Input your own prompt:")
    return ASK_FOR_PROMPT 

async def receive_prompt(update: Update, context):
    user = update.message.from_user
    prompt = update.message.text
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
    )
    
    anekdot = response.choices[0].message.content
    await update.message.reply_text(f"Your joke:\n{anekdot}", reply_markup=create_menu())
    return ConversationHandler.END

async def send_schedule(update: Update, context):
    query = update.callback_query
    user = query.from_user
    username = user.username
    await query.answer()

    if query.data == 'this_week':
        photo_url = schedules['this_week']['url']
        await query.message.reply_photo(photo=photo_url, reply_markup=create_menu())

    elif query.data == 'next_week':
        photo_url = schedules['next_week']['url']
        await query.message.reply_photo(photo=photo_url, reply_markup=create_menu())

    elif query.data == 'start':
        await start(update=query, context=context)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(send_schedule))
    application.add_handler(CommandHandler('get_schedule', get_schedule))
    application.add_handler(CommandHandler('get_comingweek', get_comingweek))
    application.add_handler(CommandHandler('send_anekdot', send_anekdot))
    application.run_polling()