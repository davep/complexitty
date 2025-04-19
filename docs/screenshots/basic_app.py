from argparse import Namespace

from complexitty.complexitty import Complexitty

app = Complexitty(Namespace(theme="textual-dark"))
if __name__ == "__main__":
    app.run()
