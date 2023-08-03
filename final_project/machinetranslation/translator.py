"""
    This module implements translation function
"""

from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    """Function translates text from english to french
    Args:
    Returns:
        String: French text
    """
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text


def french_to_english(french_text):
    """Function translates text from french to english
    Args:
        englishText ( String ): French text
    Returns:
        String: English text
    """
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
