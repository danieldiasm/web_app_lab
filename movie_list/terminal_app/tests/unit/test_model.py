from unittest import TestCase
from unittest.mock import MagicMock
import os

import model as model

class TestModelMocked(TestCase):

    def test_create_db(self):
        model.initialize_db = MagicMock()
        model.initialize_db.return_value = None

        moviedb = model.database()

        expected_result = True
        actual_result = os.path.isfile(moviedb.dbfile)

        self.assertEqual(actual_result, expected_result, msg="Failed creating DB File!")
