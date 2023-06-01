# pip install aiogram
# bot - ���������� ������� �� ������������ � �����
# Dispatcher - ����������� ����������
# executor - ��������� ���
# types - ��������� ������������ ��������� ������������
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
TOKEN = '6225197499:AAG9qAOpIF7VlrmTPptDAEuPORcnIbv4BrE'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# ����� ���������
@dp.message_handler(commands=['start'])
async def say_hello(message: types.Message):
    list1 = [
        [
            types.KeyboardButton(text='����� ������ ���'),
            types.KeyboardButton(text='����� ��� �����'),
            types.KeyboardButton(text='������'),
            types.KeyboardButton(text='��� ���� �����?'),

        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=list1)
    await message.reply('������!', reply_markup=keyboard)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)



# reply - ������ - ����� ��� �������� �������
# inline - ������ - ������, ����������� � ����������


executor.start_polling(dp, skip_updates=True)

