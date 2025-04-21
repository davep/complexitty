from argparse import Namespace

from complexitty.complexitty import Complexitty

app = Complexitty(
    Namespace(
        colour_map=None,
        max_iteration=None,
        multibrot=None,
        theme="textual-dark",
        x_position=None,
        y_position=None,
        zoom=None,
    )
)
if __name__ == "__main__":
    app.run()
