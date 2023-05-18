# Databricks notebook source
print ('mk test notebook!!')

# COMMAND ----------

def reverse(s):
    return s[::-1]

import unittest

class TestHelpers(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse('abc'), 'scba')

r = unittest.main(argv=[''], verbosity=2, exit=False)
assert r.result.wasSuccessful(), 'Test failed; see logs above'

# COMMAND ----------


