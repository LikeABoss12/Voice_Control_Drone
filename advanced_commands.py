from functions_for_commands import *
print(my_drone.get_battery())
print(sr.__version__)

while True:
    result = voice_command()
    statement = execute_command(result)
    print(statement)
    if statement is True:
        del result
        del statement
        continue
    else:
        print('Loop Failed!')
        break