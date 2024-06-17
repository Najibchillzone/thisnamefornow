


word_list = [
    "time", "person", "year", "way", "day", "thing", "man", "world", "life", "hand", "part", "child", "eye",
    "woman", "place", "work", "week", "case", "point", "government", "company", "number", "group", "problem",
    "fact", "school", "book", "job", "country", "word", "state", "business", "issue", "side", "kind", "head",
    "house", "service", "friend", "father", "power", "hour", "game", "line", "end", "member", "law", "car",
    "city", "community", "name", "president", "team", "minute", "idea", "kid", "body", "information", "back",
    "parent", "face", "others", "level", "office", "door", "health", "person", "art", "war", "history", "party",
    "result", "change", "morning", "reason", "research", "girl", "guy", "moment", "air", "teacher", "force",
    "education", "arm", "writer", "sea", "market", "news", "death", "mind", "thought", "girl", "boy", "age",
    "parent", "field", "hair", "standard", "mouth", "view", "window", "paper", "space", "form", "support",
    "event", "truth", "story", "example", "food", "everyone", "edge", "society", "country", "end", "production",
    "care", "city", "room", "reason", "exercise", "market", "sense", "view", "family", "subject", "question",
    "soul", "quality", "fact", "mind", "force", "action", "night", "idea", "ground", "direction", "development",
    "rest", "rock", "language", "part", "plan", "experience", "eye", "name", "north", "south", "east", "west",
    "level", "group", "thing", "story", "record", "daughter", "space", "movement", "return", "development",
    "agreement", "officer", "worker", "trade", "history", "tale", "marriage", "power", "respect", "understanding",
    "development", "nation", "experience", "income", "front", "course", "road", "challenge", "voice", "book",
    "newspaper", "memory", "authority", "afternoon", "sea", "mother", "knowledge", "son", "fishing", "literature",
    "problem", "chance", "organization", "size", "term", "court", "structure", "figure", "table", "theory", "set",
    "society", "tax", "employment", "food", "star", "idea", "state", "heart", "evidence", "distance", "style",
    "opinion", "religion", "flight", "decade", "effort", "bed", "painting", "ocean", "occupation", "package",
    "depth", "possibility", "gift", "brother", "training", "culture", "brother", "article", "attack", "scene",
    "district", "skill", "crime", "unit", "election", "ice", "boat", "song", "engineering", "food", "district",
    "speaker", "animal", "theme", "technology", "department", "pressure", "manager", "operation", "statement",
    "energy", "practice", "union", "district", "series", "thinking", "hospital", "church", "unit", "metal", "design",
    "candidate", "supply", "bone", "election", "horse", "investigation", "sector", "percent", "marriage", "device",
]

alphabet_string = (
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
)

def lost_response(ind):

    funny_responses = [
        "Oops! Looks like you missed the mark. The hangman's getting more fashionable though!",
        "Close, but no banana... oh wait, that's not the word!",
        "Not quite! The hangman's practicing for his marathon though.",
        "Oh no, another wrong guess! The hangman's starting to look like a modern art masterpiece.",
        "That's not it! The hangman's got his groove on though, disco style.",
        "Almost there! The hangman's getting creative with his yoga poses.",
        "Not quite right! The hangman's now modeling for a new fashion line.",
        "Oh no! The hangman's doing some unexpected acrobatics.",
        "Close but no cigar! The hangman's preparing for a dance-off.",
        "Oops, not this time! The hangman's trying out for a new role in a mime show.",
        "Not the letter we're looking for! The hangman's now moonlighting as a contortionist.",
        "Missed it by a hair! The hangman's practicing his opera singing.",
        "Almost had it! The hangman's taking a break to try out some stand-up comedy.",
        "Not quite! The hangman's now a world-renowned abstract artist.",
        "Nice try! The hangman's teaching us all how to juggle."
    ]
    print(funny_responses[ind])