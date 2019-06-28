#hmh16c
#harrison hill

#takes a fair number of minutes to run on size of 150
#acceptable speed at sizes under 50 or so

#It prints out the current iteration so you can see the current status
#(and so you can tell its not in an infinite loop)

#it takes longer to PLOT the data as it does calculate it.
#there is probably a better way to plot it but I couldn't find one

#program is O(n^2) so I'm not too surprised it slows down at large samples

#this feels a little brute forced, but then again we're literally doing 
#addition on thousands of individual cells and copying them from place to place, 
#so I don't see how to do it any other way

import numpy as np
import matplotlib.pyplot as plt

startval = int(input("enter starting temperature/size: "))

	#the + 2 is for the halo cells
state = np.zeros((startval + 2, startval + 2))
#print(state)

	#set up the halo cells on left side
for x in range(startval + 2):
	state[0][x] = startval

#print(state)

nextstate = np.copy(state)

def makestate(state, size):
	for x in range(1, size):
		changedline = False
		for y in range(1, size + 1):
			temp = nextstate[x][y]
			nextstate[x][y] = (state[x-1][y] + state[x+1][y] + state[x][y-1] + state[x][y+1])/4
			if nextstate[x][y] != temp:
				changedline = True
		if changedline == False:	#if we go through an entire column and nothing changed, that means its all zeros from here on out
			#print("BREAKING EARLY")
			break		#so just break the loop

					#this doesn't happen often, but it does help for the first 100 or so iterations on large samples


	#iterate through simulation
for x in range(3000):
	print("running iteration ", x)
	
	#generate new state
	makestate(state, startval)

	#check if they're equal
	if (np.array_equal(state, nextstate)):
		print("converged!")
		break
	#change current state and loop again
	state = np.copy(nextstate)


	#find appropriate color and plot each point
for x in range(1, startval + 1):
	for y in range(1, startval + 1):
		print("plotting point [", x, "][", y,"]...")
		if state[x][y] <= (startval/8):
			plt.plot(x, y, color='black', marker='o', markeredgecolor='black', markeredgewidth=0.5)
		elif state[x][y] <= (startval/4):
			plt.plot(x, y, color='blue', marker='o', markeredgecolor='black', markeredgewidth=0.5)
		elif state[x][y] <= (startval/8) * 3:
			plt.plot(x, y, color='aqua', marker='o', markeredgecolor='black', markeredgewidth=0.5)
		elif state[x][y] <= (startval/2):
			plt.plot(x, y, color='lawngreen', marker='o', markeredgecolor='black', markeredgewidth=0.5)
		elif state[x][y] <= (startval/8) * 5:
			plt.plot(x, y, color='yellow', marker='o', markeredgecolor='black', markeredgewidth=0.5)
		elif state[x][y] <= (startval/4) * 3:
			plt.plot(x, y, color='orange', marker='o', markeredgecolor='black', markeredgewidth=0.5)
		elif state[x][y] <= (startval/8) * 7:
			plt.plot(x, y, color='red', marker='o', markeredgecolor='black', markeredgewidth=0.5)
		else:
			plt.plot(x, y, color='darkred', marker='o', markeredgecolor='black', markeredgewidth=0.5)


#print(state)
plt.show()
