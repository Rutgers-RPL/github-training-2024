import sys # Please don't touch this
sys.path.append('./introductions') # or this (bonus points if you know why)

# Put all imports below this line
from introductions import shivampatel # import the file containing your individual introduction blurb
from introductions import kashvichandwani
from introductions import ivanz
from introductions import ianquaye
from introductions import aaronordonez
from introductions import mokshithanelluri
from introductions import matthewschaming
from introductions import sophiaabbassi
# Put all imports above this line

def main():
    # Call your intro function below this line
    shivampatel.intro() 
    kashvichandwani.intro()
    ivanz.intro()
    ianquaye.intro()
    aaronordonez.intro()
    mokshithanelluri.intro()
    matthewschaming.intro()
    sophiaabbassi.intro()
    # Call you intro function above this line


if __name__ == '__main__':
    main()
