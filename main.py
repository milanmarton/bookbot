import sys

def main():
    path_to_file = sys.argv[1]
    text = get_text(path_to_file)
    print(text)


def get_text(path):
    with open(path) as f:
        return f.read()


main()