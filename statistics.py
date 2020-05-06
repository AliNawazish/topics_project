import os

max = 0
count = 1
categories = {}

for filename in os.listdir("files_unmodified"):
    f = open("files_unmodified/{}".format(filename), 'r')
    l = len(f.read())

    if l > max:
        max = l


    if l in categories:
        tmp = categories[l]
        tmp += 1
        categories[l] = tmp
    else:
        categories[l] = 1
    # print("Files processed: {}".format(count))
    count += 1

print("")
print("Maximum size: ", max)
print("Categories: ", len(categories))
print(categories)