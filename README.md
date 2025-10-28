# Translator
This project demonstrates a simple translator that uses the API to access a text translation service.

## Features
- **Library**: This translator using a translators library.
- **Simplicity**: Almost anyone can make such a translator for free.
- **Flexible customization**: You can add your own functionality to this translator if you want.

## Requirements
- translators: <code>pip install -U translators</code>
- Python 3.9

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/arven338/translator-with-api.git
   cd translator-with-api
2. Install library:
   ```bash
   pip install -U translators
   ```

## Usage

### Importing the Module
Import the classes from `translator.py`:
```Python
import translator
from translator import * # Importing all classes
```
Using example:
```Python
# Create object.
ts = AI_Translator() # You can change the language if you wish.

source = "Я очень обожаю вишневый коктель!" # Script Automatically detects the language (default).
translated = ts.translate(source)
print(translated) # Outputing.
