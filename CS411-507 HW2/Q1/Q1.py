def subgroupGenerator(order):
    residues = []
    generators = []
    mult = 1
    for candidate in range(2,101):
        for i in range(1,101):
            mult = (mult * candidate) % 101                     # Multiplication in mod 101 (n = 101)
            if mult not in residues:
                residues.append(mult)
            else:
                # If we find an element for second time for some i, that means we are in a cycle without completing all possible residues
                # Break the loop and look for the next candidate
                break
        if len(residues) == order:              
            #If the number of unique residues equal to order of the group then the candidate is a generator
            generators.append(candidate)

        #Before checking the next element, restart the setup by clearing mult and residues list
        residues.clear()
        mult = 1
        

    print(sorted(generators))
    print(len(generators))


subgroupGenerator(25)
