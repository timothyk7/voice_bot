import wit
import json
import logging

import speech_recognition as sr

from os import system

class Conversation:
	def __init__(self, name, recognizer):
		self._logger = logging.getLogger(__name__)
		self.name = name
		self.recognizer = recognizer
		self.WIT_AI_KEY = "7H4YZTGMNPABHZRLCTEPCYM25LMH2X5Y"

	def listen(self):
		"""
		
	    Start voice robot to listen for commands
	    """
		wit.init()
		turnoff = False
		while not turnoff:

			with sr.Microphone() as source:
				self._logger.info("Microphone started")
				audio = self.recognizer.listen(source)

			cmd = self._ai(audio)

			if (cmd == "stop"):
				turnoff = True
		wit.close()

		system("say Good bye")

	def _ai(self, audio):
		"""

	    Processes and performs actions based on commands
	    Arguments:
        	audio -- audio from microphone
	    Returns:
	        String
	    """

		cmd = ""

		try:
			cmd = self.recognizer.recognize_wit(audio, key=self.WIT_AI_KEY)
			self._logger.debug(self.name + " thinks you said: " + cmd)

			if (cmd != None and cmd != ""):
				response = wit.text_query(cmd, self.WIT_AI_KEY)
				parsed = json.loads(response)
				self._logger.debug(json.dumps(parsed, sort_keys=True, indent=4, separators=(',', ': ')))

		except sr.UnknownValueError:
			self._logger.error(self.name + " could not understand audio")
		except sr.RequestError as e:
			self._logger.error("Could not request results from " + self.name + " service; {0}".format(e))

		return cmd
