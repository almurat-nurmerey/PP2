# ex 1: break the loop when the condition is met
archons_list = ["Toronto", "Copenhagen", "London", "Vienna", "Bern", "Lisbon", "Rome"]
for archon in archons_list:
    print(archon)
    if (archon == "London"):
        break


# ex 2: break the loop but not inclusively
archons_list = ["Toronto", "Copenhagen", "London", "Vienna", "Bern", "Lisbon", "Rome"]
for archon in archons_list:
    if archon == "Bern": # 1 step after
        break
    print(archon)
