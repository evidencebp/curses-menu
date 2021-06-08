import cursesmenu.curses_menu
from cursesmenu.items import MenuItem


def main():
    menu = cursesmenu.curses_menu.CursesMenu("Test Menu", "subtitle")
    for i in range(100):
        menu.append_item(MenuItem("item{}".format(i), should_exit=True))
    menu.show()


if __name__ == "__main__":
    main()
