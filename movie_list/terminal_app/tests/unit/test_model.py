from unittest import TestCase
from unittest.mock import patch
import os

import model as model
import queries

class TestModelInstance(TestCase):

    def setUp(self) -> None:
        self.patcher1 = patch('model.Database.initialize_db')
        self.MockClass1 = self.patcher1.start()

    def tearDown(self) -> None:
        self.patcher1.stop()

    def test_create_class(self):
        
        movie_list_model = model.Database()
        self.assertTrue(isinstance(movie_list_model, model.Database))

class TestModelInit(TestCase):

    def setUp(self) -> None:
        self.patcher1 = patch('model.Database.exec_only')
        self.MockClass1 = self.patcher1.start()

    def tearDown(self) -> None:
        self.patcher1.stop()

    def test_initialize_db(self) -> None:
        movie_list_model = model.Database()
        movie_list_model.initialize_db()

        # Assert if initialize db was called with query
        self.MockClass1.assert_called_with(queries.create_table_movies)

class TestExecMethods(TestCase):

    def test_exec_only(self):
        pass

    def test_exec_fetchall(self):
        pass