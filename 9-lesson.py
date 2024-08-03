# 📌LESSON 9
# elif
# and, or

# a = int(input("a:"))
# if a == 0:
#     print("oge ten")
#     print("0 ge ten' ")
# elif a%2==1:
#     print("taq san")
# else:
#     print("jup san ")

# til= input("tildi tanlan' uz/en/ru : ")
# if til=="uz":
#     print("Assalamu aleykum")
# elif til=="en":
#     print("Hello")
# elif til=="ru":
#     print("привет")
# else:
#     print("uz/en/ru tilin tanlan'!")

# a=int(input('jasinizdi kiritin: '))
# if a<=4:
#     print("Kiriw biypul")
# elif 4<a<=12:
#     print("Bilet bahasi 5000 swm")
# else:
#     print("Bilet bahasi 10000 swm")


# san=int(input("san kiritin: "))
# if san==0:
#     print("o ge ten")
# elif san>0:
#     print("on san") 
# else:
#     print("teris san")
# ati=input("atinizdi kiritin: ")
# fam= input("familyanizdi kiritin: " )
# if ati or fam:
#     print("Salem")
# else:
#     print("Atinizdi ya familyanizdi kiritin!")
    

# kun=input(" bugin neshinshi kun? : ")
# if kun=="6" or kun.lower()=="qalakun":
#     print("Bugin dem aliw kuni ")
# else:
#     print("Harma")
    

# summa=input("summani kiritin': ")
# if summa.isdigit() and int(summa)>0 and int(summa)<500000:
#     print("Raxmet!")
# else:
#     print("Qatelik bar!")






# cena=15000
# shay=True
# salat=False
# if shay and salat:
#     cena+= 10000
# elif shay or salat:
#     cena+= 5000
#     print(cena)



# menu=['palaw', 'gurtik', 'shawle', 'narin', 'somsa']
# awqat=input("Qanday awqat jeysiz? ")
# if awqat.lower() in menu:
#     print(" Buyirtpa qabillandi! ")
# else:
#     print("Keshiresiz , bunday awqat menuda joq! ")        
        
# menu=['palaw', 'gurtik', 'shawle', 'narin', 'somsa']
# buyirtpalar=['palaw', 'somsa', 'manti', 'shashlik']
# if buyirtpalar:
#     for awqat in buyirtpalar:
#         if awqat in menu:
#             print(f"menuda {awqat} bar ")
#         else:
#             print(f"menuda {awqat} joq")





# a=int(input('jasinizdi kiritin: '))
# if a<=4 or a>60:
#     print("Sizge kiriw biypul")
# elif a<18:
#     print("Siz ushin bilet bahasi 10000 swm  ")
# else:
#     print("Siz ushin bilet bahasi 20000 swm")



# a=int(input('a: '))
# b=int(input('b: '))
# if a==b:
#     print(f"{a} = {b}")
# elif a>b:
#     print(f" {a}>{b}")    
# else:
#     print(f" {a}<{b}")
        
# onimler=['alma', 'erik', 'almurt', 'banan', 'juzim', 'anar', 'garbiz', 'apelsin', 'malina', 'limon']
# sebet=[]
# print('sebetke 5 onimdi qosin: ')
# n=0
# for n in range(5):
#     sebet.append(input(f" {n+1}shi onimdi qosin "))
#     # n+=1
#     print(sebet)
#     n+=1
# if sebet:
#   for onim in sebet:
      
#       if onim in onimler:
#           print(f"Dukanimizda {onim} bar")
#       else:
#           print(f"Dukanimizda {onim} joq")
