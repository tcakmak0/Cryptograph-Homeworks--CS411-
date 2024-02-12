cipherText = "NLPDLC"
candidateText = ""
for i in range(1, 26):
    for c in cipherText:
        candidateText += chr(ord('A') + ((ord(c) - ord('A')) - i) % 26)

    print("For key: ", i, "Possible plain text is: ", candidateText)
    candidateText = ""  # Clears the candidate text for next search.

    # By using the 2 for loops above, we check all possible shifts.
    # Since all the capital letters are consecutively ordered in ASCII, taking their distance from 'A' will gives us letter's index
    # By subtracting all possible values in mod 26 we obtain all possible shifts in this configuration.
