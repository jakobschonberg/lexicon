#C1, C2
class Printer():
    def display_status(self):
        return "printer status"

class Screen():
    def display_status(self):
        return "screen status"

#C3
objects = [
    Printer(),
    Screen()
]

#C4
for object in objects:
    print(object.display_status())

#C5
#See lab10_A5.... really... why are we doing the same thing again?