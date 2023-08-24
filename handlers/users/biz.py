from aiogram import types
from keyboards.default.keyboard import menu, biz
from loader import dp

@dp.message_handler(text="💻 AKT haqida")
async def oraqaga(message: types.Message):
    await message.answer("Masul xodim haqida malumot:\n\nF.I.O: Abdug'aniyev Axror Shavkat o'g'li\nLavozimi: FullStack dasturchi\nTel raqami: +998 94 344 19 29", reply_markup=biz)

@dp.message_handler(text="🛒 Magazinlar haqida")
async def oraqaga(message: types.Message):
    await message.answer("Masul xodim haqida malumot:\n\nF.I.O: Sindorov Bekzod Farhod o'g'li\nLavozimi: Biznesmen\nTel raqami: +998 33 557 77 84", reply_markup=biz)


@dp.message_handler(text="🏩 Davolanish")
async def oraqaga(message: types.Message):
    await message.answer("Masul xodim haqida malumot:\n\nF.I.O: Abdumajidov Abduvali Sharof o'g'li\nLavozimi: Doktor\nTel raqami: +998 97 794 37 79", reply_markup=biz)


@dp.message_handler(text="🌿 Dehqonchilik")
async def oraqaga(message: types.Message):
    await message.answer("Masul xodim haqida malumot:\n\nF.I.O: Mulumanov Diyorbek Olim o'g'li\nLavozimi: Dehqon\nTel raqami: +998 90 494 64 61", reply_markup=biz)


@dp.message_handler(text="🐄 Chorvachilik")
async def oraqaga(message: types.Message):
    await message.answer("Masul xodim haqida malumot:\n\nF.I.O: To'qinov Javohir Valijon o'g'li\nLavozimi: Chorvachilik\nTel raqami: +998 90 229 93 89", reply_markup=biz)


@dp.message_handler(text="🍇 Uzumchilik")
async def oraqaga(message: types.Message):
    await message.answer("Masul xodim haqida malumot:\n\nF.I.O: Jo'raxo'jayev Jahon Murod o'g'li\nLavozimi: Bog'bon\nTel raqami: +998 88 680 70 70", reply_markup=biz)


@dp.message_handler(text="🔙 Ortga")
async def oraqaga(message: types.Message):
    await message.answer("Sizga qanday yordam bera olamiz.\nQuydagi menulardan birini tanlang", reply_markup=menu)