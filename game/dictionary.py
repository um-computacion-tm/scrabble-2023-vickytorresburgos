
# class DictionaryConnectionError(Exception):
#     pass

# def validate_word(word):
#     search = dle.search_by_word(word=word)
#     if search is None:
#         raise DictionaryConnectionError()
#     return search.meta_description != 'Versión electrónica 23.6 del «Diccionario de la lengua española», obra lexicográfica académica por excelencia.'

from pyrae import dle
print(dle.search_by_word(word='hola'))
{'title': 'hola | Definición | Diccionario de la lengua española | RAE - ASALE', 'articles': [{'id': 'KYtLWBc', 'lema': {'lema': 'hola', 'index': 0, 'female_suffix': ''}, 'supplementary_info': [{'text': 'Voz expr. (Voz expresiva); cf. (confer) ingl. (inglés o inglesa) hello, al. (alemán o alemana) hallo.'}], 'definitions': [{'index': 1, 'category': {'abbr': 'interj.', 'text': 'interjección'}, 'abbreviations': [{'abbr': 'U.', 'text': 'Usado, usada, usados o usadas'}], 'sentence': {'text': 'como salutación familiar.'}, 'examples': []}, {'index': 2, 'category': {'abbr': 'interj.', 'text': 'interjección'}, 'abbreviations': [{'abbr': 'p. us.', 'text': 'poco usado o usada, poco usados o usadas'}, {'abbr': 'U.', 'text': 'Usado, usada, usados o usadas'}, {'abbr': 'U. t. repetida.', 'text': 'Usada también repetida'}], 'sentence': {'text': 'para denotar extrañeza, placentera o desagradable.'}, 'examples': []}, {'index': 3, 'category': {'abbr': 'interj.', 'text': 'interjección'}, 'abbreviations': [{'abbr': 'desus.', 'text': 'desusado, desusada, desusados o desusadas'}, {'abbr': 'Era u.', 'text': 'Era usado o usada'}], 'sentence': {'text': 'para llamar a los inferiores.'}, 'examples': []}], 'complex_forms': [], 'other_entries': []}]}