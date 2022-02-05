filen=open("qwerty.txt",'r')
fn1=open("qwerty.txt",'w')
cont=filen.readlines()
for i in range(0,len(cont)):
 if(i % 2 == 0):
  fn1.write(cont[i])
 else:
  pass
fn1.close()
fn1=open("qwerty.txt",'r')
cont1=fn1.readlines()
print(cont1)
filen.close()
fn1.close()
