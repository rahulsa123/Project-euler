#first 1_2_3_4_5_6_7_8_9_0 convert into 1_2_3_4_5_6_7_8_9 last known digit is 0.
# here last digit is 9 so solution will contain 3 or 7 at the end, using loop from lower limit to upper then
#some RE. and i got the solution.


import re
p = re.compile("1[1-9]2[1-9]3[1-9]4[1-9]5[1-9]6[1-9]7[1-9]8[1-9]9")
s=101010103
while(not p.match(str(s**2))):
     if(s%10==3):
             s+=4
     else:
             s+=6
