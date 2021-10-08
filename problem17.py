single_diget = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}

teens = {10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}

double_diget = {20:"twenty", 30:"thirty", 40:"fourty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"}

triple_diget = {100:"onehundredand", 200:"twohundredand", 300:"threehundredand", 400:"fourhundredand", 500:"fivehundredand", 600:"sixhundredand", 700:"sevenhundredand", 800:"eighthundredand", 900:"ninehundredand"}

twc = len("onethousand") # total word count

for i in range(1,1000):
    wc = 0 # word count
    if i//100 > 0:
        wc += len(triple_diget[(i // 100)*100])
        print(triple_diget[(i // 100)*100], end=" ")
        if (i % 100) == 0:
            wc -= 3 # get rid of the "and" bit
    if (i % 100)//10 >= 2:
        wc += len(double_diget[int((i % 100)//10)*10])
        print(double_diget[int((i%100)//10)*10], end=" ") 
        if str(i)[-1] != "0":
            wc += len(single_diget[int(str(i)[-1])])
            print(single_diget[int(str(i)[-1])], end=" ")
    elif (i % 100)//10 == 1:
        wc += len(teens[i % 100])
        print(teens[i % 100], end=" ")
    elif (i % 100)//10 == 0:
        if i % 100 != 0:
            wc += len(single_diget[i % 100])
            print(single_diget[i % 100], end=" ")
    print(" "+str(wc))
    twc += wc

print(twc)
