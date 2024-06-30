#  Exercise: Array DataStructure

# 1. Let us say your expense for every month are listed below,
#     January - 2200
#     February - 2350
#     March - 2600
#     April - 2130
#     May - 2190
#     Create a list to store these monthly expenses and using that find out,

monthly_expenses = [2200, 2350, 2600, 2130, 2190]
# print(monthly_expenses)

# 1. In Feb, how many dollars you spent extra compare to January?
feb_expense =  monthly_expenses[1] - monthly_expenses[0]
# print(feb_expense)

# 2. Find out your total expense in first quarter (first three months) of the year.
frist_quarter = monthly_expenses[0] + monthly_expenses[1] + monthly_expenses[2]
# print(frist_quarter)

# 3. Find out if you spent exactly 2000 dollars in any month
# print(f' expense done in jun month', 2000 in monthly_expenses)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
monthly_expenses.append(1980)
# print(monthly_expenses)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
# print(monthly_expenses[3])
monthly_expenses[3] = monthly_expenses[3] + 200 
# print(monthly_expenses[3])


# 2. You have a list of your favourite marvel super heros.

heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
# print(len(heros))

# 2. Add 'black panther' at the end of this list
# heros.append('black panther')
# print(heros)

# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# heros.remove('black panther')
heros.insert(3, "black panther")
# print(heros)

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros.remove('thor')
heros.remove('hulk')
heros.insert(1, "Doctor Strange")
# print(heros)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

heros.sort()
print(heros)