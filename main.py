Heroes = {
  "AAA" : "Starlord",
  "AAB" : "Drax",
  "ABA" : "Black Panther",
  "ABB" : "Doctor Strange",
  "BAA" : "Winter Soldier",
  "BAB" : "Rocket Raccoon",
  "BBA" : "Captain America",
  "BBB" : "Iron Man",
  "CAA" : "Groot",
  "CAB" : "Hulk",
  "CBA" : "Spiderman",
  "CBB" : "Mantis",
  "DAA" : "Thanos",
  "DAB" : "Thor",
  "DBA" : "Hawkeye",
  "DBB" : "Black Widow",
  "DBC" : "MoonByul"
}

name = input ("Hello, what is your name? ")
answer = input ("Hello " + name + "! Ready to play? Y or N ")
print()
if answer.upper() == "Y":
  question1 = input ("What color would you choose? (Choose A, or B)\nA) Blue \nB) Red\n")
  question2 = input ("What game would you play? (Choose A, or B)\nA) Minecraft \nB) Fortnite\n")
  question3 = input ("What sport would you prefer? (Choose A, or B)\nA) Tennis \nB) Basketball\n")
  choice = question1 + question2 + question3
  wait = input ("Do you want to know your favorite marvel Hero? Y/N: ")
  if wait.upper() == "Y":
    print("Your Favorite Hero is " + Heroes[choice.upper()])
  else:
    print("Okay")
else:
  print("Okay, Bye bye")
