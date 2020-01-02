
#the value holds the key of what each type beats
value = {"r": "s", "p":"r", "s":"p"}

def rps():
  #hand is determended by the input, but the first sign is what is checked. could be r/p/s
  hand1 = input("hand1? \n rock, paper, or sissor? \n")
  hand2 = input("hand2? \n rock, paper, or sissor? \n")

  if value[hand1[0]] == hand2[0]:
    print("hand1 beats hand2!")
    if input("new game?")[0] == "y":
      print("\n*\n*\n*")
      rps()
  if hand1[0] == hand2[0]:
    print("both choose the same")
    if input("new game?")[0] == "y":
      print("\n*\n*\n*")
      rps()
  else:
    print("hand2 beat hand1!")
    if input("new game?")[0] == "y":
      print("\n*\n*\n*")
      rps()

rps()
