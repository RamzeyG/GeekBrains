# Доделать реализацию функции eval со скобками

def CalculateString(x):
    def PlusMinus(num):
            
        if(num[1] == '-'):
            num[0] = float(num[0])-float(num[2])
            num.pop(1)
            num.pop(1)
        elif(num[1] == '+'):
            num[0] = float(num[0])+float(num[2])
            num.pop(1)
            num.pop(1)
        elif(num[1] == ''):
            num.pop(1)
        while(len(num) >= 3):
            PlusMinus(num)

        return float(num[0])

    def Magic(res):
        num = []
        blend = ''
        DoubleMinus = 0
        for i in range(0, len(res)):
                    
            if(res[i] != '*' and res[i] != '/' and res[i] != '+' and res[i] != '-'):
                blend = blend + res[i]
                if(i == len(res)-1):
                    num.append(blend)
                    blend = ''
            else:
                if(res[i] == '-' and DoubleMinus == 0):
                    DoubleMinus = 1
                    num.append(blend)
                    num.append(res[i])
                    blend = ''
                elif(DoubleMinus == 1 and res[i] == '-'):
                    blend = blend + res[i]
                else:
                    num.append(blend)
                    num.append(res[i])
                    blend = ''
            
        for i in range(0, len(num)-1):
            if(num[i] == ''):
                num.pop(i)
        
        while('*' in num or '/' in num):
            for i, val in enumerate(num):
                if(val == '*'):
                    num[i-1] = float(num[i-1])*float(num[i+1])
                    num.pop(i)
                    num.pop(i)
                if(val == '/'):
                    num[i-1] = float(num[i-1])/float(num[i+1])
                    num.pop(i)
                    num.pop(i)
        
        return PlusMinus(num)

    if('(' in x):
        z = x.replace(')', '(').split('(')
        
        for i in range(0, len(z)-1):
            if(z[i] == ''):
                z.pop(i)

        for i in range(0, len(z)):
            if(str(z[i][0]).isdigit() == True):
                z[i] = Magic(z[i])

        

        res = ''
        for i in z:
            res = res + str(i)
        

        print(Magic(res))
    else:
        print(Magic(x))




print(eval('(1+5*1/2)*3-6/(9-61)/2'))

CalculateString('(1+5*1/2)*3-6/(9-61)/2')




