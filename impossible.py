
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
ansa = [[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]]



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
biased =   [[0],
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
layer =    [[0],
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
def layer(inputa,layerweight,layerbias):
	for kkr in range(0,len(inputa)):
		for i in range(0,len(layerweight)):
			for j in range(0,len(ansa)):
				ansa[j][kkr][0] = inputa[kkr][0]*layerweight[i][kkr]
	for kkr in range(0, len(unbiased)):
		unbiased[kkr][0]=ansa[0][kkr][0]+ansa[1][kkr][0]+ansa[2][kkr][0]+ansa[3][kkr][0]+ansa[4][kkr][0]+ansa[5][kkr][0]+ansa[6][kkr][0]+ansa[7][kkr][0]+ansa[8][kkr][0]+ansa[9][kkr][0]+ansa[10][kkr][0]+ansa[11][kkr][0]+ansa[12][kkr][0]+ansa[13][kkr][0]+ansa[14][kkr][0]+ansa[15][kkr][0]+ansa[16][kkr][0]+ansa[17][kkr][0]+ansa[18][kkr][0]
	for kkr in range(0, len(biased)):
		biased[kkr][0] = unbiased[kkr][0]+layerbias[kkr][0]
	for kkr in range(0,len(layer)):
		layer[kkr][0] = 1/(1+math.exp(-1*(biased[kkr][0])))
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
ansaa = [[[0],[0],[0],[0],[0],[0],[0],[0],[0]],		
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]]]

ansaz = [[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
  	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]],
	[[0],[0],[0],[0],[0],[0],[0],[0],[0]]]
totalputs = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
outputbias = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
sigfood = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
ultimate = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
for kkr in range(0,len(totalputs)):
		totalputs[kkr][0] = ansaa[0][kkr][0]+ansaa[1][kkr][0]+ansaa[2][kkr][0]+ansaa[3][kkr][0]+ansaa[4][kkr][0]+ansaa[5][kkr][0]+ansaa[6][kkr][0]+ansaa[7][kkr][0]+ansaa[8][kkr][0]+ansaa[9][kkr][0]+ansaa[10][kkr][0]+ansaa[11][kkr][0]+ansaa[12][kkr][0]+ansaa[13][kkr][0]+ansaa[14][kkr][0]+ansaa[15][kkr][0]+ansaa[16][kkr][0]+ansaa[17][kkr][0]+ansaa[18][kkr][0]
def output(inputa,layer,outputweightin,outputweightlay,outputbias):
	for kkr in range(0,len(ansaa)):
		for j in range(0,len(ansaa[0])):
			for i in range(o,len(ansaa[0])):
				for k in range(0,len(ansaz)):
					ansaa[kkr][j][0] = inputa[kkr][0]*outputweightin[j][i]
					ansaz[k][j][0] = layer[k][0]*outputweightlay[j][i]
	for kkr in range(0,len(totalputs)):
		totalputs[kkr][0] = ansaa[0][kkr][0]+ansaa[1][kkr][0]+ansaa[2][kkr][0]+ansaa[3][kkr][0]+ansaa[4][kkr][0]+ansaa[5][kkr][0]+ansaa[6][kkr][0]+ansaa[7][kkr][0]+ansaa[8][kkr][0]+ansaa[9][kkr][0]+ansaa[10][kkr][0]+ansaa[11][kkr][0]+ansaa[12][kkr][0]+ansaa[13][kkr][0]+ansaa[14][kkr][0]+ansaa[15][kkr][0]+ansaa[16][kkr][0]+ansaa[17][kkr][0]+ansaa[18][kkr][0]+ansaz[0][kkr][0]+ansaz[1][kkr][0]+ansaz[2][kkr][0]+ansaz[3][kkr][0]+ansaz[4][kkr][0]+ansaz[5][kkr][0]+ansaz[6][kkr][0]+ansaz[7][kkr][0]+ansaz[8][kkr][0]+ansaz[9][kkr][0]+ansaz[10][kkr][0]+ansaz[11][kkr][0]+ansaz[12][kkr][0]+ansaz[13][kkr][0]+ansaz[14][kkr][0]+ansaz[15][kkr][0]
	for kkr in range(0,len(outputbias)):
		sigfood[kkr][0] = totalinputs[kkr][0]+outputbias[kkr][0]
	for kkr in range(0,len(ultimate)):
		ultimate[kkr][0] = 1/(1+math.exp(-1(sigfood[kkr][0])))
