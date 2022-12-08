
s = 'иванов иван'

for i in range(len(s)):
        print(i)
        if i == 0 or i - 1 == ' ':
                s[i] = s[i].upper()
        print(s[i])
        
