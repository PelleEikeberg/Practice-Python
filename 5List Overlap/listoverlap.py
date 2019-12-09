
class TwoList():
    def __init__(self, a, b=None):
        """

        Arguments
        ------------
        a: list/str
            a list or str in format "2,3,4"

        b: list/str/None
            a list or str in format "1,2,5"
            if False will just store a
        """
        def picktingitemout(a):
            ret = []
            for i in a:
                try:
                    ret.append(float(i))
                except:
                    ret.append(i)
                    
            return ret

        try:
            if type(a) == list and len(a) == 2:
                self.a = picktingitemout(a[0])
                self.b = picktingitemout(a[1])
            else:
                self.a = picktingitemout(a)
                self.b = picktingitemout(b)

        except:
            raise ValueError("""the list/lists is not in the way the program accepts, error in __init__""")



    def samevalues(self, returning=True, printing=False):
        """a fuction that takes the two lists from __init__ and uses then to find the common factors.

        Arguments
        """


        a = self.a
        b = self.b

        samevalues = []
        
        for i in a:
            if i in b:
                samevalues.append(i)
        

        if printing:
            print(samevalues, "\n is the values that are in both lists")
        

        if returning:
            return samevalues



if __name__ == "__main__":
    list1 = [1,2,3,4,5,6,7,8,9,10]
    list2 = [1,8]
    list3 = [[1,2], [1,2,3]]

    x = TwoList(list1, list2)
    x.samevalues(False, True)

    y = TwoList(list3)
    y.samevalues(False, True)

    z = TwoList("1,4,3", [1,2, 9,"4"])
    z.samevalues(False, True)
