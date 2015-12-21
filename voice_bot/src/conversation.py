
import wit
import json
import speech_recognition as sr

class Conversation:
	def __init__(self, name):
		self.name = name
		self.WIT_AI_KEY = "7H4YZTGMNPABHZRLCTEPCYM25LMH2X5Y"

	def listen(self):
		r = sr.Recognizer()
		wit.init()
		turnoff = False
		while not turnoff:

			with sr.Microphone() as source:
				print("Say something!")
				audio = r.listen(source)

			cmd = self.ai(r, audio)

			if (cmd == "stop"):
				turnoff = True

		wit.close()

		print "Good bye"

	def ai(self, recognizer, audio):
		cmd = ""

		try:
			cmd = recognizer.recognize_wit(audio, key=self.WIT_AI_KEY)
			print("Wit.ai thinks you said: " + cmd)

			if (cmd != None and cmd != ""):
				response = wit.text_query(cmd, self.WIT_AI_KEY)
				parsed = json.loads(response)
				print json.dumps(parsed, sort_keys=True, indent=4, separators=(',', ': '))

		except sr.UnknownValueError:
			print("Wit.ai could not understand audio")
		except sr.RequestError as e:
			print("Could not request results from Wit.ai service; {0}".format(e))

		return cmd
