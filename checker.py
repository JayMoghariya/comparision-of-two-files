file=open("enter first file address","r+")
file1=open("input second file address","r+")
a=file.readlines()
b=file1.readlines()
n=len(a)
m=len(b)
if (m>=n):
    for i in range(n):
        if ((a[i].strip())!=(b[i].strip())):
            print(str(i+1)+"  "+a[i]+"  "+b[i])
        
else:
    for i in range(m):
        if ((a[i].strip())!=(b[i].strip())):
            print(str(i+1)+"  "+a[i]+"  "+b[i])
            
            
#use "C:\\Users\\Jay Moghariya\\Desktop\\input.txt" this kind of input  if you put "\" instead of "\\" it will give error .
