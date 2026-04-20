from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💳 ТАРИФЫ")],
        [KeyboardButton(text="👤 ЛИЧНЫЙ КАБИНЕТ")],
        [KeyboardButton(text="📱 ИНСТРУКЦИЯ")],
        [KeyboardButton(text="🆘 ПОМОЩЬ")],
        [KeyboardButton(text="ℹ️ О СЕРВИСЕ")]
    ],
    resize_keyboard=True
)

tariffs_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎁 Тест (7 дней) - 0₽")],
        [KeyboardButton(text="💳 Стандарт (1 месяц) - 149₽")],
        [KeyboardButton(text="📦 Базовый (3 месяца) - 299₽")],
        [KeyboardButton(text="🚀 Оптимальный (6 месяцев) - 499₽")],
        [KeyboardButton(text="👑 Годовой (1 год) - 899₽")],
        [KeyboardButton(text="⬅️ Назад")]
    ],
    resize_keyboard=True
)

admin_contact = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="👨‍💻 Написать администратору",
            url="https://t.me/slip14a"
        )]
    ]
)