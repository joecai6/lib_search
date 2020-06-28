import pandas as pd
import numpy as np

list_author = []

df = pd.read_pickle('../test_data/records_test.pkl')
print("Rows ", len(df))
df['Author'] = df['Author'].apply(lambda name: name[0].upper() + name[1:])

df = df.sort_values('Author')

#preprocessing
dict = {}

for _,row in df.iterrows():
    author = row['Author']
    last_name_char = author[0]
    if last_name_char not in list_author:
        list_author.append(last_name_char)

    dict[last_name_char] = dict.get(last_name_char, 0) + 1


print(dict)
print(list_author)

begin = 0
end = 0

for char in list_author:
    end = dict.get(char) + begin
    if ord(char) >= ord('A') and ord(char) <= ord('Z'):
        df.iloc[begin:end,:].to_csv("../test_data/authors/author_" + str(char) + ".txt", sep='\t', header=False)
    else:
        df.iloc[begin:end,:].to_csv("../test_data/authors/author_symb" + ".txt", sep='\t', mode='a', header=False)
    begin = end

print("Splitted into alphabetical files")