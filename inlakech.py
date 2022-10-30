from PIL import Image, ImageDraw
import random,math

float_gen= lambda a,b:random.uniform(a,b)

image=Image.new("RGB",(4000,6000),color=(255,222,173))

draw=ImageDraw.Draw(image)


pointsx=[]
pointsy=[]
for i in range(100,7404):
    k=0
    k=(i)*math.sin(i)**(-2)
    pointsx.append(k)
for i in range(100,7404):
    k=0
    k=(i)*math.tan(i)**2
    pointsy.append(k)

for x,y in zip(pointsx,pointsy):
    a = 0
    b = 1
    number=pointsx.index(x)+1
    if number>=len(pointsx):
        break
    for _ in range(30):
        color=(0,0,0)
        draw.line((x+a,y+a,x+b,y+b),fill=color,width=65)
        a+=1
        b+=1
    for _ in range(30):
        draw.line((x+a,y+a,x+b,y+b),fill=color,width=65)
        a-=1
        b-=1

color=(255,239,213)
draw.rectangle((0,0,100,6000),width=50,fill=color)
draw.rectangle((3900,0,6000,6000),width=50,fill=color)
draw.rectangle((0,0,4000,200),width=50,fill=color)
draw.rectangle((0,5800,4000,6000),width=50,fill=color)


image.save(r"C:\Users\ABDULLAH\Desktop\nft.png")

new_image=Image.open(r"C:\Users\ABDULLAH\Desktop\nft.png")
pixels=new_image.load()
for i in range(new_image.size[0]):
    for j in range(new_image.size[1]):
        r,g,b=pixels[i,j]
        noisee=float_gen(0.5,1.5)
        pixels[i,j]=(int(r*noisee),int(g*noisee),int(b*noisee))
new_image.save(r"C:\Users\ABDULLAH\Desktop\nft.png")
