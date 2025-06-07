# Write a program to fill in a letter template given below with name and date.
# letter =''
# Dear <| Name | >,
# You are selected!
# <| Date |>

letter='''   
Dear <| Name | >,
You are selected!
<| Date |>
'''
print(letter.replace("<| Name | >","Madhav").replace("<| Date |>","2025/6/7"))

# here replace function is used to replace the selected function with specific function 

