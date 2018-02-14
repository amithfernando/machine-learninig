from movie_data import DataSet
from tokenizer import TrainingDataTokenizer

# read data set
dataset=DataSet()
movie_dialogs=dataset.get_movie_dialogs()
grouped_dialogs=dataset.group_dialogs(movie_dialogs)
# actor :'' , dialgos : []

# tokenize patterns
grouped_tokenized_patterns=[]
tokenizer=TrainingDataTokenizer()
for group_dialog in grouped_dialogs:
    tokenized_patterns=tokenizer.tokenize(group_dialog.dialogs)
    grouped_tokenized_patterns.append((group_dialog.actor,tokenized_patterns))

print(grouped_tokenized_patterns)


