print("Welcome the Ip address to binary converter!!\n")
def gather_ip_address():
  ip_address_list = []
  ip_address = input("\nEnter IP address: ")
  ip_address_list = list(ip_address.split("."))
  while '' in ip_address_list:
    ip_address_list.remove('')
  ip_address_list = [int(item) for item in ip_address_list]
  binary_ip = f"The ip address converted to binary is {ip_address_list[0]:08b}.{ip_address_list[1]:08b}.{ip_address_list[2]:08b}.{ip_address_list[3]:08b}"
  print(binary_ip)

while True:    
  try: 
    gather_ip_address()
    break
  except:
    print("Error: Invalid IP address.\n")

answer = ""

while True:    
  try: 
    try:
      answer = input("Would you like to convert another IP address? (y/n): ")
      answer = answer.lower()
      answer = answer.replace(".", "")
    except:
      print("Error: Invalid input.\n")

    if answer == "y":
      gather_ip_address()

    elif answer == "n":
      print("Thank you for using the IP address to binary converter! Goodbye!")
      break

    else:
      print("Error: Invalid input.\n")
  except:
    print("Error: Invalid IP address.\n")


if answer == "n":
  exit()

ip_address_list = ip_address_list[:-1]