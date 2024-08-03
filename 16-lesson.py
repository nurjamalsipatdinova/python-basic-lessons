"""
Created on Tue Apr 23 14:46:14 2024
TEMA: Funkciya
@author: acer
"""

# def bahalaw(atlar):
#     bahalar={}
#     while atlar:
#         at=atlar.pop()
#         baha=input(f"{at.title()} ga baha qoyin:")
#         bahalar[at]=int(baha)
#     return bahalar
# studentler=['bayram', 'rasul', 'artur', 'sultan']
# bahalar=bahalaw(studentler)
# print(bahalar)



# def toliq_ati(ati,familyasi,ochestvasi=" "):
#     if ochestvasi:
#         at_fam=f"{ati} {familyasi} {ochestvasi}"
#     else:
#         at_fam=f"{ati} {familyasi}"
#     return at_fam.title()
# student1=toliq_ati("ali", "nizamov")
# student2=toliq_ati("artur", "nizamov", "polatovich")




# def summa(*sanlar):
#     jiyindi=0
#     for san in sanlar:
#         jiyindi+=san
#     return jiyindi
# obshi=summa(8,6,8,9,2,3)
# print(obshi)


# def consol(*atlar):
#     for i in atlar:
#         print(i.title)
    
# atlar=["darmen", "artur", "rasul"]
# print(atlar)




# def avto_info(kompaniya, model, **maglumatlar):
#     maglumatlar["kompaniya"]=kompaniya
#     maglumatlar["model"]=model
#     return maglumatlar
# avto1=avto_info("gm", "malibu", color="qara", jil=2018)
# avto2=avto_info("Kia", "k5", color="aq", jil=2019)
# print(avto1)
# print(avto2)


# def mandat( **ball):
#     # ball["darmen"]=73
#     # ball["artur"]=68
#     # ball["timur"]=96
#     for key,value in ball.items():
#         print(f"{key.title()} {value} ball aldi ")
#     return ball 
# n=mandat(darmen=73, artur=68, timur=96)
# print(n)
