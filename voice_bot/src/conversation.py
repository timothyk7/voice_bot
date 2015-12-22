import wit
import json

import speech_recognition as sr

class Conversation:
	def __init__(self, name, recognizer):
		self.name = name
		self.recognizer = recognizer
		self.WIT_AI_KEY = "7H4YZTGMNPABHZRLCTEPCYM25LMH2X5Y"

	def listen(self):
		wit.init()
		turnoff = False
		while not turnoff:

			with sr.Microphone() as source:
				print("Say something!")
				audio = self.recognizer.listen(source)

			cmd = self.ai(audio)

			if (cmd == "stop"):
				turnoff = True
		wit.close()

		print "Good bye"

	def ai(self, audio):
		cmd = ""

		try:
			cmd = self.recognizer.recognize_wit(audio, key=self.WIT_AI_KEY)
			print(self.name + " thinks you said: " + cmd)

			if (cmd != None and cmd != ""):
				response = wit.text_query(cmd, self.WIT_AI_KEY)
				parsed = json.loads(response)
				print json.dumps(parsed, sort_keys=True, indent=4, separators=(',', ': '))

		except sr.UnknownValueError:
			print(self.name + " could not understand audio")
		except sr.RequestError as e:
			print("Could not request results from " + self.name + " service; {0}".format(e))

		return cmd
