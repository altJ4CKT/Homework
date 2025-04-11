lights = []

class lightSwitch:
    lightSwitches: list

    def __init__(self, lightSwitches):
        self.lightSwitches = lightSwitches
        self.createLights()

    def createLights(self):
        for i in range(1, 11):
            temp=[]
            for j in range(1, 11):
                temp.append(False)
            self.lightSwitches.append(temp)

    def lightSwitchProblem(self, num):
        counter=1
        for i in range(0, len(self.lightSwitches)):
            for j in range(0, 10):
                if counter % num == 0:
                    self.lightSwitches[i][j] = not self.lightSwitches[i][j]
                counter += 1
        for row in self.lightSwitches:
            row = str(row)
            print("".join(row))
        print()





x: lightSwitch = lightSwitch(lights)
for i in range(1, 100):
    lightSwitch.lightSwitchProblem(x, i)
