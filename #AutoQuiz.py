#Funtion AutoQuiz
import sqlite3
from DrissionPage import ChromiumPage
conn = sqlite3.connect('AutoCoursera_DB.sqlite')
cursor = conn.cursor()
page = ChromiumPage()

def manipulate(answers):
    answers = list(answers[0])
    answers_new = answers[0].split('\n')
    return answers_new

#Search answer in answerDB
def check_string_in_list(my_list, search_string):
     return any(search_string in s for s in my_list)

#Quiz part doesn't open a new tab, stay on that tab object
page.get("https://www.coursera.org/learn/critical-thinking-skills/quiz/2ipTM/1-3-practice-quiz")
page._wait_loaded
page.ele('tag=button@data-test=action-button').click()
page.wait.ele_displayed('#rc-FormPartsQuestion')
listQuestionForm = page.eles('@class=rc-FormPartsQuestion')
i = 0 
for parts in listQuestionForm:
    i = i + 1
    print(i,"\n")
    listQuestionForm_children = parts.children()
    rc_FormPartsQuestion_row = listQuestionForm_children[0]  #1
    rc_FormPartsQuestion_row_pii_hide = listQuestionForm_children[1] #2
    rc_FormPartsQuestion_row_1 = rc_FormPartsQuestion_row.child("@class=rc-FormPartsQuestion__contentCell") #3
    question_container = rc_FormPartsQuestion_row_1.child(1).child(1).child(1).child(1).child(1).child(1)
    print(question_container.text) #Question
    question_Uncomplete = str(question_container.text)
    question_complete = question_Uncomplete.strip()
    print(question_complete)
    cursor.execute("SELECT Answer FROM academic_writing WHERE Quests LIKE ?", ('%'+question_complete+'%',))
    answerss = cursor.fetchall()
    # print("THIS IS THE ANSWER")
    print(answerss)
    answerDB = manipulate(answerss)
        # print("\n") 
    rc_FormPartsQuestion_row_pii_hide_1 = rc_FormPartsQuestion_row_pii_hide.child('@class=rc-FormPartsQuestion__contentCell') #4
        # print(rc_FormPartsQuestion_row_pii_hide_1)
        #Check if there are input box or multiple choice question
    questionClass = rc_FormPartsQuestion_row_pii_hide_1.child()
    questionClassType = questionClass.attr("class")
        # print("this answer type : ",questionClassType)   ---------Check_____Question_____Type------------
    if(questionClassType == "rc-TextInputBox"):
        print("Input_box")
            #Code to handle the input box
            #rc_group_answer may not appear with text input type
    elif(questionClassType == "rc-FormPartsMcq"):
        rc_group_answer =  questionClass  #5
            # print("multiple")
        rc_list_div_tag = rc_group_answer.children('tag=div') #6
        for divTag in rc_list_div_tag: 
            divTag_2nd_child = divTag.child(1).child(1) #7 Tag : lable
            InputTag = divTag_2nd_child.child('tag=input')
                # if(InputTag.attr('type')=='radio'):
            tagSpanContainAnswer = InputTag.next('tag=span') #8.2
            answer = tagSpanContainAnswer.child(1).child(1).child(1).child(1).child(1).child(1).text
                # print(answer)
            if(check_string_in_list(answerDB,answer)):
                InputTag.click()
    elif(questionClassType==None):
            # print("this is multiple answers")
            # lableTag = divTag.child(1).child(1)
        rc_group_answer = questionClass.children('tag=div')
        for divTag in rc_group_answer:
            lableTag = divTag.child(1).child(1)
            InputTag = lableTag.child('tag=input@type=checkbox')
                # print(inputElement)
            answerContainer = InputTag.next('tag=span')
            answer = answerContainer.child(1).child(1).child(1).child(1).child(1).child(1).text
                # print(answer)
            if(check_string_in_list(answerDB,answer)):
                InputTag.click()
page.ele('tag=input@@id=agreement-checkbox-base@@aria-labelledby=check-agree').click()
page.wait.ele_loaded('@@data-test=submit-button@!disable=')
page.ele('tag=button@@type=button@@data-test=submit-button').click()         
        
        
        
    
    
    
