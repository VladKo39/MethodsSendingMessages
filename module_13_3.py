from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

''''''
key_file='key.txt'
#храню пароль
with open (key_file,'r',encoding='utf-8') as file:
    #чипаю пароль
      key_=str(file.read().strip())
api = key_

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_message(message):
     await message.answer(f'Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__== '__main__':
    executor.start_polling(dp,skip_updates=True)