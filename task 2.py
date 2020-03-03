class Vegetable:
    def __init__(self, mass0):
        name = ''
        self.mass = mass0
class Potato(Vegetable):
    def __init__(self, mass0):
        self.mass = mass0

    name = 'картофель'

class Onion(Vegetable):
    def __init__(self, mass0):
        self.mass = mass0

    name = 'лук'

class Carrot(Vegetable):
    def __init__(self, mass0):
        self.mass = mass0

    name = 'морковь'

class Egg:
    def __init__(self, original0):
        self.original = original0

class Meat:
    def __init__(self, original0, mass0):
        self.original = original0
        self.mass = mass0

class Sause:

    def __init__(self):
        self.sause = []
        self.egg = 0
        self.meat = 0
        self.m_carrot = 0
        self.m_onion = 0
        self.m_potato = 0
    def add(self, other):

        if type(other)==Egg:
            self.sause.append(other)
            self.egg +=1
        elif type(other)==Meat:
            self.meat += other.mass
            self.sause.append(other)
        elif type(other)==Potato:
            self.m_potato += other.mass
            self.sause.append(other)

        elif type(other)==Carrot:
            self.m_carrot += other.mass
            self.sause.append(other)

        elif type(other)==Onion:
            self.m_onion += other.mass
            self.sause.append(other)
        else:
            print("Ввели некорректный объект. Информация не записана")

    def recept(self):
        #получение ингредиентов соуса
        i = 0
        print("Для соуса необходимо:")
        p = False
        m = False
        e = False
        c = False
        o = False
        while i < len(self.sause):
            if type(self.sause[i]) == Egg and e == False:
                e = True
                if self.egg != 0:
                    print(str(self.egg) + "яицо " +  self.sause[i].original)

            elif type(self.sause[i]) == Meat and m == False:
                m = True
                if self.meat != 0:
                    print(str(self.meat) + "грамм " + self.sause[i].original +" мяса")
            elif type(self.sause[i]) == Potato and p == False:
                p = True
                if self.m_potato != 0:
                    print(str(self.m_potato) + "грамм картофеля")

            elif type(self.sause[i]) == Carrot and c == False:
                c = True
                if self.m_carrot != 0:
                    print(str(self.m_carrot) + "грамм морковки")

            elif type(self.sause[i]) == Onion and o == False:
                o = True
                if self.m_onion != 0:
                    print(str(self.m_onion) + "грамм лука")

            i += 1


v1 = Potato(150)
v2 = Onion(300)
v3 = Carrot(400)
m = Meat("(говядина)", 600)
e = Egg("(куриное)")

s = Sause()
s.add(v1)
s.add(v2)
s.add(v3)
s.add(m)
s.add(e)
s.add(e)
s.add(e)
s.recept()