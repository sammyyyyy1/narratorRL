from cohere import Client

from server.env import COHERE_SECRET_KEY


def get_summary(text):

    cohere = Client(COHERE_SECRET_KEY)
    response = cohere.summarize(
        model='summarize-xlarge',
        temperature=1,
        length='medium',
        extractiveness='high',
        format='bullets',
        text=text
    )
    summary = response.summary

    return summary


def get_lang(text):

    cohere = Client(COHERE_SECRET_KEY)
    arr = [text]
    languages = []
    results = co.detect_language(arr).results
    for item in results:
        languages.append(item.language_name)
        
    return languages[0]


# wip
def get_keywords(text):
    pass



