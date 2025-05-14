from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils import user_data, send_discord_message

router = Router()

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Send Message")],
        [KeyboardButton(text="Settings")],
        [KeyboardButton(text="Set Webhook")]
    ],
    resize_keyboard=True
)

settings_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Enable/Disable Embed")],
        [KeyboardButton(text="Change Embed Color")],
        [KeyboardButton(text="Change Avatar")],
        [KeyboardButton(text="Change Username")],
        [KeyboardButton(text="Back")]
    ],
    resize_keyboard=True
)

@router.message(Command("start"))
async def start(msg: types.Message):
    await msg.answer("💎", reply_markup=main_kb)

@router.message(lambda message: message.text == "Settings")
async def settings_menu(msg: types.Message):
    await msg.answer("Settings:", reply_markup=settings_kb)

@router.message(lambda message: message.text == "Back")
async def back(msg: types.Message):
    await msg.answer("Main menu:", reply_markup=main_kb)

@router.message(lambda message: message.text == "Set Webhook")
async def set_webhook(msg: types.Message):
    user_data.setdefault(msg.from_user.id, {})["state"] = "set_webhook"
    await msg.answer("Paste the Discord Webhook URL:")

@router.message(lambda message: message.text == "Send Message")
async def ask_message(msg: types.Message):
    user_data.setdefault(msg.from_user.id, {})["state"] = "send_message"
    await msg.answer("Enter the message to send to Discord:")

@router.message(lambda message: message.text == "Change Embed Color")
async def change_color(msg: types.Message):
    user_data.setdefault(msg.from_user.id, {})["state"] = "Change Color"
    await msg.answer("Enter new color in HEX format (#RRGGBB):")

@router.message(lambda message: message.text == "Change Avatar")
async def change_avatar(msg: types.Message):
    user_data.setdefault(msg.from_user.id, {})["state"] = "Change Avatar"
    await msg.answer("Enter image URL (1:1 aspect ratio):")

@router.message(lambda message: message.text == "Change Username")
async def change_username(msg: types.Message):
    user_data.setdefault(msg.from_user.id, {})["state"] = "Change Username"
    await msg.answer("Enter new username for the sender:")

@router.message()
async def text_handler(msg: types.Message):
    uid = msg.from_user.id
    state = user_data.get(uid, {}).get("state")

    if state == "set_webhook":
        user_data.setdefault(uid, {})["webhook"] = msg.text
        user_data[uid]["state"] = None
        await msg.answer("Webhook saved.")

    elif state == "send_message":
        webhook = user_data.get(uid, {}).get("webhook")
        if not webhook:
            await msg.answer("Please set the webhook first.")
            return
        embed = user_data.get(uid, {}).get("embed", False)
        color = user_data.get(uid, {}).get("color", "#000000")
        username = user_data.get(uid, {}).get("username")
        avatar = user_data.get(uid, {}).get("avatar")
        success = send_discord_message(webhook, msg.text, embed, color, username, avatar)
        if success:
            await msg.answer("📲")
            await msg.answer("Sent!")
        else:
            await msg.answer("Error while sending.")


    elif state == "Change Embed Color":
        user_data.setdefault(uid, {})["color"] = msg.text
        user_data[uid]["state"] = None
        await msg.answer("Color updated.")

    elif state == "Change Avatar":
        user_data.setdefault(uid, {})["avatar"] = msg.text
        user_data[uid]["state"] = None
        await msg.answer("Avatar updated.")

    elif state == "Change Username":
        user_data.setdefault(uid, {})["username"] = msg.text
        user_data[uid]["state"] = None
        await msg.answer("Username updated.")

    elif state == "Enable/Disable Embed":
        current = user_data.get(uid, {}).get("embed", False)
        user_data.setdefault(uid, {})["embed"] = not current
        await msg.answer(f"Embed: {'enabled' if not current else 'disabled'}")

    elif msg.text == "Change Embed Color":
        user_data.setdefault(uid, {})["state"] = "Change Color"
        await msg.answer("Enter the new color in HEX format (#RRGGBB):")

    elif msg.text == "Change Avatar":
        user_data.setdefault(uid, {})["state"] = "Change Avatar"
        await msg.answer("Enter image URL (1:1 aspect ratio):")

    elif msg.text == "Change Username":
        user_data.setdefault(uid, {})["state"] = "Change Username"
        await msg.answer("Enter new username for the sender:")
