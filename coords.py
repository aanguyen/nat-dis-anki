#Use this snippet to determine where coordinates are on the screen for anki
import pyautogui

print("Pres ctrl+c to exit")

try:
	while True:
		x, y = pyautogui.position()
		positionStr = "Current position- X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
		print(positionStr, end="")
		print("\b" * len(positionStr), end="", flush=True)
except KeyboardInterrupt:
	print("\nDone.")