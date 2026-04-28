from collections import Counter

def substitutions(words, phrases):
    # 1. Map sorted word signatures to their frequency in the `words` list
    anagram_counts = Counter()
    for word in words:
        # Sort the characters of the word to create the signature
        signature = ''.join(sorted(word))
        anagram_counts[signature] += 1

    results = []

    # 2. Calculate the combinations for each phrase
    for phrase in phrases:
        combinations = 1
        # Split the phrase by spaces to get individual words
        for word in phrase.split():
            signature = ''.join(sorted(word))
            # Multiply by the number of available anagrams for this word
            combinations *= anagram_counts[signature]

        results.append(combinations)

    return results
