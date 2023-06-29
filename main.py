
import random
import numpy as np
import csv, os
import _thread
import matplotlib.pyplot as plt

print(str(0)+','+str( 0),file = open('target.csv','w'))
def controle_arrastar():
	os.system('python3 controle.py')
_thread.start_new_thread(controle_arrastar,())

initial = [5,5]
limites = [(-800,800),(-800,800)]

cores = np.array([
    ( 31, 119, 180), (174, 199, 232), (255, 127,  14), (255, 187, 120),
    ( 44, 160,  44), (152, 223, 138), (214,  39,  40), (255, 152, 150),
    (148, 103, 189), (197, 176, 213), (140,  86,  75), (196, 156, 148),
    (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
    (188, 189,  34), (219, 219, 141), ( 23, 190, 207), (158, 218, 229),

    ( 31, 119, 180), (174, 199, 232), (255, 127,  14), (255, 187, 120),
    ( 44, 160,  44), (152, 223, 138), (214,  39,  40), (255, 152, 150),
    (148, 103, 189), (197, 176, 213), (140,  86,  75), (196, 156, 148),
    (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
    (188, 189,  34), (219, 219, 141), ( 23, 190, 207), (158, 218, 229),

    ( 31, 119, 180), (174, 199, 232), (255, 127,  14), (255, 187, 120),
    ( 44, 160,  44), (152, 223, 138), (214,  39,  40), (255, 152, 150),
    (148, 103, 189), (197, 176, 213), (140,  86,  75), (196, 156, 148),
    (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
    (188, 189,  34), (219, 219, 141), ( 23, 190, 207), (158, 218, 229),

    ( 31, 119, 180), (174, 199, 232), (255, 127,  14), (255, 187, 120),
    ( 44, 160,  44), (152, 223, 138), (214,  39,  40), (255, 152, 150),
    (148, 103, 189), (197, 176, 213), (140,  86,  75), (196, 156, 148),
    (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
    (188, 189,  34), (219, 219, 141), ( 23, 190, 207), (158, 218, 229)

]) / 255.


class Particula: 
	def __init__(self,initial):
		self.posicao=[]
		self.vel=[] 
		self.melhor_posicao=[] 
		self.menor_erro=-1 
		self.erro=-1     
		for i in range(0,dimensoes): 
			self.vel.append(random.uniform(-1,1))
			self.posicao.append(initial[i])
	
	def atualizar_velocidade(self,melhor_pos_global): 
		w = 0.5
		c1 = 1 
		c2 = 2 
		
		for i in range(0,dimensoes): 
			r1=random.random()
			r2=random.random()
			
			cog_vel=c1*r1*(self.melhor_posicao[i]-self.posicao[i])
			social_vel=c2*r2*(melhor_pos_global[i]-self.posicao[i])
			self.vel[i]=w*self.vel[i]+cog_vel+social_vel 
		
	def atualizar_posicao(self,limites): 
		for i in range(0,dimensoes):
			self.posicao[i]=self.posicao[i]+self.vel[i]
			
			
			if self.posicao[i]>limites[i][1]:
				self.posicao[i]=limites[i][1]

				
			if self.posicao[i] < limites[i][0]:
				self.posicao[i]=limites[i][0]
	
	
	def evaluate_fitness(self,fitness_function):
		self.erro=fitness_function(self.posicao) 
		print("erro:",self.erro)
		
		if self.erro < self.menor_erro or self.menor_erro==-1:
			self.melhor_posicao=self.posicao 
			self.menor_erro=self.erro

def fitness_function(x):
	x0,y0 = getXY('target.csv') 
	x0=float(x0)
	y0=float(y0)
	total=0 
	total+=(x0-x[0])**2 +(y0-x[1])**2
	return total


def getXY(filename):
	lat=0
	long=0
	with open(filename) as csvDataFile:
		csvReader = csv.reader(csvDataFile)
		for row in csvReader:
			lat = row[0]
			long= row[1]
	return lat,long
import time

class PSO():
	def __init__(self,fitness_function,initial,limites,num_Particulas):
		global dimensoes 
		
		dimensoes = len(initial) 
		global_menor_erro=-1             
		melhor_pos_global=[] 
		self.gamma = 0.0001
		enxame=[]
		for i in range(0,num_Particulas):
			enxame.append(Particula(initial))

		i=0
		while True: 
			for j in range(0,num_Particulas):
				enxame[j].evaluate_fitness(fitness_function)
				print('Melhor posição global',enxame[j].erro,global_menor_erro)

				
				if enxame[j].erro < global_menor_erro or global_menor_erro == -1:
					melhor_pos_global=list(enxame[j].posicao) 
					global_menor_erro=float(enxame[j].erro)
					plt.title("Simulação de enxame com PSO, Nº de particulas:{}, taxa de erro:{}".format(num_Particulas,round(global_menor_erro,1)))
					
				if i%2==0:	
					global_menor_erro=-1
					melhor_pos_global = list([enxame[j].posicao[0]+self.gamma*(enxame[j].erro)*random.random() ,enxame[j].posicao[1]+self.gamma*(enxame[j].erro)*random.random() ])
					
				
			posicao_0 = {}
			posicao_1 = {}
			for j in range(0,num_Particulas): 
				posicao_0[j] = []
				posicao_1[j] = []	
			
			for j in range(0,num_Particulas): 
				enxame[j].atualizar_velocidade(melhor_pos_global)
				enxame[j].atualizar_posicao(limites) 
				
			
				posicao_0[j].append(enxame[j].posicao[0])
				posicao_1[j].append(enxame[j].posicao[1])
		
				plt.xlim([-500, 500])
				plt.ylim([-500, 500])
				
			for j in range(0,num_Particulas):
				plt.plot(posicao_0[j], posicao_1[j],  color = cores[j],marker = 'o'  )


			x,y = getXY('target.csv')	 
			plt.plot(float(x), float(y),  color = 'k',marker = 'o'  )
			plt.pause(0.00001)
			
			plt.clf() 
			i+=1
		

		
PSO(fitness_function,initial,limites,num_Particulas=8)

