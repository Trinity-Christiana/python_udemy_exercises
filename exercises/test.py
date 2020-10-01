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
        print("errors: " + str(len(cls.errors)))
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
        actual_answer = beginner_exercises.ex_001()
        expected_answer = 18
        self.assertEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_002(self):
        actual_answer = beginner_exercises.ex_002()
        expected_answer = "c"
        self.assertEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_003(self):
        actual_answer = beginner_exercises.ex_003()
        expected_answer = "b"
        self.assertEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_004(self):
        actual_answer = beginner_exercises.ex_004()
        expected_answer = 3
        self.assertEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_005(self):
        actual_answer = beginner_exercises.ex_005()
        expected_answer = "b"
        self.assertEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_006(self):
        actual_answer = beginner_exercises.ex_006()
        expected_answer = ['d', 'e', 'f'] 
        self.assertEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_007(self):
        actual_answer = beginner_exercises.ex_007()
        expected_answer = ['a', 'b', 'c']
        self.assertEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_008(self):
        actual_answer = beginner_exercises.ex_008()
        expected_answer = "i"
        self.assertEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_009(self):
        actual_answer = beginner_exercises.ex_009()
        expected_answer = ['h', 'i', 'j']
        self.assertEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_010(self):
        actual_answer = beginner_exercises.ex_010()
        expected_answer = 
        self.assertEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_011(self):
        actual_answer = beginner_exercises.ex_011()
        expected_answer = 
        self.assertEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_012(self):
        actual_answer = beginner_exercises.ex_012()
        expected_answer = 
        self.assertEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_013(self):
        actual_answer = beginner_exercises.ex_013()
        expected_answer = 
        self.assertEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_014(self):
        actual_answer = beginner_exercises.ex_014()
        expected_answer = 
        self.assertEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    # def test_010(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_010(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_010(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_010(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_010(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_010(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_020(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_020(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_020(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_020(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_020(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_020(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_020(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_020(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_020(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_020(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_030(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_030(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_030(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_030(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_030(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_030(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_030(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_030(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_030(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_030(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_040(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_040(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_040(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_040(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_040(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_040(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_040(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_040(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_040(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_040(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_050(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_050(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_050(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_050(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_050(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_050(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_050(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_050(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_050(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_050(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_060(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_060(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_060(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_060(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_060(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_060(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_060(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_060(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_060(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_060(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_070(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_070(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_070(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_070(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_070(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_070(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_070(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_070(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_070(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_070(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_080(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_080(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_080(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_080(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_080(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_080(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_080(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_080(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_080(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_080(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_090(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_090(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_090(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_090(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_090(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_090(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_090(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_090(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_090(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_090(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_100(self):
        # actual_answer = beginner_exercises.ex_000()
        # expected_answer = 
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1

if __name__ == '__main__':
    unittest.main()