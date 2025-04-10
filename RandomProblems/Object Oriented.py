class Car:
    def driverDoor(self):
        print("driver opened door!")
    def engineSound(self):
        print("kkkkkkrummmmm")

class Ferrari(Car):
    def engineSound(self):
        print("ZZZZVROOOOOOOOMMMM")

if __name__ == "__main__":
    ferrari = Ferrari()
    ferrari.driverDoor()
    ferrari.engineSound()