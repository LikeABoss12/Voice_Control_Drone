import speech_recognition as sr
import djitellopy as tello
my_drone = tello.Tello()
my_drone.connect()
my_mic = sr.Microphone()
r = sr.Recognizer()


def voice_command():  # This function allows repeated voice commands
    with my_mic as source:
        print("Say Command Here: ")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)  # Informational purposes
            return text
        except Exception as e:
            print(f"Exception: {e}")


def execute_command(result_one):
    # Takeoff
    if result_one == 'takeoff':
        my_drone.takeoff()
        return True

    # Land
    elif result_one == 'land':
        my_drone.land()
        return True

    # Flip
    elif 'flip' in result_one:
        if 'forward' in result_one:
            my_drone.flip_forward()
            return True
        elif 'back' in result_one:
            my_drone.flip_back()
            return True
        elif 'right' in result_one:
            my_drone.flip_right()
            return True
        elif 'left' in result_one:
            my_drone.flip_left()
            return True

    # Move
    elif 'move' in result_one:
        if 'forward' in result_one:
            y = ''
            for element in result_one:
                if element.isdigit():
                    y = y + element
            if y != '':
                my_drone.move_forward(int(y))
                del y
                return True
            else:
                my_drone.move_forward(100)
                return True

        elif 'back' in result_one:
            y = ''
            for element in result_one:
                if element.isdigit():
                    y = y + element
            if y != '':
                my_drone.move_back(int(y))
                del y
                return True
            else:
                my_drone.move_back(100)
                return True

        elif 'left' in result_one:
            y = ''
            for element in result_one:
                if element.isdigit():
                    y = y + element
            if y != '':
                my_drone.move_left(int(y))
                del y
                return True
            else:
                my_drone.move_left(100)
                return True

        elif 'right' in result_one:
            y = ''
            for element in result_one:
                if element.isdigit():
                    y = y + element
            if y != '':
                my_drone.move_right(int(y))
                del y
                return True
            else:
                my_drone.move_right(100)
                return True

        elif 'up' in result_one:
            y = ''
            for element in result_one:
                if element.isdigit():
                    y = y + element
            if y != '':
                my_drone.move_up(int(y))
                del y
                return True
            else:
                my_drone.move_up(100)
                return True

        elif 'down' in result_one:
            y = ''
            for element in result_one:
                if element.isdigit():
                    y = y + element
            if y != '':
                my_drone.move_down(int(y))
                del y
                return True
            else:
                my_drone.move_down(100)
                return True

    else:
        return False
