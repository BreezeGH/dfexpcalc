usrLvl = int(input("What level are you right now (1-50)?"))
usrXP = int(input("What is your XP count right now?"))
usrPrs = int(input("What prestige are you right now (0-10)?"))
usr20 = str(input("Are you a Kamado (write \"y\" or \"n\")?"))
usr10 = str(input("Are you a Tokito or Ubuyashiki (write \"y\" or \"n\")?"))

if(usrLvl==1):
    baseXP = (142058-0)
elif(usrLvl==2):
    baseXP = (142058-132)
elif(usrLvl==3):
    baseXP = (142058-271)
elif(usrLvl==4):
    baseXP = (142058-421)
elif(usrLvl==5):
    baseXP = (142058-587)
elif(usrLvl==6):
    baseXP = (142058-773)
elif(usrLvl==7):
    baseXP = (142058-985)
elif(usrLvl==8):
    baseXP = (142058-1228)
elif(usrLvl==9):
    baseXP = (142058-1508)
elif(usrLvl==10):
    baseXP = (142058-1831)
elif(usrLvl==11):
    baseXP = (142058-2204)
elif(usrLvl==12):
    baseXP = (142058-2633)
elif(usrLvl==13):
    baseXP = (142058-3125)
elif(usrLvl==14):
    baseXP = (142058-3687)
elif(usrLvl==15):
    baseXP = (142058-4327)
elif(usrLvl==16):
    baseXP = (142058-5051)
elif(usrLvl==17):
    baseXP = (142058-5868)
elif(usrLvl==18):
    baseXP = (142058-6785)
elif(usrLvl==19):
    baseXP = (142058-7810)
elif(usrLvl==20):
    baseXP = (142058-8951)
elif(usrLvl==21):
    baseXP = (142058-10216)
elif(usrLvl==22):
    baseXP = (142058-11614)
elif(usrLvl==23):
    baseXP = (142058-13152)
elif(usrLvl==24):
    baseXP = (142058-14840)
elif(usrLvl==25):
    baseXP = (142058-16686)
elif(usrLvl==26):
    baseXP = (142058-18700)
elif(usrLvl==27):
    baseXP = (142058-20890)
elif(usrLvl==28):
    baseXP = (142058-23265)
elif(usrLvl==29):
    baseXP = (142058-25834)
elif(usrLvl==31):
    baseXP = (142058-28607)
elif(usrLvl==32):
    baseXP = (142058-31593)
elif(usrLvl==33):
    baseXP = (142058-34802)
elif(usrLvl==34):
    baseXP = (142058-38243)
elif(usrLvl==35):
    baseXP = (142058-41926)
elif(usrLvl==36):
    baseXP = (142058-50057)
elif(usrLvl==37):
    baseXP = (142058-54525)
elif(usrLvl==38):
    baseXP = (142058-59275)
elif(usrLvl==39):
    baseXP = (142058-64317)
elif(usrLvl==40):
    baseXP = (142058-69661)
elif(usrLvl==41):
    baseXP = (142058-75318)
elif(usrLvl==42):
    baseXP = (142058-81298)
elif(usrLvl==43):
    baseXP = (142058-87612)
elif(usrLvl==44):
    baseXP = (142058-94270)
elif(usrLvl==45):
    baseXP = (142058-101283)
elif(usrLvl==46):
    baseXP = (142058-108662)
elif(usrLvl==47):
    baseXP = (142058-116418)
elif(usrLvl==48):
    baseXP = (142058-124562)
elif(usrLvl==49):
    baseXP = (142058-133105)
elif(usrLvl==50):
    baseXP = (142058-142058)
elif(usrLvl>50):
    baseXP = (142058-142058)
    print("You are already higher than level 50, you don't need any more experience to prestige.")
elif(usrLvl<1):
    print("You entered an impossible level.")
    baseXP = null

if(usr20=="y"):
    familyXP = 0.2
elif(usr10=="y"):
    familyXP = 0.1
elif(usr10!="y" + usr20!="y"):
    familyXP = 0.0

rqrXP = ((baseXP-usrXP)/((baseXP-usrXP)*(familyXP+(usrPrs*0.2+1)))*(baseXP-usrXP))
displayXP = int(rqrXP)


print("You need " + str(displayXP) + "EXP in order to get to level 50.")
print("You need to do " + str((rqrXP//21000) + (0 < rqrXP%21000)) + " (" + str(round((rqrXP/21000),2)) + ")" + " infinity castles (assuming you beat all bosses and grip no demons) to get to level 50.")
print("You need to do " + str((rqrXP//6000) + (0 < rqrXP%6000)) + " (" + str(round((rqrXP/6000),2)) + ")" + " Kaigakus in order to get to level 50.")
print("You need to do " + str((rqrXP//300) + (0 < rqrXP%300)) + " (" + str(round((rqrXP/300),2)) + ")" + " Zenitsus in order to get to level 50.")