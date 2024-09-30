import random
ucount=0
ccount=0
 
x=['stone','paper','sizzer']

while True:
    print('''           
                        new game........
                        1.PLAY GAME
                        2.EXIT......''')
    r=int(input(''))
    if r==1:
     for s in range(1,6):
      print('''
         1.stone
        2.paper
        3.sizzer''')
      userinput=int(input(''))
      compchoise=random.choice(x)
      if(userinput==1):
       userchoise='stone'
      elif(userinput==2):
       userchoise='paper'
      elif(userinput==3):
       userchoise='sizzer'
      if(userchoise==compchoise):
       print('''
               ROUND IS DRAW
                     BOTH ARE CHOOSE SAME 
                      ''') 
      elif(userchoise=='sizzer' and compchoise=='paper') or ( userchoise=='stone' and compchoise=='sizzer') or (userinput=='paper'and compchoise=='stone') :
       print('your choise is   ', userchoise)
       print(' OPPONENT CHOISE IS',compchoise)
       print(''' YOU WIN THE ROUND 
                        ''')
       ucount=ucount+1
     else:
      print('your choise is   ', userchoise)
      print(' OPPONENT CHOISE IS',compchoise)
      print(''' YOU loose THE ROUND ''')
      ccount+=1
     print('your score is',ucount)  
     print('opponent score is',ccount)
     if(ucount>>ccount):
      print('''           you win the game''')
     else:
         print('''        you loose the game''')
             
    else: 
        break
         


