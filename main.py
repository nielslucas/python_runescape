import pyautogui as gui
import time
from Chains.Crafting.CraftingMain import *
from Chains.HA.HAMain import *
gui.FAILSAFE = True

time.sleep(5)

for i in range(1):
    time.sleep(1)
    main = CraftingMain()
    main.SelectToCraftItem()