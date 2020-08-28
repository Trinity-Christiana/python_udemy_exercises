import unittest
from beginner import exercises as beginner_exercises

class TestStringMethods(unittest.TestCase):

    currentResult = None # holds last result object passed to run method
    score = 0
    @classmethod
    def setResult(cls, amount, errors, failures, skipped, score):
        cls.amount, cls.errors, cls.failures, cls.skipped, cls.score = \
            amount, errors, failures, skipped, score

    @classmethod
    def tearDownClass(cls):
        print("\ntests run: " + str(cls.amount))
        # print("errors: " + str(len(cls.errors)))
        print("failures: " + str(len(cls.failures)))
        print("success: " + str(cls.amount - len(cls.errors) - len(cls.failures)))
        # print("skipped: " + str(len(cls.skipped)))
        print("Your score: " + str(cls.score))
        level = "Beginner"

        if cls.score > 75 and cls.score <151:
            level = "Intermediate"
        elif cls.score > 150:
            level = "Advanced"

        print("Your level: " + level)

    def tearDown(self):
        amount = self.currentResult.testsRun
        errors = self.currentResult.errors
        failures = self.currentResult.failures
        skipped = self.currentResult.skipped
        score = self.score
        self.setResult(amount, errors, failures, skipped, score)

    def run(self, result=None):
        self.currentResult = result # remember result for use in tearDown
        unittest.TestCase.run(self, result) # call superclass run method

    def test_001(self):
        passed = beginner_exercises.ex_001() == 18
        self.assertTrue(passed)
        if passed:
            self.score += 1

    def test_002(self):
        passed = beginner_exercises.ex_002() == "c"
        self.assertTrue(passed)
        if passed:
            self.score += 1
            


if __name__ == '__main__':
    unittest.main()