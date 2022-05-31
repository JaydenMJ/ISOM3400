doc='''<table border="0">
       <thead>
            <tr><th>Option Required Courses</th><th>&nbsp;</th></tr>
       </thead>
       <tbody>
            <tr>
              <td data-title="ISOM-IS Courses">ISOM 4100 - <span>Information Systems Auditing</span></td>
              <td data-title="General Req.">3 credits</td>
           </tr>
           <tr>
              <td data-title="ISOM-IS Courses">ISOM 4300 - <span>Information Systems Control and Assurance</span></td>
              <td data-title="General Req.">3 credits</td>
           </tr>
           <tr>
<td data-title="ISOM-IS Courses"><strong>Extra courses/credits for ISA Option</strong></td>
<td data-title="General Req.">2 courses (6 credits)</td>
           </tr>
       </tbody>
</table>''' 

output=doc.splitlines()

info=[]
newdict={}
extralist=[]
course=[]
for line in output:
    if "td" and "ISOM 4" in line:        
        extra=line.strip(" ").replace('<td data-title="ISOM-IS Courses">',"").replace('<span>',"").replace('</span></td>',"").split(" -")
        for items in extra:
            if "ISOM" in items:
                course.append(extra[0])
                newdict.update({items:extra[1]})
creditlist=[]
       
for line in output:
    if "td" and "credits<" in line: 
        credit=line.replace('<td data-title="General Req.">',"").replace('credits</td>','').strip(" ")
        credit=int(credit)
        creditlist.append(credit)
        

final={}
final={course:credit for (course, credit) in zip(course,creditlist) }
print(final)