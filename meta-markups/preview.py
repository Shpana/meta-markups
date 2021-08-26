from options import author, select_authors


@author("Shpana")
@author("Roman")
class BookAboutDecorators: ...


if __name__ == "__main__":
    for author_option in select_authors(BookAboutDecorators):
        print(author_option)
