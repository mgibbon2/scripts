import ctypes
import pygetwindow as window
from pynput import keyboard
from pywinauto import Desktop

# Defaults in [X, Y, W, H]
spotify_defaults = []
spotify_title = "Spotify"
discord_defaults = []
discord_title = "Discord"
internet_defaults = []
internet_title = "Google Chrome"

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0)
print(f"SCREENSIZE: {screensize}")
match screensize:
    # desktop dimensions
    case (2560):
        spotify_defaults = [3647, 550, 800, 600]
        discord_defaults = [3507, 186, 940, 500]
        internet_defaults = [2586, 549, 864, 608]
    # laptop dimensions
    case (1920):
        spotify_defaults = [887, 34, 1000, 750]
        discord_defaults = [33, 372, 1175, 625]
        internet_defaults = [25, 34, 918, 678]
    case _:
        print("UNINITIALIZED SETUP VARIABLES")

windows = Desktop(backend="uia").windows()
print([w.window_text() for w in windows])

def resize_window(window_title, defaults):
    try:
        print(f"Window title: {window_title}.\n------------------------------")
        resized = False
        moved = False
        
        # Find the window using pygetwindow
        current_window = window.getWindowsWithTitle(window_title)[0]
        if current_window.isMinimized:
            print(f"Window is minimized.")
        elif ctypes.windll.user32.IsZoomed(current_window._hWnd) != 0:
            print(f"Window is maximized.")
        else:
            print(f"Size: ({current_window.size.width}, {current_window.size.height})\nPosition: ({current_window.left}, {current_window.top})")
            # Resize the window
            if current_window.size != (defaults[2], defaults[3]):
                resized = True
                current_window.resizeTo(defaults[2], defaults[3])
                print(f"Window was resized.")
            if current_window.left != defaults[0] or current_window.top != defaults[1]:
                moved = True
                current_window.moveTo(defaults[0], defaults[1])
                print(f"Window was moved.")
            if resized or moved:
                print(f"Size: ({current_window.size.width}, {current_window.size.height})\nPosition: ({current_window.left}, {current_window.top})")
            else:
                print(f"Window was not affected.")
    except (IndexError, window.PyGetWindowException):
        print(f"Window was not found.")
    print(f"------------------------------\n\n")

def on_activate():
    resize_window(spotify_title, spotify_defaults)
    resize_window(discord_title, discord_defaults)
    resize_window(internet_title, internet_defaults)

with keyboard.GlobalHotKeys({
    '<ctrl>+<alt>+m': lambda: on_activate(),
}) as keys:
    keys.join()