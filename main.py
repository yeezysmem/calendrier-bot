from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ConversationHandler
from datetime import datetime
from g4f.client import Client
import g4f
import nest_asyncio
nest_asyncio.apply()
# g4f.disable_ssl_verification() 
# Токен бота
TOKEN = '7495078009:AAG9m37Qhx5rfC98RLuHLRcBq_IuBc_Ks1Q'
ASK_FOR_PROMPT = range(1)
client = Client()
schedules = {
    'this_week': {
        'url': 'https://imgur.com/a/Zw4O1Hw',
    },
    'next_week': {
        'url': 'https://imgur.com/a/PkSZfkc',
    },
    # Додай інші тижні за потреби
}

# Функція для створення меню
def create_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🗓 Поточний розклад", callback_data='this_week')],
        [InlineKeyboardButton("🗓 Наступний тиждень", callback_data='next_week')]
    ])

# Функція старту
async def start(update: Update, context):
    user = update.message.from_user  # Отримуємо інформацію про користувача
    username = user.username
    await update.message.reply_text(
        text="Оберіть одну з опцій нижче:",  # Add a welcome message
        reply_markup=create_menu()
    )

# Функція для отримання актуального розкладу
async def get_schedule(update: Update, context):
    photo_url = schedules['this_week']['url']
    await update.message.reply_photo(photo=photo_url, reply_markup=create_menu())

async def get_comingweek(update: Update, context):
    photo_url = schedules['next_week']['url']
    await update.message.reply_photo(photo=photo_url, reply_markup=create_menu())

# Функція для отримання анекдота
async def send_anekdot(update: Update, context):
    query = update.callback_query
    user = query.from_user  # Отримуємо інформацію про користувача
    username = user.username
    await query.answer()
    
    # Отримуємо анекдот через GPT API
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Придумай короткий жарт або анекдот, включаючи одного або кількох з таких персонажів не обовʼязково всіх персонажів у персонажів є опис використовуй його для анекдотів: Даня, Віка(яка закохана в Нікіту, вона психолог, обожнює відповідати так се бон, се бьян, се дроль бо вона вчить французьку), Діма(він дуже сатиричний 17 річний хлопчик), Нікіта(Він гей,який не ходить на навчання, постійно шукає відмазки), Нестор(він дуже спокійний завжди), і Ананас(його звати Анас, він араб і спілкується тільки арабською або французьскою мовою). Жарт має бути веселим і креативним, але не обов'язково всі персонажі повинні бути в кожному жарті, стеж за тим щоб анекдот був завершений і смішний."}],
    )
   # Перевіряємо, чи є відповідь і чи містить вона дані
    anekdot = response.choices[0].message.content 
    await query.message.reply_text(f"Анекдот для {username}:\n{anekdot}", reply_markup=create_menu())

# Функція для отримання анекдота
async def send_fanfik(update: Update, context):
    query = update.callback_query
    user = query.from_user  # Отримуємо інформацію про користувача
    username = user.username
    await query.answer()
    
    # Отримуємо анекдот через GPT API
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Нікіта захворів на рак ануса, напиши йому приємних слів щоб він одужав і побажай чогось від лиця анімешніци."}],
    )
   # Перевіряємо, чи є відповідь і чи містить вона дані
    fanfik = response.choices[0].message.content 
    await query.message.reply_text(f"Фанфік для @AkameGaNick :\n{fanfik}", reply_markup=create_menu())

async def send_polska(update: Update, context):
    query = update.callback_query
    user = query.from_user  # Отримуємо інформацію про користувача
    username = user.username
    await query.answer()
    
    # Отримуємо анекдот через GPT API
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Napisz Nestorowi coś miłego po polsku."}],
    )
   # Перевіряємо, чи є відповідь і чи містить вона дані
    polska = response.choices[0].message.content 
    await query.message.reply_text(f"цитата для @h3llacious :\n{polska}", reply_markup=create_menu())
# Функція для обробки кнопки "Налаштувати анекдот"
async def customize_anekdot(update: Update, context):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("Введіть свій запит для анекдота:")
    
    return ASK_FOR_PROMPT 

# Обробка введеного користувачем промпту
async def receive_prompt(update: Update, context):
    user = update.message.from_user
    prompt = update.message.text
    
    # Використовуємо введений промпт для створення анекдота
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
    )
    
    anekdot = response.choices[0].message.content
    await update.message.reply_text(f"Ваш анекдот:\n{anekdot}", reply_markup=create_menu())
    
    return ConversationHandler.END  # Завершуємо діалог
# Функція відправки розкладу
async def send_schedule(update: Update, context):
    query = update.callback_query
    user = query.from_user  # Отримуємо інформацію про користувача
    username = user.username
    await query.answer()

    if query.data == 'this_week':
        photo_url = schedules['this_week']['url']
        await query.message.reply_photo(photo=photo_url, reply_markup=create_menu())

    elif query.data == 'next_week':
        photo_url = schedules['next_week']['url']
        await query.message.reply_photo(photo=photo_url, reply_markup=create_menu())

    elif query.data == 'start':
        await start(update=query, context=context)  # Використовуємо query.message

# Основний блок програми
if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(send_schedule))
    application.add_handler(CommandHandler('get_schedule', get_schedule))
    application.add_handler(CommandHandler('get_comingweek', get_comingweek))
    # application.add_handler(CommandHandler('send_anekdot',send_anekdot))
    # application.add_handler(CommandHandler('send_fanfik',send_fanfik))
     # Обробник для налаштування анекдота через введений промпт
    # conv_handler = ConversationHandler(
    # entry_points=[CommandHandler('start', start)],
    # states={
    #     CHOOSING: [
    #         MessageHandler(Filters.text & ~Filters.command, choice),
    #         CallbackQueryHandler(choice_callback)
    #     ],
    # },
    # fallbacks=[CommandHandler('cancel', cancel)],
    # per_message=True 
    # )



    # application.add_handler(conv_handler)
    application.run_polling()
