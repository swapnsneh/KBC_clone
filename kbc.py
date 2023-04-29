question_list=["1. 'Dandia' is a popular dance of ","2. The Rath Yatra at Puri is celebrated in honour of which Hindu deity"] 

option_list=[["A.Punjab", "B.Gujarat", "C.Tamil Nadu", "D.Maharashtra"],["A. Ram","B.Jaganath","C.Shiva","D. Vishnu"]] 

correct_list=["B","B"]

correct_answer_prize= 0

for idx, i in enumerate(question_list):
    print(i)
    # print(idx)
    
    print(option_list[idx])
    user_input=input("Enter the correct option: ")

    if user_input == correct_list[idx]:
        correct_answer_prize = correct_answer_prize+1000
        print("Correct answer\n","You win ",correct_answer_prize)  

    else:
        print("Wrong answer")

        print("You won Rs." , correct_answer_prize)
        break
