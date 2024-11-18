def cels_fah(celsius):
  return(celsius * 9/5) + 32

def fah_cels(fahrenheit ):
  return(fahrenheit -32) * 5/9

while True:
  option = int(input("Enter your option > \n"
                        "1. celsius to fahrenheit \n"
                        "2. fahrenheit to celsius \n"
                        "3. exit \n"
                    ))
  if option == 1:
    celsius = float(input("Enter the temperature  in celsius"))
    print("The temperature in fahrenheit is", cels_fah(celsius))
  elif option == 2:
    fahrenheit = float(input("Enter the temperature  in fahrenheit"))
    print(" The temperature in celsius is", fah_cels(fahrenheit))
  else:
    print("quit")
    break
        
