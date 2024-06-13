class Game:
    def __init__(self):
        self.MAX_SCORE_LENGTH = 60

    def guess(self, word_1, word_2):
        if len(word_1) == len(word_2):
            return self.MAX_SCORE_LENGTH

        if self.is_double_length(word_1, word_2):
            return 0

    def is_double_length(self, word_1, word_2):
        return max(len(word_1), len(word_2)) >= min(len(word_1), len(word_2)) * 2
