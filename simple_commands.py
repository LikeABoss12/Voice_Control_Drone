# Setup
from functions_simple_commands import *
my_drone = tello.Tello()
my_drone.connect()
print(my_drone.get_battery())
my_mic = sr.Microphone()
r = sr.Recognizer()
my_drone.takeoff()
print(sr.__version__)

# Comparison Code
result_one = voice_command()
result_one = str(result_one)
execute_command(result_one)