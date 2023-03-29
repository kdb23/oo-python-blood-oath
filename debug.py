import ipdb
from lib import *

# test your code here
# e.g.

# f1 = Follower( 'Emiley', 31, 'Living the Dream' )
# c1 = Cult( 'Heavens Gate', 'San Diego', 1974, 'Human Metamorphosis' )

# bo1 = BloodOath( '2019-09-16', f1, c1 )

# c1.followers => ???
# f1.cults => ???

f1 = Follower( 'Emiley', 31, 'Living the Dream' )
f2 = Follower( 'Chandler', 23, 'Work Hard Play Hard' )

c1 = Cult( 'Heavens Gate', 'San Diego', 1974, 'Human Metamorphosis' )
c2 = Cult( 'Hanging Rock Camping', 'Greensboro', 1992, 'Go Go Power Rangers' )
c3 = Cult('Dakota', 'AK', 2023, 'push to main')

bo1 = BloodOath( '2019-09-16', f1, c1 )
bo2 = BloodOath( '1992-12-08', f2, c2 )


print( "Mwahahaha!" )
ipdb.set_trace()