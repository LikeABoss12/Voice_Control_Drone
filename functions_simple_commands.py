import speech_recognition as sr
import djitellopy as tello
my_drone = tello.Tello()
my_drone.connect()
my_mic = sr.Microphone()
r = sr.Recognizer()

def voice_command():  # This function allows repeated voice commands
    with my_mic as source:
        print("Command: ")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)  # Informational purposes
            return text
        except Exception as e:
            print(f"Exception: {e}")

def execute_command(result_one):
    if result_one == 'takeoff':
        my_drone.takeoff()

    elif result_one == 'land':
        my_drone.land()

    # Flip
    elif 'flip' in result_one:
        if 'forward' in result_one:
            my_drone.flip_forward()
        elif 'back' in result_one:
            my_drone.flip_back()
        elif 'right' in result_one:
            my_drone.flip_right()
        elif 'left' in result_one:
            my_drone.flip_left()

    # Move
    elif 'move' in result_one:
        if 'forward' in result_one:
            y = ''
            for element in result_one:
                if element.isdigit() is True:
                    y = y + element
                    my_drone.move_forward(int(y))
                else:
                    my_drone.move_forward(100)
            del y

        elif 'back' in result_one:
            y = ''
            for element in result_one:
                if element.isdigit() is True:
                    y = y + element
                    my_drone.move_back(int(y))
                else:
                    my_drone.move_back(100)
            del y

        elif 'left' in result_one:
            y = ''
            for element in result_one:
                if element.isdigit() is True:
                    y = y + element
                    my_drone.move_left(int(y))
                else:
                    my_drone.move_left(100)
            del y

        elif 'right' in result_one:
            y = ''
            for element in result_one:
                if element.isdigit() is True:
                    y = y + element
                    my_drone.move_right(int(y))
                else:
                    my_drone.move_right(100)
            del y

        elif 'up' in result_one:
            y = ''
            for element in result_one:
                if element.isdigit() is True:
                    y = y + element
                    my_drone.move_up(int(y))
                else:
                    my_drone.move_up(100)
            del y

        elif 'down' in result_one:
            y = ''
            for element in result_one:
                if element.isdigit() is True:
                    y = y + element
                    my_drone.move_up(int(y))
                else:
                    my_drone.move_up(100)
            del y
