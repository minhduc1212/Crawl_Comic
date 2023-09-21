from unidecode import unidecode

def remove_accents(text):
    return unidecode(text)

accent_removed_text = remove_accents('bố')
print(accent_removed_text)