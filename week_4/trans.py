#s = "The exhibition, called Nightingale in 200 Objects, People & Places, will continue for a year. St Thomas' is one of a small number of hospitals in Britain with an area for the treatment of coronavirus patients.The emphasis on sanitation, good hygiene, fresh air, exercise, good food... no matter how much we advance, those fundamental foundational principles of Florence are still very much the basis of modern nursing,"
new = ""

for i in s:
    if i == "e":
        new += "h"
    elif i == "h":
        new += "t"
    elif i == "t":
        new += "e"
    else :
        new += i

print(new)