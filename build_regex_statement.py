import pandas as pd
import numpy as np
import re 

file = 'free_email_provider_domains.txt'
character = '|'

"""read in file"""
df = pd.read_csv(file)

"""add a column to the dataframe with the character you want to insert between each row in the df.
Give the column the same name as the character to avoid having to drop the header """
df[character] = character

"""convert DF to a string, and drop the last character of the string
for a regex statement this would drop the training pipe | """
text_string = pd.DataFrame.to_string(df,columns=None,col_space=0,index=False)
text_string = text_string[:-2]

"""define a function to remove white space from string, call function """
def remove(string): 
    pattern = re.compile(r'\s+') 
    return re.sub(pattern, '', string) 

text_string = remove(text_string)

"""create text file, write string to file and output file """
output_file = open("output_regex_statement.txt", "w")
output_file.write(text_string)
output_file.close()


