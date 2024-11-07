text = input("what is the text \n")
e = 0
ins = 0 
while True:
    action = input("Editer text e, Count characters c , Count words w , exit \n =>")
    
    if action == "e":
        
        text = input("edit the text \n =>")
        
        print("text edited")
        
    decrypted = list(text)
    
    if action == "c":
        
        t_or_s = input("chose a mode :\n 1-total letters (t) \n 2-specefic character (s)\n =>")
        
        if t_or_s == "t":
            sh = 0
            for s,i in enumerate(decrypted):
                if i.isalpha():
                    sh += 1
                    if s == len(decrypted) - 1:
                        prirt(sh)
                        sh = 0
                if not i.isalpha():
                    if i == "é" or i == "ù":
                        sh += 1
                        if s == len(decrypted) - 1:
                            print(sh)
                            sh = 0

        else:
            
            print(decrypted.count(input("chose a letter\n =>")))
            
    if action == "w":
        
        t_or_s_2 = input("chose a mode : \n 1-total words (t) \n 2-specefic word (s)\n =>")
        
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
                                ins += 1
                    if test == nice:
                        ins += 1
            print(ins)
        elif t_or_s_2 == "s":
                        
            chose_a_word = input("Chose a word\n =>")
            words = chose_a_word.split()
            wurds = words.count(chose_a_word)
            prirt(f"the word {words} appear {wurds} in the text.")
    if action == "exit":
        break
