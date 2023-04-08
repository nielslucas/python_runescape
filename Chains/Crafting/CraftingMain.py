import pyautogui as gui
import time
import random
from Chains.Crafting.Rings.SapphireRing import *
from Chains.Crafting.Necklace.RubyNecklace import *

gui.FAILSAFE = True


class CraftingMain:
    def __init__(self):
        self.waitTimes = (0.25, 1)
        self.ItemService = RubyNecklace()

    def Execute(self):
        print('lets do some crafting')
        self.GetItems()
        self.WalkToSemler()
        self.SelectToCraftItem()
        self.BackToBank()
        self.DropItemToBank()


    def GetItems(self):
        self.GetItem((847, 860), (534, 555))
        self.GetItem((889, 900), (534, 555))


    def GetItem(self, xRange, yRange):
        time.sleep(random.uniform(*self.waitTimes))

        x = random.randint(*xRange)
        y = random.randint(*yRange)
        gui.moveTo(x, y)

        time.sleep(random.uniform(*self.waitTimes))

        gui.click(button='right')
        self.GetXQuantity(x, y)

    def GetXQuantity(self, x, y):
        time.sleep(random.uniform(*self.waitTimes))
        x = x + random.randint(-60, 60)
        y =  y + random.randint(66, 70)
        gui.moveTo(x, y)
        gui.click()

    def ClickOnLocation(self, xRange, yRange, buttonType = 'left'):
        time.sleep(random.uniform(*self.waitTimes))
        x = random.randint(*xRange)
        y = random.randint(*yRange)
        gui.moveTo(x, y)
        gui.click(button=buttonType)
        return (x, y)

    def WalkToSemler(self):
        self.ClickOnLocation((1375, 1385), (375, 383))

    def SelectToCraftItem(self):
        self.DoesPixelHaveColorCode(696, 309, 73, 64, 52)

        self.ClickOnLocation(self.ItemService.CraftItemLocationX, self.ItemService.CraftItemLocationY)
        time.sleep(random.uniform(23, 26))
        print('And we are done?')

    def BackToBank(self):
        time.sleep(random.uniform(*self.waitTimes))
        (x, y) = self.ClickOnLocation((19, 92), (812, 863), 'right')
        y = y + 40
        self.ClickOnLocation((x-10,x+10), (y-1,y+1))

        self.DoesPixelHaveColorCode(720, 64, 72, 62, 51)

    def DropItemToBank(self):
        time.sleep(random.uniform(*self.waitTimes))
        (x, y) = self.ClickOnLocation((1750, 1765), (750, 765), 'right')
        y = y + 70
        self.ClickOnLocation((x - 8, x + 8), (y - 1, y + 1))

    def DoesPixelHaveColorCode(self, x, y, r, g, b):
        for i in range(1000):
            time.sleep(1)
            rgb = gui.pixel(x, y)
            print(rgb)
            if(rgb[0] != r):
                continue
            if (rgb[1] != g):
                continue
            if (rgb[2] != b):
                continue

            break



