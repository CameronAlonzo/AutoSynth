import random
#autosynth/DataGenerator
from DataGenerator import *

class TextDataGenerator(DataGenerator):
    def __init__(self, vocab_size=100, sentence_length=100, n_sentences=100):
        self.vocab_size = vocab_size
        self.sentence_length = sentence_length
        self.n_sentences = n_sentences
        self.vocabulary = [f'word{i}' for i in range(self.vocab_size)]

    def generate(self):
        sentences = []
        for _ in range (self.n_sentences):
            sentence = ''.join(random.choices(self.vocabulary, k=self.sentence_length))
            sentences.append(sentence)
        return sentences