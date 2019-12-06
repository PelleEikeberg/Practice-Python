from OddOrEven import Number

"""here we want to expand upon the class Numbers from OddOrEven.py
"""

class AdvancedNumber(Number):
    def __init__(self, number=None):
        """inherits the __init__ from Number if just normal number
        or uses new method if its a list. 
        """
        if type(number) != list:
            print("hei")
            super().__init__(float(number))
        elif type(number) == list:
            self.number = []
            for i in number:
                self.number.append(i)
        else:
            raise TypeError("number added inn does not fill any of the type categories ´int/float/list´")

    
    def divisors(self, printing=True, returning=False):
        """fuction for finding the divisors of a number

        Arguments
        -------------
        printing: bool
            a bool if the fuction should print
        
        returning: bool
            a bool if we should return the dictonary of the divisors
        

        Returns
        -------------
        None / dic: dictonary
            if returning == True, then will return the divisors as the value of the key = number
        """
        if type(self.number) == list:
            numbers = self.number
        else:
            try:
                number = float(self.number)
            except ValueError:
                print("the number must be float/int if not list")


        def divisorsof(num):
            divisors = []
            for i in range(1, int(num)+1):
                if num % i == 0:
                    divisors.append(i)

            return divisors

        try: # checks if numbers is created.
            check = numbers
            dic = {}
            for numb in numbers:
                dic[numb] = divisorsof(numb)
            
            if printing:
                for i in dic:
                    if i % 1 != 0:
                        print(i, " is diviseble by ", dic[i], end=" ")
                        print("!the program cant calculate for non .0 floats") 
                    else:
                        print(i, " is diviseble by ", dic[i])
        except:
            try:
                dic = {}
                dic[number] = divisorsof(number)

                if printing:
                    if number % 1 != 0:
                        print(number, " is diviseble by ", dic[number], end=" ")
                        print("!the program cant calculate for non .0 floats") 
                    else:
                        print(number, " is diviseble by ", dic[number])
            except:
                raise RuntimeError("!the program could not find a list or float/int of number")
                
        if returning:
            return dic





if __name__ == "__main__":
    x = AdvancedNumber(float(3.2))
    x.divisors()

    y = AdvancedNumber([1,2.2,4, 222])
    y.divisors()