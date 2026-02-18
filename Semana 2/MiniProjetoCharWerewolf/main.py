from char import character, save_character, load_character, create_character
import json

def main():
    while True:
      print("\n1 - Create character")
      print("2 - Save character")
      print("3 - Load character")
      print("4 - Exit")
      

      option = input("Choose an option: ")

      if option == "1":
        create_character()
      elif option == "2":
        save_character(character)
      elif option == "3":
        loaded_character = load_character()
        print(loaded_character)
      elif option == "4":
        print("Exiting program...")
        break
      else:
        print("Invalid option, try again.")