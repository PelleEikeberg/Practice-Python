

class Number():
    def __init__(self, number=None):
        if number == None:
            try:
                innputt = input("please state number in ´2´ (example) or in list ´[1,2,3]´")
                try:
                    number = list(innputt)
                except:
                    number = float(innputt)

            except ValueError:
                        print("the number does not match any of the working types (int/float/list)")
        if type(number) == list:
            self.number = []
            for i in number:
                try:
                    self.number.append(float(i))
                except TypeError:
                    print("all items in list number must be int/float")
        
        if type(number) == int or type(number) == float:
            try:
                self.number = float(number)
            except RuntimeError:
                print("number was accepted as float/int but could not be turned into float")

    def printlessthan(self, numberlessthan=5, msg=False):
        numbers = self.number

        assert (type(numbers) == list), "the number must be a list"


        numbersless = []
        for i in range(len(numbers)):
            if float(numbers[i]) > numberlessthan:
                numbersless.append(numbers[i])
            
        print(numbersless)
               
        if msg:
            print("is the numbers in list less than", numberlessthan)
        

if __name__ == "__main__":
    x = Number([1,2,3,4,5,6,7,8,9,10,1])
    x.printlessthan()
    print("\n"*2)
    x.printlessthan(6, True)