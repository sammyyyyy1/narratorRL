from ..env import COHERE_SECRET_KEY
import cohere
from cohere.responses.classify import Example

def is_legible(text):
    co = cohere.Client(COHERE_SECRET_KEY) 
    response = co.classify(
    model='large',
    inputs=["text"],
    examples=[Example("jjfiasfijss", "Gibberish"),
                Example("Hello, how are you", "Legible"),
                Example("a. _-F. , =. _ S _. eee eo PReESCA!. OLY. (tel el. ye VA LA. _. ms. inet. 8CEro - fi pa rola, L-valine (47 rN ,\"}\nLOG a. _-F. , =. _ S _. eee eo PReESCA!. OLY. (tel el. ye VA LA. _. ms. inet. 8CEro - fi pa rola, L-valine (47 rN ,", "Gibberish"),
                Example("At Cohere, we are committed to breaking down barriers and expanding access to cutting-edge NLP technologies that power projects across the globe. By mak", "Legible"),
                Example("a i yt 3 j    n 87 9 c d i o ps w E j I  O ", "Gibberish"),
                Example("Identification (Drivers License, Student Cards, or Health Cards)\nNotebook + Pen\nLaptop and Charger\nPhone and Charger\nHeadphones\n\n\n", "Legible"),
                Example("\"text\": \":,. BAESS. x. N. S. console. 1] og (text - Le dia Speech. _ tex es,. ee nst pause = async OF = aor await Speech. pause()j. nimated. sequence([ animated. timing (pa tovalue: Lao duration: 520, . usenativeorivers : ue DD tart (( y = fDi & me 1. useAnL. pros EMS ee \' pone - 1oad. ania vn vt 4 puto. i meni\"", "Gibberish"),
                Example("US es. BOBBY RD. 7. 32 33 3 35 36 37 3S 22 Pas = 23 T- 2 me. . animated. tewalees 1 geration: 52 a\"}\nLOG US es. BOBBY RD. 7. 32 33 3 35 36 37 3S 22 Pas = 23 T- 2 me. . animated. tewalees 1 geration: 52 a", "Gibberish"),
                Example("ieuhruoeirwo 7364", "Gibberish"),
                Example("mAJOR LEAGUE HACKING. Activate $1 00 in free Azure credits! rhackathon project On the cloud by activating your Azure for Students offer. Seamlessly deploy from GitHub and use services like machine learning, low code tools, and much more!. Build you. hackp.aci microsoft", "Legible"),
                Example("what no one h as done anything at all richard has like stone tools sam has iron tools people didn't join cause hackathon this weekend i grinded because i am a jobles if you join you will be the 4th person how about it", "Legible"),])
    legibility = response[0].confidence
    return legibility > 0.75