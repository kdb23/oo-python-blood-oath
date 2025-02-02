from .bloodoath import BloodOath

class Follower:

    all = []

    def __init__(self, name, age, life_motto ):
        self.name = name
        self.age = age
        self.life_motto = life_motto
        Follower.all.append(self)

    @property
    def oaths(self):
        oath_list = []
        for oath in BloodOath.all:
            if oath.follower == self:
                oath_list.append(oath)
        return oath_list
    
    @property
    def cults(self):
        return [ o for o in self.oaths]
    
    def join_cult(self, cult_instance):
        return BloodOath("2023-04-01", cult_instance, self)

    @classmethod
    def of_a_certain_age(cls, fol_age):
        return [f.name for f in cls.all if f.age >= fol_age]