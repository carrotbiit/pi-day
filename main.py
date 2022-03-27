# password = "ryanisthebest"
# teacher = input("")

while True:
  name = input("your full name:")
  classroom = input("your class:")
  confirm = input("confirm data:/nare you sure this data is clear, correct, and you would like to proceed? (yes/no)")
  if confirm.lower() == "yes":
    break
print("how to use:\n- type digits of pi AFTER the decimal point\n- only type numbers, or else the results will not be accurate\n- when you have typed all your digits of pi press ENTER")
while True:
  pi = input("pi = 3.")
  pi_list = []
  pi_list_correct = []
  for i in pi:
    pi_list.append(i)
  
  
  with open("pi.txt") as file:
    for i in range(len(pi_list)):
      char = file.read(1)
      pi_list_correct.append(char)
  
  
  
  error = False
  count = 0
  for i in range(len(pi_list)):
    if pi_list[i] == pi_list_correct[i] and error == False:
      count += 1
    else:
      error = True
  proceed = input("confirm input:/nare you sure this is your final answer? (yes/no)")
  if proceed.lower() == "yes":
    break
  else:
    print("requizing...")

print("thank you for your submission")

data = "name: "+ name+ ", class: "+ classroom+ ", digits memorized: "+ str(count)+ "\n"
statsdump = "name: "+ name+ ", class: "+ classroom+ ", input: "+ pi+ "\n"


stats = open("scores.txt", "a")
stats.write(data)
stats.close()
inputs = open("inputs.txt", "a")
inputs.write(statsdump)
inputs.close()
