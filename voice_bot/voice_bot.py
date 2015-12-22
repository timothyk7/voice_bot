# -*- coding: utf-8 -*-
import speech_recognition as sr

from src.conversation import Conversation

class Bob:
	def __init__(self):
		self.name = "Bob"
		self.recognizer = sr.Recognizer()

	def run(self):
			conversation = Conversation(self.name, self.recognizer)

			conversation.listen()

if __name__ == "__main__":
	bob = Bob()
	bob.run()