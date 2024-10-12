# 🚁 🌲 🌊 🔥 🟩 🏥 🏦 💛 🪣 ☁ ⚡ 🏆

from map import Map
from helicopter import Helicopter as Heli
from clouds import Clouds
from pynput import keyboard
import time
import os
import json

TICK_SLEEP = 0.05
TREE_UPDATE = 50
CLOUDS_UPDATE = 100
FIRE_UPDATE = 75
MAP_W, MAP_H = 20, 10
MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)} # Клавиши передвижения

def on_release(key):
    global heli, tick, clouds, field
    c = key.char.lower()
    if c in MOVES.keys(): # обработка движения вертолёта
        dx, dy = MOVES[c][0], MOVES[c][1]
        heli.move(dx, dy)
    elif c == 'f': # f - сохранение игры
        data = {"helicopter": heli.export_data(),
                "clouds": clouds.export_data(),
                "map": field.export_data(),
                "tick": tick}
        with open("level.json", "w") as lvl:
            json.dump(data, lvl)
    elif c == 'g': # g - загрузка игры
        with open("level.json", "r") as lvl:
            data = json.load(lvl)
            heli.import_data(data["helicopter"])
            clouds.import_data(data["clouds"])
            field.import_data(data["map"])        

field = Map(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)
heli = Heli(MAP_W, MAP_H)

listener = keyboard.Listener(
    on_press=None, 
    on_release=on_release)
listener.start()

tick = 1
while True:
    os.system("cls" if os.name == 'nt' else "clear")  # Очистка экрана для Windows/Unix
    field.process_helicopter(heli, clouds)
    heli.print_stats()
    field.print_map(heli, clouds)
    print(f"Tick: {tick}")
    tick += 1
    time.sleep(TICK_SLEEP)
    if tick % TREE_UPDATE == 0:
        field.generate_tree()
    if tick % FIRE_UPDATE == 0:
        field.update_fires(heli)
    if tick % CLOUDS_UPDATE == 0:
        clouds.update()