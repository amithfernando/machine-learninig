from movie_data import DataSet


ds=DataSet()

dialogs=ds.get_movie_dialogs()
grouped_dialogs=ds.group_dialogs(dialogs)


