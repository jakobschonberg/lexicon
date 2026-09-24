#G1
class CPU:
    def __init__(self, model):
        self.model = model

#G2
class Computer:
    def __init__(self, brand, cpu):
        self.brand = brand
        self.cpu = cpu

#G3
cpu = CPU("NVIDIA 5090")
computer = Computer("Acer", cpu)

#G4
print(computer.brand, computer.cpu.model)

#G5
#Just because you CAN inherit doesn't mean it's always a good idea to inherit.
#Inheritance should only be used when the child class describes the parent class in an extending way.
#Further, maybe we'd like the computer to have 0, 1 or more than 1 CPU, by
#making Computer inherit CPU we would force it to be a CPU. Meaning it has all attributes and methods of CPU once and only once.
#That's maybe not what we want.
#In my experience "HAS-A" architecture is used a lot more than inheritance and rightly so.

#G6
#Car / Engine (HAS-A)
#Manager / Employee (IS-A)
#Course / Teacher (HAS-A)
#Phone / Device (IS-A)