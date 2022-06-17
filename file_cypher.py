import os

def progress_bar(pourcentage, palier):
    if pourcentage < 5 and palier == 0:
        palier += 5
        print('[--------------------] 0%')
    elif pourcentage >= 5 and pourcentage < 10 and palier == 5:
        palier += 5
        print('[■-------------------] 5%')
    elif pourcentage >= 10 and pourcentage < 15 and palier == 10:
        palier += 5
        print('[■■------------------] 10%')
    elif pourcentage >= 15 and pourcentage < 20 and palier == 15:
        palier += 5
        print('[■■■-----------------] 15%')
    elif pourcentage >= 20 and pourcentage < 25 and palier == 20:
        palier += 5
        print('[■■■■----------------] 20%')
    elif pourcentage >= 25 and pourcentage < 30 and palier == 25:
        palier += 5
        print('[■■■■■---------------] 25%')
    elif pourcentage >= 30 and pourcentage < 35 and palier == 30:
        palier += 5
        print('[■■■■■■--------------] 30%')
    elif pourcentage >= 35 and pourcentage < 40 and palier == 35:
        palier += 5
        print('[■■■■■■■-------------] 35%')
    elif pourcentage >= 40 and pourcentage < 45 and palier == 40:
        palier += 5
        print('[■■■■■■■■------------] 40%')
    elif pourcentage >= 45 and pourcentage < 50 and palier == 45:
        palier += 5
        print('[■■■■■■■■■-----------] 45%')
    elif pourcentage >= 50 and pourcentage < 55 and palier == 50:
        palier += 5
        print('[■■■■■■■■■■----------] 50%')
    elif pourcentage >= 55 and pourcentage < 60 and palier ==55:
        palier += 5
        print('[■■■■■■■■■■■---------] 55%')
    elif pourcentage >= 60 and pourcentage < 65 and palier ==60:
        palier += 5
        print('[■■■■■■■■■■■■--------] 60%')
    elif pourcentage >= 65 and pourcentage < 70 and palier ==65:
        palier += 5
        print('[■■■■■■■■■■■■■-------] 65%')
    elif pourcentage >= 70 and pourcentage < 75 and palier ==70:
        palier += 5
        print('[■■■■■■■■■■■■■■------] 70%')
    elif pourcentage >= 75 and pourcentage < 80 and palier ==75:
        palier += 5
        print('[■■■■■■■■■■■■■■■-----] 75%')
    elif pourcentage >= 80 and pourcentage < 85 and palier ==80:
        palier += 5
        print('[■■■■■■■■■■■■■■■■----] 80%')
    elif pourcentage >= 85 and pourcentage < 90 and palier ==85:
        palier += 5
        print('[■■■■■■■■■■■■■■■■■---] 85%')
    elif pourcentage >= 90 and pourcentage < 95 and palier ==90:
        palier += 5
        print('[■■■■■■■■■■■■■■■■■■--] 90%')
    elif pourcentage >=95 and pourcentage < 100 and palier ==95:
        palier += 5
        print('[■■■■■■■■■■■■■■■■■■■-] 95%')
    elif pourcentage == 100 :
        print('[■■■■■■■■■■■■■■■■■■■■] 100%')

    return palier

def accueil():
    print('+-------------------------------------------------+')
    print('|                                                 |')   
    print('|                     ACCUEIL                     |')
    print('|                                                 |')
    print('+-------------------------------------------------+')
    print('         VEUILLEZ CHOISIR L ACTION A EFFECTUER')  
    print('1 : chiffrer un fichier')
    print('2 : déchiffre un fichier')
    print('3 : cacher un message dans un fichier jpg')
    choix = input()
    while choix != '1' and choix != '2' and choix != '3':
        print("veuillez choisir entre 1 et 2 et 3 !!!!!!")
        choix = input()
    
    return choix


def demander_fichier():
    continuer = False
    while continuer == False:
        print('veuillez entrer un chemin valide :')
        file_path = input()
        file_path = file_path.replace('"','')
        if not os.path.isfile(file_path):
            print('ceci n est pas un fichier')
        else:
            continuer = True
    return file_path

def demander_cle():
    continuer = False
    while continuer == False:
        print('veuillez entrer une clé valide : ')
        cle = input()
        for c in cle:
            if ord(c)<32 or ord(c)>126:
                print('le caractère '+c+' n est pas valide')
                continuer = False
                break
            else:
                continuer = True
    
    return cle

def chiffrer(fichier, cle):
    fic = open(fichier, 'rb')
    new_fic = open(fichier+'.chiffre','wb')
    new_fic.close()
    octet = fic.read(1).hex()
    palier = 0
    i = 0
    while octet:
        progression = i*100/os.path.getsize(fichier)
        octet_chiffre = (int(octet,16) + ord(cle[i%len(cle)])) % 256
        byte_octet_chiffre = hex(octet_chiffre).replace('0x','')
        if len(byte_octet_chiffre) == 1:
            byte_octet_chiffre = '0'+byte_octet_chiffre
        new_fic = open(fichier+'.chiffre','ab')
        new_fic.write(bytes.fromhex(byte_octet_chiffre))
        octet = fic.read(1).hex()
        palier = progress_bar(progression, palier)
        i += 1
       
    new_fic.close()
    fic.close()
    os.remove(fichier)
    print('le fichier '+os.path.basename(fichier)+' à bien été chiifré')

def dechiffrer(fichier, cle):
    fic = open(fichier,'rb')
    new_fic = open(fichier.replace('.chiffre',''),'wb')
    new_fic.close()
    octet = fic.read(1).hex()
    palier = 0
    i = 0
    while octet:
        progression = i*100/os.path.getsize(fichier)
        octet_dechiffre = (int(octet,16) - ord(cle[i%len(cle)])) % 256
        byte_octet_dechiffre = hex(octet_dechiffre).replace('0x','')
        if len(byte_octet_dechiffre) == 1:
            byte_octet_dechiffre = '0' + byte_octet_dechiffre
        new_fic = open(fichier.replace('.chiffre',''),'ab')
        new_fic.write(bytes.fromhex(byte_octet_dechiffre))
        octet = fic.read(1).hex()
        palier = progress_bar(progression, palier)
        i += 1
    
    new_fic.close()
    fic.close()
    os.remove(fichier)
    print('le fichier '+os.path.basename(fichier)+' à bien été déchifré')

def demander_message():
    print("entrez un message à cacher :")
    message = input()
    return message

def cacher_message(fichier, message):
    fic = open(fichier,'rb')
    new_fic = open('image_secrete.jpg','wb')
    new_fic.close()
    new_fic = open('image_secrete.jpg','ab')
    octet = fic.read(1).hex()
    palier = 0
    i = 0
    j = 0
    while octet:
        progression = i*100/os.path.getsize(fichier)
        if i > (os.path.getsize(fichier) // 2) and j < len(message):
            new_oc = hex(ord(message[j])).replace('0x','')
            new_fic.write(bytes.fromhex(new_oc))
            j += 1
        else:
            new_fic.write(bytes.fromhex(octet))
        octet = fic.read(1).hex()
        palier = progress_bar(progression, palier)
        i += 1


action = accueil()

if action == '1' :
    fichier = demander_fichier()
    cle = demander_cle()
    chiffrer(fichier,cle)
elif action == '2':
    fichier = demander_fichier()
    cle = demander_cle()
    dechiffrer(fichier,cle)
else:
    fichier = demander_fichier()
    while fichier.find('.jpg') < 0: 
        print('il semble que ce ne soit pas un jpg')
        fichier = demander_fichier()
    message = demander_message()   
    cacher_message(fichier, message)
