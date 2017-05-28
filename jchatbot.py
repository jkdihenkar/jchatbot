import cmd
import sys
from es import es
from configurations import Configurations


class jchatbot(cmd.Cmd):
    """
    JDs Chat BOT
    """

    version = Configurations.app_version

    if Configurations.elasticsearch_checkonstartup:
        intro = "Welcome to JD's chatbot ... version 0.2 [cmdLine version]... \n\n" \
                "Connected to backend v1 => ES ( {} ) and Lucene ( {} )".format(
            es().test_connection()['version']['number'],
            es().test_connection()['version']['lucene_version']
        )
    else:
        intro = "Welcome to JD's chatbot ... version 0.2 [cmdLine version]... \n"

    intro += Configurations.app_features

    prompt = "({}) jchatbot > ".format(version)

    def do_hello(self, arg):
        'Greet the chatbot'
        print("Nahh I'm loading AI to mah brain! DND...")

    def do_bye(self, arg):
        'Bbye'
        print("Good you understand what is DND! :P")
        sys.exit(0)

    def emptyline(self):
        print("Ayeeh!.. Stop pressing enter randomly!")

    def default(self, line):
        print("Dont you know how to talk to jchatbot? :/")

    def postloop(self):
        self.do_bye("Bye")


if __name__ == "__main__":
    sys.excepthook = Configurations.cleanexitonanyexcept
    jchatbot().cmdloop()