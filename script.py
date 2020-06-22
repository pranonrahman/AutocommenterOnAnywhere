import pyautogui
import time 

mySentences = []

f = open('textOfComment.txt','r')
lines = f.readlines()

for line in lines:
	mySentences.append(line)
time.sleep(10)
for i in range(1000000):
	pyautogui.typewrite(mySentences[i%len(mySentences)])
	pyautogui.typewrite('\n')
	time.sleep(0.765)

	
