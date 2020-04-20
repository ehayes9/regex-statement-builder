import pandas as pd
import numpy as np
import re 

"""input filename and character to separate rows (delimiter, max number of characters per regex statement """

file = 'most_common_noncorp_email.csv'
character = '|'
max_char = 1000


def read_file_add_column(file,character):
	df = pd.read_csv(file)
	df[character] = character
	return df

def split_dataframes(max_rows,df):
	"""create array of dfs by spliting df into several dfs based on max rows specified"""
	array_of_dfs = []
	while len(df) > max_rows:
		top = df[:max_rows]
		array_of_dfs.append(top) 
		df = df[max_rows:]
	else: 
		array_of_dfs.append(df)

	return array_of_dfs	

def df_to_string(df):
	"""drop index before converting DF to a string
	drop the trailing "|" character from the end of the regexp statement"""
		# df_as_string = df.rename(columns=df.iloc[0]).drop(df.index[0])
	df = pd.DataFrame.to_string(df,columns=None,col_space=0,index=False)
	df = df[:-2]

	return df

def remove_whitespace(string): 
	"""remove white space from string """
	pattern = re.compile(r'\s+') 
	
	return re.sub(pattern, '', string) 

def create_files(list,i):
	for string in list:
		output_file = open(f"output_regex_statement_{i}.txt".format(i=i), "w")
		# file.write(string)
		# file.close()
		i=i+1

#TODO: find way to split string to nearest '|' 



def split_string(text, max_char): 
	"""take a large regex statement and break it into smaller elements based on the max character limitation,
	and the delimiter character defined
	"""
	array_of_regex_statements = []
	while len(text) > max_char:
		# create a substring with same # of characters are max_char
		sub_string = text[:max_char]
		delim_position = test_sub_string.rfind(character) # search from the right, find the first occurrence of '|'
		print(delim_position)
		# if the '|' character exists in test substring
		if delim_position != 1: 
			sub_string = sub_string[:delim_position] 
		# else no change to substring, no need to write out explicitly
		array_of_regex_statements.append(sub_string)
		# any part of the test substring that isn't consumed by rfind, add back to the original string
		remainder_string = sub_string[delim_position:].split(character)[1] # remove the '|', if it exists
		text = text[max_char:]
		text = remainder_string + text 
	else: 
		array_of_regex_statements.append(text)

	return array_of_regex_statements	


if __name__ == "__main__":

	df = read_file_add_column(file=file,character=character)
	df = df_to_string(df) 
	string = remove_whitespace(df)
	array_of_regex_statements = split_string(string=string, max_char=max_char)

	df = pd.DataFrame(array_of_regex_statements,index=None) #convert to DF
	df.to_csv('output.csv',index=False) #output to CSV

