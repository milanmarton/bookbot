import sys

def main():
    path_to_file = sys.argv[1]
    text = get_text(path_to_file)
    word_count = calc_word_count(text)
    print(word_count)

def get_text(path):
    with open(path) as f:
        return f.read()

def calc_word_count(text):
    words = text.split()
    return len(words)

main()