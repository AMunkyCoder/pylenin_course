# Write a Python program to draw the below Pyramid.

#     *     
#    ***    
#   *****   
#  *******  
# ********* 

def pyra():
    for i in range(1, 10, 2):
        x = i * "*"
        print(x.center(10))

if __name__ == '__main__':
    pyra()