import speech_recognition as sr
import requests
import helper 

#Gets speech from the user's microphone.
def get_speech():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening: ")
		audio = r.listen(source)
		speech = r.recognize_sphinx(audio)
	return speech

#Performs the request given a speech command.
def request(command):
	print command
	if (command == helper.get_command()) :
		headers = {"Authorization": "Bearer %s" % helper.get_token()}
		response = requests.post("https://api.lifx.com/v1/lights/all/toggle", headers = headers)
		print response
	else :
		print "Unrecognized Command. Try again."

#Runs this as a module.
if __name__ == '__main__':
	main()


