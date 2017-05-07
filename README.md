# Lights

Voice command for LIFX.

## Description
Lights is a simple Python program that uses voice recognition to turn on your LIFX bulbs. Alexa and Google Home have this functionality available out of the box, but why not code it yourself?

## How it works
Lights consists of only four files:

* ```lights.py``` - Python script that runs the program.
* ```helper.py``` - Reads the configuration token and user-defined command to toggle the lights.
* ```request.py``` - Contains the functions that make the logic and API request functions.
* ```config.json``` - Contains the LIFX OAuth token and user-defined command to toggle the lights.

The ```request.py``` file uses [Uberi's Speech Recognition module](https://github.com/Uberi/speech_recognition) for Python.

## How to use it

1. Install Uberi's Speech Recognition module: ```pip install SpeechRecognition```.
2. Clone this repo.
3. Edit ```config.json``` with your LIFX OAuth token. If you don't have a token, you can easily generate one here: [LIFX Cloud Settings](https://cloud.lifx.com/settings)
4. Run the program: ```python lights.py```.
5. Irreverently declare "let there be light." 

Note that the [LIFX API](https://api.developer.lifx.com/docs/toggle-power) only allows for a toggle. Therefore "let there be light" will turn the lights on as well as off. Bummer.
