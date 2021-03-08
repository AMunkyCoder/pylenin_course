# Write a Python program to sort a dictionary by value.

# capital_dict_1 = {"India": "New Delhi",
#           "Pakistan": "Islamabad",
#           "Nigeria": "Abuja",
#           "Zambia": "Lusaka"}

# capital_dict_2 = {"Peru": "Lim", 
#           "Ghana": "Accra"}

def sort_dict(dct):
    dct_sorted = {k:v for k, v in sorted(dct.items(), key=lambda x: x[1])}
    return dct_sorted

if __name__ == '__main__':
    capital_dict_1 = {"India": "New Delhi",
          "Pakistan": "Islamabad",
          "Nigeria": "Abuja",
          "Zambia": "Lusaka"}

    capital_dict_2 = {"Peru": "Lim", 
          "Ghana": "Accra"}
    print(sort_dict(capital_dict_1))
    