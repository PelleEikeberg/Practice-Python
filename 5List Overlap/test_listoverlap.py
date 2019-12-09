from listoverlap import TwoList

def test_comparingvalues():

    list1 = [2,3,5]
    list2 = [1,2,4]
    #two should be the common number

    LList = TwoList(list1, list2)

    commonlist = LList.samevalues(True, False)


    assert [2.0] == commonlist, "the TwoList class could not identify all the common numbers"


def test_comparingvalueinstr():

    list1 = ["4", 2, "3"]
    list2 = "4,1,2"
    #4 and 2 should be common number


    LList = TwoList(list1, list2)

    commonlist = LList.samevalues(True, False)


    
    assert commonlist == [4,2], "the TwoList class could not identify all the common numbers, some str values could not be interperted as float/int"

    
def test_onelistoftwo():


    list1 = [1,2,5]
    list2 = [2,4,6]
    list3 = [list1, list2]

    LList = TwoList(list3)

    commonlist = LList.samevalues(True, False)


    assert commonlist == [2.0], "the program fails to find the common number of one list containing two lists"




if __name__=="__main__":

    test_comparingvalues()
    test_comparingvalueinstr()
    test_onelistoftwo()

