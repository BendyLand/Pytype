import ast
import sys


def read_file(path):
    file = ""
    with open(path) as f:
        for line in f:
            file += line + "\n"
    return file


def get_contents(tree):
    result = ast.dump(tree)
    return result


def write_file(path, contents):
    with open(path, "w") as f:
        f.write(contents)


def main(args):
    if len(args) > 1:
        file = read_file(args[1])
        tree = ast.parse(file)
        contents = get_contents(tree)
        write_file("ast.txt", contents)
        print("File written successfully!")
    else:
        print("Usage: pytype <filepath>")


if __name__ == "__main__":
    args = sys.argv
    main(args)
