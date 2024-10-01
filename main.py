from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from datetime import datetime

# Токен бота
TOKEN = '7495078009:AAG9m37Qhx5rfC98RLuHLRcBq_IuBc_Ks1Q'


schedules = {
    'this_week': {
        'url': 'https://imgur.com/a/IxAjtOc',
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
        [InlineKeyboardButton("📅 Обрати інший тиждень", callback_data='choose_week')]
    ])

# Функція старту
async def start(update: Update, context):
    await update.message.reply_text(f'Вітаю, {username}! Ви використовуєте версію Deanon 0.0.1 Beta', reply_markup=create_menu())
    user = update.message.from_user  # Отримуємо інформацію про користувача
    username = user.username
    # if username == "zhdanovvvvvv":
    #     await update.message.reply_text(f"Привіт, {username}! У тебе є спеціальне повідомлення!")
    # else:
    #     await update.message.reply_text('Вітаю! Що вас цікавить?', reply_markup=create_menu())

# Функція для отримання актуального розкладуß
async def get_schedule(update: Update, context):
    photo_url = schedules['this_week']['url']
    await update.message.reply_photo(photo=photo_url, reply_markup=create_menu())

# Функція відправки розкладу
async def send_schedule(update: Update, context):
    query = update.callback_query
    user = query.from_user  # Отримуємо інформацію про користувача
    username = user.username
    await query.answer()

  if query.data == 'this_week':
    photo_url = schedules['this_week']['url']
    
    # Перевіряємо username і відправляємо відповідне повідомлення
    if username == "zhdanovvvvvv":
        await query.message.reply_text(f"Привіт, {username}! Добрий день пане розробник, я молюся на вас:")
    elif username == "AkameGaNick":
        await query.message.reply_text(f"Привіт, {username}! Зайчик, доброе утро - Твоя Віка):")
    elif username == "ap3lsinus":
        await query.message.reply_text(f"Привіт, {username}! Я ебучий задрот, насріть мені на грудь (Без негатива):")
    elif username == "kotan_sheva":
        await query.message.reply_text(f"Привіт, {username}! Ельфбарчики по 10 евро, пишіть:")
    elif username == "h3llacious":
        await query.message.reply_text(f"Привіт, {username}! НЯ, КАвай, Нестор-сан, ващі шлюхи вже заспавнені:")
    elif username == "Rainf0rd":
        await query.message.reply_text(f"Привіт, {username}! Rainf0rd - задеанонілі:")

    # Відправляємо фото незалежно від того, який username
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
            # Додай інші тижні за потреби
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Оберіть тиждень:", reply_markup=reply_markup)
    elif query.data.startswith('week_'):
        week_data = schedules.get(query.data)
        if week_data:
            photo_url = week_data['url']
            await query.message.reply_photo(photo=photo_url, reply_markup=create_menu())
        else:
            await query.message.reply_text("Цей тиждень недоступний.", reply_markup=create_menu())
    elif query.data == 'start':
        await start(update=query, context=context)  # Використовуємо query.message

# async def set_commands(application):
#     commands = [
#         BotCommand(command="start", description="Запустити бота"),
#         BotCommand(command="get_schedule", description="Отримати поточний розклад"),
#     ]
#     await application.bot.set_my_commands(commands)

# Основний блок програми
if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(send_schedule))
    application.add_handler(CommandHandler('get_schedule', get_schedule))
    # application.post_init(set_commands(application))
    application.run_polling()









