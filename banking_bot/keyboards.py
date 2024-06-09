from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder


# Main menu keyboard
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Баланс счета")],
        [KeyboardButton(text="Заявка на внесение"), KeyboardButton(text="Заявка на вывод")],
        [KeyboardButton(text="Условия вклада"), KeyboardButton(text="Этапы сотрудничества")],
        [KeyboardButton(text="Калькулятор", web_app=WebAppInfo(url="https://michalosman.github.io/calculator/"))],
        [KeyboardButton(text="Зарубежные переводы")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню:"
)

# Submenu for 'Условия вклада'
deposit_conditions_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Простой процент")],
        [KeyboardButton(text="Сложный процент")],
        [KeyboardButton(text="Объяснение процентов")],
        [KeyboardButton(text="Подробные условия (PDF)")],
        [KeyboardButton(text="В главное меню")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите тип процентов:"
)

# Submenu for 'Этапы сотрудничества'
cooperation_stages_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="По вкладу")],
        [KeyboardButton(text="По выводу")],
        [KeyboardButton(text="В главное меню")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите этап сотрудничества:"
)

# Submenu for 'Зарубежные переводы'
foreign_transfers_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="На карту")],
        [KeyboardButton(text="Оплата интернет услуг")],
        [KeyboardButton(text="В главное меню")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите тип перевода:"
)

# Inline keyboards for interest options
simple_interest_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="92 дня", callback_data='92_days')],
        [InlineKeyboardButton(text="123 дня", callback_data='123_days')],
        [InlineKeyboardButton(text="184 дня", callback_data='184_days')],
        [InlineKeyboardButton(text="276 дней", callback_data='276_days')],
        [InlineKeyboardButton(text="365 дней", callback_data='365_days')]
    ]
)

compound_interest_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="92 дня", callback_data='92_days')],
        [InlineKeyboardButton(text="123 дня", callback_data='123_days')],
        [InlineKeyboardButton(text="184 дня", callback_data='184_days')],
        [InlineKeyboardButton(text="276 дней", callback_data='276_days')],
        [InlineKeyboardButton(text="365 дней", callback_data='365_days')]
    ]
)

explanation_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Что такое простой процент", callback_data='simple_explanation')],
        [InlineKeyboardButton(text="Что такое сложный процент", callback_data='compound_explanation')]
    ]
)