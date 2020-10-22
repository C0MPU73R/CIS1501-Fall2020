import random


def print_hanging_man(number_of_incorrect_guesses):
    if number_of_incorrect_guesses == 6:
        gallows = '''
|------
|     |
|     0
|   --|--
|     /\\
|
|
|_________
        '''
        print(gallows)
    elif number_of_incorrect_guesses == 5:
        gallows = '''
|------
|     |
|     0
|   --|--
|     /
|
|
|_________
        '''
        print(gallows)
    elif number_of_incorrect_guesses == 4:
        gallows = '''
|------
|     |
|     0
|   --|--
|     
|
|
|_________
        '''
        print(gallows)
    elif number_of_incorrect_guesses == 3:
        gallows = '''
|------
|     |
|     0
|   --|
|     
|
|
|_________
        '''
        print(gallows)
    elif number_of_incorrect_guesses == 2:
        gallows = '''
|------
|     |
|     0
|     |
|
|
|_________
        '''
        print(gallows)
    elif number_of_incorrect_guesses == 1:
        gallows = '''
|------
|     |
|     0
|   
|
|
|
|_________
        '''
        print(gallows)
    elif number_of_incorrect_guesses == 0:
        gallows = '''
|------
|     |
|     
|   
|
|
|
|_________
           '''
        print(gallows)


def guess_a_letter(letters_guessed):
    letter = input("Guess a letter").lower()

    while len(letter) > 1 or ( not letter.isalpha() ) or letter in letters_guessed:
        if letter in letters_guessed:
            print("You already guessed that letter")
        if not letter.isalpha():
            print("You can only guess letters")
        if len(letter) > 1:
            print("please enter a single letter")

        letter = input("Guess a letter").lower()

    letters_guessed.append(letter)

    return letter


def create_hidden_word(random_word, letters_guessed):
    hidden_word = ""
    for letter in random_word:
        if letter in letters_guessed:
            hidden_word += letter
        else:
            hidden_word += "_"
    return hidden_word