for ikkk in range(0, len(layerweight)):
	for jkkk in range(0, len(layerweight[0])):
		layerweight[ikkk][jkkk] = random.randint(-777, 777)
for ikkk in range(0, len(layerbias)):
	for jkkk in range(0, len(layerbias[0])):
		layerbias[ikkk][jkkk] = random.randint(-777, 777)
for ikkk in range(0, len(outputweightin)):
	for jkkk in range(0, len(outputweightin[0])):
		outputweightin[ikkk][jkkk] = random.randint(-777, 777)
for ikkk in range(0, len(outputweightlay)):
	for jkkk in range(0, len(outputweightlay[0])):
		outputweighlay[ikkk][jkkk] = random.randint(-777, 777)
for ikkk in range(0, len(outputbias)):
	for jkkk in range(0, len(outputbias[0])):
def decide(inputa,layerweight,layerbias,outputweightin,outputweightlay,outputbias)
	layer(inputa,layerweight,layerbias)
	output(inputa,layer,outputweightin,outputweightlay,outputbias)
	if(ultimate[0][0]>ultimate[1][0]and ultimate[0][0]>ultimate[2][0]and ultimate[0][0]>ultimate[3][0]and ultimate[0][0]>ultimate[4][0]and ultimate[0][0]>ultimate[5][0]and ultimate[0][0]>ultimate[6][0]and ultimate[0][0]>ultimate[7][0]and ultimate[0][0]>ultimate[8][0]):
		deci=1
	if(ultimate[1][0]>ultimate[0][0]and ultimate[1][0]>ultimate[2][0]and ultimate[1][0]>ultimate[3][0]and ultimate[1][0]>ultimate[4][0]and ultimate[1][0]>ultimate[5][0]and ultimate[1][0]>ultimate[6][0]and ultimate[1][0]>ultimate[7][0]and ultimate[1][0]>ultimate[8][0]):
		deci=2
	if(ultimate[2][0]>ultimate[1][0]and ultimate[2][0]>ultimate[0][0]and ultimate[2][0]>ultimate[3][0]and ultimate[2][0]>ultimate[4][0]and ultimate[2][0]>ultimate[5][0]and ultimate[2][0]>ultimate[6][0]and ultimate[2][0]>ultimate[7][0]and ultimate[2][0]>ultimate[8][0]):
		deci=3
	if(ultimate[3][0]>ultimate[2][0]and ultimate[3][0]>ultimate[1][0]and ultimate[3][0]>ultimate[0][0]and ultimate[3][0]>ultimate[4][0]and ultimate[3][0]>ultimate[5][0]and ultimate[3][0]>ultimate[6][0]and ultimate[3][0]>ultimate[7][0]and ultimate[3][0]>ultimate[8][0]):
		deci=4
	if(ultimate[4][0]>ultimate[0][0]and ultimate[4][0]>ultimate[1][0]and ultimate[4][0]>ultimate[2][0]and ultimate[4][0]>ultimate[3][0]and ultimate[4][0]>ultimate[5][0]and ultimate[4][0]>ultimate[6][0]and ultimate[4][0]>ultimate[7][0]and ultimate[4][0]>ultimate[8][0]):
		deci=5
	if(ultimate[5][0]>ultimate[0][0]and ultimate[5][0]>ultimate[1][0]and ultimate[5][0]>ultimate[2][0]and ultimate[5][0]>ultimate[3][0]and ultimate[5][0]>ultimate[4][0]and ultimate[5][0]>ultimate[6][0]and ultimate[5][0]>ultimate[7][0]and ultimate[5][0]>ultimate[8][0]):
		deci=6
	if(ultimate[6][0]>ultimate[0][0]and ultimate[6][0]>ultimate[1][0]and ultimate[6][0]>ultimate[2][0]and ultimate[6][0]>ultimate[3][0]and ultimate[6][0]>ultimate[4][0]and ultimate[6][0]>ultimate[7][0]and ultimate[6][0]>ultimate[8][0]and ultimate[6][0]>ultimate[5][0]):
		deci=7
	if(ultimate[7][0]>ultimate[0][0]and ultimate[7][0]>ultimate[1][0]and ultimate[7][0]>ultimate[2][0]and ultimate[7][0]>ultimate[3][0]and ultimate[7][0]>ultimate[4][0]and ultimate[7][0]>ultimate[5][0]and ultimate[7][0]>ultimate[6][0]and ultimate[7][0]>ultimate[8][0]):
		deci=8
	if(ultimate[8][0]>ultimate[0][0]and ultimate[8][0]>ultimate[1][0]and ultimate[8][0]>ultimate[2][0]and ultimate[8][0]>ultimate[3][0]and ultimate[8][0]>ultimate[4][0]and ultimate[8][0]>ultimate[5][0]and ultimate[8][0]>ultimate[6][0]and ultimate[8][0]>ultimate[7][0]):
		deci=9
	if(deci==1):
		choice='a'
	if(deci==2):
		choice='b'
	if(deci==3):
		choice='c'
	if(deci==4):
		choice='d'
	if(deci==5):
		choice='e'
	if(deci==6):
		choice='f'
	if(deci==7):
		choice='g'
	if(deci==8):
		choice='h'
	if(deci==9):
		choice='i'
	if(xround==5):
		xra=inputa
		xaltimate=ultimate
		xalayer=layer
		xrainput=ansaa
		xralayer=ansaz
		xafull=totalputs
		xraf=ansa
		xadeci=deci
	if(xround==4):
		xrb=inputa
		xbltimate=ultimate
		xblayer=layer
		xrbinput=ansaa
		xrblayer=ansaz
		xbfull=totalputs
		xrbf=ansa
		xbdeci=deci
	if(xround==3):
		xrc=inputa
		xcltimate=ultimate
		xclayer=layer
		xrcinput=ansaa
		xrclayer=ansaz
		xcfull=totalputs
		xrcf=ansa
		xcdeci=deci
	if(xround==2):
		xrd=inputa
		xdltimate=ultimate
		xdlayer=layer
		xrdinput=ansaa
		xrdlayer=ansaz
		xdfull=totalputs
		xrdf=ansa
		xddeci=deci
	if(xround==1):
		xre=inputa
		xeltimate=ultimate
		xelayer=layer
		xreinput=ansaa
		xrelayer=ansaz
		xefull=totalputs
		xref=ansa
		xedeci=deci
	if(oround==4):
		oraa=inputa
		oaltimate=ultimate
		oalayer=layer
		orainput=ansaa
		oralayer=ansaz
		oafull=totalputs
		oraf=ansa
		oadeci=deci
	if(oround==3):
		orbb=inputa
		obltimate=ultimate
		oblayer=layer
		orbinput=ansaa
		orblayer=ansaz
		obfull=totalputs
		orbf=ansa
		obdeci=deci
	if(oround==2):
		orcc=inputa
		ocltimate=ultimate
		oclayer=layer
		orcinput=ansaa
		orclayer=ansaz
		ocfull=totalputs
		orcf=ansa
		ocdeci=deci
	if(oround==1):
		ordd=inputa
		odltimate=ultimate
		odlayer=layer
		ordinput=ansaa
		ordlayer=ansaz
		odfull=totalputs
		ordf=ansa
		oddeci=deci
