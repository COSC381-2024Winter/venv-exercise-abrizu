import pyjokes
import random2
import pandas as panda

def main():
  names = ['Aaron', 'Michael', 'Brizuela']

  # randomly select a name from the list using random2
  random_name = random2.choice(names)

  # create a dataframe to store names using panda
  dataframe = panda.DataFrame({'Name': names})
  joke = pyjokes.get_joke()

  print(f"Hello, {random_name}!")
  print(joke)

main()
