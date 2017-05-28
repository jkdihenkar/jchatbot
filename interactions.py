"""
Glues the intents to the chatbot user interface.
"""

from intent_maps import intent_map_data
from intent_methods import IntentMethods
from intents import Intent
from configurations import Configurations

class Interactions(object):
    """
    Handles interaction with the defined intents in backend
    """

    def __init__(self):
        self.intent_mappings = intent_map_data
        self.intent_store = IntentMethods

    def load_intents_to_db_from_store(self):
        """
        * Reads intent maps, 
        * builds a Intent object 
        * and push it to DB
        """
        for intent in intent_map_data:
            for intent_phrase, intent_details in intent.items():
                iobj = Intent(
                    searchPhrase=intent_phrase,
                    intent_actions=intent_details
                )
                iobj.genid()
                iobj.commit_intent_object(dryrun=Configurations.elasticsearch_insertions_dryrun)

