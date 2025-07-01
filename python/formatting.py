import sys

states = []
capitals = []

for arg in sys.argv[1:]:
    parts = arg.split()
    states.append(parts[0])
    capitals.append(parts[1])

print("STATE      CAPITAL")
print("-------------------")

for i in range(len(states)):
    print("%-10s %s" % (states[i], capitals[i]))
