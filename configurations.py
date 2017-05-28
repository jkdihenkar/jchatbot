"""
Configurations for the chatbot

Can be a json/yml but for later. 
This should work fine for basic version. 
"""


class Configurations(object):
    """
    Config class
    """

    app_version = 'v0.2'

    app_features = \
    """ 
    The current features implemented in version includes =>
        * display help
        * say hello
        * say bye
        
    Type 'help' to get started. Enjoy!
    """

    elasticsearch_enpoint = "https://localhost:8084"

    elasticsearch_auth = ("admin", "changeme")

    elasticsearch_verify_ssl = False

    elasticsearch_checkonstartup = False

    @staticmethod
    def cleanexitonanyexcept(*args):
        print("\n\nExiting on request... ( or something nasty happened - report to jkdihenkar@gmail.com )")
