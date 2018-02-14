import nltk
from nltk.stem.lancaster import LancasterStemmer
import logging
stemmer = LancasterStemmer()
ignore_words = ['!','"','#','$','%','&','\'','(',')','*','+','-','.','/',':',';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~','\'']

class TrainingDataTokenizer:

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    def to_lower_case(self, text):
        return str(text).lower()

    def tokanize_data(self,text):
        tokenize_text=nltk.word_tokenize(text)
        return tokenize_text

    def filter_data(self,word):
        if word not in ignore_words:
            return word
        else:
            return None

    def stem_data(self,text):
        stemmed_text=stemmer.stem(text)
        return stemmed_text

    def tokenize(self,patterns):
        tokenize_patterns=[]
        for text in patterns:
            text=self.to_lower_case(text)
            text_tokens=self.tokanize_data(text)
            word_tokens=[]
            for word in text_tokens:
                word=self.filter_data(word)
                if None==word:
                    pass
                else:
                    word=self.stem_data(word)
                    word_tokens.append(word)
            #self.logger.info("pattern :  %s  , tokens : %s",text,word_tokens)
            tokenize_patterns.append(word_tokens)
        return tokenize_patterns








