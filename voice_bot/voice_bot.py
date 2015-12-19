# -*- coding: utf-8 -*-

import argparse

from src.conversation import Conversation

class Bob:
	def __init__(self):
		self.name = "Bob"

	def run(self):
		conversation = Conversation(self.name)
		conversation.dummyFunction()

if __name__ == "__main__":
	bob = Bob()
	bob.run()