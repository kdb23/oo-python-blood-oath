from .bloodoath import BloodOath

class Cult:
    
    all = []

    def __init__(self, name, city, founding_year, slogan):
        self.name = name
        self.city = city
        self.year = founding_year
        self.slogan = slogan
        Cult.all.append(self)

    @property
    def oaths(self):
        return [ o for o in BloodOath.all if o.cult == self]
    
    @property
    def followers(self):
        return [ o.follower for o in self.oaths]
    
    def recruit_follower(self, follower):
        BloodOath("2023-03-31", self, follower)

        # how to check : len(c1.followers)---2
        # adam = Follower("adam", 43, "cant stop wont stop")--
        # len(c1.followers)---3
        # c1.followers[-1].name---'adam'

    @property
    def cult_population(self):
        return len(self.followers)
    
    @classmethod
    def find_by_name(cls, name_string):
        for c in cls.all:
            if c.name == name_string:
                return c
            else:
                return "Cult Not Found"
    
    @classmethod    
    def find_by_location(cls, location_string):
        return [c for c in cls.all if c.city == location_string]
    
    @classmethod
    def find_by_founding_year(cls,found_year):
        return [ c for c in cls.all if c.year == found_year]
