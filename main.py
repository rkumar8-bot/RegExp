li = []
with open(r"C:\Users\rkumar8\PycharmProjects\regularExp\test.txt") as file:
    for line in file:
        x = line.strip().split(" ")
        li.append(x[0])
se = set(li)
fi = list(se)

with open(r"C:\Users\rkumar8\PycharmProjects\regularExp\test.txt") as file:
    for _ in fi:
        a = 0
        n = 0
        file.seek(0)
        for line in file:
            fo = line.strip().split(" ")[0]
            if _ == fo:
                a += int(line.strip().split(" ")[1])
                n += 1
        avg = a/n
        print(f"\nAverage time of {_} is {avg}")
