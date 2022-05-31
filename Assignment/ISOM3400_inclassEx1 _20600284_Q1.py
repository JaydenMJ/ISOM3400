
doc='''<tbody>
 <tr>
 <td data-title="Exclusion"><span>COMP 1021</span></td>
 <td data-title="Instructor"><span>Prof. James KWOK and Prof. Jia JIA</span></td>
 <td data-title="Class Hours">
 <p><span>
 Wed and Fri 1500-1620 (L1) - Rm TBA<br>
 Tue and Thu 1030-1150 (L2) - Rm TBA<br>
 Mon 1630-1720 (La1) - Rm TBA<br>
 Mon 1330-1420 (La2) - Rm TBA<br>
 Mon 1500-1550 (La3) - Rm TBA
 </span></p>
 </td>
 </tr>
</tbody>'''

data=doc.splitlines()
tutor=[]
for line in data:
  if "Instructor" in line:
    prof=line.replace("""<td data-title="Instructor"><span>""",'').replace('</span></td>',"").split(" and ")
    print(f"Task1:\t{prof}")

list1=[]
for line in data:
    if 'Wed' in line:
        t2a=line.replace('''- Rm TBA<br>''',"")
        list1.append(t2a)
    if 'Tue' in line:
        t2b=line.replace('''- Rm TBA<br>''',"")
        list1.append(t2b)
print(f"Task2:\t{list1}")

final={}
final={name:lesson for (name, lesson) in zip(prof,list1)}
print(f"Task3:\t{final}")
# Task 1
"""
for line in data:
   if 'td' in line:
      if 'Instructor' in line:
        str1=f"{line}"
        str2=str(str1.split("span"))
        str3=str2.replace('''<td data-title="Instructor"><', '>''',"")
        str4=str3.replace("and", ",")
        str5=str4.replace('''</', '></td>''',"")
        print(str5)   
        
# Task2
list1=[]
for line in data:
    if 'Wed' in line:
        t2a=line.replace('''- Rm TBA<br>''',"")
        list1.append(t2a)
    if 'Tue' in line:
        t2b=line.replace('''- Rm TBA<br>''',"")
        list1.append(t2b)    



#Task3
list2=[]
for line in data:
   if 'td' in line:
      if 'Instructor' in line:
        str6=str5.replace('''[''',"") 
        str7=str6.replace(''']''',"") 
        str8=str7.strip("''")
    
        james=str8.replace(''', Prof. Jia JIA''',"")
        jia=str8.replace('''Prof. James KWOK , ''',"")
        list2.append(james)
        list2.append(jia)
        
dictionary = dict(zip(list2, list1))
print(dictionary)"""