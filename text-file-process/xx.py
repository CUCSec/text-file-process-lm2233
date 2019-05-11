import time
with open('log_files/201811123022.log',encoding='utf8') as f:
    count=0
    for line in f:
        student_id=line.split(',')[1]
        student_id=student_id.strip()
        print(student_id)
        if student_id[3: ]=='201811113022':
            count+=1
print(count)
time.sleep(60)