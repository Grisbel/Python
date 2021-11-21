# work to write several functions that investigate a dataset of Jeopardy! questions and answers. 
# Filter the dataset for topics that you’re interested in, compute the average difficulty of those questions.

import pandas as pd
pd.set_option('display.max_colwidth', -1)

jeopardy = pd.read_csv('jeopardy.csv')
#print(jeopardy.columns)
print(len(jeopardy))
#print(jeopardy.head(10))

# EXPLORE
#print(jeopardy['Show Number'])
#print(jeopardy[' Air Date'])
#print(jeopardy[' Round'])
#print(jeopardy[' Category'])
#print(jeopardy[' Value'])
#print(jeopardy[' Question'])
#print(jeopardy[' Answer'])

# Rename columns
jeopardy.columns = ['show_number','air_date', 'round', 'category', 'value', 'question', 'answer']
#print(jeopardy.columns)

# filters the dataset for questions that contains all of the words in a list of words.
def filter_dataset(dataset, keywords):
  filter = lambda x: all(word.upper() in x.upper() for word in keywords)
  
  return dataset[dataset['question'].apply(filter)]

#Test your original function with a few different sets of words
filtered_dataset = filter_dataset(jeopardy, ["1961", "Tel Aviv"])
print(filtered_dataset['question'])

# create a new column with the Values as float.
jeopardy["float_value"]= jeopardy.value.apply(lambda x: float(x[1:].replace(',','')) if x != "None" else 0)

# find the average value of certain topics
filtered_dataset = filter_dataset(jeopardy, ["King"])
print(filtered_dataset['float_value'].mean())

# Write a function that returns the count of the unique answers to all of the questions in a dataset.
def count_unique(dataset):
  print(dataset.answer.value_counts())
  return dataset.answer.value_counts()
count_unique(filtered_dataset)



