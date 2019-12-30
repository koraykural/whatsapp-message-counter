import re
filepath = input("Enter file name with its extention (eg. chat.txt): ")
print()
person = {}
try:
    fp = open(filepath, encoding="utf-8")
except:
    print("Couldn't open the file :(\n")
else:
    line = fp.readline()
    while line:
        x = re.search('( - ).*(: )', line)
        if x:
            s = x.group()
            s = s[3:]
            s = s[:-2]
            if s in person:
                person[s] += 1
            else:
                person[s] = 1
        line = fp.readline()
    #sorted(person.items(), key=lambda x: x[1])
    for i in person:
        ctr = i.count(':')
        if(ctr > 0 or person[i] == 1):
            pass
        else:
            print(i + ": " + str(person[i] + 1))
    fp.close()
x=input("\nPress any key to exit...\n")