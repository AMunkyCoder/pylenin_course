# Qns 1
# Check if the following list of terms are keywords in Python.
# check, i, Exception, flush, nonlocal, async, await

import keyword

kw_list = [ "check", "i", "Exception", "flush", "nonlocal", "async", "await", "elif", "import"]

for kw in kw_list:
    if keyword.iskeyword(kw):
        print("{} is a keyword".format(kw))
    else:
        print("{} is not a keyword".format(kw)) 

print("##############")

for kw in kw_list:
    if kw in keyword.kwlist:
        print("{} is a keyword".format(kw))