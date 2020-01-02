import getpass
#the value holds the key of what each type beats
value = {"r": "s", "p":"r", "s":"p"}

def rps():
  #hand is determended by the input, but the first sign is what is checked. could be r/p/s
  hand1 = getpass.getpass("hand1? \n rock, paper, or sissor? \n").lower()
  hand2 = getpass.getpass("hand2? \n rock, paper, or sissor? \n").lower()

  if value[hand1[0]] == hand2[0]:
    print("hand1 beats hand2!")
    if input("new game?").lower()[0] == "y":
      print("\n*\n*\n*")
      rps()
  if hand1[0] == hand2[0]:
    print("both choose the same")
    if input("new game?").lower()[0] == "y":
      print("\n*\n*\n*")
      rps()
  else:
    print("hand2 beat hand1!")
    if input("new game?").lower()[0] == "y":
      print("\n*\n*\n*")
      rps()

rps()
