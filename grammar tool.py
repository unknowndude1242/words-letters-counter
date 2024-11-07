text = input("Quelle est le text \n")
e = 0
initiansong = 0 
while True:
    action = input("Editer le text e, Compter le nombre de lettre l , Compter le nombre de mot w \n =>")
    
    if action == "e":
        
        text = input("edit the text ")
        
        print("text edité")
        
    decrypted = list(text)
    
    if action == "l":
        
        t_or_s = input("choisi un mode :\n 1-lettre total (t) \n 2-lettre spécéfique (s)\n =>")
        
        if t_or_s == "t":
            shing = 0
            for s,i in enumerate(decrypted):
                if i.isalpha():
                    shing += 1
                    if s == len(decrypted) - 1:
                        print(shing)
                        shing = 0
                if not i.isalpha():
                    if i == "é" or i == "ù":
                        shing += 1
                        if s == len(decrypted) - 1:
                            print(shing)
                            shing = 0

        else:
            
            print(decrypted.count(input("Choisi une lettre\n =>")))
            
    if action == "w":
        
        t_or_s_2 = input("choisi un mode : \n 1-Tous les mots (t) \n 2-Mot spécéfique (s)\n =>")
        
        if t_or_s_2 == "t":
            
            for test,i in enumerate(decrypted):
                
                nice = len(decrypted) - 1
                
                if i.isalpha():
                    
                    if test != nice:
                        
                        next = test + 1
                        
                        if not decrypted[next].isalpha():
                            
                            if decrypted[next] == "'":
                                
                                continue
                            else:
                                initiansong += 1
                    if test == nice:
                        initiansong += 1
            print(initiansong)
        elif t_or_s_2 == "s":
                        
            chose_a_word = input("Choisi un mot\n =>")
            words = chose_a_word.split()
            wurds = words.count(chose_a_word)
            print(f"Le mot {words} apparait {wurds} fois dans le text.")
    if action == "fermé":
        break
