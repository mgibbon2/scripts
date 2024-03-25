from dotenv import load_dotenv
import os
from pynput import keyboard
import subprocess

load_dotenv()

encrypted_file = "src/encrypted.enc"
decrypted_file = "src/decrypted.txt"
password = os.getenv("DECRYPT_PASSWORD")

def encrypt_file(input_file, output_file, password):
    command = f'openssl enc -aes-256-cbc -salt -pbkdf2 -in {input_file} -out {output_file} -pass pass:{password}'
    subprocess.run(command, shell=False, creationflags=subprocess.CREATE_NO_WINDOW)

def decrypt_file(input_file, output_file, password):
    command = f'openssl enc -d -aes-256-cbc -pbkdf2 -in {input_file} -out {output_file} -pass pass:{password}'
    subprocess.run(command, shell=False, creationflags=subprocess.CREATE_NO_WINDOW)

with keyboard.GlobalHotKeys({
    '<ctrl>+<alt>+e+f': lambda: encrypt_file(decrypted_file, encrypted_file, password),
    '<ctrl>+<alt>+d+f': lambda: decrypt_file(encrypted_file, decrypted_file, password),
}) as keys:
    keys.join()