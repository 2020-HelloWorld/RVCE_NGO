import firebase_admin 
from firebase_admin import credentials 
from firebase_admin import firestore
import datetime

cred = credentials . Certificate ( "serviceAccountKey.json" ) 
firebase_admin.initialize_app ( cred )

db=firestore.client()

Q1={'Was the program good and useful?','Did you understand most of the topics/information shared?','Did you enjoy the activities?','Are the presentations /  videos/work materials good to see, read and easy to understand?','Has your knowledge increased about different career paths / job opportunities / preparation?','Do you have better clarity now on your next steps than before the program?','Do you recommend this program for your juniors / other friends too?','Will you reach out to us if you have questions?','Is it easy for you to set your own goals now? Can you do it?','Has your career choices changed with new or more options now?','Are you more aware and confident about your career choices as well as decision making now?','Which part of the session you enjoyed the most?','Which part of the session you enjoyed the least?','Overall rating for the workshop? Rating Scale 1-10'}

Q2={'Did they attend Career Guidance workshop by DreamPath Foundation?','2.	What is the student doing now(after 10th)?','3.	Which course has student joined after 10th?','Why did he/she choose to join the above?','5.	How did he/she decide (eg parents decided, friends were joining that college, school teachers, advice self decision with parents etc?','6.	How did the DreamPath workshop help him/her with the choice?','If so, what way?','Was the workshop useful and other resources from DreamPath useful?'}

Q3={'Did they attend Career Guidance workshop by DreamPath Foundation?','What is the student doing now(after 12th)?','Which course has student joined after 12th?','Why did he/she choose to join the above?','How did he/she decide (eg parents decided, friends were joining that college, school teachers advice, self decision with parents etc?','How did the DreamPath workshop help him/her with the choice?'
,'If so what way?','Was the workshop useful and other resources from DreamPath useful?'}

db.collection('Dreampath').document('2017').collection('Student').document("S1").set({'name':'John','email ID':'john@gmail.com','Phone no.':'9591224945','Date':'09/10/2017','Q1[0]':1,'Q1[0].1':'Yes the program was really usefull','Q1[1]':1,'Q1[1].1':'Yes I clearly understood the infomation shared','Q1[2]':1,'Q1[2].1':'Yes the activities were really engaging','Q1[3]':1,'Q1[3].1':'Yes the resources are well structured and hence easy to understand.','Q1[4]':1,'Q1[4].1':'Yes, I came to know about various career paths.','Q1[5]':3,'Q1[5].1':'Yes, I have a much better idea now but I will have to discuss about this with my parents.','Q1[6]':1,'Q1[6].1':'Yes I would surely recommend his program to my juniors and other friends.','Q1[7]':1,'Q1[7].1':'Yes I will surely approach you guys for any doubts','Q1[8]':1,'Q1[8].1':'Yes now it has become easy for me to set my goals.','Q1[9]':'Yes I am open to a lot more career options now than before.','Q1[10]':'I am definitely more aware of the career options but I am still thinking about my decision now.','Q1[11]':'The activities conducted were the best.','Q1[12]':'','Q1[13]':9,'Q2[0]':1,'Q2[1]':'Taken up Science','Q2[2]':'PCMC','Q2[3]':'I chose to join PCMC since I feel that I am more inclined towards maths and love problem solving','Q2[4]':'self decision with parents','Q2[5]':1,'Q2[6]':'It hepled me realize my strengths and weaknesses and opened up a lot of options.','Q2[7]':1,'Q3[0]':1,'Q3[1]':'Looking for various options and trying to figure the option which suits him the best.','Q3[2]':'Engineering','Q3[3]':'Love for problem solving','Q3[4]':'self decision with parents','Q3[5]':1,'Q3[6]':'Opened up a lot of options','Q3[7]':1})