import time
import Power

if __name__ == '__main__':
    while True:
        # Get speed and validate
        speedInput = raw_input("Set speed: ")
        try:
            speed = int(speedInput)
            if speed < 0 or speed > 100:
                print("Speed must be between 0 and 100")
            else:
                break
        except ValueError:
            print("Speed must be an integer")
            continue
        
        # Get direction and validate
        directionInput = raw_input("Set direction, f or b: ")
        try:
            direction = directionInput.toLower()
            if direction != "f" or direction != "b":
                print("Direction must be either f or b")
            else:
                break
        except:
            continue
        
        # Main logic
        if direction == "f":
            # Add 2nd argument for duration
            Power.forward(speed)
        elif direction == "b":
            # Add 2nd argument for duration
            Power.backward(speed)
        else:
            Power.stop()