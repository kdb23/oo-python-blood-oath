from .bloodoath import BloodOath

class Cult:

    all = []

    def __init__(self, name, city, year, slogan):
        self.name = name
        self.city = city
        self.year = year
        self.slogan = slogan
        Cult.all.append(self)

    @property
    def oaths(self):
        return[o for o in BloodOath.all if o.cult == self]
    
    @property
    def followers(self):
        return[o.follower for o in self.oaths]

    def recruit_follower(self, follower):
        return BloodOath("2012-12-12", self, follower )
    
    def cult_population(self):
        return len(self.followers)

    @classmethod
    def find_by_name(cls, name_string):
        for c in cls.all:
            if c.name == name_string:
                return c
        return 'Cult Not Found'
    
    @classmethod
    def find_by_location(cls, loc):
        return [l.name for l in cls.all if l.city == loc]
    
    @classmethod
    def find_by_founding_year(cls,found_year):
        return [ c.name for c in cls.all if c.year == found_year]