import csv
import sys


def main():
    txt =""
    rows=[]

    # TODO: Check for command-line usage
    """
    if (sys.argv != 3):
        sys.exit("command-line")
    """
    # TODO: Read database file into a variable
    with open (sys.argv[1]) as file:
        reader =csv.DictReader(file)
        for row in reader:
            rows.append(row)

        field=reader.fieldnames
        field.pop(0)

    # TODO: Read DNA sequence file into a variable
    with open (sys.argv[2],"r") as f:
            txt = f.read()
    # TODO: Find longest match of each STR in DNA sequence
    matches = {}
    for k in field:
        matches[k] = longest_match(txt,k)

    # TODO: Check database for matching profiles
    match = 0
    bol = 0
    for people in rows:
        for i in matches:
            if matches[i] == int(people[i]):
                match +=1
        if match == len(matches) :
            print(people["name"])
            bol = 1
        match=0
    if bol == 0:
        print ("No match")








    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
