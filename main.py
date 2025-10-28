from translator import * # Import the module

# creating translator object
translator = AI_Translator()

# Creating cycle for translating
while True:
  source = input("Translate: ")
  translated_text = translator.translate(source)
  print(translated_text)
  print()
