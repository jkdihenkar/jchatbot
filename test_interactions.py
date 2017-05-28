import interactions
import unittest


class TestInteractions(unittest.TestCase):
    """
    Tests interactions
    """
    def setUp(self):
        self.TestInteraction = interactions.Interactions()

    def test_interaction_load_to_db(self):
        self.TestInteraction.load_intents_to_db_from_store()
