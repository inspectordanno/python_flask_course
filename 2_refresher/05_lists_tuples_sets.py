l = ["Bob", "Rolf", "Anne"] # list can be modified, order is guaranteed
t = ("Bob", "Rolf", "Anne") # tuple can't be modified, order is guranteed
s = {"Bob", "Rolf", "Anne"} # can be modified but no duplicates, no subscript notation

l.append("Smith")
print(l)

l.remove("Bob")
print(l)

s.add("Ryan")
print(s)