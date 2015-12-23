# -*- coding: utf-8 -*-
import logging
import argparse

import speech_recognition as sr

from src.conversation import Conversation

class Bob:
	def __init__(self):
		self._logger = logging.getLogger(__name__)

		self.name = "Bob"
		self.recognizer = sr.Recognizer()

	def run(self):
			conversation = Conversation(self.name, self.recognizer)
			self._logger.info("Started listening")
			self._logger.debug("testing")
			conversation.listen()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Bob Voice Control Center')
	parser.add_argument('-d', '--debug', action='store_true', help='Show debug messages')
	args = parser.parse_args()

	logger = logging.getLogger()

	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)
	formatter = logging.Formatter('%(asctime)s: %(levelname)s - %(name)s - %(message)s')
	ch.setFormatter(formatter)
	logger.addHandler(ch)

	logger.setLevel(logging.INFO)

	if args.debug:	
		logger.setLevel(logging.DEBUG)


	bob = Bob()
	bob.run()