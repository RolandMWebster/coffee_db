from coffee_db.app.utils import Site
from coffee_db.app.pages import HomePage


pages = [HomePage()]

site = Site(
    pages=pages,
    name="Coffe Site",
    content_name="Coffee Site"
)


def main():
    site.write()


if __name__ == "__main__":
    main()