from pyscript import document, display

set_1 = {"Fries", "Burger"}
set_2 = {"Fries", "Burger", "Coke", "Apple Pie"}

#isplay(set_1.issubset(set_2), target="output1")  # Alternative way to check if set_1 is a subset of set_2
#display(set_1 <= set_2, target="output1")  # (Subset) Output would display true
#display(set_1 < set_2, target="output1")  # (Proper Subset) Output would display true
#display(set_2 >= set_1, target="output1")  # (Superset) Output would display true
#display(set_2 > set_1, target="output1")  # (Proper Superset) Output would display true 

subjects = ["Math", "Science", "Filipino", "Ict"]
converted_version = frozenset(subjects)
display(converted_version, target="output1")