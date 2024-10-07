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
        'url': 'https://imgur.com/a/ZpD9st1',
        'week_number': datetime.now().isocalendar()[1]  # Номер поточного тижня
    },
    'week_1': {
        'url': 'https://imgur.com/a/IxAjtOc',
        'week_number': datetime.now().isocalendar()[1] + 1  # Тиждень 1
    },
    'week_2': {
        'url': 'https://imgur.com/a/ZpD9st1',
        'week_number': datetime.now().isocalendar()[1] + 2  # Тиждень 2
    },
    'week_3': {
        'url': 'https://imgur.com/a/qcie19e',
        'week_number': datetime.now().isocalendar()[1] + 3  # Тиждень 3
    },
    'week_4': {
        'url': 'https://imgur.com/a/2WgxENd',
        'week_number': datetime.now().isocalendar()[1] + 4  # Тиждень 4
    },
    'week_5': {
        'url': 'https://imgur.com/a/UIKp04q',
        'week_number': datetime.now().isocalendar()[1] + 5  # Тиждень 5
    },
    'week_6': {
        'url': 'https://imgur.com/a/YaN28Rz',
        'week_number': datetime.now().isocalendar()[1] + 6  # Тиждень 6
    },
    'week_7': {
        'url': 'https://imgur.com/a/iNY4mOX',
        'week_number': datetime.now().isocalendar()[1] + 7  # Тиждень 7
    },
    'week_8': {
        'url': 'https://imgur.com/a/rFNDOgi',
        'week_number': datetime.now().isocalendar()[1] + 8  # Тиждень 8
    },
    'week_9': {
        'url': 'https://imgur.com/a/lBUXqig',
        'week_number': datetime.now().isocalendar()[1] + 9  # Тиждень 8
    },
    'week_10': {
        'url': 'https://imgur.com/a/94roFmD',
        'week_number': datetime.now().isocalendar()[1] + 10  # Тиждень 8
    },
    'week_11': {
        'url': 'https://imgur.com/a/gpykloU',
        'week_number': datetime.now().isocalendar()[1] + 11  # Тиждень 8
    },
    'week_12': {
        'url': 'https://imgur.com/a/uCDDJ4l',
        'week_number': datetime.now().isocalendar()[1] + 12  # Тиждень 8
    },
    'week_13': {
        'url': 'https://imgur.com/a/mWFnmSv',
        'week_number': datetime.now().isocalendar()[1] + 13  # Тиждень 8
    },
    # Додай інші тижні за потреби
}

# Функція для створення меню
def create_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🗓 Поточний розклад", callback_data='this_week')],
        [InlineKeyboardButton("📅 Обрати інший тиждень", callback_data='choose_week')],
        [InlineKeyboardButton("🤣 Анекдот дня", callback_data='anekdot_day')],
        [InlineKeyboardButton("🍑 Тегнути Нікіту", callback_data='fanfik_day')],
        [InlineKeyboardButton("🧛 Тегнути Нестора", callback_data='polska_day')],
        [InlineKeyboardButton("⚙️ Написати свій промпт (В наступному оновленні)", callback_data='customize_anekdot')]
    ])

# Функція старту
async def start(update: Update, context):
    user = update.message.from_user  # Отримуємо інформацію про користувача
    username = user.username
    await update.message.reply_text(f'Вітаю, {username}! Ви використовуєте версію AnekdotGPT4 0.2', reply_markup=create_menu())

# Функція для отримання актуального розкладу
async def get_schedule(update: Update, context):
    photo_url = schedules['this_week']['url']
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
        if username == "zhdanovvvvvv":
            await query.message.reply_text(f"Привіт, {username}! Добрий день пане розробник, я молюся на вас:")
        elif username == "AkameGaNick":
            await query.message.reply_text(f"Привіт, {username}! Зайчик, доброе утро - Твоя Віка):")
        elif username == "ap3lsinus":
            await query.message.reply_text(f"Привіт, {username}! Головний VIPERR 1337:")
        elif username == "kotan_sheva":
            await query.message.reply_text(f"Привіт, {username}! Ельфбарчики по 10 евро, пишіть:")
        elif username == "h3llacious":
            await query.message.reply_text(f"Привіт, {username}! НЯ, КАвай, Нестор-сан, ващі шлюхи вже заспавнені:")
        elif username == "Rainf0rd":
            await query.message.reply_text(f"Привіт, {username}! Rainf0rd - задеанонілі:")

        await query.message.reply_photo(photo=photo_url, reply_markup=create_menu())

    elif query.data == 'choose_week':
        keyboard = [
            [InlineKeyboardButton("30/09", callback_data='week_1')],
            [InlineKeyboardButton("07/10", callback_data='week_2')],
            [InlineKeyboardButton("14/10", callback_data='week_3')],
            [InlineKeyboardButton("21/10", callback_data='week_4')],
            [InlineKeyboardButton("28/10 канікули", callback_data='week_5')],
            [InlineKeyboardButton("04/11", callback_data='week_6')],
            [InlineKeyboardButton("11/11", callback_data='week_7')],
            [InlineKeyboardButton("18/11", callback_data='week_8')],
            [InlineKeyboardButton("25/11", callback_data='week_9')],
            [InlineKeyboardButton("02/12", callback_data='week_10')],
            [InlineKeyboardButton("09/12", callback_data='week_11')],
            [InlineKeyboardButton("16/12", callback_data='week_12')],
            [InlineKeyboardButton("23/12 канікули", callback_data='week_13')],
            [InlineKeyboardButton("🔙 Назад до меню", callback_data='start')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Оберіть тиждень:", reply_markup=reply_markup)
    elif query.data == 'anekdot_day':
        await send_anekdot(update, context) 
    elif query.data == 'fanfik_day':
        await send_fanfik(update, context)
    elif query.data == 'polska_day':
        await send_polska(update, context)
    elif query.data.startswith('week_'):
        week_data = schedules.get(query.data)
        if week_data:
            photo_url = week_data['url']
            await query.message.reply_photo(photo=photo_url, reply_markup=create_menu())
        else:
            await query.message.reply_text("Цей тиждень недоступний.", reply_markup=create_menu())
    
    elif query.data == 'start':
        await start(update=query, context=context)  # Використовуємо query.message

# Основний блок програми
if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(send_schedule))
    application.add_handler(CommandHandler('get_schedule', get_schedule))
    application.add_handler(CommandHandler('send_anekdot',send_anekdot))
    application.add_handler(CommandHandler('send_fanfik',send_fanfik))
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
