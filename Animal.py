class animal:
    sName = ""
    nAge = 0
    sType = ""

    def __init__(self, name, age, type):
        self.sName = name
        self.nAge = age
        self.sType = type

    def __str__(self):
        return self.sName + "[Age: " + str(self.nAge) + ", Type: " + self.sType + "]"
        ## Adding comment to test


    # Check values of anmal objects to see if they match. Return true when animals share exact values. 
    def __eq__(self, other):
        returnVal = False
        
        if isinstance(other, animal):
            if self.sType == other.sType:
                if self.sName == other.sName:
                    if self.nAge == other.nAge:
                        returnVal = True 

        return returnVal

    def __lt__(self, other):
        returnVal = False
        if isinstance(other, animal):
            if self.sType < other.sType:
                returnVal = True

        return returnVal
