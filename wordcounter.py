def most_frequent(String):
    String=String.lower()
    x=set(String)
    x=list(x)
    for i in x:
        count=0
        for j in String:
            if j==i:
                count+=1
        print(i,"=",count)

a=input('Please enter a string:\n')
most_frequent(a)