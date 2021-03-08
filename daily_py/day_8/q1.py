# Write a Python code to merge 2 dictionaries as shown below.

# capital_dict_1 = {"India": "New Delhi",
#           "Pakistan": "Islamabad",
#           "Nigeria": "Abuja",
#           "Zambia": "Lusaka"}

# capital_dict_2 = {"Peru": "Lim", 
#           "Ghana": "Accra"}

def dic_merge(dict1, dict2):
    for k, v in dict2.items():
        dict1[k] = v
    return dict1

if __name__ == '__main__':
    capital_dict_1 = {"India": "New Delhi",
          "Pakistan": "Islamabad",
          "Nigeria": "Abuja",
          "Zambia": "Lusaka"}
    capital_dict_2 = {"Peru": "Lim", 
          "Ghana": "Accra"}

    print(dic_merge(capital_dict_1, capital_dict_2))
