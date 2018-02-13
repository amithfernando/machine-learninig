from operator import itemgetter
from itertools import groupby

class MovieDialog:

    def __init__(self,actor,dialogs) -> None:
        super().__init__()
        self.actor=actor
        self.dialogs=dialogs



class DataSet:

    def get_movie_dialogs(self):
        movie_dialogs=[]
        lines = open('raw_data/movie_lines.txt', encoding='utf-8', errors='ignore').read().split('\n')
        id2line = {}
        for line in lines:
            _line = line.split(' +++$+++ ')
            if len(_line) == 5:
                dialog= _line[4]
                actor = _line[3]
                movie_dialog={'actor':actor,'dialog':dialog}
                movie_dialogs.append(movie_dialog)
        return movie_dialogs

    def group_dialogs(self,movie_dialogs):
        # Sort by the desired field first
        movie_dialogs.sort(key=itemgetter('actor'))
        grouped_dialogs=[]
        # Iterate in groups
        for date, items in groupby(movie_dialogs, key=itemgetter('actor')):
            dialogs=MovieDialog(date,items)
            grouped_dialogs.append(dialogs)
        return grouped_dialogs


ds=DataSet()
lines=ds.get_movie_dialogs()

gd=ds.group_dialogs(lines)
print(gd)
print("ok")