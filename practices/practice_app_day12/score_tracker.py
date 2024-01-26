# score_tracker.py

class ScoreTracker:
    def __init__(self):
        self.score = 0

    def increase_score(self):
        self.score += 1

    def get_score(self):
        return self.score
