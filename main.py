import sys

def main():
    path_to_file = sys.argv[1]
    with open(path_to_file) as f:
        file_contents = f.read()
        print(file_contents)


main()