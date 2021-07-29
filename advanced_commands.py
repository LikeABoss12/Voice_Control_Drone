from functions_for_commands import *
print(my_drone.get_battery())
print(sr.__version__)

while True:
    my_drone.send_rc_control(0, 0, 0, 0)
    result = voice_command()
    statement = execute_command(result)
    print(statement)

    if statement is True:
        del result
        del statement
        continue

    if int(my_drone.get_battery()) < 20:
        print('Low Battery!')
        my_drone.land()
        my_drone.end()

    else:
        continue

my_drone.__del__()
