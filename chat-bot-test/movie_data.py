from operator import itemgetter
import operator
import itertools
from itertools import groupby
import os

class MovieDialog:

    def __init__(self,actor,dialogs) -> None:
        super().__init__()
        self.actor=actor
        self.dialogs=dialogs



class DataSet:

    def get_movie_dialogs(self):
        movie_dialogs=[]
        project_path=os.path.dirname(os.path.realpath(__file__))
        lines = open(project_path+'/raw_data/movie_lines.txt', encoding='utf-8', errors='ignore').read().split('\n')
        id2line = {}
        for line in lines:
            _line = line.split(' +++$+++ ')
            if len(_line) == 5:
                dialog= _line[4]
                actor = _line[3]
                if actor:
                    actor=actor.replace('"' ,'')
                    movie_dialog={'actor':actor,'dialog':dialog}
                    movie_dialogs.append(movie_dialog)
        return movie_dialogs

    def group_dialogs(self,movie_dialogs):
        # Sort by the desired field first
        movie_dialogs.sort(key=itemgetter('actor'))
        grouped_dialogs=[]
        # Iterate in groups
        for key, items in itertools.groupby(movie_dialogs, operator.itemgetter('actor')):
            dialogs=[]
            for dialog in list(items):
                dialogs.append(dialog['dialog'])
            grouped_dialogs.append(MovieDialog(key,dialogs))
        return grouped_dialogs
