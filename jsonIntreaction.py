import json
import webbrowser  
import os
import subprocess



def checkShortcut(comb: str) -> dict:
    with open('shortcuts.json', 'r', encoding="utf-8") as file:
        data = json.load(file)
    
    for shortcut in data['shortcuts']:
        if shortcut['combination'] in comb:
            return make_action(shortcut['action'])
        
    return make_action({"type": "Not Found"})


def make_action(action: dict):
    if action['type'] == "Not Found":
        return False
    elif action['type'] == "website":
        website(action['link'])
    elif action['type'] == "path":
        path(action['path'])
    elif action['type'] == "app":
        app(action['name'])

    return True

def website(link: str):
    webbrowser.open(link, new=0, autoraise=True)

def path(path: str): 
    os.startfile(f"{path}")

def app(name: str):
    subprocess.run(f"{name}")