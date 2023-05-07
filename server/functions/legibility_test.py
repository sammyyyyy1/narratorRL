from ..env import COHERE_SECRET_KEY
import cohere
from cohere.responses.classify import Example

def is_legible(text):
    co = cohere.Client(COHERE_SECRET_KEY) 
    response = co.classify(
    model='large',
    inputs=[text],
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
                Example("what no one h as done anything at all richard has like stone tools sam has iron tools people didn't join cause hackathon this weekend i grinded because i am a jobles if you join you will be the 4th person how about it", "Legible"),
                Example("Avil 7 7 estoelling outhor of THE GLASS HOTEL Uf 000 STATION ELEVEN", "Gibberish"),
                Example("""hy ety UL thi i id Mee i iby Ve ty 4 4 oh 4 iy My Wy yr LL oe i v j 4 1 haf y Un st 5 jah Meg 1 NAY f Ui Hai Atte ig bane ky 4 preg Ma IRS ree ve i f Dye 7 2 3 Ne ae f La s my be f2 4 A k oPre 1 Ba a wo i ae NA y ks 1 P tie Aas Core OA Oe A ON s Tie haan Vey Ie wht if 0s F ei p ih f f ret YOU ARE Ah ete thle aay oh y Ad Whe ta ey cp Tey a lodiooyes doin i f 4 A ela E EN aL Po tod 4 i f 
                           Pea Shea Br trek ae 4 W y RA Pa i A fs yt Wir AE View et 2 WAY try MM gat 8 pil hike 4 4 4 7 tb posh f Leg f i q ie Ach 4 f DA ia ie Laer oh Aaa tg eee rey ray m i iy ov Ne o A lh X ts t f 4 s y baie A lan a f 44 i baa hay q 7 4 ae f fy ef i 4 dy on""", "Gibberish"),
                Example("""e not Sylvie Not Sylvie Not Sylvie Flsewhere they found skeletons on the beach Because small pox had already arrived In the signing line after that nights lecture signing her name over and over again Olives thoughts kept drifting toward disaster To Xander with best wishes Olive Llewellyn To Claudio with best wishes Olive Llewellyn To Sohail with best wishes Olive Llewellyn To Hyeseung with best wishes Olive Llewellyn Was there going to be another pandemic A new cluster of cases had appeared in New Zealand that morning Stel room that night was mostly beige with a painting of ravagantly petalled pink Earth flowera peony over""","Legible"),
                Example("qowieurytqowieurytqowieurytqowieurytqowieuryt", "Gibberish"),
                Example("The quick brown fox jumps over the lazy dog", "Legible"),
                Example("kfudlsf4y4o23uhfkjf23", "Gibberish"),
                Example("I went to the store to buy some milk and bread", "Legible"),
                Example("2@#fowir82#$dkfn92*", "Gibberish"),
                Example("The sun was setting behind the mountains, casting a warm orange glow over the valley", "Legible"),
                Example("askjdfha;sldkfjqwerpoiquwer", "Gibberish"),
                Example("In the beginning God created the heavens and the earth", "Legible"),
                Example("9u23n4fiq28@#JDOIFJ)_@!#J!DQ8f", "Gibberish"),
                Example("She sells seashells by the seashore", "Legible"),
                Example("12345qwertyuiopasdfghjklzxcvbnm67890", "Gibberish"),
                Example("The cat sat on the mat", "Legible"),
                Example("aoeuidhtnspyfgcrlqjkxbmwvz", "Gibberish"),
                Example("To be or not to be, that is the question", "Legible"),
                Example("kjasfkhcalkweu#(*Y#@(H#@*C(JH)@", "Gibberish"),
                Example("Roses are red, violets are blue", "Legible"),
                Example("poaisdfj293rjfnskdfo238ru2#@(JD!Q9f", "Gibberish"),
                Example("The moon shone brightly in the night sky", "Legible"),
                Example("""reappeared nearer the towering foothills, flowed through canyons where eagles soared on currents of rising airbob shmurda hahaha cup cup laptop""", "Legible"),
                Example(""" Its a binary condition She h dn She had not ng enough She se been sleeping gh She set down her water glags When they ventured ashore they found villages that could sed hundreds b a Willagee have hou but those villages were abandoned When they ventured farther they realized that the forest was a grav e yard This was the part of the lecture that had been easy before giving birth to her daughter and was now almost impossible""", "Legible"),
                ])
    legibility = response[0].labels["Legible"].confidence
    print(legibility)
    return legibility > 0.75