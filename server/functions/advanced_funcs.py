from cohere import Client

from server.env import COHERE_SECRET_KEY


def get_summary(text):

    cohere = Client(COHERE_SECRET_KEY)
    response = cohere.summarize(
        model='summarize-xlarge',
        temperature=0.1,
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
    results = cohere.detect_language(arr).results
    for item in results:
        languages.append(item.language_name)

    return languages[0]


def get_keywords(text):

    cohere = Client("nCnCpljhAaNwrkZjVDllnDaR5JCbF3NJRcRK7Z33")

    prompt = f"""
    Passage: Climate change is one of the biggest challenges facing our planet. The burning of fossil fuels, deforestation, and other human activities are causing the Earth's temperature to rise, leading to more extreme weather events, rising sea levels, and other environmental problems. It is crucial that we take action to reduce our carbon footprint, transition to renewable energy sources, and protect vulnerable ecosystems.
    
    TLDR: Climate change, fossil fuels, deforestation, temperature rise, extreme weather, sea level rise, environmental problems, carbon footprint, renewable energy, ecosystem protection
    --
    Passage: The boy wnet to the store and boughht some bread. He wass happy to see that the price had gon down. He also met a girl he liiked, and they talked about their day. Later, he found out that he had lost his walllet and was upset.
    
    TLDR: boy, store, bread, price, girl, talked, lost wallet, upset
    --
    Passage: Once up on a time, there was a prinsess who lived in a castle. She had a lot of dreses and jewells but was unhappy. One day, she met a talking frog who told her that she needed to find true love to be truly happy. The prinsess then went on a journey to find her true love.
    
    TLDR: princess, castle, dresses, jewels, unhappy, talking frog, true love, journey
    --
    Passage: Roses are red, violets are blu, sugar is sweet, and so are you. This is a famus poem that has been used in many love letters and cards. It is a way to express love and affection to someone special.
    
    TLDR: roses, violets, sugar, famous poem, love letters, affection, special
    --
    Passage: Once upon a time, there was a dragon who lived in a cave. The dragon loved to hoard treasure and would often attack nearby villages to collect more. One day, a brave knight came to slay the dragon and put an end to its terrorizing. After a fierce battle, the knight emerged victorious and the dragon was no more.
    
    TLDR: dragon, cave, treasure, attack, nearby villages, brave knight, slay, terrorizing, fierce battle, victorious
    --
    Passage: Grate for cheeze and carrots, this gratr is a must-have in every kitchen. It's easy to use and cleen, and the blades are sharp and durable. Just be carefull when handeling it to avoid any accidents.
    
    TLDR: Grater, cheese, carrots, must-have, kitchen, easy to use, clean, sharp, durable, handling, accidents.
    --
    Passage: To assamble the furniture, start by sorting all the pieces and matching them to the instructions. Then, use the allen ranch to tighten all the screws and bolts until they are secure. Make sure to follw the steps in the correct order to avoid any problems.
    
    TLDR: Assemble, furniture, sort, pieces, instructions, allen wrench, tighten, screws, bolts, secure, follow, steps, correct order, problems.
    --
    Passage: This book contians 10 spooky stories that will keep you up at night. Each story is written by a different author and has its own unique twist. Read them alone or with friends, but be warned - you may never look at the dark the same way again!
    
    TLDR: Book, spooky stories, keep you up, night, different author, unique twist, read alone, with friends, warned, dark
    --
    Passage: Our new vacuum cleaner is the ultimat cleaning machine! With its powerful suction and easy-to-use attachments, it can clean even the most stubborn dirt and debris. Plus, it's lightweight and portable, so you can take it anywhere you go.
    
    TLDR: Vacuum cleaner, ultimate cleaning machine, powerful suction, easy-to-use, attachments, stubborn dirt, debris, lightweight, portable, anywhere
    --
    Passage: Looking for a delicious and healthy snack? Try our new line of organic, gluten-free granola bars! Made with all-natural ingredients and packed with protein and fiber, they're the perfect snack for any time of day. Available now at your local health food store.
    
    TLDR: Delicious, healthy snack, organic, gluten-free, granola bars, all-natural ingredients, protein, fiber, perfect snack, any time of day, local health food store
    --
    Passage: Chocolate is one of the most popular treats in the world. It comes in many forms, from milk chocolate to dark chocolate, and is often used in desserts and candy. However, it also has some health benefits, such as improving heart health and reducing inflammation
    
    TLDR: Chocolate, popular, treats, milk chocolate, dark chocolate, desserts, candy, health benefits, heart health, reducing inflammation
    --
    Passage: Congratulations on your new job as a softwear engineeer! You'll be responsible for developing and maintaining computer programs and applications. Your tasks include writing code, testing software, and troubleshooting problems. We're excited to have you on board and look forward to seeing what you can do!
    
    TLDR: New job, software engineer, developing, maintaining, computer programs, applications, writing code, testing software, troubleshooting, on board
    --
    Passage: Looking for a career in healthcare? Come visit our booth at the career fair and learn about the exciting opportunities available in the industry. From nursing to medical administration, we have a wide range of career paths for you to explore. Don't miss this chance to jumpstart your career!
    
    TLDR: Healthcare, career, booth, career fair, opportunities, nursing, medical administration, career paths, explore, jumpstart
    --
    Passage: Attention all DIY enthusiasts! Our new tool set has everything you need to tackle any project. With a variety of wrenches, pliers, and screwdrivers, you'll be able to fix anything around the house. Plus, our durable carrying case makes it easy to keep your tools organized and portable. Order now and start your next project!
    
    TLDR: DIY enthusiasts, tool set, project, wrenches, pliers, screwdrivers, fix, durable carrying case, organized, portable, order
    --
    Passage: Get ready for the adventure of a lifetime with our new travel package! You'll explore some of the world's most breathtaking destinations and experience new cultures like never before. Plus, our experienced tour guides will be with you every step of the way. Don't wait, book your trip today!
    
    TLDR: Adventure, lifetime, travel package, breathtaking destinations, experience, cultures, experienced tour guides, every step, book, trip
    --
    Passage: Attention all sports fans! Our new line of sports equipment is perfect for athletes of all levels. From basketballs to soccer balls, we have everything you need to get in the game. Plus, our high-quality materials and advanced technology ensure that you'll have the best performance possible. Order now and start playing like a pro!
    
    TLDR: Sports fans, sports equipment, athletes, basketballs, soccer balls, everything you need, high-quality materials, advanced technology, best performance, order
    --
    """
    
    custom_prompt = f"{prompt}\nPassage: {text}\n\nTLDR:"
    keywords = []
    for _ in range(10):
        response = cohere.generate(
            model='medium',
            prompt=custom_prompt,
            max_tokens=10,
            temperature=1,
            stop_sequences=["--"])
        keywords = response.generations[0].text.strip("\n--").lstrip(" ").split(", ")
        if len(keywords) > 1:
            break

    output_text = ', '.join(keywords)

    return output_text



