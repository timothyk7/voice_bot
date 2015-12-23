# -*- coding: utf-8 -*-
import logging
import argparse
import sys

import speech_recognition as sr

from client.conversation import Conversation
from util import diagnosis

class Bob:
	def __init__(self):
		self._logger = logging.getLogger(__name__)

		self.name = "Bob"
		self.recognizer = sr.Recognizer()

	def run(self):
			conversation = Conversation(self.name, self.recognizer)
			self._logger.info("Started listening")
			conversation.listen()

def getLogger():
	logger = logging.getLogger()

	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)
	formatter = logging.Formatter('%(asctime)s: %(levelname)s - %(name)s - %(message)s')
	ch.setFormatter(formatter)
	logger.addHandler(ch)

	logger.setLevel(logging.INFO)

	return logger

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Bob Voice Control Center')
	parser.add_argument('-d', '--debug', action='store_true', help='Show debug messages')
	args = parser.parse_args()

	logger = getLogger()

	if args.debug:	
		logger.setLevel(logging.DEBUG)

	if not diagnosis.check_network_connection():
		sys.exit(1)

	bob = Bob()
	bob.run()