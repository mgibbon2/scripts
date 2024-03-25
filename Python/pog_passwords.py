from dotenv import load_dotenv
import os
import pygetwindow as window
from pynput import keyboard
from pywinauto import Application
import subprocess

load_dotenv()

# defaults
league_accounts = os.getenv("LEAGUE_ACCOUNTS").split(",")
realm_account = os.getenv("REALM_ACCOUNT")
warframe_account = os.getenv("WARFRAME_ACCOUNT")

input_file = "src/encrypted.enc"
output_file = "src/decrypted.txt"
password = os.getenv("DECRYPT_PASSWORD")

def decrypt_file(input_file, output_file, password):
    command = f'openssl enc -d -aes-256-cbc -pbkdf2 -in {input_file} -out {output_file} -pass pass:{password}'
    subprocess.run(command, shell=False, creationflags=subprocess.CREATE_NO_WINDOW)

def decrypt_to_array(input_file, output_file, password):
    decrypt_file(input_file, output_file, password)
    decrypted_content = []
    with open("src/decrypted.txt") as decrypted_file:
        decrypted_content = decrypted_file.readlines()
    # remove new line character
    decrypted_content = [s[:-1] for s in decrypted_content]
    os.remove(output_file)
    return decrypted_content

def log_in(account_number):
    window_title = window.getActiveWindowTitle()
    if "Riot Client" in window_title:
        username_index = find_username_index(league_accounts[account_number])
        print(f"Riot Client - Logging in as {logins[username_index]}")
        login_riot_client(logins[username_index], logins[username_index + 1])
    elif "Warframe" in window_title:
        username_index = find_username_index("Warframe")
        print(f"Warframe - Logging in as {warframe_account}")
        login_warframe(logins[username_index + 1])
    elif "RotMG" in window_title:
        print(f"RotMG Exalt Launcher - Logging in as {realm_account}")
        username_index = find_username_index(realm_account)
        login_rotmg(logins[username_index], logins[username_index + 1])
    else:
        print("UNKNOWN WINDOW")

def find_username_index(username):
    for i in range(0, len(logins)):
        if logins[i] == username:
            return i

def login_riot_client(username, password):
    app = Application(backend="uia").connect(title_re=".*Riot Client.*")
    app.RiotClient.type_keys(username)
    app.RiotClient.type_keys("{TAB}")
    app.RiotClient.type_keys(password)
    app.RiotClient.type_keys("{ENTER}")

def login_warframe(password):
    app = Application(backend="uia").connect(title_re="Warframe")
    app.Warframe.type_keys(password)
    app.Warframe.type_keys("{ENTER}")

def login_rotmg(email, password):
    app = Application(backend="win32").connect(title_re=".*RotMG.*")
    app.top_window().set_focus()
    app.top_window().type_keys(email)
    app.top_window().type_keys("{TAB}")
    app.top_window().type_keys(password)
    app.top_window().type_keys("{ENTER}")

def on_activate(number):
    print(f"HOTKEY PRESSED: {number}");
    log_in(number)

logins = decrypt_to_array(input_file, output_file, password)

with keyboard.GlobalHotKeys({
    '<ctrl>+<alt>+0': lambda: on_activate(0),
    '<ctrl>+<alt>+1': lambda: on_activate(1),
    '<ctrl>+<alt>+2': lambda: on_activate(2),
    '<ctrl>+<alt>+3': lambda: on_activate(3),
    '<ctrl>+<alt>+4': lambda: on_activate(4),
    '<ctrl>+<alt>+5': lambda: on_activate(5),
    '<ctrl>+<alt>+6': lambda: on_activate(6),
    '<ctrl>+<alt>+9': lambda: on_activate(9),
    '<ctrl>+<alt>+7': lambda: on_activate(7),
    '<ctrl>+<alt>+8': lambda: on_activate(8),
    '<ctrl>+<alt>+8': lambda: on_activate(9),
}) as keys:
    keys.join()