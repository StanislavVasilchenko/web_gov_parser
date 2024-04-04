from parser.tasks import get_links


def main():
    get_links.delay()


if __name__ == '__main__':
    main()
