



class Stringinstance():
    def __init__(self, string=None):
        """a class that takes a tring an converts it to a list of individual objects in list
        """
        if string == None:
            try:
                self.string = []
                string = str(input("please enter string:"))
                for i in string:
                    self.string.append(i)
            except:
                raise RuntimeError("the str from input was not accepted")
        else:
            try:
                self.string = []
                for i in str(string):
                    self.string.append(i)
            except:
                raise RuntimeError("the string was not accepted in __init__")
    

    def palindrome(self, Print=True, Return=False):
        """a fuction that tries to flipp a list and see if the content and indexes is the same
        """
        flipped = self.string[::-1]

        palindrome = True

        for i in range(len(flipped)):
            if flipped[i] != self.string[i]:
                palindrome = False
            else:
                pass
        

        if palindrome:
            if Print:
                print(self.string)
                print("the string is a palindrome! :)")
            else:
                pass
            if Return:
                return True
            else:
                pass
        else:
            if Print:
                print(self.string)
                print("the string is not a palindrome :/")
            else:
                pass
            if Return:
                return False
            else:
                pass

if __name__ == "__main__":
    sstring = "agnes i senga"
    X = Stringinstance(sstring)
    X.palindrome()

    ssstring = "hei i gås"
    Y = Stringinstance(ssstring)
    Y.palindrome()