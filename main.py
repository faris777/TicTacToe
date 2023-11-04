import random as r

def displayboard(list):
    print(f"*-----*-----*-----*")
    print(f"|  {list[0][0]}  |  {list[0][1]}  |  {list[0][2]}  |")
    print(f"*-----*-----*-----*")
    print(f"|  {list[1][0]}  |  {list[1][1]}  |  {list[1][2]}  |")
    print(f"*-----*-----*-----*")
    print(f"|  {list[2][0]}  |  {list[2][1]}  |  {list[2][2]}  |")
    print(f"*-----*-----*-----*")

list = [[1,2,3],[4,5,6],[7,8,9]]
def userinput(userinput,list,value):
    for j in range(len(list)):
        for i in range(len(list[j])):
            if userinput == list[j][i]:
                list[j][i] = value
                print(list[j][i])
    return displayboard(list)


def win_checker(list):
    flag = False
    #row win checker
    if list[0][0] == list[0][1] == list[0][2]:
        flag = True
    elif  list[1][0] == list[1][1] == list[1][2]:
        flag = True
    elif list[2][0] == list[2][1] == list[2][2]:
        flag = True
        #diagonal win checker
    elif list[0][0] == list[1][1] == list[2][2]:
        flag = True
    elif list[0][2] == list[1][1] == list[2][0]:
        flag = True
    #row checker
    elif list[0][0] == list[1][0] == list[2][0]:
        flag = True
    elif  list[0][1] == list[1][1] == list[2][1]:
        flag = True
    elif list[0][2] == list[1][2] == list[2][2]:
        flag = True
    return flag

# print(userinput(5,list,'X'))

while True:
   o = r.randint(1,9)
   print(o)
   u =int(input('please enter your position'))
   x = input('Please enter your O or X')
   userinput(u,list ,x)
   userinput(o, list, 'X')
   if (win_checker(list)):
       break



#
# displayboard(list)