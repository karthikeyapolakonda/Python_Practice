#solved set matrix zeros DSA Question in the laboratory

#Week 1 practice  22/01/2025 - Theory Class
n = int(input("Enter no.of Rows:"))
for i in range(n, 0, -1):
    print(f'{i}' * (n-i+1))
# Enter no.of Rows:7
# 7
# 66
# 555
# 4444
# 33333
# 222222
# 1111111

n = int(input("Enter n :"))
fir = 0
sec = 1
i = 0
while i < n:
    print(fir, end = ' ')
    temp = fir + sec
    fir = sec
    sec = temp
    i += 1
# Enter n :15
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 

x = int(input("Enter from :"))
y = int(input("Enter to :"))
res = []
for i in range(x, y + 1):
    curr = 0
    for j in range(1, i + 1):
        if i % j == 0:
            curr += 1
            if curr > 2:
                break
    if curr == 2:
        res.append(i)
print('Prime Numbers from', x, 'to', y, '=', res)
# Enter from :10
# Enter to :35
# Prime Numbers from 10 to 35 = [11, 13, 17, 19, 23, 29, 31]

# Local Variable
def add():
    x = 10
    y = 20
    z = x + y
    print('The Sum is', z)
add()
# The Sum is 30

# Global Variable
x = 190
def main():
    global x
    print(x)
    x = 'Python'
    print(x)
main()
print(x)
# 190
# Python
# Python
