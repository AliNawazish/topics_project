import csv


with open('message_swapped.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:

        if line_count == 0:
            line_count += 1
            continue
        # if len("".join(row)) == 282:
        #     print(row.index("340108"))
        f = open("message_swapped/{}.txt".format(line_count), "w")
        f.write("".join(row))
        f.close()

        line_count += 1
