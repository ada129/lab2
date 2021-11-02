#9.1
m_list = set()  # множества
m = int(input('kol-vo knig h:'))
n_list = set()
n = int(input('kol-vo knig s:'))

for q in range(m):
    book = (input('h_book:'))
    m_list.add(book)
for w in range(n):
    book = (input('s_book:'))
    n_list.add(book)

    if book in m_list:
        print('y')
    else:
        print('n')
#9.2
from collections import Counter  # подсчет количества

m = int(input())
familii = []
for i in range(m):
    for j in range(int(input())):
        q = input()
        familii.append(q)  # добавление аргумента в конец списка
list1 = dict(Counter(familii))  # словарь
for who in list1:
    if list1.get(who) == m:
        print(who)
#9.3
kolvo = int(input("kol-vo:"))
list1 = set()
list2 = set()

for i in range(kolvo):
    famil = str(input())
    if famil in list1:
        list2.add(famil)
    else:
        list1.add(famil)
rez = list1 - list2
itog = kolvo - len(rez)
print(itog)
#9.4
kolvo_holod = int(input())
holodilnik = set()
prod = set()

for i in range(kolvo_holod):
    holodilnik.add(input())
recept = int(input())

for i in range(recept):
    name_recept = str(input())
    prod_recept = int(input())
    check = True
    for q in range(prod_recept):
        prod.add(input())
    for w in prod:
        if not w in kolvo_holod:
            check = False

    if check:
        print(name_recept)
    prod = set()
#10.1
s = input('mess: ')
n = int(input('num: '))
if 0 < n <= len(s):
    print(s[n-1])
else:
    print('err')
#10.2
def ceasar_encode(letter, shift):
    if letter.isalpha():
        number = ord(letter) + shift % 32
        if number > 1103:
            number -= 32
        return chr(number)
    return letter


shift = int(input())
for l in input():
    print(ceasar_encode(l, shift), end='')
#10.3
inp = input()
if inp[0].lower() == 'а':
    print('y')
else:
    print('n')
#10.4
print(input()[-1])
#10.5
word=input()
while (word[0]=="а" or word[0]=="А"):
      word=input()
#10.6
path = input()
char = path[0]
way_list = path[1:].split('V')
num_spaces = 0
for move in way_list:
    if move and move[0] == '<':
        num_spaces -= len(move)
    print(' '*num_spaces + char*(1+len(move)))
    if move and move[0] == '>':
        num_spaces += len(move)
#11.1
inp = input()
max_p = max(inp.split('р'))  # Метод split() разбивает строку по указанному разделителю и возвращает список строк
print(len(max_p))
#11.2
count = int(input())

for i in range(count):
    inp = input()
    if inp[:4] == '####':
        continue
    if inp[:2] == '%%':
        print(inp[2:])
    else:
        print(inp)
 #11.3
inp = input().lower()
n = int(input()) - 1
letter = input().lower()
if (0 < n <= len(inp)) and (letter in inp) and (len(letter) == 1):
    print('y') if inp[n] == letter else print('n')
else:
    print('err')
#11.5
inp = input()
while len(inp):
    print(inp)
    inp = inp[1: -1]
#12.1
n_white = int(input())
white_list = []

for i in range(n_white):
    white_list.append(input())

black = []
n_black = int(input())

for j in range(n_black):
    black.append(input())
for a in black:
    if a in white_list:
        print(a)
#12.2
s = input()
n = int(s[:4])
total = int(s[4:])
error = []
true = 0

for i in range(n):
    s = input()
    price = int(s[:7])
    amount = int(s[8:12])
    cost = int(s[13:])
    if price * amount != cost:
        error.append(i + 1)
    true += price * amount
print(total - true)
for x in error:
    print(x, end=' ')
#12.3
n=int(input())
mag=[]
for i in range(n):
    mag.append(input())
