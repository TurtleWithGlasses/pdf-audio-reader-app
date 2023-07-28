import pyttsx3

engine_object = pyttsx3.init()
engine_object.setProperty("rate", 150)
engine_object.setProperty("voice", "f1")
engine_object.say("Hello world")
engine_object.runAndWait()