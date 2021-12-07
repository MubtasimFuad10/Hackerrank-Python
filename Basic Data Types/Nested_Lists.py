if __name__ == '__main__':

    marks=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marks.append([score, name])
    marks.sort()
    for i in range(len(marks)):
         if marks[i][0] > marks[0][0]:
             print(marks[i][1])

             if (i+1) >= len(marks) or marks[i+1][0]>marks[i][0]:
               break
       
       


