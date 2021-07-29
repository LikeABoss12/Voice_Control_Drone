# Setup
from functions_for_commands import *
print(my_drone.get_battery())
print(sr.__version__)

# Comparison Code
result_one = voice_command()
result_one = str(result_one)
execute_command(result_one)