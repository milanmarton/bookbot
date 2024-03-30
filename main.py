import sys

def main():
    path_to_file = sys.argv[1]
    text = get_text(path_to_file)
    word_count = calc_word_count(text)
    letter_count = calc_letter_count(text)
    print(letter_count)

def get_text(path):
    with open(path) as f:
        return f.read()

def calc_word_count(text):
    words = text.split()
    return len(words)

def calc_letter_count(text):
    lowered_text = text.lower()
    letter_count = {}
    for c in lowered_text:
        if c in letter_count:
            letter_count[c] += 1
        else:
            letter_count[c] = 1
    return letter_count

main()