def pour_water(juga, jugb):
    print("%d\t%d" % (juga, jugb))

    if jugb == fill:
        print("Target achieved!")
        return
    elif jugb == max2:
        pour_water(0, juga)
    elif juga != 0 and jugb == 0:
        pour_water(0, juga)
    elif juga == fill:
        pour_water(juga, 0)
    elif juga < max1:
        pour_water(max1, jugb)
    elif juga < (max2 - jugb):
        pour_water(0, juga + jugb)
    else:
        pour_water(juga - (max2 - jugb), jugb + (max2 - jugb))


max1 = int(input("Enter capacity of Jug A: "))
max2 = int(input("Enter capacity of Jug B: "))
fill = int(input("Enter target amount: "))

pour_water(0, 0)

# Enter capacity of Jug A: 5
# Enter capacity of Jug B: 12
# Enter target amount: 1
# 0       0
# 5       0
# 0       5
# 5       5
# 0       10
# 5       10
# 3       12
# 0       3
# 5       3
# 0       8
# 5       8
# 1       12
# 0       1
# Target achieved!
