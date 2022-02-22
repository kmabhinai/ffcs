file=open("ffcs.csv","r+")
data=file.readlines()
course_code,course_title,credit,slot,emp_name=[],[],[],[],[]

for i in data:
    course_code1,course_title1,credit1,slot1,emp_name1=i.split(",")
    course_code.append(course_code1),course_title.append(course_title1),credit.append(credit1)
    slot.append(slot1),emp_name.append(emp_name1)

#Deleting the titles
course_code.pop(0),course_title.pop(0),credit.pop(0),slot.pop(0),emp_name.pop(0)
credit_req=float(input("Number of Credits required are :- "))
course_code_taken,slot_taken,credit_count,count=[],[],0,-1
early_slots={"A1","L1","L7","C1","B1","L13","D1","L19","E1","L25"}
early_lab={"L3","L4","L5","L6","L9","L10","L11","L12","L15","L16","L17","L18","L21","L22","L23","L24","L27","L28","L29","L30"}
if len(course_code)>0:
    for i in course_code:
        count+=1
        if credit_count+float(credit[count])<=credit_req:
            if i not in course_code_taken:
                if len(set(slot[count].split("+")) & early_slots) ==0:
                    if len(set(slot[count].split("+")) & set(slot_taken)) ==0:
                        #For Theory
                        if course_code[count][-1]=="L" or course_code[count][0:4]=="BSTS":
                            slot2=slot[count].split()
                            if slot2[0][-1]=="2":
                                course_code_taken.append(i)
                                slot_temp=slot[count].split("+")
                                for j in slot_temp:
                                    slot_taken.append(j)
                                credit_count+=float(credit[count])
                                print("\nCourse Code :- ",i)
                                print("Course Title :- ",course_title[count])
                                print("No. of Credits :- ",credit[count])
                                print("Slot :- ",slot[count])
                                print("Name of the professor :- ",emp_name[count])
                        #For Lab
                        if course_code[count][-1]=="P":
                            if len(set(slot[count].split("+")) & early_lab) >0:
                                course_code_taken.append(i)
                                slot_temp=slot[count].split("+")
                                for j in slot_temp:
                                    slot_taken.append(j)
                                credit_count+=float(credit[count])
                                print("\nCourse Code :- ",i)
                                print("Course Title :- ",course_title[count])
                                print("No. of Credits :- ",credit[count])
                                print("Slot :- ",slot[count])
                                print("Name of the professor :- ",emp_name[count])
else:
    print("Please Enter the data in the ffcs.csv file created in the same location of this file with \nA1 cell as COURSE CODE \nB1 cell as COURSE TITLE \nC1 cell as CREDITS \nD1 cell as SLOT \nE1 cell as EMPLOYEE NAME")
file.close()