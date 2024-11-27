with open("test.txt") as f:
    data = f.read().split("\n\n")
    words = data[0][6:].split(",")
    runes = [list(x) for x in data[1].splitlines()]
    for i in range(len(words)):
        words.append(words[i][::-1])
    
