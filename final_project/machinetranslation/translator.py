
"""Translator"""

import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def create_translator_instance():
    """Create IBM Translator Instance."""

    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(url)

    return language_translator


def english_to_french(english_text):
    """translation to French"""
    language_translator = create_translator_instance()
    translation_to_france = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = translation_to_france.get('translations')[0]['translation']
    return french_text


def french_to_english(french_text):
    """translation to English"""
    language_translator = create_translator_instance()
    translation_to_english = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = translation_to_english.get('translations')[0]['translation']
    return english_text