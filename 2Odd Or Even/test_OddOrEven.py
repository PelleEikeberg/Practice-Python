from OddOrEven import Number

def test_numbergetsaccsepted():
    number = float(1)

    succsess = True

    try:
        x = Number(number)
        y = Number(number=2)
    except:
        succsess = False
    
    assert succsess == True, "the program did not accept a float, might have error in __init__"


def test_2isEven():
    number = 2
    x = Number(2)
    succsess = x.isEven()
    assert succsess, "2 is not an even number, Runtime error in Number.isEven()"




if __name__ == "__main__":

    test_numbergetsaccsepted()
    test_2isEven()
