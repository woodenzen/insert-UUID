import re
import shutil
import os


def check():
    with open(zettel_path) as f:
        datafile = f.readlines()
    for line in datafile:
        if token in line:
            return True
    return False


dir = "/Users/will/Dropbox/Projects/testzks/daniel"
token = "›"


for file in os.listdir(dir):
    if file.endswith(".md"):
        zettel_path = (os.path.join(dir, file))
        uuid = os.path.join(file)
        res = re.findall("(\d{12})", uuid)
        if not res:
            continue
        with open(zettel_path, "r") as prev_file:
            if check() == 0:
                print("temp/" + os.path.join(file))
                with open("temp/" + os.path.join(file), "w") as new_file:
                    prev_contents = prev_file.readlines()
                    # you may add the new line to this list at any position
                    prev_contents.insert(1, f"›[[{res[0]}]]\n")
                    # print(prev_contents)
                    new_file.write(''.join(''.join(elems)
                                           for elems in prev_contents))
