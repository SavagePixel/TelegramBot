import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import curse

logging.basicConfig(level=logging.INFO)

# Для сервера
#proxy_url = "http://proxy.server:3128"
#bot = Bot(token="6232512304:AAGrLPlyv_5mCDGQ39BDZV3Y6_WAVEf_7Eg", proxy=proxy_url)

# локальный запуск
bot = Bot(token="6232512304:AAGrLPlyv_5mCDGQ39BDZV3Y6_WAVEf_7Eg")

dp = Dispatcher(bot)

HelpButton = KeyboardButton("Помощь")
CurseButton = KeyboardButton("Курс криптовалют")
InfoButton = KeyboardButton("О боте")
AuthorButton = KeyboardButton("Авторы")

greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
greet_kb.add(HelpButton, CurseButton, InfoButton, AuthorButton)


@dp.message_handler(Command("start"))
async def start(message: types.Message):
  await message.answer("Привет, я бот помощник в мире криптовалюты",
                       reply_markup=greet_kb)


@dp.message_handler(content_types='text')
async def MainButton(message: types.Message):
  if message.text == "Авторы":
    await message.reply("Создатель: @hkkk89", reply_markup=greet_kb)

  elif message.text == "Курс криптовалют":

    with open("CoinData.txt", "r") as file:
      src = file.read()
      await message.reply(src, parse_mode="HTML")

  elif message.text == "О боте":
    await message.reply(
      "Это бот помощник, он может найти интересующий вас материал на тему криптовалют",
      reply_markup=greet_kb)

  elif message.text == "Помощь":
    await message.reply("Если вы нашли недочет или баг, пишите сюда: @hkkk89",
                        reply_markup=greet_kb)

  else:
    await message.reply("Бот не знает такой комманды")


async def main():
  await dp.start_polling(bot)


bot.polling(non_stop=True, interval=0)

if __name__ == "__main__":
  asyncio.run(main())