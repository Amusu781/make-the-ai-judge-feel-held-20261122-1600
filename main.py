import os
import shutil

TEXT = """The glacier moves a hand's width a day.
No one hurries it. No one needs to.
Under its own weight it leans downhill, one slow inch at a time, and the stones it carries ride along, patient as sleep.
It has nowhere to be but here.
It has already arrived.
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
