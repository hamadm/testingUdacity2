
# coding: utf-8

# In[5]:

levels = ["Easy", "Medium", "Hard"]
questions = ["___(1)___, officially the City often known by its initials ___(2)___, is the cultural, financial, and commercial center of Southern ___(3)___. It is the ___(4)___ most populous city in the United States (after New York City)","___(1)___ is the capital and largest city of Egypt. The city's metropolitan area is the ___(2)___ in the Middle East and the Arab world, and is associated with ancient Egypt, as the famous ___(3)___ pyramid complex. Located near the ___(4)___ Delta.","___(1)___ is the capital ___(2)___. located along the ___(3)___ River in the northern part of the country. The city in 2015 had the highest per capita ___(4)___ rates in the world"]
answers = [["Los Angeles","LA","California","second"],["Cairo","largest","Giza","Nile"],["Caracas","Venezuela","Guaire","murder"]]
def menu():
    choice = raw_input("Select the level of difficulty: Easy, Medium, Hard type exit to exit: ")
    if choice.upper() == "EXIT":
        return 1
    i=0
    while i< len(levels):
        if(choice.upper() == levels[i].upper()):
            runQuestions(i)
            return 0
        i+=1
    print "Wrong input please try again"
    return 0

def runQuestions(difficultyIndex):
    tries = 0
    while tries <2:
        print questions[difficultyIndex]
        userInput = ["","","",""]
        i = 0
        while i<len(userInput):
            userInput[i]= raw_input("fill the blank "+str(i+1)+" : ")
            i +=1
        result = checkAnswers(userInput, difficultyIndex)
        
        if result == "correct":
            print "You have answered correctly"
            return
        elif result == "wrong" and tries < 1:
            print "You have One or more answers not correct, please try again"
        else:
            print "You have One or more answers not correct, you have no more tries"
            return
        tries += 1
            
def checkAnswers(userInput, difficultyIndex):
    i = 0
    while i<len(userInput):
        if userInput[i].upper() != answers[difficultyIndex][i].upper():
            return "wrong"
        i +=1
    return "correct"


status = 0
while status == 0:
    status = menu()


# In[ ]:




# In[ ]:



