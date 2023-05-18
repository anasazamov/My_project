from mtranslate import translate

def to_translate(matn, tillar="en"):
    tarjima_natija = translate(matn, tillar)
    return tarjima_natija

