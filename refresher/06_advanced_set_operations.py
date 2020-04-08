friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
print('difference:', local_friends)

oneValueTuple = (30,) # need trailing comma for a one value tuple
otherOneValuetupe = 30 # no parens also work

empty = abroad.difference(friends)
print('empty:', empty)

total = friends.union(abroad)
print('total:', total)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print('intersection:', both)



