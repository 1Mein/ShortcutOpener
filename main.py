import keyboard
from translator import scan_code_to_key
import jsonIntreaction
import pystray
from pystray import MenuItem as item
from PIL import Image
import threading

currentComb: str = ''
is_logging: bool = False

icon = pystray.Icon("messi", Image.open("messi.jpg"), "ShortcutOpener")





def keyLogger(key):
    global currentComb, is_logging
    currentComb += scan_code_to_key[key.scan_code]

    if currentComb[-2:] == '\\\\':
        is_logging = not is_logging

        if is_logging:
            icon.icon = Image.open("neymar.jpg")
        else:
            icon.icon = Image.open("messi.jpg")
            
        currentComb = ''
    elif not is_logging and len(currentComb)>1:
        currentComb = currentComb[-1:]

    if not is_logging:
        return
    
    

    if len(currentComb) > 10:
        currentComb = currentComb[-5:]
    
    if jsonIntreaction.checkShortcut(currentComb[-5:]):
        currentComb = ''


def on_exit(icon, item):
    icon.stop()
    keyboard.unhook_all()
    exit()

def run_tray_thread():
    icon.menu = pystray.Menu(item("Exit", on_exit))
    icon.run()



def main():
    tray_thread = threading.Thread(target=run_tray_thread, daemon=True)
    tray_thread.start()

    keyboard.on_press(keyLogger)
    tray_thread.join()

if __name__ == '__main__':
    main()