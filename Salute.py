
def Hu():
  print("Ciao sono Hu BoYong Stefano")

  return True

def Corti():
  return True

def Solari():
  print("Questa porzione del Programma e' gestita da Rocco")

  return True

def Esci():
  print("Programma Finito")
  return False

def main():
  menu_chose = {
    1 : Hu,
    2 : Corti,
    3 : Solari,
    0 : Esci,
  }
  
  running = True

  print("Selezionare la Scelta: \n\t1.Hu\n\t2.Corti\n\t3.Solari\n\t0.Esci")
  while running == True:
    wtd = input("Inserire la scelta: ")

    if wtd not in menu_chose.keys():
      print("Inavlid input")
      input("Enter to continue...")
      continue
    else:
      running = menu_chose[wtd]
 

    input("Enter to continue...")
  
#---------------------------------------------------------------------
if __name__== "__main__":
    main()
