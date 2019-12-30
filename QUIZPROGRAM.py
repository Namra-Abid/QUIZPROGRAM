list={
    0:{    "seat_no":1,
         "question":"What is the name of founder of Pakistan",
         "option":["ALI","NAMRA","QUAID-E-AZAM"],
         "answer":"QUAID-E-AZAM",
    },
  1:  { "seat_no":2,
         "question":"capital of pakistan",
         "option":["KARACHI","HYDERABAD","ISLAMABAD"],
         "answer":"ISLAMABAD",
    },
   2: {
"seat_no":3,
         "question":"national flower of Pakistan",
         "option":["ROSE","JASMINE","LOTUS"],
         "answer":"JASMINE"
    },
}
score=0
i=0
for v in list:
  display= str(list[i]["seat_no"])+" : "+ list[i]["question"] + "\n" +list[i]["option"][0]+ "\n" +list[i]["option"][1]+ "\n" +list[i]["option"][2]
  print(display)
  answer=input("your answer is : ")
  if answer.upper()==list[i]["answer"]:
      i=i+1
      score+=1

print("your score is : " ,score)