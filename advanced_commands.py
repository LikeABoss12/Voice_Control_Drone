from functions_for_commands import *
my_drone = tello.Tello()
mic = sr.Microphone()
recognizer = sr.Recognizer()
my_drone.connect()
print(my_drone.get_battery())
print(sr.__version__)

while my_drone.connect() is True:
    result = voice_command()
    statement = execute_command(result)

    if statement == True:
        continue

    else:
        print('Loop Failed')
        break
