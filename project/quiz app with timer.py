import time
try:
 questions=("1-Volacnic eruption do not occur in the- ",   # questions in tuple
            "2-Which one of the following ports is the oldest port in india",
           "3-Indus river orginates in-",
           "4-Tsunami are not caused by",
           "5-The metal whose salts are sencitive to light") 
 options=((" A.Baltic sea"," B.Black sea"," C.caribbean sea"," D.Caspin sea"),
         (" A.Mumbai Port"," B.Chennai Port"," C.Kolkata Port "," D Vishakhaptnam Port"),
         (" A.Kinnaur"," B.Ladakh"," C.Nepal"," D.Tibet"),
         (" A.Hurricanes"," B.Earthquakes"," C.Undersea Landslide"," D.Volcanic eruption"),
         (" A.Zinc"," B.Silver"," C.Copper"," D.Aluminum"),)
 correct_answer=("A","B","D","A","B") #correct answer
 num=0
 your_answer=[] 
 score=0
 start_time=time.time() #To  start get time
 time_duration=1*60 #set timer to 1 minute
 print(" \nThe Quiz is started you got 1 minute to complete\n All the best :)")
 for question in questions:
    if (time.time()-start_time)<time_duration: # set timer
       print()
       print(question)# printing question
       for option in options[num]:#printing option usin indexing
        print(option)
       your_answer1=str(input("Enter your answer (A,B,C,D):").upper()) #input the user answer
       if your_answer1 in ["A","B","C","D"]:# cheaking the input
          your_answer.append(your_answer1)
          if your_answer1==correct_answer[num]:
             print()
             print("YOUR ANSWER IS CORRECT!") 
             score+=1
          else:
           print()
           print("YOUR ANSWER IS INCORRECT!")
           print(f"{correct_answer[num]} is the correct answer")
       else:
        print("\nYou entered invalid input")
        continue
       num+=1
    else:
      print("\nYOU RAN OUT OF TIME!!")
      break 
 end_time=time.time()# geting  end time in seconds
 total_time=end_time-start_time
 print(f"\nQuiz Ended,{total_time:.2f} seconds where taken to complete")# used .2f get two decimals
 print('\nRESULT')
 print(f"YOU SCORED {score} out of {num}") #prints your score
except TypeError as error1:
  print(f"A type error occured-{error1}") 
except ValueError as error2:
  print(f"A value error occured-{error2}")   

    


    




   