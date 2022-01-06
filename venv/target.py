class Target:
    '''A class for the target person to store the attributes of the target.'''
    # define constructor with parameters as simple strings the user could input. Final attribute is a comma separated strng the user could enter
    # the attributes parameter is meant to encapsulate words, abberivations, or phrases one would expect to find in sources related to the target
    def __init__(self, name, job, location, school, attributes):
        # may be put a try-except here incase these attributes are null, will come to this later
            # likely will make these the mandatory attributes, minimum required to do searches
        # these are the minimum required attributes to do searches
        self.name = name
        self.loc = location
        self.job = job
        self.school = school

        # the attributes parameter must be converted from a comma separated string into a list of strings using the .split() function
        # attributes will be used to search profiles and webpages
        extras = attributes.split(", ")

        # add common attributes to the list so they can be used in searches as well
        extras.extend((self.name, self.loc, self.job, self.school))
        self.attributes = extras


        # create list to store search results of instagramSearch, each element of the list is of type Result. List can be later used to rank search results for user
        self.instagramResults = []


    # define a function to return the instagram results, ordered by the highest score
    def getInstagramResults(self):
        s = ""

        # sort the instagram results by descending score using the sort() function, the key is a simple lambda function to check that the score of the result is
        self.instagramResults.sort(reverse=True, key=lambda x: x.score)

        # create easy to read string for the user and return it
        for i in range(len(self.instagramResults)):
            s += "Result at: " + self.instagramResults[i].url + " matched " + str(self.instagramResults[i].score) + " out of " + str(len(self.attributes)) + " attrbutes \n"

        return s