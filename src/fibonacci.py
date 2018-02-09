# @lamhotsimamora
# Fibonacci Application
# 2018
import os

class Fibonacci: 
    def __init__(self,_length):
        self._length = _length

    def generateFibonacci(self):
        start = 0
        data = []
        for i in range(self._length):
            data.append(start)
            if i==0 :
                start = start + 1 
            else:
                start = data[i] + data[i-1]
        return data 

def resultFibo(a):
    fibo = Fibonacci(a)
    result = fibo.generateFibonacci()  
    print(str(result))
    showMenu()

def processFibo(num):
    length = 120
    fibo = Fibonacci(length)
    res  = fibo.generateFibonacci()
    if num in res:
        print('Number '+str(num)+' is fibonacci')
    else:
        print('Number '+str(num)+' is not fibonacci')
    showMenu()

def createFibo():
    os.system('cls')
    check = True
    while check:
        val = input('How many number of fibonacci do you want ? ')
        try:
            get   = int(val)
            check = False
            resultFibo(get)
            break
        except ValueError:
            check = True
            createFibo() 

def checkFibo():
    os.system('cls')
    check = True
    print(" ")
    while check:
        val = input('Input the number ! ')
        try:
            get   = int(val)
            check = False
            processFibo(get)
            break
        except ValueError:
            check = True
            createFibo() 
   
menu = None
def showMenu():
    check = True
    print(" ")
    while check:
        menu = input("Select Menu : ")
        try:
            get   = int(menu)
            check = False
            if get ==  1:
               createFibo()
               break
            elif get == 2: 
               checkFibo()
               break
            elif get == 3:
                about()
                break
            else:
               showMenu()
        except ValueError:
            check = True
            showMenu() 

def about():
    print(" ")
    print('Developer @lamhotsimamora')
    print('Fibonacci Application v.1.0')
    print('https://github.com/lamhotsimamora')
    showMenu()

print("*********************************************")
print("================ SELECT MENU ================")
print("*********************************************")
print("1.  Generate Fibonacci                       ")
print("2.  Check Fibonacci Number                   ")
print("3.  About                                    ")
print("*********************************************")
showMenu()



