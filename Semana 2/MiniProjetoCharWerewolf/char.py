import json
from unicodedata import name

'''character = {
  "name": "Klaus",
  "concept": "Guardião Urbano",
  "tribe": "Presas de Prata",
  "auspice": "Ahroun",
  "race": "Hominideo",

  "atributos": {
    "fisicos": {
      "forca": 3,
      "destreza": 2,
      "vigor": 3
    },
    "sociais": {
      "carisma": 2,
      "manipulacao": 2,
      "aparencia": 3
    },
    "mentais": {
      "percepcao": 3,
      "inteligencia": 2,
      "raciocinio": 2
    }
  },

  "habilidades": {
    "talentos": {
      "briga": 3,
      "esquiva": 2
    }
  },

  "vantagens": {
    "furia": 4,
    "gnose": 2,
    "forca_vontade": 3
  }
}

print(character)'''


def save_character(character):
  with open("character.json", "w") as file:
    json.dump(character, file, indent=4)

def load_character():
  with open("character.json", "r") as file:
    return json.load(file)
  
def create_character():
    name = input("Enter character name: ")
    concept = input("Enter character concept: ")
    tribe = input("Enter character tribe: ")
    auspice = input("Enter character auspice: ")
    print("Defina os atritutos Fisicos:")
    strenght = int(input("Força: "))
    dexterity = int(input("Destreza: "))
    stamina = int(input("Vigor: "))
    print("Defina os atritutos Sociais:")
    charisma = int(input("Carisma: "))
    manipulation = int(input("Manipulação: "))
    appearance = int(input("Aparência: "))
    print("Defina os atritutos Mentais:")
    perception = int(input("Percepção: "))
    intelligence = int(input("Inteligência: "))
    wits = int(input("Raciocínio: "))
    print("Defina as habilidades e talentos: ")
    brawl = int(input("Briga: "))
    dodge = int(input("Esquiva: "))
    print("Defina as vantagens: ")
    rage = int(input("Fúria: "))
    gnosis = int(input("Gnose: "))
    willpower = int(input("Força de Vontade: "))
    
    character = {
        "name" : name, 
        "concept" : concept,
        "tribe" : tribe,
        "auspice" : auspice,
        "attributes" : {
          "physical" : {
            "strength" : strenght,
            "dexterity" : dexterity,
            "stamina" : stamina
          },
          "social" : {
            "charisma" : charisma,
            "manipulation" : manipulation,
            "appearance" : appearance
          },
          "mental" : {
            "perception" : perception,
            "intelligence" : intelligence,
            "wits" : wits
          }
        },
        "skills" : {
          "talents" : {
            "brawl" : brawl,
            "dodge" : dodge
          }
        },
        "advantages" : {
          "rage" : rage,
          "gnosis" : gnosis,
          "willpower" : willpower
        }
      }
    
    return character

  