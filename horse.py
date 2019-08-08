class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return self.name

    def self_instruction(self):
        print("私は{}です。{}歳です。".format(self.name, self.age))

    def get_old(self):
        self.age += 1

class Rider(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.my_horse = []

    def __lshift__(self, horse):
        if isinstance(horse, Horse):
            if horse.owner.name == "":#野生の馬のとき
                horse.owner = self
                self.my_horse.append(horse)
            elif horse.owner != self:
                horse.owner.my_horse.pop(horse.owner.my_horse.index(horse))
                horse.owner = self
                self.my_horse.append(horse)
        else:
            print("馬じゃないよ")

    def self_instruction(self):
        super().self_instruction()
        print("私の持ち馬は{}頭です。".format(len(self.my_horse)))

    def print_my_horse(self):
        print("私の持ち馬は、")
        for horse in self.my_horse:
            print(" {}, {}歳".format(horse.name, horse.age))
        print("です。")

class Horse(Animal):
    horse_list = []
    def __init__(self, name, age, owner=None):
        super().__init__(name, age)
        self.owner = Rider("", 0)#仮の持ち主を入れておく
        if owner != None:
            owner << self
        self.horse_list.append(self)

    def self_instruction(self):
        super().self_instruction()
        print("私の主は{}です。".format(self.owner.name))


sato = Rider("sato", 21)
suzuki = Rider("suzuki", 30)
uma = Horse("uma", 21, sato)
umauma = Horse("umauma", 4, sato)
uuma = Horse("uuma", 2, suzuki)
yaseiba = Horse("yaseiba", 0)

uma.get_old()
yaseiba.get_old()

suzuki << uma
suzuki << uma
sato << yaseiba

sato.self_instruction()
sato.print_my_horse()
suzuki.self_instruction()
suzuki.print_my_horse()
print(Horse.horse_list)
