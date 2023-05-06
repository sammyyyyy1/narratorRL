from string import punctuation

from cohere import Client
from contractions import fix as fix_contractions

cohere = Client()


def clean_text(text):

    text = text.translate(str.maketrans("", "", punctuation))
    text = " ".join(text.split())
    text = fix_contractions(text)
    text = text.strip()

    # remove numbers (generally not needed)
    # cleaned_string = ''.join([i for i in text if not i.isdigit()])
    #
    # Refactoring common emoticons (probably also not needed)
    # EMOTICONS = {
    #     u":‑)": "Happy face or smiley",
    #     u":)": "Happy face or smiley",
    #     u":-]": "Happy face or smiley",
    #     u":]": "Happy face or smiley",
    #     u":-3": "Happy face smiley",
    #     u":3": "Happy face smiley",
    #     u":->": "Happy face smiley",
    #     u":>": "Happy face smiley",
    #     u"8-)": "Happy face smiley",
    #     u":o)": "Happy face smiley",
    #     u":-}": "Happy face smiley",
    #     u":}": "Happy face smiley",
    #     u":-)": "Happy face smiley",
    #     u":c)": "Happy face smiley",
    #     u":^)": "Happy face smiley",
    #     u"=]": "Happy face smiley"
    # }
    # ans = re.compile(r"(' + '|'.join(k for k in EMOTICONS) + ')")
    # cleaned_string = ans.sub(r"", cleaned_string)

    return text
