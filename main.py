import sys

def main():
    path_to_file = sys.argv[1]
    text = get_text(path_to_file)
    word_count = calc_word_count(text)
    letter_count_dict = calc_letter_count(text)
    print_report(path_to_file, word_count, letter_count_dict)
    

def print_report(path, word_count, letter_count_dict):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print("")
    sorted_letter_count = sort_dict(letter_count_dict)
    for l_dict in sorted_letter_count:
        print(f"The '{l_dict['char']}' character was found {l_dict['count']} times")
    print("--- End report ---")


def sort_dict(dict):
    char_list = []
    for char, count in dict.items():
        if char.isalpha():
            char_list.append({'char': char, 'count': count})
    char_list.sort(reverse=True, key=lambda x: x['count'])
    return char_list


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