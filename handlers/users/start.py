from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.keyboard import menu, biz
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("Assalamu alaykum. Sizga qanday yordam bera olamiz.\nQuydagi menulardan birini tanlang", reply_markup=menu)

@dp.message_handler(text="📑 Biz haqimizda")
async def bot_start(message: types.Message):
    await message.answer("\nIste’molchining huquqlari buzilgan taqdirda, u sudga murojaat qilishga haqlidir. Da’volar, agar qonunlarda boshqacha qoida belgilanmagan bo‘lsa, javobgar, iste’molchi joylashgan erdagi yoki zarar etkazilgan joydagi sudga taqdim etiladi.\n\nIste’molchilar o‘z huquqlarining buzilishi bilan bog‘liq da’volar bo‘yicha, shuningdek, tovar (ish, xizmat)lar xavfsiz bo‘lishi ularning sifati ustidan nazoratni amalga oshiruvchi davlat organlari, iste’molchilarning jamoat birlashmalari iste’molchining (iste’molchilar nomuayyan doirasining) manfaatlarini ko‘zlab qo‘zg‘atiladigan da’volar bo‘yicha davlat boji to‘lashdan ozod qilinadilar.", reply_markup=biz)
