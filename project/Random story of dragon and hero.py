import random
hero_life = 100 #life or HP
dragon_life= 100
place=["Rose Marley,","Ice peek,","Dragon city,","Little garden,"]  
time=["winter","summer","spring","rainy Day"]
event=["searching for medicine,","went to see a friend,"," gone for hunting,","randomly walking,"]
hero=["Luffy","Zoro","Sanji","Ussopu"] 
try:                                
 place1=random.choice(place) #random choice,of hero's,name,place,time,event.
 time1=random.choice(time)
 event1=random.choice(event)   #The random story
 hero1=random.choice(hero)                           
 print("Once up on time, there was a place called"+' ' +place1+' '+"There was our hero"+
       ' '+hero1+' '+'lived.\n'+"On a"+' '+time1+' '+"our hero was "+event1+' '+
      "suddenly he was encounter with a dragon.\nThe dragon was aggresive and started fight with our hero...")
            
 while True:    #Fight between Hero and Dragon
    dragon_damage=random.randint(1,20) #random damage of dragon
    hero_life-=dragon_damage
    print(f'Dragon attacked our {hero1} and deal {dragon_damage} damage.{hero1}life__{hero_life}')
    if hero_life<=0:
        print(f"Dragon killed our {hero1},The End....")
        break
    hero_damage=random.randint(1,20) # random damage of hero
    dragon_life-=hero_damage
    print(f'{hero1} attacked the dragon and deal {hero_damage} damage.Dargon life__{dragon_life}')
    if dragon_life<=0:
        print(f'{hero1} killed the dragon and continue his journey,The End....')
        break
except ValueError as error1: # checks weather there is an error
   print(f"A value Error Occured{error1}")
except TypeError as error2:
   print(f"A Type Error Occured{error2}")   


