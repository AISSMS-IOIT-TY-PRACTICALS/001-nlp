from icecream import ic

prefixes = [
    'un', 're', 'in', 'dis', 'im', 'pre', 'mis', 'non', 'anti', 'de',
    'over', 'under', 'sub', 'inter', 'trans', 'semi', 'fore', 'post', 'pro', 'mid'
]

suffixes = [
    'ing', 'ed', 'es', 'er', 'ly', 'ness', 'ment', 'ful', 'ive', 'tion',
    'sion', 'able', 'ible', 'al', 'ous', 'ity', 'est', 'less', 'ence', 'ance'
]


def custom_stem(word):
    # Remove common prefixes if present
    for prefix in prefixes:
        if word.startswith(prefix):
            word = word[len(prefix):]
            break  # Remove only one prefix

    # Remove common suffixes if present
    for suffix in suffixes:
        if word.endswith(suffix):
            word = word[:-len(suffix)]
            break  # Remove only one suffix

    return word


# Test the custom stemmer
words = [
    'unhappiness', 'recovery', 'misunderstood', 'running', 'happiness',
    'prevalent', 'disapproval', 'overloading', 'underestimate', 'submarine',
    'interact', 'transition', 'semicircle', 'forewarned', 'postgraduate',
    'proactive', 'midpoint', 'antivirus', 'deactivation', 'endless',
    'beautiful', 'invisible', 'movable', 'boldness', 'cleanliness'
]

stemmed_words = [custom_stem(word) for word in words]

# Using icecream for pretty output
ic(words)
ic(stemmed_words)
