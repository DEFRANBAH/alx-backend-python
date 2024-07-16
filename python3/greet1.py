import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    
    def do_greet(self, repository):
                
        if repository:
            print ("hi,", repository)
        else:
            print ('hi')

    def do_help(self, line):
        print('\n'.join(["greet [repository]",
        "Greet the named repository"]))
    def do_EOF(self, line):
        return True
    
    def postloop(self):
        print()

if __name__ == '__main__':
    HelloWorld().cmdloop()
