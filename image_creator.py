import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import cm

count = 1
n = 2


for filename in os.listdir("message_swapped"):
    f = open("message_swapped/{}".format(filename), 'r')
    content = f.read()

    if len(content) == 282:
        # print(content)
        num = 2
        decimal_ary = [int(content[i:i+2],16) for i in range(0,len(content),2)]
        
        while (num * num) < len(decimal_ary):
            num += 1

        while len(decimal_ary) != (num*num):
            decimal_ary.append(0)

        # print(len(decimal_ary), num*num)
        img = np.array(decimal_ary).reshape(num, num)

        new_img = Image.fromarray(np.uint8(img), 'L')
        scaled = new_img.resize((16, 16))
        scaled.save('malicious_data/message_swapped/{}.png'.format(count))
        count += 1


print("")