question_list=[["'Dandia' is a popular dance of ","A.Punjab", "B.Gujarat", "C.Tamil Nadu", "D.Maharashtra",2 ] ,
               ["The Rath Yatra at Puri is celebrated in honour of which Hindu deity","A. Ram","B.Jaganath","C.Shiva","D. Vishnu",2]] 

levels=[1000,2000,3000,4000,5000] 
money =0

for i in range(0, len(question_list)):
    print(f"Question for Rs.{levels[i]}")
    question = question_list[i]
    print(question[0])
    print(question[1],          question[2])
    print(question[3],          question[4])

    user_reply= int(input("Enter your answer(1,2,3,4): "))
    if user_reply == question[5]:
        print(f"Correct Answer, You have won Rs.{levels[i]}")
        money = money+levels[i]

    else:
        print("Wrong Answer!")
        break

print(f"Your take home money is Rs.{money}")
