# polymorphism
class peacock:
    def fly(self):
        print("peacock can fly")
    def swim(self):
        print("peacock can't swim")
class fish:
    def swim(self):
        print("fish can swim ")
    def fly(self):
        print("fish can't fly")
# common interface
    def flying_test(bird):
        bird.fly()
# instantiate object
name_1=peacock()
name_2=fish()
# object passing
flying_test(name_1)
flying_test(name_2)