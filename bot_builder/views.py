# bot_builder/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BotTemplateForm
from .models import BotTemplate
import os
import zipfile

def create_bot_template(request):
    if request.method == 'POST':
        form = BotTemplateForm(request.POST)
        if form.is_valid():
            bot_template = form.save()
            generate_bot_code(bot_template)
            return redirect('bot_download', bot_id=bot_template.id)
    else:
        form = BotTemplateForm()
    return render(request, 'bot_builder/create_bot_template.html', {'form': form})

def bot_download(request, bot_id):
    bot_template = BotTemplate.objects.get(id=bot_id)
    file_path = f'generated_bots/{bot_template.name}.zip'
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename="{bot_template.name}.zip"'
        return response

def generate_bot_code(bot_template):
    bot_code = f"""
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from time import sleep
import requests.exceptions
import logging


logger = logging.getLogger('Logger')


def main():
    bot_token = '7324429775:AAGGyexIHTCHvLBhP-DoTBKHhqn8uVaJbCM'
    bot = Bot(token=bot_token)
    dp = Dispatcher()

    logger.setLevel(logging.WARNING)
    logger.warning("TG_bot запущен")

    @dp.message(Command(commands=["start"]))
    async def send_welcome(message: Message):
        await message.answer("{bot_template.start_message}")

    @dp.message()
    async def echo(message: Message):
        await message.answer(message.text)

    while True:
        try:
            # dp.include_routers(start_dialog, cart_dialog)
            dp.run_polling(bot)
        except requests.exceptions.ReadTimeout:
            pass
        except requests.exceptions.ConnectionError:
            logging.exception("TG_bot упал с ошибкой")
            sleep(120)


if __name__ == '__main__':
    main()
"""
    os.makedirs('generated_bots', exist_ok=True)
    bot_file_path = f'generated_bots/{bot_template.name}.py'
    with open(bot_file_path, 'w') as f:
        f.write(bot_code)

    zip_path = f'generated_bots/{bot_template.name}.zip'
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.write(bot_file_path, os.path.basename(bot_file_path))
