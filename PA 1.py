
infile = input("Enter file name")

f1 = open(infile)

f1.seek(0)

ar = []


for i in range(0,5):
    a = int(f1.readline())
    ar.append(a)

print("length is ", len(ar))