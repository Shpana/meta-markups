from pprint import pprint

from options import \
    author, with_tag, AuthorMarkupOption, TagMakrupOption

from markups import load_options


# Markup Meta Data

@author("Michail")
@author("Roman")
@with_tag("Trauser for MIHANGO")
class BookAboutDecorators: ...


if __name__ == "__main__":

    # Load Meta Data
    pprint(load_options(BookAboutDecorators, TagMakrupOption))
    pprint(load_options(BookAboutDecorators, AuthorMarkupOption))
