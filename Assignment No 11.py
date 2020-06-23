#Quiz App

quiz = [
    {
      "Q1":"colour of banana?",
      "op":["a) yellow","b) Blue","c) Green","d) Black"],
      "ans":"a"
    },
    {
       "Q2" :"provinces of pakistan?",
       "option" :["a) Two", "b) Three", "c) Five", "d) Four"],
       "ans" :"d"
    },
    {
       "Q3" :"national flower of pakistan?",
       "option" :["a) sun flower", "b) jasmine", "c) rose", "d) lily"],
       "ans" :"b"
    },
    {
       "Q4":"Total Muslim Countries?",
       "op":["a) 48","b) 50","c) 52","d) 54"],
       "ans":"c"
    },
       ]
option = ["a","d","b","c"]
    i = 0
    
    for question in quiz:
        answer = input(question)
        if answer == option[i]:
            i = i+1
            print("\n Correct Answer: " + answer)
        else:
            print("\n Wrong Answer")





