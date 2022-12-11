import re
import os

def check():
    with open(zettel_path) as f:
        datafile = f.readlines()
    for line in datafile:
        if token in line:
            return True
    return False

def titlecase(s):
    return re.sub(
        r"[A-Za-z]+('[A-Za-z]+)?",
        lambda word: word.group(0).capitalize(),s)

dir = "/Users/will/Dropbox/Projects/testzks/daniel/"
token = "›"

for file in os.listdir(dir):
    if file.endswith(".txt") and file.startswith("20"):
        zettel_path = (os.path.join(dir, file))
        file_name = os.path.join(file)
        note_name = file_name[13:-4]
        old_note_name = file[:-4]
        note_name = titlecase(note_name)
        note_name = note_name.replace('-', ' ')
        old_note_name = titlecase(old_note_name)
        old_note_name = old_note_name.replace('-', ' ')
        # res = re.findall("(\d{12})", file_name)
        # if not res:
        #     continue
        with open(zettel_path, "r") as prev_file:
            if check() == 0:
                print(dir + "tmp/" + os.path.join(file))
                print(old_note_name)
                with open(dir + "tmp/" + os.path.join(file), "w") as new_file:
                    prev_contents = prev_file.readlines()
                    # you may add the new line to this list at any position
                    prev_contents.insert(0, f"title: {note_name}\n\n") # ›[[{res[0]}]]\n
                    # print(prev_contents)
                    new_file.write(''.join(''.join(elems)
                                           for elems in prev_contents))
