from string import punctuation

def longest_word_in_file(file_name) -> None:
    file = open(file_name, 'r').read()
    for sym in punctuation:
        file = file.replace(sym, '')
    ms = list(map(str, file.split()))
    print(ms)
    mss = list()
    a = max(map(len, ms))
    for i in ms:
        if len(i) == a:
            mss.append(i)
    print(mss[-1])

longest_word_in_file('test')