def gitgood(xround,oround,win,xra,xaltimate,xalayer,xrainput,xralayer,xafull,xraf,xadeci,xrb,xbltimate,xblayer,xrbinput,xrblayer,xbfull,xrbf,xbdeci,xrc,xcltimate,xclayer,xrcinput,xrclayer,xcfull,xrcf,xcdeci,xrd,xdltimate,xdlayer,xrdinput,xrdlayer,xdfull,xrdf,xddeci,xre,xeltimate,xelayer,xreinput,xrelayer,xefull,xref,xedeci,oraa,oaltimate,oalayer,orainput,oralayer,oafull,oraf,oadeci,orbb,obltimate,oblayer,orbinput,orblayer,obfull,orbf,obdeci,orcc,ocltimate,oclayer,orcinput,orclayer,ocfull,orcf,ocdeci,ordd,odltimate,odlayer,ordinput,ordlayer,odfull,ordf,oddeci):
	
	if(oround=2):
		ckplr=0
		bkplr=2/10
		akplr=1
		dkplr=0
		ekplr=0
	if(oround=3):
		ckplr=1/10
		bkplr=2/10
		akplr=1
		dkplr=0
		ekplr=0
	if(oround=4):
		ckplr=2/10
		bkplr=1/10
		akplr=1/20
		dkplr=1/20
		ekplr=0
	if(win==x):
		time=0
		for i in range(len(xround),0):
			time=time+1
				if(time==1):
					xyz=1
				if(time==2):
					xyz=1/10
				if(time==3):
					xyz=1/20
				if(time==4):
					xyz=1/25
				if(time==5):
					xyz=1/40
			if(i==5):
				input=xra
				output=xaltimate
				layer=xalayer
				ansaa=xrainput
				ansaz=xralayer
				totalputs=xafull
				ansa=xraf
				deci=xadeci

			if(i==4):
				input=xrb
				output=xbltimate
				layer=xblayer
				ansaa=xrbinput
				ansaz=xrblayer
				totalputs=xbfull
				ansa=xrbf
				deci=xbdeci
			if(i==3):
				input=xrc
				output=xcltimate
				layer=xclayer
				ansaa=xrcinput
				ansaz=xrclayer
				totalputs=xcfull
				ansa=xrcf
				deci=xcdeci
			if(i==2):
				input=xrd
				output=xdltimate
				layer=xdlayer
				ansaa=xrdinput
				ansaz=xrdlayer
				totalputs=xdfull
				ansa=xrdf
				deci=xddeci
			if(i==1):
				input=xre
				output=xeltimate
				layer=xelayer
				ansaa=xreinput
				ansaz=xrelayer
				totalputs=xefull
				ansa=xref
				deci=xedeci
				time=0
			for i in range(0,len,output):
				if(i==deci):
					target=(1-output[i][0])*xyz+output[i][0]
					if(target>1):
						target=1
				else
					target=(0-output[i][0])*xyz+output[i][0]
					if(target<0):
						target=0
				pob=(bias[i][0]/(bias[i][0]+totalputs[i][0])*77
				potp=(totalputs[i][0]/(bias[i][0]+totalputs)*77
				x+pob=y+potp
				z=(log((1-target)/target))/(y*bias[i][0]+x*totalputs[i][0])
				bias=bias*y*z
				sum=0
				sub=0
				for i in range	
for evo in range(0,100000):
	a = "#"
	b = "#"
	c = "#"
	d = "#"
	e = "#"
	f = "#"
	g = "#"
	h = "#"
	i = "#"

	owin = 0
	xwin = 0
	xround=0
	oround=0
	while(xwin == 0 and owin == 0):
    		xplace = 0
		while(xplace == 0):
        		xround=xround+1
			if(a == "#" and b == "#" and c == "#" and d == "#" and e == "#" and f == "#" and g == "#" and h == "#" and i == "#"):
				inputa[9][0]=1
			if(a == 'x'):
				inputa[0][0]=1
			if(b == 'x'):
				inputa[1][0]=1
			if(c == 'x'):
				inputa[2][0]=1
			if(d == 'x'):
				inputa[3][0]=1
			if(e == 'x'):
				inputa[4][0]=1
			if(f == 'x'):
				inputa[5][0]=1
			if(g == 'x'):
				inputa[6][0]=1
			if(h == 'x'):
				inputa[7][0]=1
			if(i == 'x'):
				inputa[8][0]=1
			if(a == 'o'):
				inputa[10][0]=1
			if(b == 'o'):
				inputa[11][0]=1
			if(c == 'o'):
				inputa[12][0]=1
			if(d == 'o'):
				inputa[13][0]=1
			if(e == 'o'):
				inputa[14][0]=1
			if(f == 'o'):
				inputa[15][0]=1
			if(g == 'o'):
				inputa[16][0]=1
			if(h == 'o'):
				inputa[17][0]=1
			if(i == 'o'):
				inputa[18][0]=1
			decide(inputa,layerweight,layerbias,outputweightin,outputweightlay,outputbias)
			xchoice = choice
        		if(xchoice == 'a'):
            			if(a == 'o' or a == 'x'):
                #tell network it is trash
            		else:
                		a = 'x'
                		xplace = 1
        		elif(xchoice == 'b'):
            			if(b == 'o' or b == 'x'):
                #tell network it is trash
            			else:
                			b = 'x'
                			xplace = 1
        		elif(xchoice == 'c'):
            			if(c == 'o' or c == 'x'):
                #tell network it is trash
            			else:
                			c = 'x'
               			 	xplace = 1
        		elif(xchoice == 'd'):
            			if(d == 'o' or d == 'x'):
                #tell network it is trash
            			else:
                			d = 'x'
                			xplace = 1
        		elif(xchoice == 'e'):
           		 	if(e == 'o' or e == 'x'):
                #tell network it is trash
            			else:
                			e = 'x'
                			xplace = 1
        		elif(xchoice == 'f'):
            			if(f == 'o' or f == 'x'):
                #tell network it is trash
            			else:
                			f = 'x'
                			xplace = 1
        		elif(xchoice == 'g'):
            			if(g == 'o' or g == 'x'):
                #tell network it is trash
            			else:
                			g = 'x'
                			xplace = 1
        		elif(xchoice == 'h'):
            			if(h == 'o' or h == 'x'):
                #tell network it is trash
           			else:
                			h = 'x'
                			xplace = 1
        		elif(xchoice == 'i'):
            			if(i == 'o' or i == 'x'):
                #tell network it is trash
            			else:
                			i = 'x'
                			xplace = 1
        	
        
    		if ((a=='x' and b=='x' and c=='x') or (d=='x' and e=='x' and f=='x') or (g=='x' and h=='x' and i=='x') or (a=='x' and d=='x' and g=='x') or (b=='x' and e=='x' and h=='x') or (c=='x' and f=='x' and i=='x') or (a=='x' and e=='x' and i=='x') or (c=='x' and e=='x' and g=='x')):
        	xwin = 1
				gitgood(xround,oround,win,xra,xaltimate,xalayer,xrainput,xralayer,xafull,xraf,xadeci,xrb,xbltimate,xblayer,xrbinput,xrblayer,xbfull,xrbf,xbdeci,xrc,xcltimate,xclayer,xrcinput,xrclayer,xcfull,xrcf,xcdeci,xrd,xdltimate,xdlayer,xrdinput,xrdlayer,xdfull,xrdf,xddeci,xre,xeltimate,xelayer,xreinput,xrelayer,xefull,xref,xedeci,oraa,oaltimate,oalayer,orainput,oralayer,oafull,oraf,oadeci,orbb,obltimate,oblayer,orbinput,orblayer,obfull,orbf,obdeci,orcc,ocltimate,oclayer,orcinput,orclayer,ocfull,orcf,ocdeci,ordd,odltimate,odlayer,ordinput,ordlayer,odfull,ordf,oddeci)
        	break
    		oplace = 0
    		while(oplace == 0):
			oround=oround+1
			if(a == "#" and b == "#" and c == "#" and d == "#" and e == "#" and f == "#" and g == "#" and h == "#" and i == "#"):
				inputa[9][0]=1
			if(a == 'o'):
				inputa[0][0]=1
			if(b == 'o'):
				inputa[1][0]=1
			if(c == 'o'):
				inputa[2][0]=1
			if(d == 'o'):
				inputa[3][0]=1
			if(e == 'o'):
				inputa[4][0]=1
			if(f == 'o'):
				inputa[5][0]=1
			if(g == 'o'):
				inputa[6][0]=1
			if(h == 'o'):
				inputa[7][0]=1
			if(i == 'o'):
				inputa[8][0]=1
			if(a == 'x'):
				inputa[10][0]=1
			if(b == 'x'):
				inputa[11][0]=1
			if(c == 'x'):
				inputa[12][0]=1
			if(d == 'x'):
				inputa[13][0]=1
			if(e == 'x'):
				inputa[14][0]=1
			if(f == 'x'):
				inputa[15][0]=1
			if(g == 'x'):
				inputa[16][0]=1
			if(h == 'x'):
				inputa[17][0]=1
			if(i == 'x'):
				inputa[18][0]=1
			decide(inputa,layerweight,layerbias,outputweightin,outputweightlay,outputbias)
        		ochoice = choice
        			if(ochoice == 'a'):
            				if(a == 'x' or a == 'o'):
                #tell network it is trash
            				else:
                				a = 'o'
                				oplace = 1
        			elif(ochoice == 'b'):
            				if(b == 'x' or b == 'o'):
                #tell network it is trash
            				else:
                				b = 'o'
                				oplace = 1
        			elif(ochoice == 'c'):
            				if(c == 'x' or c == 'o'):
                #tell network it is trash
            				else:
                				c = 'o'
		        			oplace = 1
				elif(ochoice == 'd'):
            				if(d == 'x' or d == 'o'):
                #tell network it is trash
            				else:
                				d = 'o'
               					 oplace = 1
        			elif(ochoice == 'e'):
            				if(e == 'x' or e == 'o'):
                #tell network it is trash
            				else:
                				e = 'o'
                				oplace = 1
        			elif(ochoice == 'f'):
            				if(f == 'x' or f =='o'):
                #tell network it is trash
            				else:
                				f = 'o'
                				oplace = 1
        			elif(ochoice == 'g'):
            				if(g == 'x' or g == 'o'):
                #tell network it is trash
		
					else:
                				g = 'o'
                				oplace = 1
        			elif(ochoice == 'h'):
            				if(h == 'x' or h == 'o'):
                #tell network it is trash
		
            				else:
                				h = 'o'
                				oplace = 1
        			elif(ochoice == 'i'):
            				if(i == 'x' or i == 'o'):
                #tell network it is trash
		
            				else:
                				i = 'o'
                				oplace = 1
        		
    			if ((a=='o' and b=='o' and c=='o') or (d=='o' and e=='o' and f=='o') or (g=='o' and h=='o' and i=='o') or (a=='o' and d=='o' and g=='o') or (b=='o' and e=='o' and h=='o') or (c=='o' and f=='o' and i=='o') or (a=='o' and e=='o' and i=='o') or (c=='o' and e=='o' and g=='o')):
        			owin = 1
        			gitgood(xround,oround,win,xra,xaltimate,xalayer,xrainput,xralayer,xafull,xraf,xadeci,xrb,xbltimate,xblayer,xrbinput,xrblayer,xbfull,xrbf,xbdeci,xrc,xcltimate,xclayer,xrcinput,xrclayer,xcfull,xrcf,xcdeci,xrd,xdltimate,xdlayer,xrdinput,xrdlayer,xdfull,xrdf,xddeci,xre,xeltimate,xelayer,xreinput,xrelayer,xefull,xref,xedeci,oraa,oaltimate,oalayer,orainput,oralayer,oafull,oraf,oadeci,orbb,obltimate,oblayer,orbinput,orblayer,obfull,orbf,obdeci,orcc,ocltimate,oclayer,orcinput,orclayer,ocfull,orcf,ocdeci,ordd,odltimate,odlayer,ordinput,ordlayer,odfull,ordf,oddeci)
				break
