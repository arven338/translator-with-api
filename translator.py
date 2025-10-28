import translators as ts # Import library

# Source translator class
class AI_Translator:
  # Constructor with default-parameters
  def __init__(self, source_language='auto', target_language='en'):
    self.source_language = source_language
    self.target_language = target_language

  # Base translate function
  def translate(self, text):
    try:
      translated = ts.translate_text(query_text=text, translator='google', from_language=self.source_language, to_language=self.target_language)
      return translated
    except Exception as e:
      return str(e)
