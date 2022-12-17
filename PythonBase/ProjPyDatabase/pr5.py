morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
         'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
         'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
         'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••', }
text = list('Ignition sequence start'.lower().split())
print(text)

for i in range(len(text)):
        for j in range(len(text[i])):
                if j != len(text[i]) - 1:
                        print(morze[text[i][j]],end = ' ')
                else:
                        print(morze[text[i][j]])
        
        

