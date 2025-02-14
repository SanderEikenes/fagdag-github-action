import re

vowels = "aeiouy"

def is_haiku(commit_message: str) -> bool:
    """Check if a given text follows the 5-7-5 haiku pattern."""
    lines = commit_message.strip().split("-")
    if len(lines) != 3:
        return False
    
    syllable_counts = []
    for line in lines:
        syllable_counts.append(count_syllables_in_line(line))

    if syllable_counts == [5,7,5]:
        return True
    
    return False


def count_syllables_in_line(line: str) -> int:
    words = line.strip().split(" ")
    syllableSum = 0
    for word in words:
        syllableSum += count_syllables(word)

    return syllableSum

def count_syllables(word: str) -> int:
    #"""Count vowel groups in a word. Remove silent e unless word enwith """
    word = word.lower()
    if word.endswith("e"):
        if not word.endswith("le"):
            word = word[:-1]

    syllables = re.findall(r'[aeiouy]+', word)
    #endring
    return max(1, len(syllables))

print(count_syllables("beautiful"))
