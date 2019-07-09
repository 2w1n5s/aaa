
import math
import random
inputa= [[0],
	 [0],
	 [0],
	 [0],	
	 [0],
	 [0],
	 [0],
	 [0],
	 [0],
	 [0],
	 [0],
	 [0],
	 [0],
	 [0],
	 [0],
	 [0],
	 [0],
	 [0],
	 [0]]
layerweight = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
layerbias = [[0],
	     [0],
	     [0],
	     [0],
	     [0],
	     [0],
	     [0],
	     [0],
	     [0],
	     [0],
	     [0],
	     [0],
	     [0],
	     [0],
	     [0],
	     [0]]
ansa = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansb = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansc = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansd = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
anse = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansf = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansg = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansh = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansi = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansj = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansk = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansl = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansm = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansn = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
anso = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansp = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansq = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansr = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
anss = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
unbiased = [[0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0]]
biased = [[0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0]]
layer = [[0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0],
	    [0]]
for kkr in range(0, len(inputa)):
	ansa[kkr][0] = inputa[0][0]*layerweight[kkr][0]
	ansb[kkr][0] = inputa[1][0]*layerweight[kkr][1]
	ansc[kkr][0] = inputa[2][0]*layerweight[kkr][2]
	ansd[kkr][0] = inputa[3][0]*layerweight[kkr][3]
	anse[kkr][0] = inputa[4][0]*layerweight[kkr][4]
	ansf[kkr][0] = inputa[5][0]*layerweight[kkr][5]
	ansg[kkr][0] = inputa[6][0]*layerweight[kkr][6]
	ansh[kkr][0] = inputa[7][0]*layerweight[kkr][7]
	ansi[kkr][0] = inputa[8][0]*layerweight[kkr][8]
	ansj[kkr][0] = inputa[9][0]*layerweight[kkr][9]
	ansk[kkr][0] = inputa[10][0]*layerweight[kkr][10]
	ansl[kkr][0] = inputa[11][0]*layerweight[kkr][11]
	ansm[kkr][0] = inputa[12][0]*layerweight[kkr][12]
	ansn[kkr][0] = inputa[13][0]*layerweight[kkr][13]
	anso[kkr][0] = inputa[14][0]*layerweight[kkr][14]
	ansp[kkr][0] = inputa[15][0]*layerweight[kkr][15]
	ansq[kkr][0] = inputa[16][0]*layerweight[kkr][16]
	ansr[kkr][0] = inputa[17][0]*layerweight[kkr][17]
	anss[kkr][0] = inputa[18][0]*layerweight[kkr][18]
for kkr in range(0, len(unbiased)):
	unbiased[kkr][0] = ansa[kkr][0]+ansb[kkr][0]+ansc[kkr][0]+ansd[kkr][0]+anse[kkr][0]+ansf[kkr][0]+ansg[kkr][0]+ansh[kkr][0]+ansi[kkr][0]+ansj[kkr][0]+ansk[kkr][0]+ansl[kkr][0]+ansm[kkr][0]+ansn[kkr][0]+anso[kkr][0]+ansp[kkr][0]+ansq[kkr][0]+ansr[kkr][0]+anss[kkr][0]
for kkr in range(0, len(biased)):
	biased[kkr][0] = unbiased[kkr][0]+layerbias[kkr][0]
for kkr in range(0,len(layer)):
	layer[kkr][0] = 1/(1+exp(-1*(biased[kkr][0])))
