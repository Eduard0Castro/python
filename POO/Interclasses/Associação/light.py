from typing import Type

class LightSwitch:
    def __init__(self, comodo):
        self.comodo = comodo

    def turn_on(self):
        print(f"Turning on the light {self.comodo}")
    
    def turn_off(self):
        print(f"Turning off the light {self.comodo}")

class Person:

    def __init__(self, name):
        self.name = name

    def turn_on(self, light_switch: Type[LightSwitch]):
        print(self.name, end=" is ")
        light_switch.turn_on()

    def turn_off(self, light_switch: Type[LightSwitch]):
        print(self.name, end=" is ")
        light_switch.turn_off()

    def sleep(self):
        print(f"{self.name} is going to sleep right now")


if __name__ == "__main__":
    dinning_room = LightSwitch("Dinning room")
    living_room = LightSwitch("Living room")

    hugo = Person("Hugo")

    dinning_room.turn_on()
    hugo.turn_off(dinning_room)
    hugo.sleep()
    
