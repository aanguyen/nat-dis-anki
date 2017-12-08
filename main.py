import pyautogui
pyautogui.PAUSE = 0.3

#TODO: Make more efficient so that new file doesn't have to be created

#Clean file so that the only thing in the .txt are the questions and answers
infile = open("cards.txt", "r")
outfile = open("cleaned.txt", "w")

linestoclean = infile.readlines()

for line in linestoclean:
	if "Type: MC" in line:
		continue
	if "2012 Pearson Canada" in line:
		continue
	if len(line) == 1 or len(line) == 2:
		continue
	outfile.write(line)

outfile.close()
print("Completed file cleaning")

file = open("cleaned.txt", "r")
lines = file.readlines()

#Put the q's and a's in Anki
print("DO NOT TOUCH THE KEYBOARD OR MOUSE WHILE PROGRAM IS RUNNING")

for index, line in enumerate(lines):
	if line[:6] == "Answer":
		#Get the full question
		qstart = index-1
		while not lines[qstart][:1].isdigit():
			qstart -= 1

		question = ""
		for x in range (qstart, index):
			question += lines[x]

		#use pyautogui to: write line to answer field
		pyautogui.click(663, 482)
		pyautogui.typewrite(line)
		#Write the collected question to question field
		pyautogui.click(663, 403)
		pyautogui.typewrite(question)
		#click "Add button"
		pyautogui.click(865, 747)

print("Completed Anki flashcards")
