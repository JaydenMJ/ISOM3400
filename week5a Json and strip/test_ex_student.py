
#%%
# Question 3

html_doc='''
<table border="0">
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

out_html=html_doc.splitlines()

for idx,line in enumerate(out_html):
   if 'td' in line:
      if 'Systems' in line:
         str1=f"[{idx}]{line}"
         str2=str1.split("span")
         print(str2)
# %%
