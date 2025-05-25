import re
#check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("Yes!, We have match!")
else:
    print("No Match")