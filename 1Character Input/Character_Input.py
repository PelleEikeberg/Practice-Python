
class Person():
    """A class to store info about a person
    """
    def __init__(self, Name=None, Age=None):
        """The Initial Person, needs Name and age. if Name and age is not specified the program
        will ask for it.

        Arguments
        --------------
        Name: None/str
            the name of the Person
        
        Age: None/str
            the age of person
        """
        if Name == None and Age == None:
            nameandage = input("what is your name and age? please say in ´name age´ or ´name,age´")

            try:
                name, age = nameandage.split()
            except:
                try:
                    name, age = nameandage.split(",")
                except:
                    raise RuntimeError("the name and age did not match ´name age´ or ´name,age´")
        
            try:
                self.name, temp = neme.split(",")
            except:
                self.name = name; self.age = age
        
        elif type(Name) == str and type(Age) == str:
            self.name = Name; self.age = Age
        
        else:
            raise TypeError("name and age must be given in str type")

    
    def years_100(self, year=100, pr=True, ret=False, msg=True):
        """Prints the year the Person reaches 100years or the []years specified.
        also prints the number of years ´left´ until 100/[] years

        user can also say if the want the values returned or printed or printed with message

        Arguments
        -----------------
        year: str/int/list.
            the year/goal to calculate given the starting year/position.

        pr: bool
            if the program should print year Person.age == 100 or not
            if msg == True a small message will follow.
        
        ret: bool
            if the program should return the year the Person.age == 100 or not
            if msg == True, will also return the number of years left.
        
        msg: bool
            if the print or ret should use the advanced version


        Returns
        ----------
        None:
            if ret == False

        year: int
            the year the user will turn 100
            if ret == True & msg == False
        
        year, numbertill: int, int
            the year , numbertill the year the Person turns 100
        """
        Name = self.name; Age = self.age
        
        if pr==True or ret == True:
    
            if type(Age) == str:
                try:
                    Age = int(Age)
                except:
                    try:
                        Age = int(input("whats your Age?"))
                    except:
                        raise TypeError("the Age must be given in type == int or str")

            if type(year) != list:
                if Age > year:
                    numbertill = Age - year
                elif Age < year or Age == year:
                    numbertill = year - Age
            if type(year) == list:
                if Age > all(year):
                    numbertill = []
                    for i in year:
                        numbertill.append(i - Age)
                else:
                    raise ValueError("the values of year must be all less than age")
            

            from datetime import datetime
            now = datetime.now()
            currentyear = now.year


        else: # if print == False and ret == False then we dont need to do anything really
            return None



        if pr == True:
            birth = (currentyear - Age)
            if type(year) != list:
                year100 = birth + year
            if type(year) == list:
                year100 = []
                for i in year:
                    year100.append(birth + int(i))
            


            if msg == True:
                if type(year) != list:
                    mess = str("is the year " + str(Name) + " will turn " + str(year) + " years")
                if type(year) == list:
                    mess = []
                    for i in year:
                        mess.append(str("is the year " + str(Name) + " will turn " + str(i) + " years"))

            else:
                mess = ""

                
            if type(year) != list:
                print(year100, mess)
            if type(year) == list and type(year100) == list:
                year100year = zip(mess, year100)
                for i,j in year100year:
                    print(j, i)

            if msg == True:
                if type(year) != list:
                    print(numbertill, "is the year " + str(Name) + " will turn ", str(year))
                if type(year) == list:
                    numbertillyear = zip(numbertill, year)
                    for i,j in numbertillyear:
                        print(str(i), "is the year " + str(Name) + " will turn ", str(j))

        
        if ret == True:
            birth = (currentyear - Age)
            year100 = birth + 100

            if msg == False:
                return year100
            
            if msg == True:
                return year100, numbertill




if __name__ == "__main__":
    Pelle = Person("Pelle", "20")
    Pelle.years_100(year=[30,50,100])









