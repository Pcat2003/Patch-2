import sqlite3
from DrissionPage import ChromiumPage
conn = sqlite3.connect('AutoCoursera_DB.sqlite')
cursor = conn.cursor()
question_complete = "In lesson 1.3a, Jonathon mentions that he learnt two valuable skills when he struggled to pass a first year university course. What were they?"
cursor.execute("SELECT Answer FROM academic_writing WHERE Quests LIKE ?", ('%'+question_complete+'%',))
answers = cursor.fetchall()
# print("THIS IS THE ANSWER")
# print(answers)
answers = list(answers[0])
answers_new = answers[0].split('\n')
print(answers_new)


#Tim kiem 1 string lieu co ton tai trong 1 phan tu trong list
# my_list = ['apple', 'banana putaas', 'orange']
# search_string = 'banana'


# if any(search_string in s for s in my_list):
#     print("Chuỗi '{}' tồn tại trong danh sách.".format(search_string))
# else:
#     print("Chuỗi '{}' không tồn tại trong danh sách.".format(search_string))