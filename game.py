


class Game:
    def __init__(self):
        self.MAX_SCORE_LENGTH = 60
    def guess(self, word_1, word2):
        if len(word_1) == len(word2):
            return self.MAX_SCORE_LENGTH