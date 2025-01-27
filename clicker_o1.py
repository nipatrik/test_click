import pyautogui
import time
import random
from pynput import mouse, keyboard

# Variables to store user-defined points
reload_point = None
click_points = []
paused = False
stopped = False

# Function to capture mouse click points
def on_click(x, y, button, pressed):
    global reload_point, click_points

    if pressed:
        print(f"Point captured: ({x}, {y})")

        if reload_point is None:
            reload_point = (x, y)
            print("Reload point set.")
        elif len(click_points) < 10:
            click_points.append((x, y))
            print(f"Click point {len(click_points)} set.")

        if reload_point and len(click_points) == 10:
            return False

# Function to handle keyboard events
def on_press(key):
    global paused, stopped
    try:
        if key == keyboard.Key.f9:  # Pause/Resume on FN+F9
            paused = not paused
            state = "paused" if paused else "resumed"
            print(f"Execution {state}.")
        elif key == keyboard.Key.f11:  # Stop on FN+F11
            stopped = True
            print("Execution stopped.")
            return False
    except AttributeError:
        pass

# Capture user-defined points
print("Please click to set the reload point, followed by 10 click points.")
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

print(f"Reload point: {reload_point}")
print(f"Click points: {click_points}")

# Check if all points are set
if not reload_point or len(click_points) != 10:
    print("Error: Not all points were set.")
    exit(1)

# Start keyboard listener
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# Main loop variables
total_clicks = 0
clicks_per_cycle = random.randint(1100, 1300)

# Main clicking loop
while total_clicks < 110000 and not stopped:
    if not paused:
        for _ in range(clicks_per_cycle):
            if stopped or paused:
                break

            point = random.choice(click_points)
            pyautogui.click(point)
            total_clicks += 1
            print(f"Click {total_clicks} performed.")
            time.sleep(random.uniform(0.08, 0.1))

            if total_clicks >= 110000 or stopped or paused:
                break

        if not stopped and not paused:
            # Reload action
            print("Reloading page...")
            pyautogui.click(reload_point)

            # Countdown for 15 seconds
            for i in range(15, 0, -1):
                if stopped or paused:
                    break
                print(f"Resuming in {i} seconds...")
                time.sleep(1)

            clicks_per_cycle = random.randint(1100, 1300)  # Recalculate clicks per cycle

print("Task completed. Total clicks performed:", total_clicks)

