from enum import Enum


class LANGUAGES(Enum):  # Language = 'language file suffix'
    ENGLISH = 'en'
    EN = 'en'
    CHINESE_SIMPLIFIED = 'chs'
    CHS = 'chs'


DEFAULT_LANGUAGE = LANGUAGES.ENGLISH
languages_mapping = {}


def load_lang(lang: LANGUAGES = DEFAULT_LANGUAGE, sep: str = ',',
              line_sep: str = '\n'):
    with open('local/lang_%s.csv' % lang.value, encoding='utf-8') as f:
        mapping = {}
        lines = f.read().split(line_sep)
        for line in lines:
            if line != '' and not line.startswith('#'):
                pair = line.split(sep)
                mapping[pair[0]] = pair[1]
        languages_mapping[lang] = mapping


def local(id: str, lang: LANGUAGES = DEFAULT_LANGUAGE):
    # if the selected language is not loaded, load that language
    if lang not in languages_mapping.keys():
        load_lang(lang)
    # if this id is not defined in this language
    if id not in languages_mapping[lang].keys():
        # if this id is also not defined in the default language
        if id not in languages_mapping[DEFAULT_LANGUAGE].keys():
            return id
        return languages_mapping[DEFAULT_LANGUAGE][id]
    return languages_mapping[lang][id]


if __name__ == '__main__':
    print(local('ARC_EMITTER_1', LANGUAGES.CHS))
