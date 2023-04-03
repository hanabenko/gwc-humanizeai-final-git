import openai
openai.api_key = "ENTER AI KEY FROM https://platform.openai.com/account/api-keys"

def runQuizzerMode(language):
    print("Hi! Welcome to the quizzer mode, where your AI assistant will ask you questions in your target language, without much other feedback. Type 'QUIT' to stop this mode and return to the default chatbot.")
    answer = ""
    while answer != "QUIT":
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = [{"role": "user", "content":"Ask me a question in " + language + "."}])
        print("Chatbot: " + completion.choices[0].message.content)
        answer = input("You: ")
    print ("Thanks for enjoying quizzer mode. Feel free to continue to talk to your AI Assistant or to return to quizzer mode at any point by typing 'quizzer mode'." "\n")

def runVocabMode (language):
    ultimateVocabList = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us', 'be', 'have', 'do', 'say', 'go', 'can', 'get', 'would', 'make', 'know', 'will', 'think', 'take', 'see', 'come', 'could', 'want', 'look', 'use', 'find', 'give', 'tell', 'work', 'may', 'should', 'call', 'try', 'ask', 'need', 'feel', 'become', 'leave', 'put', 'mean', 'keep', 'let', 'begin', 'seem', 'help', 'talk', 'turn', 'start', 'might', 'show', 'hear', 'play', 'run', 'move', 'like', 'live', 'believe', 'hold', 'bring', 'happen', 'must', 'write', 'provide', 'sit', 'stand', 'lose', 'pay', 'meet', 'include', 'continue', 'set', 'learn', 'change', 'lead', 'understand', 'watch', 'follow', 'stop', 'create', 'speak', 'read', 'allow', 'add', 'spend', 'grow', 'open', 'walk', 'win', 'offer', 'remember', 'love', 'consider', 'appear', 'buy', 'wait', 'serve', 'die', 'send', 'expect', 'build', 'stay', 'fall', 'cut', 'reach', 'kill', 'remain', 'time', 'year', 'people', 'way', 'day', 'man', 'thing', 'woman', 'life', 'child', 'world', 'school', 'state', 'family', 'student', 'group', 'country', 'problem', 'hand', 'part', 'place', 'case', 'week', 'company', 'system', 'program', 'question', 'work', 'government', 'number', 'night', 'point', 'home', 'water', 'room', 'mother', 'area', 'money', 'story', 'fact', 'month', 'lot', 'right', 'study', 'book', 'eye', 'job', 'word', 'business', 'issue', 'side', 'kind', 'head', 'house', 'service', 'friend', 'father', 'power', 'hour', 'game', 'line', 'end', 'member', 'law', 'car', 'city', 'community', 'name', 'president', 'team', 'minute', 'idea', 'kid', 'body', 'information', 'back', 'parent', 'face', 'others', 'level', 'office', 'door', 'health', 'person', 'art', 'war', 'history', 'party', 'result', 'change', 'morning', 'reason', 'research', 'girl', 'guy', 'moment', 'air', 'teacher', 'force', 'education', 'other', 'new', 'good', 'high', 'old', 'great', 'big', 'American', 'small', 'large', 'national', 'young', 'different', 'black', 'long', 'little', 'important', 'political', 'bad', 'white', 'real', 'best', 'right', 'social', 'only', 'public', 'sure', 'low', 'early', 'able', 'human', 'local', 'late', 'hard', 'major', 'better', 'economic', 'strong', 'possible', 'whole', 'free', 'military', 'true', 'federal', 'international', 'full', 'special', 'easy', 'clear', 'recent', 'certain', 'personal', 'open', 'red', 'difficult', 'available', 'likely', 'short', 'single', 'medical', 'current', 'wrong', 'private', 'past', 'foreign', 'fine', 'common', 'poor', 'natural', 'significant', 'similar', 'hot', 'dead', 'central', 'happy', 'serious', 'ready', 'simple', 'left', 'physical', 'general', 'environmental', 'financial', 'blue', 'democratic', 'dark', 'various', 'entire', 'close', 'legal', 'religious', 'cold', 'final', 'main', 'green', 'nice', 'huge', 'popular', 'traditional', 'cultural']
    print("Hi! Welcome to the vocabulary mode, where your AI chatbot will ask you vocabulary questions based on the list of 400 most important words in any language according to Oxford researchers. Type 'QUIT' to stop this mode and return to the default chatbot.")
    answer = ""
    while answer != "QUIT":
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = [{"role": "user", "content":"Translate a random word from this list into " + language + " and ask me about what they mean. Here is the list: " + str(ultimateVocabList)}])
        print("Chatbot: " + completion.choices[0].message.content)
        answer = input("You: ")
    print ("Thanks for enjoying vocabulary mode. Feel free to continue to talk to your AI Assistant or to return to vocabulary mode at any point by typing 'vocab'." "\n")

def runSpecialMode (language):
    print("Hi! Welcome to the special mode... So, you've dared to enter.")
    answer = input("You must choose: baby red pandas (type 'P') or the cinematic masterpiece Cars 2 (type 'C').")
    if answer == 'P':
        print ("Welcome to an infinte loop of poems... muahahaha. You did this to yourself. Enjoy.")
        while True:
            completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = [{"role": "user", "content":"Write a poem in " + language + " inspired by a famous " + language + " poet."}])
            print("Chatbot: " + completion.choices[0].message.content + "\n\n")
    elif answer == 'C':
        print ("Welcome to an infinte loop of puns... muahahaha. You did this to yourself. Enjoy.")
        while True:
            completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = [{"role": "user", "content":"Tell me a pun in " + language + "."}])
            print("Chatbot: " + completion.choices[0].message.content + "\n")
    else:
        print ("Indecisive, huh.")

messages = []
system_msg = input("System: What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})
print("System: Your new assistant is ready!")
targetLanguage = input("Chatbot: What language are you aiming to practice? ")

print("Chatbot: Great! I'm excited to help you with that language.\nThere are a few basic modes that will help you navigate your journey. For simulating interview or conversation questions, enter quizzer mode by typing 'quizzer mode' at any point when talking to the bot. Additionally, to practice vocabulary from Oxford's list of 400 most essential words in a language, type 'vocab'. For a special secret mode, type 'surprise'. \n \n")

print("Chatbot: How may I help you today?")

while input != "quit":
    message = input("You: ")
    if (message).lower() == "quizzer mode":
        print("Entering Quizzer Mode...")
        runQuizzerMode(targetLanguage)
    elif (message).lower() == "vocab":
        print("Entering Vocabulary Mode...")
        runVocabMode (targetLanguage)
    elif (message).lower() == "surprise":
        print ("Entering Special Mode...")
        runSpecialMode (targetLanguage)
    else:
        messages.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        print("Chatbot: " + reply + "\n")