for i in range(n//2):
    print(mag.pop(0),mag.pop(1))
#12.4
tring = input()
count = 1
for i in range(len(string)-1):
    if i <= len(string):
        if string[i] == string[i + 1]:
            count += 1
        else:
            a = string[i]
            print(count, string[i])
            count = 1
print(count, string[i])
#12.5
num = int(input())
r, rr, dd = 1, [], []

while r not in rr:
    rr.append(r)
    dd.append(10 * r // num)
    r = 10 * r % num
print(*dd[rr.index(r):])
#13.2
print(*sorted((int(input('enter num: ')) for _ in range(int(input(': ')))), reverse=True),
      sep="\n")
#13.4
s = int(input())
first = [int(input()) for i in range(s)]
second = first[:]
n = int(input())
for i in range(n):
    brother = int(input())
    if brother == 1:
        first[int(input())] += int(input())
    elif brother == 2:
        second[int(input())] += int(input())
print(*first)
print(*second)
dd = 0
for i in range(len(first)):
    if first[i] == second[i]:
        dd = dd + 1
print(dd)
#13.5
N = int(input())
results = []
for i in range(N):
    results.append((input(), int(input())))
m = len(results)
for i in range(m - 1):
    for j in range(m - i - 1):
        if results[j][1] > results[j + 1][1]:
            results[j] = results[j + 1]
            results[j + 1] = results[j]
k = m // 2
the_final = results[k:]
first = results[: k]
m = len(the_final)
for i in range(m - 1):
    for j in range(m - i - 1):
        if the_final[j] > the_final[j + 1]:
            the_final[j] = the_final[j + 1]
            the_final[j + 1] = the_final[j]
for i in the_final:
    print(i[0])
m = len(first)
for i in range(m - 1):
    for j in range(m - i - 1):
        if first[j] > first[j + 1]:
            first[j], first[j + 1] = first[j + 1], first[j]
for i in first:
    print(i[0])
#13.6
f = {'A': [' *   ', '* *  ', '***  ', '* *  ', '* *  '], 'B': ['**   ', '* *  ', '**   ', '* *  ', '**   '],
     'C': [' *   ', '* *  ', '*    ', '* *  ', ' *   '], 'D': ['**   ', '* *  ', '* *  ', '* *  ', '**   '],
     'E': ['***  ', '*    ', '**   ', '*    ', '***  '], 'F': ['***  ', '*    ', '**   ', '*    ', '*    '],
     'G': [' **  ', '*    ', '* *  ', '* *  ', ' **  '], 'H': ['* *  ', '* *  ', '***  ', '* *  ', '* *  '],
     'I': ['***  ', ' *   ', ' *   ', ' *   ', '***  '], 'J': [' **  ', '  *  ', '  *  ', '* *  ', ' *   '],
     'K': ['* *  ', '**   ', '*    ', '**   ', '* *  '], 'L': ['*    ', '*    ', '*    ', '*    ', '***  '],
     'M': ['* *  ', '***  ', '***  ', '***  ', '* *  '], 'N': ['* *  ', '***  ', '***  ', '* *  ', '* *  '],
     'O': ['***  ', '* *  ', '* *  ', '* *  ', '***  '], 'P': ['***  ', '* *  ', '***  ', '*    ', '*    '],
     'Q': ['***  ', '* *  ', '* *  ', '***  ', '***  '], 'R': ['**   ', '* *  ', '**   ', '* *  ', '* *  '],
     'S': [' **  ', '*    ', ' *   ', '  *  ', '**   '], 'T': ['***  ', ' *   ', ' *   ', ' *   ', ' *   '],
     'U': ['* *  ', '* *  ', '* *  ', '* *  ', '***  '], 'V': ['* *  ', '* *  ', '* *  ', '* *  ', ' *   '],
     'W': ['* *  ', '* *  ', '* *  ', '***  ', '* *  '], 'X': ['* *  ', '* *  ', ' *   ', '* *  ', '* *  '],
     'Y': ['* *  ', '* *  ', '* *  ', ' *   ', ' *   '], 'Z': ['***  ', '  *  ', ' *   ', '*    ', '***  ']}
string = input()
for i in range(5):
    for k in string:
        print(f.get(k)[i], end='')
    print()
#13.7
n = int(input())
list = []
for i in range(n):
    list.append(input())
k = int(input())
a = 0
print(list[0])
del list[0]
for i in range(n):
    if len(list) > a + k - 1:
        a += k - 1
        print(list[a])
        del list[a]
    else:
        a = 0
        if len(list) > a:
            print(list[a])
            del list[a]
#14.1
n = int(input())
ingridient = []
for i in range(n):
    enter = input()
    if 'лук' not in enter:
        ingridient.append(enter)
print(' ,'.join(ingridient))
#14.3
print('\n'.join(input().split()))
#14.4
a = list(map(int, input().split()))
xmax = len(a)
ymax = max(a)
print('*'*(xmax + 2))
print('*' + ' '*xmax + '*')
for y in range(1, ymax + 1):
    print(end='*')
    for ak in a:
        if ak >= ymax - y + 1:
            print(end='*')
        else:
            print(end=' ')
    print('*')
#14.5
url =[list(i.split("=")) for j in list(input().split("?")) for i in list(j.split("&"))][1:]
key = input()
for i in range(len(url)):
    if url[i][0] == key:
        print(url[i][1])
#15.1
a = input()
print(*[i for i in input().split() if a.upper() in i or a in i], sep='\n')
#15.2
string = input()
c = 0
for a in string:
    if a != ' ' and a != '\t':
        c += 1
print(c)
#15.3
string = input()
string = string.upper()
k = 0
for i in range(0, len(string)):
    if string.count(string[i]) > k:
        k = string.count(string[i])
print(k)
#15.5
n = int(input())
queue = []
for i in range(n):
    s = input().split()
    if 'встал' in s[1]:
        queue.append(s[0])
    elif s[0] == 'Привет,':
        queue.insert(queue.index(s[1][:-1])+1, s[2])
    elif s[1] == 'хватит':
        queue.remove(s[0][:-1])
print(*queue, sep='\n')
#16.1
n=int(input())
bak=[[0]*n for i in range(n)]
for i in range(n*n):
    n[int(n**(1/2))][i]=int(input())
k=int(input())
for i in range(k):
    n[int(input())][int(input())]-=8
for i in  range(n):
    for j in range(n):
        print(n[i][j])
#16.2
a = []
for i in range(int(input())):
    string = input().split(',')
    a.append(string)
for i in range(int(input())):
    cords = [int(i) for i in input().split(',')]
    d = a[cords[0]]
    word = d[cords[1]]
    print(word)
#16.4
n = int(input())
s = [[]]
for i in range(n - 1):
    s.append([int(j) for j in input().split()])
station = input().split()
a = int(station[0])
b = int(station[1])
l = s[max(a, b)][min(a, b)]
z = -1
for i in range(n):
    if i != a and i != b:
        if l > s[max(a, i)][min(a, i)] + s[max(i, b)][min(i, b)]:
            l = s[max(i, b)][min(i, b)] + s[max(i, b)][min(i, b)]
            z = i
if z != -1:
    print(z)
else:
    print(a)
#17.1
def transliteration2(text):
    rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    eng = 'a|b|v|g|d|e|e|zh|z|i|i|k|l|m|n|o|p|r|s|t|u|f|kh|tc|ch|sh|shch||y||e|iu|ia|A|B|V|G|D|E|E|Zh|Z|I|I|K|L|M|N|' \
          'O|P|R|S|T|U|F|Kh|Tc|Ch|Sh|Shch||Y||E|Iu|Ia'.split(
        '|')
    return text.translate({ord(k): v for k, v in zip(rus, eng)})
#17.2
string = {}
for _ in range(int(input())):
    val, key = input().split()
    if key in string:
        string[key].append(val)
    else:
        string[key] = [val]
for _ in range(int(input())):
    key = input()
    if key in string:
        print(*string[key])
    else:
        print('no')
#17.4
n = int(input())
post = input().split(' опубликовал пост, количество просмотров: ')
pop = {post[0]: [int(post[-1]), 'origin']}
for _ in range(n - 1):
    post = input()
    repost, post = post.split(' отрепостил пост у ')
    author, views = post.split(', количество просмотров: ')
    pop[repost] = [int(views), author]
    while author != 'origin':
        pop[author][0] += int(views)
        author = pop[author][1]
for val in pop.values():
    print(val[0])
#17.5
data = {}
for _ in range(int(input())):
    answer = input()
    data[answer] = data.get(answer)
for _ in range(int(input())):
    a = ''
    ok = False
    for i in input().split('/'):
        if i:
            a = a + '/' + i
        if a in data:
            ok = True
    if ok:
        print('y')
    else:
        print('n')
