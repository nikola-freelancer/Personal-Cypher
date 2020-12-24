abc = ['a', 'b', 'c', 'd', 'e', 
'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
  's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
go_on=True

def cypher (the_text, the_shift, the_direction):
  cypher_text=""
  if the_direction=="decode":
    the_shift*=-1
  for char in the_text:
    if char in abc:
      position=abc.index(char)
      new_position=position+the_shift
      cypher_text+=abc[new_position]
    else:
      cypher_text+=char
  
  print(f"The text has been {the_direction}d.\n Here it is: {cypher_text}")

while go_on:
  direction=input("Encode or Decode?\n").lower()
  text=input(f"What text do you want {direction}d?\n")
  shift=int(input("Determine the shift: "))
  shift%=26
  cypher(text, shift, direction)
  answer=input("Continuing? If not write N, \nOtherwise write anything else. ")
  if answer=="N":
    go_on=False
    print("Exiting. ")
  else:
    go_on=True