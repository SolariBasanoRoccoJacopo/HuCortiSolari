
def Hu():
  pass

def Corti():
  pass

def Solari():
  pass

def main():
  menu_chose = {
    1 : Hu,
    2 : Corti,
    3 : Solari,
  }
  
  print("Selezionare la Scelta: \n\t1.Accedi\n\t2.Registrati\n\t3.Esci")
  while True:
    wtd = input("Inserire la scelta: ")

    if wtd not in menu_chose.keys():
      print("Inavlid input")
      input("Enter to continue...")
      continue
    else:
      menu_chose[wtd]
 

    input("Enter to continue...")
  
#---------------------------------------------------------------------
if __name__== "__main__":
    main()