outputweightin = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
outputweightlay = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
ansaa = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansbb = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
anscc = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansdd = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansee = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansff = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansgg = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
anshh = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansii = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansjj = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
anskk = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansll = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansmm = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansnn = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansoo = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
anspp = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansqq = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansrr = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansss = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansaz = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansbz = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
anscz = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansdz = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansez = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansfz = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansgz = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
anshz = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansiz = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansjz = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
anskz = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
anslz = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansmz = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansnz = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ansoz = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
anspz = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
totalputs = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
outputbias = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
sigfood = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ultimate = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
for kkr in range(0,len(outputweightin)):
	ansaa[kkr][0] = inputa[0][0]*outputweightin[kkr][0]
	ansbb[kkr][0] = inputa[1][0]*outputweightin[kkr][1]
	anscc[kkr][0] = inputa[2][0]*outputweightin[kkr][2]
	ansdd[kkr][0] = inputa[3][0]*outputweightin[kkr][3]
	ansee[kkr][0] = inputa[4][0]*outputweightin[kkr][4]
	ansff[kkr][0] = inputa[5][0]*outputweightin[kkr][5]
	ansgg[kkr][0] = inputa[6][0]*outputweightin[kkr][6]
	anshh[kkr][0] = inputa[7][0]*outputweightin[kkr][7]
	ansii[kkr][0] = inputa[8][0]*outputweightin[kkr][8]
	ansjj[kkr][0] = inputa[9][0]*outputweightin[kkr][9]
	anskk[kkr][0] = inputa[10][0]*outputweightin[kkr][10]
	ansll[kkr][0] = inputa[11][0]*outputweightin[kkr][11]
	ansmm[kkr][0] = inputa[12][0]*outputweightin[kkr][12]
	ansnn[kkr][0] = inputa[13][0]*outputweightin[kkr][13]
	ansoo[kkr][0] = inputa[14][0]*outputweightin[kkr][14]
	anspp[kkr][0] = inputa[15][0]*outputweightin[kkr][15]
	ansqq[kkr][0] = inputa[16][0]*outputweightin[kkr][16]
	ansrr[kkr][0] = inputa[17][0]*outputweightin[kkr][17]
	ansss[kkr][0] = inputa[18][0]*outputweightin[kkr][18]
	ansaz[kkr][0] = layer[0][0]*outputweightlay[kkr][1]
	ansbz[kkr][0] = layer[1][0]*outputweightlay[kkr][2]
	anscz[kkr][0] = layer[2][0]*outputweightlay[kkr][3]
	ansdz[kkr][0] = layer[3][0]*outputweightlay[kkr][4]
	ansez[kkr][0] = layer[4][0]*outputweightlay[kkr][5]
	ansfz[kkr][0] = layer[5][0]*outputweightlay[kkr][6]
	ansgz[kkr][0] = layer[6][0]*outputweightlay[kkr][7]
	anshz[kkr][0] = layer[7][0]*outputweightlay[kkr][8]
	ansiz[kkr][0] = layer[8][0]*outputweightlay[kkr][9]
	ansjz[kkr][0] = layer[9][0]*outputweightlay[kkr][10]
	anskz[kkr][0] = layer[10][0]*outputweightlay[kkr][11]
	anslz[kkr][0] = layer[11][0]*outputweightlay[kkr][12]
	ansmz[kkr][0] = layer[12][0]*outputweightlay[kkr][13]
	ansnz[kkr][0] = layer[13][0]*outputweightlay[kkr][14]
	ansoz[kkr][0] = layer[14][0]*outputweightlay[kkr][15]
	anspz[kkr][0] = layer[15][0]*outputweightlay[kkr][16]
for kkr in range(0,len(outputweightin)):
	totalputs[kkr][0] = ansaa[kkr][0]+ansbb[kkr][0]+anscc[kkr][0]+ansdd[kkr][0]+ansee[kkr][0]+ansff[kkr][0]+ansgg[kkr][0]+anshh[kkr][0]+ansii[kkr][0]+ansjj[kkr][0]+anskk[kkr][0]+ansll[kkr][0]+ansmm[kkr]+ansnn[kkr]+ansoo[kkr]+anspp[kkr]+ansqq[kkr]+ansrr[kkr][0]+ansss[kkr][0]+ansaz[kkr][0]+ansbz[kkr][0]+anscz[kkr][0]+ansdz[kkr][0]+ansez[kkr][0]+ansfz[kkr][0]+ansgz[kkr][0]+anshz[kkr][0]+ansiz[kkr][0]+ansjz[kkr][0]+anskz[kkr][0]+anslz[kkr][0]+ansmz[kkr][0]+ansnz[kkr][0]+ansoz[kkr][0]+anspz[kkr][0]
for kkr in range(0,len(outputbias)):
	sigfood[kkr][0] = totalinputs[kkr][0]+outputbias[kkr][0]
for kkr in range(0,len(ultimate)):
	ultimate[kkr][0] = 1/(1+exp(-1(sigfood[kkr][0])))
for ikkk in range(0, len(layerweight)):
	for jkkk in range(0, len(layerweight[0])):
		layerweight[ikkk][jkkk] = random.randint(-77, 77)
for ikkk in range(0, len(layerbias)):
	for jkkk in range(0, len(layerbias[0])):
		layerbias[ikkk][jkkk] = random.randint(-77, 77)
for ikkk in range(0, len(outputweightin)):
	for jkkk in range(0, len(outputweightin[0])):
		outputweightin[ikkk][jkkk] = random.randint(-77, 77)
for ikkk in range(0, len(outputweightlay)):
	for jkkk in range(0, len(outputweightlay[0])):
		outputweighlay[ikkk][jkkk] = random.randint(-77, 77)
for ikkk in range(0, len(outputbias)):
	for jkkk in range(0, len(outputbias[0])):
		outputbias[ikkk][jkkk] = random.randint(-77, 77)	
