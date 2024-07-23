#creating a dictonary

programming_dictonary = {
    "name" : "Dipesh Shrestha",
    "father" : "Dipak Shrestha",
    "mother" : "Sangita Shrestha",
    "sister" : "Sayara Shrestha",
}

#accesing the dictonary value
print(programming_dictonary["name"])

#adding the new key value to the dictonary
programming_dictonary["uncle"] = "Subash  Shrestha"
print(programming_dictonary)

#edit the value to the existing dictonary
programming_dictonary["father"] = "Deepak Shrestha"
print(programming_dictonary["father"])

#creating empty dictonary
empty_dictonary = {}    
print(empty_dictonary)

#looping through the dictonary
number = 0
for key in programming_dictonary:
    number += 1
    print(f"{number}. {key} : {programming_dictonary[key]}.")