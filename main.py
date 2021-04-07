#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# :Author: snxx
# :Copyright: (c) 2021 snxx
# For license and copyright information please follow this like:
# https://github.com/snxx-lppxx/Cloud-vk-bot/blob/master/LICENSE
''' GitHub:                          snxx-lppxx/Cloud-vk-bot '''

# Importing modules
import vk_api
import time
import json

from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from source.resource.word import err
from source.betypes.config import token, version, gid

from vk_api.keyboard import VkKeyboard, VkKeyboardColor

vk = vk_api.VkApi(token=token)
vk._auth_token()
vk.get_api()
longpoll = VkBotLongPoll(vk, gid)

settings = dict(one_time=False, inline=True)

class Server(object):

	# Send starting message. Etry point
	print('{}\n{}{}\n'.format('Server started...', 'API: ', version))

# INFDEF MAIN
	def __init__(self, keyboard):
		''' Creating keyboards '''

		# Keyboard number-1
		keyboard.add_callback_button(label='1', 
			                         color=vk_api.keyboard.VkKeyboardColor.SECONDARY,
			                         payload={"type": "show_snackbar", "text": "1"}
		)
		keyboard.add_line()
		# Keyboard number-2
		keyboard.add_callback_button(label='2', 
			                         color=vk_api.keyboard.VkKeyboardColor.POSITIVE,
			                         payload={"type": "open_link", "link": "https://github.com/snxx-lppxx"}
		)
		keyboard.add_line()
		# Keyboard number-3
		keyboard.add_callback_button(label='3', 
			                         color=vk_api.keyboard.VkKeyboardColor.SECONDARY,
			                         payload={"type": "open_link", "link": "https://github.com/snxx-lppxx"}
		)
# ENDIF MAIN

# IFNDEF LOGICS
f_toggle: bool = False

for event in longpoll.listen():
	keyboard = vk_api.keyboard.VkKeyboard(**settings)
	try:
		if event.type == vk_api.bot_longpoll.VkBotEventType.MESSAGE_NEW:

			if event.from_user:
				# Checking correctness 
				if event.obj.message['text'] != '':
					if 'callback' not in event.obj.client_info['button_actions']:
						print(f'Client does not supported: {event.obj.message["from_id"]}')
						vk.messages.send(user_id = event.obj.message['from_id'], peer_id = event.obj.message['from_id'], 
							             message = 'Здравствуйте, я Ваш консультант, могу чем-то помочь?', random_id = 0, keyboard=keyboard.get_keyboard()
						)

		elif event.type == VkBotEventType.MESSAGE_EVENT:
			if event.object.payload.get('type') in CALLBACK_TYPES:
				r = vk.messages.sendMessageEventAnswer(
					event_id = event.object.event_id, 
					user_id = event.object.user_id,
					peer_id = event.object.peer_id, 
					event_data = json.dumps(event.object.payload))

				f_toggle = not f_toggle

			if 'Negative' in event.obj.text:
				vk.messages.send(peer_id = event.obj.message['peer_id'], message = '1', random_id = 0)

			if 'Primary' in event.obj.text:
				vk.messages.send(peer_id = event.obj.message['peer_id'], message = '2', random_id = 0)

			if 'Secondary' in event.obj.text:
				vk.messages.send(peer_id = event.obj.message['peer_id'], message = '3', random_id = 0)

	except Exception as e:
		time.sleep(0.75)
# ENDIF LOGICS

if __name__ == '__main__':
	Server(object).main(keyboard)
