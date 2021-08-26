from options import \
    author, with_tag, AuthorMarkupOption, TagMakrupOption

from markups import load_options


# Markup Meta Data

@author("Michail")
@author("Roman")
@with_tag("Trauser for MIHANGO")
class BookAboutDecorators: 

    @author("Roman")
    @property
    def content(): ...


if __name__ == "__main__":

    # Load Meta Data
    print(load_options(BookAboutDecorators, TagMakrupOption))
    print(load_options(BookAboutDecorators, AuthorMarkupOption))

    print(load_options(BookAboutDecorators.content, AuthorMarkupOption))
