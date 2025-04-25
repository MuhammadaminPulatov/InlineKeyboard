import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="products"), KeyboardButton(text="electronics")],
        [KeyboardButton(text="clother"), KeyboardButton(text="basket")]
    ],
    resize_keyboard=True
)

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="products", callback_data="products"),
            InlineKeyboardButton(text="electronics", callback_data="electronics")
        ],
        [
            InlineKeyboardButton(text="clother", callback_data="clother"),
            InlineKeyboardButton(text="basket", callback_data="basket")
        ]
    ]
)

@dp.message(CommandStart())
async def start(message: Message):
    name = message.from_user.full_name
    await message.answer(f"Salom, {name} 👋", reply_markup=reply_keyboard)
    await message.answer("Quyidagilardan birini tanlang:", reply_markup=inline_keyboard)


@dp.message(F.text.in_(["products", "electronics", "clother", "basket"]))
async def reply_handler(message: Message):
    await message.answer(f"{message.text}")

@dp.callback_query(F.data.in_(["products", "electronics", "clother", "basket"]))
async def inline_handler(callback: CallbackQuery):
    await callback.answer()  # yuklanishni yopadi
    await callback.message.answer(f"{callback.data}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
