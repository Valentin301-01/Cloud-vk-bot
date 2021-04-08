#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# :Author: snxx
# :Copyright: (c) 2021 snxx
# For license and copyright information please follow this like:
# https://github.com/snxx-lppxx/Cloud-vk-bot/blob/master/LICENSE
''' GitHub:                          snxx-lppxx/Cloud-vk-bot '''

import vk_api
import time
import json

from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api.keyboard import VkKeyboard
from config import token, version, gid

# Настройка vk api
vk = vk_api.VkApi(token=token)
vk._auth_token()
longpoll = VkBotLongPoll(vk, gid)
vk = vk.get_api()
settings = dict(one_time=False, inline=True)
f_toggle: bool = False

# Отправить стартовое сообщение. Точка входа
print('{}\n{}{}\n'.format('Server started...', 'API: ', version))


# функция для генерации базовой клавиатуры
def generate_keyboard(keyboard):
    # Клавиатура-1
    keyboard.add_callback_button(label='Куда я попал?',
                                 color=vk_api.keyboard.VkKeyboardColor.SECONDARY,
                                 payload={"type": "show_snackbar", "text": "Магазин ОблакО"}
                                 )
    keyboard.add_line()
    # Клавиатура-2
    keyboard.add_callback_button(label='Каталог',
                                 color=vk_api.keyboard.VkKeyboardColor.POSITIVE,
                                 payload={"type": "open_link", "link": "https://vk.com/market-203370905"}
                                 )
    keyboard.add_line()
    # Клавиатура-3
    keyboard.add_callback_button(label='Каталог',
                                 color=vk_api.keyboard.VkKeyboardColor.SECONDARY,
                                 payload={"type": "open_link", "link": "https://vk.com/market-203370905"}
                                 )

    return keyboard


keyboard = generate_keyboard(vk_api.keyboard.VkKeyboard(**settings))
for event in longpoll.listen():
    print(event.type)
    try:
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_user:
                if event.obj.message['text'] != '':
                    vk.messages.send(user_id=event.obj.message['from_id'], peer_id=event.obj.message['from_id'],
                                     message='Здравствуйте, я Ваш консультант, могу чем-то помочь?', random_id=0,
                                     keyboard=keyboard.get_keyboard()
                                     )

        elif event.type == VkBotEventType.MESSAGE_EVENT:
            r = vk.messages.sendMessageEventAnswer(
                event_id=event.object.event_id,
                user_id=event.object.user_id,
                peer_id=event.object.peer_id,
                event_data=json.dumps(event.object.payload))

            f_toggle = not f_toggle

            if 'Negative' in event.obj.text:
                vk.messages.send(peer_id=event.obj.message['peer_id'], message='1', random_id=0)

            if 'Primary' in event.obj.text:
                vk.messages.send(peer_id=event.obj.message['peer_id'], message='2', random_id=0)

            if 'Secondary' in event.obj.text:
                vk.messages.send(peer_id=event.obj.message['peer_id'], message='3', random_id=0)

    except Exception as e:
        time.sleep(0.75)
# ENDIF LOGICS
