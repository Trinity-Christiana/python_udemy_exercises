import unittest
import exercises as exercises


class TestStringMethods(unittest.TestCase):

    currentResult = None  # holds last result object passed to run method
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

        if cls.score > 75 and cls.score < 151:
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
        self.currentResult = result  # remember result for use in tearDown
        unittest.TestCase.run(self, result)  # call superclass run method

    def test_001(self):
        actual_answer = exercises.ex_001()
        expected_answer = 18
        self.assertEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_002(self):
        actual_answer = exercises.ex_002()
        expected_answer = "c"
        self.assertMultiLineEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_003(self):
        actual_answer = exercises.ex_003()
        expected_answer = "b"
        self.assertMultiLineEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_004(self):
        actual_answer = exercises.ex_004()
        expected_answer = 3
        self.assertEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_005(self):
        actual_answer = exercises.ex_005()
        expected_answer = "b"
        self.assertMultiLineEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_006(self):
        actual_answer = exercises.ex_006()
        expected_answer = ['d', 'e', 'f']
        self.assertListEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_007(self):
        actual_answer = exercises.ex_007()
        expected_answer = ['a', 'b', 'c']
        self.assertListEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_008(self):
        actual_answer = exercises.ex_008()
        expected_answer = "i"
        self.assertMultiLineEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_009(self):
        actual_answer = exercises.ex_009()
        expected_answer = ['h', 'i', 'j']
        self.assertListEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_010(self):
        actual_answer = exercises.ex_010()
        expected_answer = ['a', 'c', 'e', 'g', 'i']
        self.assertListEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 2

    def test_011(self):
        actual_answer = exercises.ex_011()
        expected_answer = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                           10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.assertListEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_012(self):
        actual_answer = exercises.ex_012()
        expected_answer = [10, 20, 30, 40, 50, 60, 70, 80, 90,
                           100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
        self.assertListEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_013(self):
        actual_answer = exercises.ex_013()
        expected_answer = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
                           '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
        self.assertListEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 2

    def test_014(self):
        actual_answer = exercises.ex_014()
        expected_answer = ['1', 2, 1]
        self.assertCountEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 2

    def test_015(self):
        actual_answer = exercises.ex_015()
        expected_answer = {"a": 1, "b": 2}
        self.assertIsInstance(actual_answer, dict)
        self.assertIs(actual_answer["a"], 1)
        self.assertIs(actual_answer["b"], 2)
        if actual_answer == expected_answer:
            self.score += 1

    def test_016(self):
        actual_answer = exercises.ex_016()
        expected_answer = 2
        self.assertEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_017(self):
        actual_answer = exercises.ex_017()
        expected_answer = 3
        self.assertEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_018(self):
        actual_answer = exercises.ex_018()
        expected_answer = "Smith"
        self.assertMultiLineEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 1

    def test_019(self):
        actual_answer = exercises.ex_019()
        expected_answer = {'a': 1, 'c': 3, 'b': 2}
        self.assertDictEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 2

    def test_020(self):
        actual_answer = exercises.ex_020()
        expected_answer = 6
        self.assertEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 2

    def test_021(self):
        actual_answer = exercises.ex_021()
        expected_answer = {'a': 1}
        self.assertDictEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 2

    def test_022(self):
        actual_answer = exercises.ex_022()
        expected_answer = {
            "a": [
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10
            ],
            "b": [
                11, 12, 13, 14, 15, 16, 17, 18, 19, 20
            ],
            "c": [
                21, 22, 23, 24, 25, 26, 27, 28, 29, 30
            ]}
        self.assertDictEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 2

    def test_023(self):
        actual_answer = exercises.ex_023()
        expected_answer = 13
        self.assertEqual(actual_answer, expected_answer)
        if actual_answer == expected_answer:
            self.score += 2

    def test_024(self):
        actual_answer = exercises.ex_024()
        answer = self.assertIn(
            "b has value [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]", actual_answer)
        self.assertIn(
            "c has value [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]", actual_answer)
        self.assertIn(
            "a has value [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]", actual_answer)

        self.score += 2

    # def test_020(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_020(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_020(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_020(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_020(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_020(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_030(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_030(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_030(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_030(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_030(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_030(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_030(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_030(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_030(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_030(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_040(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_040(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_040(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_040(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_040(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_040(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_040(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_040(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_040(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_040(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_050(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_050(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_050(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_050(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_050(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_050(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_050(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_050(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_050(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_050(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_060(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_060(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_060(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_060(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_060(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_060(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_060(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_060(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_060(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_060(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_070(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_070(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_070(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_070(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_070(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_070(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_070(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_070(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_070(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_070(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_080(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_080(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_080(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_080(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_080(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_080(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_080(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_080(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_080(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_080(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_090(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_090(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_090(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_090(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_090(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_090(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_090(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_090(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_090(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_090(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1
    # def test_100(self):
        # actual_answer = exercises.ex_000()
        # expected_answer =
        # self.assertEqual(actual_answer, expected_answer)
        # if actual_answer == expected_answer:
        #     self.score += 1


if __name__ == '__main__':
    unittest.main()
