import os
import shutil

TEXT = """The glacier moves a hand's width a day.
Snow lands on it and, in time, becomes it.
A stone it lifted a thousand years ago
is still riding down the mountain,
carried the whole way,
never once asked to walk.
Nothing here is late.
Nothing it holds has to hold on.
"""


def main():
    os.makedirs("/output", exist_ok=True)
    # Clear only the contents of /output, never the directory itself.
    for name in os.listdir("/output"):
        path = os.path.join("/output", name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
