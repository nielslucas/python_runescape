import pyautogui as gui
import time
import random
gui.FAILSAFE = True

class HAMain:
    def __init__(self):
        self.waitTimes = (0.25, 1)

    def Execute(self):
        (x, y) = self.GetRandomPosition()
        # print("x" + x + "y" + y)

        for i in range(25):
            time.sleep(random.uniform(*self.waitTimes))

            shouldWeChangePoistion = random.randint(0, 10) > 5
            if(shouldWeChangePoistion):
                random.uniform(2, 4)
                (x, y) = self.GetRandomPosition()
                # print("new postion x" + x + "y" + y)

            gui.moveTo(x, y)
            gui.click()
            time.sleep(random.uniform(*self.waitTimes))
            gui.click()
            time.sleep(random.uniform(2,4))

    def GetRandomPosition(self):
        x = random.randint(1608, 1615)
        y = random.randint(832, 845)

        return (x, y)
