words = ['abc-123', 'def-456', 'ghi-789', 'abc-456', 'abc', 'abcc', 'non-abc']
checklist = ['abc']
# for item in my_list:
#     if 'abc' in item:
#        print(item)
# matching = [s for s in my_list if "abc" in s]
# print(matching)
#
# for 'abc' in my_list:
#     print()


matches = []
for c in checklist:
    if c in words:
        matches.append(c)
print(matches)
