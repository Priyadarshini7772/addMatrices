print("The rows and columns of two matrices must be same")
rows=int(input("Enter No.of Rows in matrices: "))
cols=int(input("Enter No.of Columns in Matrices: "))

matr1=[]
matr2=[]
print("Give values for Matrix1")
for i in range(rows):
    row=[]
    for j in range(cols):
        ele=int(input(f"Enter [{i}],[{j}]: "))
        row.append(ele)
    matr1.append(row)
print("Give Values for Matrix2")
for i in range(rows):
    row=[]
    for j in range(cols):
        ele=int(input(f"Enter [{i}],[{j}]: "))
        row.append(ele)
    matr2.append(row)

result=[]
for i in range(rows):
    row=[0]*cols
    result.append(row)
    

for i in range(rows):
    for j in range(cols):
        result[i][j]=matr1[i][j]+matr2[i][j]

for i in range(rows):
    for j in range(cols):
        print(result[i][j],end=' ')
    print( )