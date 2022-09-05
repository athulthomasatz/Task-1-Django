#Task 1 
i=1
names = []
total=[]
while i<=5:
    print("Student "+ str(i))
    stud_name = input("Name of student: ")
    names.append(stud_name)
    mark1 = int(input("Enter the first mark: "))
    mark2 = int(input("Enter the second mark: "))
    mark3 = int(input("Enter the third mark: "))
    total_mark = mark1 +mark2 + mark3
    total.append(total_mark)
    print()
    i+=1
#printing all details 
print("-----Student Exam Result----")

k=0
while k<5 :
    print("Student   : "+ str(k+1))
    print("Name      : "+ names[k])
    print("Total Mark: "+ str(total[k]))
    if total[k]<35 :
        print("Status    : Fail" )
    else :
        print("Status    : Pass")
    print()
    k+=1
  



