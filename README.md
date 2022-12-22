# fix-notes

!! I do not gurantee for data loss. This is a new script and not well checked yet. Please read it yourself first.!!
!! I also did not write yet everything down that it does to handle exceptions. !!

## How to use

Before using, replace in fix_notes.py the dir_path with the path your obsidian directionary is in.

Then run it in the terminal. (It is easier if the file is in the same directionary as the file you want to cut)

## What it does

The user specifies what note the script is supposed to edit.
I use this script to edit the main note where I dump everything in.
It then cuts the note into paragraphs (empty lines will indicate a new paragraph accordingly) and creates a new note for each or appends to an existing one.
Where it gets appended or added to depends on the first line "in '...'". The script then searches for a folder with the same name, if it cannot find that it will search for a file to append to.
It will tag (format [[tag]]) the new files with the name of the directionary it is in except for the main folders.
It will try to use the second line as the name of the file. If an error accures it will just use a ascii character.

I use this script in combination with obsidian but this is not needed as the script only edits the markdown files.

## Template (no path as input, it searches automatically)

in [folder or file name]]
[first sentence, will also be used as the name]
etc...


## Example

in math
gödels satz
much mathi stuff
more mathi stuff

-> Will create a note called "gödels satz" in the directionary "math". Everything, also the category, will be printed in the note though (to check if everything went right more easily)
