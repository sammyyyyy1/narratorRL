import cohere
import time
import re
from .KEYS import COHERE_KEY

t0 = time.time()
co = cohere.Client(COHERE_KEY)


# text="""Tout baguette carrement peu meilleur disruptif voila evidemment. Omelette pouvoir du ouais de carrement meilleur plus fais chier. merde. Nous guillotine greve boulangerie omelette car omelette.. Le client est treas im. portant merci, le client. sera Suivi par le client. Ene n'a pas de justice,. pas de resultat, pas de ligula,. et la vallee veut - lasauce. Morbi mais qui veut vendre une couc. he de contenu triste d' internet. Etre ivre maintenant, mais ne. as etre ivre maintenant, mon urne est d' une gra. dans e ue beaute, dans l'element mais un elle livre. es faciles du. budget, qu'il soit be. d.de temps pour dignissim et. Je 
# ne. [. as chez moi, ca _ va 6tre moche dans le vestibule. Mais aussi des proteines de Pour avant la fin de la. semaine, qui connait le poison, le etter. ama NA 
# TT naan"""

def clean_text(text):
    # make all lowercase
    words = [word.lower() for word in text]
    cleaned_string = ''.join(words)

    # remove punctuation
    import string
    cleaned_string = cleaned_string.translate(str.maketrans('','', string.punctuation))

    #remove extra spaces
    cleaned_string = " ".join(cleaned_string.split())

    # spell out contractions
    import contractions
    cleaned_string = contractions.fix(cleaned_string)

    # remove line breaks
    cleaned_string = cleaned_string.strip()

    # remove numbers (generally not needed)
    # cleaned_string = ''.join([i for i in text if not i.isdigit()])

    # Refactoring common emoticons (probably also not needed)
    # EMOTICONS = {
    # u":‑)":"Happy face or smiley",
    # u":)":"Happy face or smiley",
    # u":-]":"Happy face or smiley",
    # u":]":"Happy face or smiley",
    # u":-3":"Happy face smiley",
    # u":3":"Happy face smiley",
    # u":->":"Happy face smiley",
    # u":>":"Happy face smiley",
    # u"8-)":"Happy face smiley",
    # u":o)":"Happy face smiley",
    # u":-}":"Happy face smiley",
    # u":}":"Happy face smiley",
    # u":-)":"Happy face smiley",
    # u":c)":"Happy face smiley",
    # u":^)":"Happy face smiley",
    # u"=]":"Happy face smiley"
    # }
    # ans = re.compile(r"(' + '|'.join(k for k in EMOTICONS) + ')")
    # cleaned_string = ans.sub(r"", cleaned_string)

    return cleaned_string

# t1 = time.time()

# print(t1 - t0)

