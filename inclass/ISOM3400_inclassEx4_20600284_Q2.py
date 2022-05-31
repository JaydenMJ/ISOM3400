

#%%
#Task 1
StudentScores  = " Chinese = 88  LS = 98  Maths = 68 "


# Write code below
if '=' in StudentScores:
        StudentScores=StudentScores.split(" ")
        

score=int(StudentScores[3])+int(StudentScores[7])+int(StudentScores[11])
print(f"[Task 1]sum={score}, and mean={round((score/3),2)}")
# %%
# Task 2
news = 'Yahoo Finance Stock market news live updates'

# write code below (1 line ONLY)
news=news.replace(' ','')
print(f"[Task2]{news}")

# %%
# Task 3
numbers = [1, 2, 3]
letters = ['a', 'p', 'm']


# write code below 

a=zip(numbers,letters)
print(f"[Task3]{list(a)}")

# %%
# Task 4
test_str = '''
            could not get driver version for /dev/input/mouse0, Not a typewriter
            could not get driver version for /dev/input/mice, Not a typewriter
                    0035  : value 0, min 0, max 1079, fuzz 0, flat 0, resolution 0
                    0036  : value 0, min 0, max 1919, fuzz 0, flat 0, resolution 0
        '''

# write code below (2 lines ONLY)
a=[]
for lines in test_str.splitlines():
        a.append(lines.split())
print(f"[Task4] w={a[3][7].replace(',','')}")
print(f"[Task4] h={a[3][7].replace(',','')}")
# %%
