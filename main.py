from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv", encoding='UTF-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
cool_contacts = [contacts_list[0]]
work_list = [contacts_list[1:]]
persons = ''
for person in work_list[0]:
  persons = persons + ','.join(person) + '\n'
pattern = r"(\w+)\s*(\w*)\s*(\w*)\s*,(\w*)\s*(\w*),(\w*),(\w*)?,(\D*)?,((\+7|8)?\s?\(?(\d{3})\)?(\s|\-)?(\d{3})(\s|\-)?(\d{2})(\s|\-)?(\d{2})\s*\(?(доб.)?\s*(\d*)\)?\s*)?,([\w\.@]*)?\s*\n?"
person_list = re.findall(pattern, persons)
total_pattern = r"\1,\2\4,\3\5\6,\7,\8,+7(\11)\13-\15-\17 \18\19,\20,"
result = re.sub(pattern, total_pattern, persons)
result_list = result.split(',')
len_result = len(result_list)
index = 0
contact = []
while index < (len_result - 1):
  contact.append(result_list[index])
  contact.append(result_list[index+1])
  contact.append(result_list[index+2])
  contact.append(result_list[index+3])
  contact.append(result_list[index+4])
  contact.append(result_list[index+5])
  contact.append(result_list[index+6])
  cool_contacts.append(contact)
  contact = []
  index += 7
index = 0
index_1 = 1
index_2 = 0
index_3 = []
len_contact = len(cool_contacts)
while index < (len_contact - 1):
  while index_1 < len_contact:
    if cool_contacts[index][0] == cool_contacts[index_1][0] and cool_contacts[index][1] == cool_contacts[index_1][1]:
      while index_2 < 7:
        if len(cool_contacts[index][index_2]) >= len(cool_contacts[index_1][index_2]):
          pass
        else:
          cool_contacts[index][index_2] = cool_contacts[index_1][index_2]
        index_2 += 1
      index_3.append(index_1)
      index_2 = 0
    index_1 += 1
  index += 1
  index_1 = index + 1
for i in index_3:
  cool_contacts[i].clear()
total_list = []
for per in cool_contacts:
  if len(per) > 0:
    total_list.append(per)
pprint(total_list)
with open("phonebook.csv", "w", encoding='UTF-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(total_list)