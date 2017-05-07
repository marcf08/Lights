import json

#Designates the config file. Rename this variable to the name of your config file.
my_file = "config.json"

#Gets the command from the config file specified.
def get_command():
	with open(my_file) as data_file:    
		data = json.load(data_file)
	return data["command"]

#Gets the token from the config file specified.
def get_token():
	with open(my_file) as data_file:
		data = json.load(data_file)
	return data["token"]

#Runs this as a module.
if __name__ == "__main__":
	main()
