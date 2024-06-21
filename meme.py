meme_dict = {'XD': 'se usa cuando algo es chistoso',
             'POSER': 'Ser unn fan por moda',
             'FANBOY': 'Fan obsesionado por un producto'
             }
             
for i in range(5):
    word = input("Que palabra quieres entender?").upper()
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Aun falta agregar elementos al diccionario")
