def letter_count(a,b):
    count = 0
    c = list(a.lower())
    d = b.lower()
    for i in range(len(c)):
        if c[i]== d:
            count = count + 1
    return count

if __name__ == '__main__':
    a = 'halLway'
    b = 'L'
    count = letter_count(a,b)
    print count