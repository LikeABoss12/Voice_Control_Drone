from functions_for_commands import *
print(my_drone.get_battery())
print(sr.__version__)

while True:
    result = voice_command()
    statement = execute_command(result)
    print(statement)
    del result
    del statement
    continue
