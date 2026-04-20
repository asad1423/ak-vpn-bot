from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from database import add_user, get_user, get_days_left, update_subscription
from keyboards import main_menu, tariffs_menu, admin_contact
from vpn import create_vpn_key
from config import ADMIN_ID

router = Router()

# ================= START =================
@router.message(Command("start"))
async def start(message:Message):

    # 🔥 РЕГИСТРАЦИЯ ПОЛЬЗОВАТЕЛЯ В БАЗЕ
    add_user(message.from_user.id, message.from_user.username)

    await message.answer_photo(
        photo="https://instasize.com/p/adb7fcdab25e956ba293d12173fa47783f8fba76ee769e768c0f4dbb66f99add",
        caption=(
            "🔐 AK VPN — быстрый и безопасный доступ в интернет\n\n"
            
            "🚀 Что ты получаешь:\n"
            "• Стабильное соединение без обрывов\n"
            "• Высокая скорость для видео, игр и соцсетей\n"
            "• Полная анонимность и защита данных\n"
            "• Работает на всех устройствах (iPhone / Android / ПК)\n\n"
            
            "🌍 Подходит для:\n"
            "• YouTube, TikTok, Instagram\n"
            "• Telegram и любые сайты\n"
            "• Обход ограничений и блокировок\n\n"
            
            "💳 Тарифы:\n"
            "• от 100₽ — доступный VPN для всех\n"
            "• 🎁 есть тест 7 дней бесплатно\n\n"
            
            "⚡️ Установка занимает 1–2 минуты\n"
            "🔑 После оплаты ты сразу получаешь доступ\n\n"
            
            "👇 Выбери тариф ниже и начни пользоваться уже сейчас"
        ),
        reply_markup=main_menu
    )



# ================= ТАРИФЫ =================
@router.message(F.text.contains("ТАРИФЫ"))
async def tariffs(message: Message):
    await message.answer(
        "💳 Информация о подписке\n\n"
        "Статус: Не активна\n"
        "💰 Баланс: 0.0 ₽\n\n"
        "Доступные тарифы:"
    , reply_markup=tariffs_menu)


# ================= TRIAL =================
@router.message(F.text.contains("Тест"))
async def trial(message: Message):

    await message.answer(
        "🎁 Чтобы получить 7 дней бесплатно:\n"
        "👉 Напишите администратору",
        reply_markup=admin_contact
    )

    await message.bot.send_message(
        ADMIN_ID,
        f"🆕 TRIAL заявка\n"
        f"Имя: {message.from_user.full_name}\n"
        f"ID: {message.from_user.id}"
    )


# ================= СТАНДАРТ =================
@router.message(F.text.contains("Стандарт"))
async def standard_1(message: Message):

    await message.answer(
        "💳 Вы выбрали: Стандарт (1 месяц)\n\n"
        "⚠️ Сейчас автоматическая оплата временно недоступна.\n\n"
        "🔧 Мы уже работаем над подключением автоплатежей — "
        "в ближайшее время всё будет доступно прямо в боте.\n\n"
        "📩 Напишите администратору:\n"
        "@slip14a\n\n"
        "⏱️ Ответим быстро и выдадим доступ\n\n"
        "Спасибо за понимание 🙌",
        reply_markup=admin_contact
    )

    username = message.from_user.username
    username_text = f"@{username}" if username else "нет username"

    await message.bot.send_message(
        ADMIN_ID,
        f"💳 Новый заказ\n"
        f"Тариф: 1 месяц\n"
        f"Пользователь: {message.from_user.full_name}\n"
        f"Username: {username_text}\n"
        f"ID: {message.from_user.id}"
    )


# ================= БАЗОВЫЙ =================
@router.message(F.text.contains("Базовый"))
async def basic(message: Message):

    await message.answer(
        "💳 Вы выбрали: Базовый (3 месяца)\n\n"
        "⚠️ Автооплата временно недоступна\n\n"
        "📩 Напишите: @slip14a",
        reply_markup=admin_contact
    )

    username = message.from_user.username
    username_text = f"@{username}" if username else "нет username"

    await message.bot.send_message(
        ADMIN_ID,
        f"💳 Новый заказ\n"
        f"Тариф: 3 месяца\n"
        f"Пользователь: {message.from_user.full_name}\n"
        f"Username: {username_text}\n"
        f"ID: {message.from_user.id}"
    )


