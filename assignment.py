score = int(input('test score:'  ))
if score<= 100 and score >= 0:
    grade1='A'
    grade2='B'
    grade3='C'
    grade4='F'
    if int(score)>= 80:
        print(grade1)
    elif int(score)>=70 and int(score) <79:
        print(grade2)
    elif int(score)>=60<69:
        print(grade3)
    else:
        print(grade4)
    int(score)%2
    print ('EVEN?:',not bool(int(score)%2))
else:
    print('invalid score')
