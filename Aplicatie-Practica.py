f=open("C:\Informatica Lista clasei 11D.txt",'r')
linii=list(f)
f.close()
nr=0
m=0
print('Nume', 'Prenume', 'Nota', 'Grupele' ,sep='\t')
x=open('Lista clasei 11D Engl1 .txt','w')
y=open('Lista clasei 11D Engl2 .txt','w')
for linie in linii:
	 print(linie.rstrip())
campuri=linie.split()
nota=int(campuri[2])
nr+=1
m+=nota
if campuri[3]=='Engl1':
	x.write(campuri[0]+' '+campuri[1]+' '+campuri[2])
	x.write('\n')
if campuri[3]=='Engl2':
    y.write(campuri[0]+' '+campuri[1]+' '+campuri[2])
    y.write('\n')
print('Media elevilor  este',m/float(nr))
x.close()
y.close()