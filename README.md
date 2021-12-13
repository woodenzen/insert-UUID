# Insert any text into a zettel at any position.

Primarily this first checks for the presents of "token", then inserts the text. 

I recommend using a backup of files to insure safety. 

In line 32 - prev_contents.insert(1, f"›[[{res[0]}]]\n") 
prev_contents.insert takes 2 arguments. The first is the line position for the insertion and the second is the f-string of the inserted text.

