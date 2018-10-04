



def print_madj(m):

	print("     "+", ".join(list(map(str,range(len(m))))))

	for  i,l in enumerate(m):
		print(i,":",l)
		

def create_madj(g):

	vertices=g[0]
	arestas=g[1]
	k=len(vertices)
	m=[]
	for i in range(k):
		m.append([])
		for j in range(k):
			m[i].append(0)
			

	for a in arestas:
		m[a[0]][a[1]]=1
		m[a[1]][a[0]]=1
		
	
	return m


def calcula_grau(v,m):

	n=0
	l=m[v]
	for el in l:
		if el!=0:
			n+=1

	return n

def eh_vizinho(a,b,m):

	return (a!=b and (m[a][b]!=0))
	

def calc_num_ligacoes_entre_vizinhos(v,m):
	n=0
	for i,a in  enumerate(m[v]):
		for j,b in enumerate(m[v]):
			if a!=0 and b!=0 and i>j:
				if eh_vizinho(i,j,m):
					n+=1
	
	return n


def calcular_menor_distancia(v_a,v_b,m,last=None):

	if last== None:
		last=v_a

	menor=-1

	n_vizinhos=0
	for i,a in enumerate(m[v_a]):
		if a==1 and i!=last:

			



			n_vizinhos+=1
			if i==v_b:
				return 1
			else:
				m[v_a][i]=2

				t=calcular_menor_distancia(i,v_b,m,i)
				m[v_a][i]=1

				if t!=None and (menor<0 or t<menor):
					menor=t

	if n_vizinhos==0:
		return None
	else:
		return menor+1






def calcula_coeficiente_clusterizacao(v,m):
	e=calc_num_ligacoes_entre_vizinhos(v,m)
	
	grau=calcula_grau(v,m)

	return 0 if grau<=1 else  2*e/float((grau*(grau-1)))
	 

if __name__=="__main__":

	vertices=list(map(int,input("digite a lista de vértices numerados desde zero:").split()))
	a=input('digite a lista de adjacencias separadas por "," e ";":').split(";")

	arestas=[]
	for el in a:
		arestas.append(list(map(int,el.split(","))))

	g=[vertices,arestas]
	
	m=create_madj(g)
	
	print_madj(m)


	print("num. vértices:", len(m))
	print("num. arestas:", len(arestas))

	s=0
	for v in vertices: 
		grau=calcula_grau(v,m)
		print("grau do vértice",v,": ",grau)
		s+=grau


	print("grau médio :", s/len(vertices))

	s=0
	for v in vertices:
		c=calcula_coeficiente_clusterizacao(v,m)
		s+=c
		print("coeficiente de clusterização para o vértice ",v,": ",c)

	print("média do coeficiente de clusterização:",s/float(len(vertices)))

	diametro=0
	menores_distancias={}
	for v_a in vertices:
		menores_distancias[v_a]=[]
		for v_b in vertices:
			if v_a!=v_b:
				d=calcular_menor_distancia(v_a,v_b,m)
				menores_distancias[v_a].append(d)
				if d > diametro:
					diametro=d
	s=0
	keys=sorted(menores_distancias.keys())
	for key in keys:
		distancias=menores_distancias[key]
		print("menores distancias do vértice ",key,":",distancias)
		media=sum(distancias)/float(len(distancias))
		s+=media
		print("média das menores distâncias para o vértice ",key,":",sum(distancias)/float(len(distancias)))

	print("média das menores distâncias do grafo:",s/float(len(vertices)))

	print("Diâmetro do grafo:",diametro)







	



