import csv

# line_count = 0
# with open('res.csv', 'r') as csv_file:
#     with open('three_values_swapped.csv', 'w') as write_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         csv_write = csv.writer(write_file, delimiter=',')
#         for row in csv_reader:
#             row[839], row[981] = row[981], row[839]
#             row[839], row[3525] = row[3525], row[839]

#             csv_write.writerow(row)
#             line_count += 1
# print('Processed {} lines.'.format(line_count))


line_count = 0
with open('res.csv', 'r') as csv_file:
    with open('message_swapped.csv', 'w') as write_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_write = csv.writer(write_file, delimiter=',')
        for row in csv_reader:
            row[2026] = "4aadb8265e8f04e27e00cc0b2151b7f74443"

            csv_write.writerow(row)
            line_count += 1
print('Processed {} lines.'.format(line_count))


# line_count = 0
# with open('res.csv', 'r') as csv_file:
#     # with open('three_values_swapped.csv', 'w') as write_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         # csv_write = csv.writer(write_file, delimiter=',')
#         for row in csv_reader:

#             if len("".join(row)) == 282:
#                 print(row.index('30101b921f7396f4f4744bffff0000000000'))
#                 break
#             line_count += 1
# print('Processed {} lines.'.format(line_count))