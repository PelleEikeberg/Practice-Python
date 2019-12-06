class Number():
    def __init__(self, number=None):
        if number == None:
            try:
                number = float(input("can you please specify the number?"))
            except:
                raise ValueError("the number must be given as float or int")
        try:
            self.number = float(number)
        except:
            raise ValueError("the number must be given as float or int")
    
    def isEven(self, nnumber=None, dividenum=2):
        """a fuction that takes number from the class and determens if it is odd or even

        Arguments
        -------------
        None 
        
        / Number: int/float
            a number which shall be determened

        
        Returns
        ---------
        Even: bool
            returns True/Flase depending on the number is Odd or Even
        """
        number = self.number

        if nnumber != None:
            number = float(nnumber)

        elif float(number % dividenum) == float(0):
            return True
        
        else:
            return False



if __name__ == "__main__":
    number = 1
    dividenumber = 3
    x = Number(number)
    if x.isEven() == True:
        print(number, "is an Even number")
        if number % 4 == 0:
            print("and ", number, "is diviseble by 4")
    elif x.isEven() == False:
        print(number, "is an Odd number")