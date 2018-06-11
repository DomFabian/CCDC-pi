
print("Successful combinations are:")
print("s1:\ts2:\ts3:\ts4:\ts5:\ts6:\ts7:")

counter = 0
total = 2 ** 7

for s1 in [False, True]:
    for s2 in [False, True]:
        for s3 in [False, True]:
            for s4 in [False, True]:
                for s5 in [False, True]:
                    for s6 in [False, True]:
                        for s7 in [False, True]:
                            net1 = not s2
                            net2 = s3 ^ s4
                            net3 = s5 or s6
                            net4 = not (s6 and s7)
                            net5 = net1 ^ net2
                            net6 = net1 or net2
                            net7 = not (net3 and net4)
                            net8 = not (s1 and net5)
                            net9 = net6 ^ net7
                            net10 = not (net8 and net9)
                            output = not net10

                            if output:
                                print(s1,s2,s3,s4,s5,s6,s7, sep='\t')
                                counter += 1

print()
print('And ' + str((counter / total) * 100) + '% of combinations work.')