# ================= ОПТИМАЛЬНЫЙ =================
@router.message(F.text.contains("Оптимальный"))
async def optimal(message: Message):

    await message.answer(
        "💳 Вы выбрали: Оптимальный (6 месяцев)\n\n"
        "⚠️ Автооплата временно недоступна\n\n"
        "📩 Напишите: @slip14a",
        reply_markup=admin_contact
    )

    username = message.from_user.username
    username_text = f"@{username}" if username else "нет username"

    await message.bot.send_message(
        ADMIN_ID,
        f"💳 Новый заказ\n"
        f"Тариф: 6 месяцев\n"
        f"Пользователь: {message.from_user.full_name}\n"
        f"Username: {username_text}\n"
        f"ID: {message.from_user.id}"
    )


# ================= ГОДОВОЙ =================
@router.message(F.text.contains("Годовой"))
async def yearly(message: Message):

    await message.answer(
        "💳 Вы выбрали: Годовой (12 месяцев)\n\n"
        "⚠️ Автооплата временно недоступна\n\n"
        "📩 Напишите: @slip14a",
        reply_markup=admin_contact
    )

    username = message.from_user.username
    username_text = f"@{username}" if username else "нет username"

    await message.bot.send_message(
        ADMIN_ID,
        f"💳 Новый заказ\n"
        f"Тариф: 12 месяцев\n"
        f"Пользователь: {message.from_user.full_name}\n"
        f"Username: {username_text}\n"
        f"ID: {message.from_user.id}"
    )
    


# ================= ЛИЧНЫЙ КАБИНЕТ =================
@router.message(F.text.contains("ЛИЧНЫЙ КАБИНЕТ"))
async def cabinet(message: Message):

    user = get_user(message.from_user.id)

    if not user:
        await message.answer("❌ Вы не зарегистрированы")
        return

    user_id, username, end_date, vpn_key = user
    days_left = get_days_left(user_id)

    await message.answer(
        f"💳 Личный Кабинет\n\n"
        f"👤 Имя: {message.from_user.full_name}\n"
        f"🆔 ID: {user_id}\n"
        f"🔑 Ключ: {vpn_key if vpn_key else 'Нет ключа'}\n"
        f"📊 Статус: {'Активна' if days_left > 0 else 'Не активна'}\n"
        f"📅 Осталось дней: {days_left}\n"
    )

# ================= АДМИН =================
@router.message(Command("addsub"))
async def addsub(message: Message):
    if message.from_user.id != ADMIN_ID:
        return

    try:
        _, user_id, days, key = message.text.split()

        user_id = int(user_id)
        days = int(days)

        await update_subscription(user_id, days, key)

        await message.answer("✅ Подписка выдана")

    except:
        await message.answer("Формат: /addsub user_id days key")


# ================= ПОМОЩЬ =================
@router.message(F.text.contains("ПОМОЩЬ"))
async def help(message: Message):

    await message.answer(
        "📝 Опишите проблему:\n\n"
        "• Что не работает?\n"
        "• Ошибка?\n"
        "• Интернет?\n"
        "• Скриншоты\n\n"
        "⚠️ Администратор ответит"
    )

    await message.bot.send_message(
        ADMIN_ID,
        f"🆘 ПОМОЩЬ\n"
        f"{message.from_user.full_name}\n"
        f"ID: {message.from_user.id}"
    )


# ================= ИНСТРУКЦИЯ =================
@router.message(F.text.contains("ИНСТРУКЦИЯ"))
async def guide(message: Message):
    await message.answer(
        "📱 Инструкция:\n\n"
        "1. Скачай Amnezia VPN\n"
        "2. Получи ключ у администратора\n"
        "3. Вставь в приложение\n"
        "4. Подключись"
    )


# ================= О СЕРВИСЕ =================
@router.message(F.text.contains("СЕРВИС"))
async def about(message: Message):
    await message.answer(
        "🚀 VPN сервис\n\n"
        "• Стабильный VPN\n"
        "• Без логов\n"
        "• Поддержка 24/7\n"
        "• 7 дней тест"
    )


# ================= НАЗАД =================
@router.message(F.text.contains("Назад"))
async def back(message: Message):
    await message.answer("Главное меню", reply_markup=main_menu)