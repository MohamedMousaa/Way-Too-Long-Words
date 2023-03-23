lines = int(input())
count = 0
i=1
while lines > count:
    word = input()
    i=i+1
    count=count+1
    length = len(word)
    if length > 10:
        word_counter =  str(length - 2)
        print(word[0] + word_counter + word[-1])
    else:
        print(word)