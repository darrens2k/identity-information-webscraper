

# defining a dictionary parser to parse through the input dictionary to define important attributes like name, school, and then group less important attributes into a list
def dictionaryParser(inputDict):
    # may be put a try-except here incase these attributes are not in the inputDict
    name = inputDict.get("name")
    loc = inputDict.get("loc")
    job = inputDict.get("job")
    school = inputDict.get("School")

    # define list to store the above attributes and all other attributes in the dictionary
    attributes = []

    # iterate through the dictionary with a for loop
    for x in inputDict.values():
        attributes.append(x)

    # return all the attributes so they can be used in the search functions
    return name, loc, job, school, attributes