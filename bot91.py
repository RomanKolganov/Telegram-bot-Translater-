
    # 18-46 закончил код

import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message             
from aiogram.filters.command import Command   

# Функция для транслитерации кириллицы на латиницу
def transliterate_name(text: str) -> str:
    translit_dict = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
        'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
        'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
        'Ф': 'F', 'Х': 'KH', 'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 
        'Ы': 'Y', 'Ъ': 'IE', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA'
    }
    
    result = ''
    for char in text:
        result += translit_dict.get(char.upper(), char)  # Переводим букву в верхний регистр, чтобы найти в словаре
    
    return result

# Создание и настройка бота
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)                        
dp = Dispatcher()                      
logging.basicConfig(level=logging.INFO)

@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}! Напиши что-нибудь на кириллице, я переведу это на латиницу.'

    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)
    
@dp.message()
async def transliterate_message(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    original_text = message.text 
    transliterated_text = transliterate_name(original_text)  # Применяем функцию транслитерации
    
    logging.info(f'{user_name} {user_id}: {original_text} -> {transliterated_text}')
    await message.answer(text=transliterated_text)

if __name__ == '__main__':
    dp.run_polling(bot)
