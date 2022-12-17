b = input()

znak = ''

for i in range(len(b)):
        if b[i] == '+':
                znak += '+'
                break
        elif b[i] == '-':
                znak += '-'
                break
        elif b[i] == '*' and b[i+1]=='*':
                znak += 'x'
                break
        elif b[i] == '*':
                znak += '*'
                break
        elif b[i] == '/':
                znak += '/'
                break
        elif b[i] == '%':
                znak += '%'
                break
b = b.replace("**", 'x')      
a, c = map(str, b.split(znak))

if c == '':
        c = '2'
znak = b[len(a):len(a)+1]
a = int(a)
c = int(c)
if znak == '+':
        print(a+c)
elif znak == '-':
        print(a-c)
elif str(znak) == 'x':
        print(a**c)
elif znak == '*':
        print(a*c)
elif znak == '/':
        print(a/c)
elif znak == '%':
        print(a/100)


