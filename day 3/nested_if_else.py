print("Students' result")

isPresent = True

if isPresent:
    marks = int( input("Enter the obtained marks: "))
    if marks >= 90:
        print("You obtained excellent marks.")
    elif marks > 40:
        print("You obtained good marks.")
    else:
        print("You obtained poor marks.")
else:
    print("Not present")