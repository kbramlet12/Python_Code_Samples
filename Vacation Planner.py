#=========================================================================================
# Program Name: Vacation Planner
# Author Name: Keegan Bramlet
# Date: 2/5/23
# Purpose of the program: Determine the return day given the Start day and length of Trip
#=========================================================================================
start_day = int(input("If Sunday is 0 and Saturday is 6, what number day do you leave? "))
days_gone = int(input("how many days are you gone? "))
end_day = (start_day + days_gone) % 7
print("Return Day:", end_day)
