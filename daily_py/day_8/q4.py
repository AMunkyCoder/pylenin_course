# Write a Python program to sum all the items in a dictionary.

# GDP_2017 = {"India": 6.6, 
#             "Zambia": 4.1, 
#             "Nigeria": 0.8,
#             "Peru":2.5, 
#             "Ghana": 8.5
#            }

def dct_sum(dct):
    dctsum = sum(dct.values())
    return dctsum

if __name__ == '__main__':
    GDP_2017 = {"India": 6.6, 
            "Zambia": 4.1, 
            "Nigeria": 0.8,
            "Peru":2.5, 
            "Ghana": 8.5
           }
    print(dct_sum(GDP_2017))