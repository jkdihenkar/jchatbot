import cmd
import sys


class jchatbot(cmd.Cmd):
    """
    JDs Chat BOT
    """
    intro = "Welcome to JD's chatbot ... version 0.2 [cmdLine version]..."

    prompt = "jchatbot > "

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
        self.say_bye()


if __name__ == "__main__":
    jchatbot().cmdloop()