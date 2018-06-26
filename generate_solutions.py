#!/usr/bin/env python3
''' Calculate all of the solutions to the puzzle and then
    write them to a file for input to another program. '''

# open the file
filename = 'solns'
my_file = open(filename, 'w')

for s1 in [False, True]:
    for s2 in [False, True]:
        for s3 in [False, True]:
            for s4 in [False, True]:
                for s5 in [False, True]:
                    for s6 in [False, True]:
                        for s7 in [False, True]:
                            for s8 in [False, True]:
                                for s9 in [False, True]:
                                    for s10 in [False, True]:
                                        net1 = not s2
                                        net2 = s3 ^ s4
                                        net3 = s5 or s6
                                        net4 = not (s6 and s7)
                                        net5 = net1 ^ net2
                                        net6 = net1 or net2
                                        net7 = not (net3 and net4)
                                        net8 = not (s1 and net5)
                                        net9 = net6 ^ net7
                                        net10 = net9 or s8 or s9 or s10
                                        net11 = not (s1 or s4 or s6 or s7 or s10)
                                        net12 = not net10
                                        net13 = net10 ^ net10
                                        net14 = not (net12 ^ net13)
                                        net15 = net8 and net11 and net14
                                        net16 = net15 and s8 and s9
                                        net17 = s2 and net16
                                        output = net17

                                        if output:
                                            my_file.write("%d%d%d%d%d%d%d%d%d%d\n"
                                                  % (s1,s2,s3,s4,s5,s6,s7,s8,s9,s10))

my_file.close()
