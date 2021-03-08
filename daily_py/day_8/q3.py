# Write a Python script to check whether a given key already exists in a dictionary.

def check_duplicate(country, dct):
    cntry = dct.get(country, "Country is not on the list")
    return cntry
    
if __name__ == '__main__':
    capital_dict_1 = {"India": "New Delhi",
          "Pakistan": "Islamabad",
          "Nigeria": "Abuja",
          "Zambia": "Lusaka"}
    country = input("Enter Country: ")
    print(check_duplicate(country, capital_dict_1))