word_list = [ 'ability', 'able', 'about', 'above', 'accept', 'according', 'account', 'across', 'action', 'activity', 'actually', 'address', 'administration', 'admit', 'adult', 'affect', 'after', 'again', 'against', 'agency', 'agent', 'agree', 'agreement', 'ahead', 'allow', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'American', 'among', 'amount', 'analysis', 'animal', 'another', 'answer', 'anyone', 'anything', 'appear', 'apply', 'approach', 'area', 'argue', 'around', 'arrive', 'article', 'artist', 'assume', 'attack', 'attention', 'attorney', 'audience', 'author', 'authority', 'available', 'avoid', 'away', 'baby', 'back', 'ball', 'bank', 'base', 'beat', 'beautiful', 'because', 'become', 'before', 'begin', 'behavior', 'behind', 'believe', 'benefit', 'best', 'better', 'between', 'beyond', 'bill', 'billion', 'black', 'blood', 'blue', 'board', 'body', 'book', 'born', 'both', 'break', 'bring', 'brother', 'budget', 'build', 'building', 'business', 'call', 'camera', 'campaign', 'cancer', 'candidate', 'capital', 'card', 'care', 'career', 'carry', 'case', 'catch', 'cause', 'cell', 'center', 'central', 'century', 'certain', 'certainly', 'chair', 'challenge', 'chance', 'change', 'character', 'charge', 'check', 'child', 'choice', 'choose', 'church', 'citizen', 'city', 'civil', 'claim', 'class', 'clear', 'clearly', 'close', 'coach', 'cold', 'collection', 'college', 'color', 'come', 'commercial', 'common', 'community', 'company', 'compare', 'computer', 'concern', 'condition', 'conference', 'Congress', 'consider', 'consumer', 'contain', 'continue', 'control', 'cost', 'could', 'country', 'couple', 'course', 'court', 'cover', 'create', 'crime', 'cultural', 'culture', 'current', 'customer', 'dark', 'data', 'daughter', 'dead', 'deal', 'death', 'debate', 'decade', 'decide', 'decision', 'deep', 'defense', 'degree', 'Democrat', 'democratic', 'describe', 'design', 'despite', 'detail', 'determine', 'develop', 'development', 'difference', 'different', 'difficult', 'dinner', 'direction', 'director', 'discover', 'discuss', 'discussion', 'disease', 'doctor', 'door', 'down', 'draw', 'dream', 'drive', 'drop', 'drug', 'during', 'each', 'early', 'east', 'easy', 'economic', 'economy', 'edge', 'education', 'effect', 'effort', 'eight', 'either', 'election', 'else', 'employee', 'energy', 'enjoy', 'enough', 'enter', 'entire', 'environment', 'environmental', 'especially', 'establish', 'even', 'evening', 'event', 'ever', 'every', 'everybody', 'everyone', 'everything', 'evidence', 'exactly', 'example', 'executive', 'exist', 'expect', 'experience', 'expert', 'explain', 'face', 'fact', 'factor', 'fail', 'fall', 'family', 'fast', 'father', 'fear', 'federal', 'feel', 'feeling', 'field', 'fight', 'figure', 'fill', 'film', 'final', 'finally', 'financial', 'find', 'fine', 'finger', 'finish', 'fire', 'firm', 'first', 'fish', 'five', 'floor', 'focus', 'follow', 'food', 'foot', 'force', 'foreign', 'forget', 'form', 'former', 'forward', 'four', 'free', 'friend', 'from', 'front', 'full', 'fund', 'future', 'game', 'garden', 'general', 'generation', 'girl', 'give', 'glass', 'goal', 'good', 'government', 'great', 'green', 'ground', 'group', 'grow', 'growth', 'guess', 'hair', 'half', 'hand', 'hang', 'happen', 'happy', 'hard', 'have', 'head', 'health', 'hear', 'heart', 'heat', 'heavy', 'help', 'here', 'herself', 'high', 'himself', 'history', 'hold', 'home', 'hope', 'hospital', 'hotel', 'hour', 'house', 'however', 'huge', 'human', 'hundred', 'husband', 'idea', 'identify', 'image', 'imagine', 'impact', 'important', 'improve', 'include', 'including', 'increase', 'indeed', 'indicate', 'individual', 'industry', 'information', 'inside', 'instead', 'institution', 'interest', 'interesting', 'international', 'interview', 'into', 'investment', 'involve', 'issue', 'item', 'itself', 'join', 'just', 'keep', 'kill', 'kind', 'kitchen', 'know', 'knowledge', 'land', 'language', 'large', 'last', 'late', 'later', 'laugh', 'lawyer', 'lead', 'leader', 'learn', 'least', 'leave', 'left', 'legal', 'less', 'letter', 'level', 'life', 'light', 'like', 'likely', 'line', 'list', 'listen', 'little', 'live', 'local', 'long', 'look', 'lose', 'loss', 'love', 'machine', 'magazine', 'main', 'maintain', 'major', 'majority', 'make', 'manage', 'management', 'manager', 'many', 'market', 'marriage', 'material', 'matter', 'maybe', 'mean', 'measure', 'media', 'medical', 'meet', 'meeting', 'member', 'memory', 'mention', 'message', 'method', 'middle', 'might', 'military', 'million', 'mind', 'minute', 'miss', 'mission', 'model', 'modern', 'moment', 'money', 'month', 'more', 'morning', 'most', 'mother', 'mouth', 'move', 'movement', 'movie', 'much', 'music', 'must', 'myself', 'name', 'nation', 'national', 'natural', 'nature', 'near', 'nearly', 'necessary', 'need', 'network', 'never', 'news', 'newspaper', 'next', 'nice', 'night', 'none', 'north', 'note', 'nothing', 'notice', 'number', 'occur', 'offer', 'office', 'officer', 'official', 'often', 'once', 'only', 'onto', 'open', 'operation', 'opportunity', 'option', 'order', 'organization', 'other', 'others', 'outside', 'over', 'owner', 'page', 'pain', 'painting', 'paper', 'parent', 'part', 'participant', 'particular', 'particularly', 'partner', 'party', 'pass', 'past', 'patient', 'pattern', 'peace', 'people', 'perform', 'performance', 'perhaps', 'period', 'person', 'personal', 'phone', 'physical', 'pick', 'picture', 'piece', 'place', 'plan', 'plant', 'play', 'player', 'point', 'police', 'policy', 'political', 'politics', 'poor', 'popular', 'population', 'position', 'positive', 'possible', 'power', 'practice', 'prepare', 'present', 'president', 'pressure', 'pretty', 'prevent', 'price', 'private', 'probably', 'problem', 'process', 'produce', 'product', 'production', 'professional', 'professor', 'program', 'project', 'property', 'protect', 'prove', 'provide', 'public', 'pull', 'purpose', 'push', 'quality', 'question', 'quickly', 'quite', 'race', 'radio', 'raise', 'range', 'rate', 'rather', 'reach', 'read', 'ready', 'real', 'reality', 'realize', 'really', 'reason', 'receive', 'recent', 'recently', 'recognize', 'record', 'reduce', 'reflect', 'region', 'relate', 'relationship', 'religious', 'remain', 'remember', 'remove', 'report', 'represent', 'Republican', 'require', 'research', 'resource', 'respond', 'response', 'responsibility', 'rest', 'result', 'return', 'reveal', 'rich', 'right', 'rise', 'risk', 'road', 'rock', 'role', 'room', 'rule', 'safe', 'same', 'save', 'scene', 'school', 'science', 'scientist', 'score', 'season', 'seat', 'second', 'section', 'security', 'seek', 'seem', 'sell', 'send', 'senior', 'sense', 'series', 'serious', 'serve', 'service', 'seven', 'several', 'sexual', 'shake', 'share', 'shoot', 'short', 'shot', 'should', 'shoulder', 'show', 'side', 'sign', 'significant', 'similar', 'simple', 'simply', 'since', 'sing', 'single', 'sister', 'site', 'situation', 'size', 'skill', 'skin', 'small', 'smile', 'social', 'society', 'soldier', 'some', 'somebody', 'someone', 'something', 'sometimes', 'song', 'soon', 'sort', 'sound', 'source', 'south', 'southern', 'space', 'speak', 'special', 'specific', 'speech', 'spend', 'sport', 'spring', 'staff', 'stage', 'stand', 'standard', 'star', 'start', 'state', 'statement', 'station', 'stay', 'step', 'still', 'stock', 'stop', 'store', 'story', 'strategy', 'street', 'strong', 'structure', 'student', 'study', 'stuff', 'style', 'subject', 'success', 'successful', 'such', 'suddenly', 'suffer', 'suggest', 'summer', 'support', 'sure', 'surface', 'system', 'table', 'take', 'talk', 'task', 'teach', 'teacher', 'team', 'technology', 'television', 'tell', 'tend', 'term', 'test', 'than', 'thank', 'that', 'their', 'them', 'themselves', 'then', 'theory', 'there', 'these', 'they', 'thing', 'think', 'third', 'this', 'those', 'though', 'thought', 'thousand', 'threat', 'three', 'through', 'throughout', 'throw', 'thus', 'time', 'today', 'together', 'tonight', 'total', 'tough', 'toward', 'town', 'trade', 'traditional', 'training', 'travel', 'treat', 'treatment', 'tree', 'trial', 'trip', 'trouble', 'true', 'truth', 'turn', 'type', 'under', 'understand', 'unit', 'until', 'upon', 'usually', 'value', 'various', 'very', 'victim', 'view', 'violence', 'visit', 'voice', 'vote', 'wait', 'walk', 'wall', 'want', 'watch', 'water', 'weapon', 'wear', 'week', 'weight', 'well', 'west', 'western', 'what', 'whatever', 'when', 'where', 'whether', 'which', 'while', 'white', 'whole', 'whom', 'whose', 'wide', 'wife', 'will', 'wind', 'window', 'wish', 'with', 'within', 'without', 'woman', 'wonder', 'word', 'work', 'worker', 'world', 'worry', 'would', 'write', 'writer', 'wrong', 'yard', 'yeah', 'year', 'young', 'your', 'yourself' ]

play_again = 'y'

while play_again == 'y':
    random_word = word_list[random.randint(0, len(word_list)-1)]
    letters_guessed = []

    number_of_incorrect_guesses = 0
    hidden_word = create_hidden_word(random_word, letters_guessed)
    print(hidden_word)

    while number_of_incorrect_guesses < 6 and "_" in hidden_word:

        letter = guess_a_letter(letters_guessed)

        if letter not in random_word:
            number_of_incorrect_guesses += 1
            print_hanging_man(number_of_incorrect_guesses)

        hidden_word = create_hidden_word(random_word, letters_guessed)
        print(hidden_word)

    print("the word was:", random_word)
    play_again = input("Do you want to play again? y/n").lower()
