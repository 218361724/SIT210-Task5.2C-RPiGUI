import RPi.GPIO as GPIO
import tkinter as tk

rootWindow = tk.Tk()
ledPins = {
    "red": 7,
    "blue": 13,
    "green": 11
}

# Setup led pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPins["red"], GPIO.OUT)
GPIO.setup(ledPins["blue"], GPIO.OUT)
GPIO.setup(ledPins["green"], GPIO.OUT)

# Handle exit
def onExit():
    GPIO.cleanup()
    rootWindow.destroy()

# Handle led selection
selectedLedColor = tk.StringVar()
def onLedSelection():
    for ledColor, ledPin in ledPins.items():
        if (ledColor == selectedLedColor.get()):
            GPIO.output(ledPin, GPIO.HIGH)
            continue
        GPIO.output(ledPin, GPIO.LOW)

# -- Configure UI widgets
# Led radio buttons
ledRadioBtns = {}
for ledColor in ledPins.keys():
    ledRadioBtns[ledColor] = tk.Radiobutton(
        rootWindow,
        text = f"Toggle {ledColor.capitalize()}",
        variable = selectedLedColor,
        value = ledColor,
        command = onLedSelection
    )
    ledRadioBtns[ledColor].pack(anchor = tk.W)
# Exit button
exitBtn = tk.Button(
    rootWindow,
    text = "Exit",
    command = onExit
)
exitBtn.pack(anchor = tk.W)

# Configure window close action
rootWindow.protocol("WM_DELETE_WINDOW", onExit)

# Render UI
rootWindow.mainloop()
