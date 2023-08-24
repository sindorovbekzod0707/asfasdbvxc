from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.personalData import PersonalData
from loader import bot


from keyboards.default.keyboard import menu, chek


@dp.message_handler(text=("📨 Murojaatlar"), state=None)
async def enter_test(message: types.Message):
    await message.answer("To'liq ismingizni kiriting.")
    await PersonalData.fullName.set()


@dp.message_handler(state=PersonalData.fullName)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {"name": fullname}
    )

    await message.answer("Murojatizni kiriting.")

    await PersonalData.next()

@dp.message_handler(state=PersonalData.murojat)
async def answer_murojat(message: types.Message, state: FSMContext):
    murojat = message.text

    await state.update_data(
        {"murojat": murojat}
    )

    await message.answer("Telefon raqam kiriting.")

    await PersonalData.next()


@dp.message_handler(state=PersonalData.phoneNum)
async def answer_phone(message: types.Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {"phone": phone}
    )
    # Ma`lumotlarni qayta o'qiymiz
    data = await state.get_data()
    name = data.get("name")
    murojat = data.get("murojat")
    phone = data.get("phone")

    msg = "Quyidai ma`lumotlar qabul qilindi:\n"
    msg = f"🏅 Ismi - {name}\n"
    msg += f"📚 Murojat - {murojat}\n"
    msg += f"🌐 Telefoni - {phone}\n"

    await message.answer(msg)
    await message.answer("Barcha ma'lumotlar to'g'rimi?", reply_markup=chek)
    await PersonalData.next()

@dp.message_handler(state=PersonalData.chesk)
async def chesk(message: types.Message, state: FSMContext):
    if message.text.lower() == "ha":
        data = await state.get_data()

        name = data.get("name")
        murojat = data.get("murojat")
        phone = data.get("phone")

        msg = f"🏅 Ismi - {name}\n"
        msg += f"📚 Murojat - {murojat}\n"
        msg += f"🌐 Telefoni - {phone}\n"

        await bot.send_message(chat_id=-948548161, text=msg)
        await message.answer("Ma`lumotlar qabul qilindi siz bilan tez oraqada bog'lanishadi.")
        await message.answer("Bosh menyu!", reply_markup=menu)
        await state.finish()
    else:
        await message.answer("Qabul qilinmadi", reply_markup=menu)
        await state.finish()