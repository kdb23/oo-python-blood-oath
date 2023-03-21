import ipdb
from lib import *

# test your code here
# e.g.

# f1 = Follower( 'Emiley', 31, 'Living the Dream' )
# c1 = Cult( 'Heavens Gate', 'San Diego', 1974, 'Human Metamorphosis' )

# bo1 = BloodOath( '2019-09-16', f1, c1 )


# c1.followers => ???
# f1.cults => ???

c1 = Cult("Little Stinkers", "Adam's Living Room", 2023, "My Code isn't working!!!")
c2 = Cult("Watchtower Society", "New York", 1888, "To fear God is not to")
c3 = Cult( 'Heavens Gate', 'San Diego', 1974, 'Human Metamorphosis' )
c3 = Cult( 'Heavens Gate 2.0', 'San Diego', 1974, 'Go Go Power Rangers' )

f1 = Follower( 'Emiley', 31, 'Living the Dream' )
f2 = Follower( "Bryn", 27, "May I ask a question?")
f3 = Follower( "Kimberly", 31, "Just Do it")

b1 = BloodOath( "1999-10-31", c1, f3)
b4 = BloodOath( "1999-10-31", c1, f3)
b2 = BloodOath( "2004-04-27", c1, f2)
b3 = BloodOath( "1887-05-30", c2, f1)



print( "Mwahahaha!" )
ipdb.set_trace()