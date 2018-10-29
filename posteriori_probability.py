import matplotlib.pyplot as plt
import math

file1 = open("data1.csv", "r")
file2 = open("data2.csv", "r")
red = []
green = []
x_red = []
y_red = []
x_green = []
y_green = []
lista_promien_x_g = []
lista_promien_y_g = []
lista_promien_x_r = []
lista_promien_y_r = []

x_do_kola = []
for line in file1:
    cords = line.split("|")
    red.append([float(cords[0].replace(",", ".")), float(cords[1].replace(",", ".").replace("\n", ""))])
    x_red.append(float(cords[0].replace(",", ".")))
    y_red.append(float(cords[1].replace(",", ".").replace("\n", "")))
for line in file2:
    cords = line.split("|")
    green.append([float(cords[0].replace(",", ".")), float(cords[1].replace(",", ".").replace("\n", ""))])
    x_green.append(float(cords[0].replace(",", ".")))
    y_green.append(float(cords[1].replace(",", ".").replace("\n", "")))




punkt_x = 1.12
punkt_y = 3.4
punkt = (punkt_x,punkt_y)
promien = 0.5





def points_on_circumference_x(center=(0, 0), r=1, n=100):
    return [(center[0]+(math.cos(2 * math.pi / n * x) * r)) for x in range(0, n + 1)]

def points_on_circumference_y(center=(0, 0), r=1, n=100):
    return [(center[1] + (math.sin(2 * math.pi / n * x) * r)) for x in range(0, n + 1)]


print(len(x_red),len(y_red))

while(len(lista_promien_x_r)==0 and len(lista_promien_x_g)==0):

    for i in range(0,len(x_red)):
        if(promien>(math.sqrt(math.pow((punkt_x-x_red[i]),2)+(math.pow((punkt_y-y_red[i]),2))))):
            lista_promien_x_r.append(x_red[i])
            lista_promien_y_r.append(y_red[i])
    for i in range(0,len(x_green)):
        if (promien>(math.sqrt(math.pow((punkt_x-x_green[i]),2)+(math.pow((punkt_y-y_green[i]),2))))):
            lista_promien_x_g.append(x_green[i])
            lista_promien_y_g.append(y_green[i])
    promien += 0.25

promien -= 0.25
calkowita = len(red)+len(green)
czerwonych_lacz = len(red)
zielonych_lacz = len(green)

czerwonych_sasied = len(lista_promien_x_r)
zielonych_sasied = len(lista_promien_x_g)

priori_red = czerwonych_lacz/calkowita
priori_green = zielonych_lacz/calkowita

czerwone_praw = czerwonych_sasied/czerwonych_lacz
zielone_praw = zielonych_sasied/zielonych_lacz

posteriori_red = priori_red * czerwone_praw
posteriori_green = priori_green * zielone_praw

print("promien:",promien)
print("green przed:",green,"red przed:",red)
print("zielonych",lista_promien_x_g,lista_promien_y_g,"czerw:",lista_promien_x_r,lista_promien_y_r)
print("zielonych",len(lista_promien_x_g),"czerw:",len(lista_promien_x_r))
print("posteriori red:",posteriori_red,"posteriori green:", posteriori_green)

grafika = plt.scatter(x_red,y_red,color='red')
grafika2 = plt.scatter(x_green,y_green,color='green')
pkt = plt.scatter(punkt_x,punkt_y,color='black')
okrag = plt.plot(points_on_circumference_x(punkt,promien,100),points_on_circumference_y(punkt,promien,100),color='yellow')
plt.show()