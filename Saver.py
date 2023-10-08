tim = "Hey this tool will really help you organizing your finances bro!!"

class Finanzen:
  def __init__(self, gehalt, fixkosten):
    self.gehalt = gehalt
    self.fixkosten = fixkosten
    self.__calc()
    
  def __calc(self):
    self.ueberfluss = self.gehalt - self.fixkosten
    self.fix = (int(self.gehalt) * 0.5)
    self.spar = (int(self.gehalt) * 0.3)
    self.fun = (int(self.gehalt) * 0.2)
    
  def usdInEuro(usd):
    return usd * 0.8
    
  def binIchReich(self):
    if self.gehalt > Finanzen.usdInEuro(10000):
      print("Yup bist reich!")
    else:
      print("haha ne du Opfer yolo")
    
def saver():
  gehalt = int(input("Wie hoch ist dein aktuelles Gehalt Netto? "))
  fixKosten = int(input("Wie hoch sind deine Fixkosten? "))
  finanzen = Finanzen(gehalt, fixKosten)
  finanzen.binIchReich()
  Finanzen.usdInEuro(5)
  if finanzen.ueberfluss > 0:
    print("Ich helfe dir mal mit deinen Finanzen! ")
    print("Du solltest "+ str(finanzen.spar)+ " sparen bro")
    
    
if __name__ == "__main__":
    saver()