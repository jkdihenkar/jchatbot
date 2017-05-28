"""
This are the actions supposed to be taken by the chatbot based on
    a formally designed action statement.

    Ex. Like open google chrome browser.
     will be searched based on lucene based matching to any designed intents
     in ES like "Google Chrome Browser" -> intent [ "open" : launch a browser ]
                "Google chrome browser" -> intent [ "search" : open chrome and google search page ]

    Here intents keywords are the must keywords present in the Phrase.
"""

from hashlib import sha256

class Intent(object):
    """
    Intent 
        id -> keyword -> sha256sum of searchPhrase [ Custom indexing ]
        searchPhrase -> text [ full text searched with fuzziness ]
        intent_actions -> list of [ intent_keyword -> function mappings ]
                            intent_keyword = text
                            intent_keyword.keyword = keyword
                            function mappings = keyword
    """
    def __init__(self, searchPhrase='', intent_actions=None):
        """
        A searchPhrase once set cannot be changed. 
        It needs entire object to be deleted.
        
        Intent actions is a mutable list.
        """
        self.id = ''
        self.searchPhrase = searchPhrase
        self.intent_actions = intent_actions

    def exists_intent_action(self, intent_keyword):
        """
        Checks if an intent exists by keyword search
        """
        pass

    def add_intent_action(self, intent_keyword, intent_function):
        """
        Adds an intent action to the Intent
        """
        pass

    def get_intent_action(self, intent_keyword):
        """
        Exists check + return dict
        """
        pass

    def commit_intent_object(self, dryrun=False):
        if dryrun:
            print("Commiting object : {} to DB".format(
                self
            ))
        else:
            # insert to es!
            pass

    def genid(self):
        self.id = str(sha256(self.searchPhrase.encode('utf-8')).hexdigest())

    def __str__(self):
        return "_id : {} / searchPhrase : {} / intentdetails: {}".format(
            self.id,
            self.searchPhrase,
            self.intent_actions
        )

    @staticmethod
    def fetch_fromDB(self, searchPhrase):
        """
        Search from db and load details to current object if any
            returns intentObject if found and loads in new object
            returns None if not found
        """
        pass



