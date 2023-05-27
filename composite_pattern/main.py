from datetime import date
from dateutil.relativedelta import relativedelta
from person import Person
from tree import Tree


def main():
    hitchhikers = Tree([
        Person('Trilian', date(1970, 3, 14)),
        Person('Arthur', date(1965, 3, 14)),
        Person('Ford', date(1995, 3, 14)),
        Person('Douglas', date(1997, 3, 14)),
        Person('Douglas', date(1999, 3, 14)),
    ])

    singles = Tree([
        Person('Marvin', date(1991, 1, 1)),
        Person('Steven', date(1993, 9, 9))
    ])

    loner = Person('Dirk', date(1990, 1, 1))

    tree1 = Tree(hitchhikers)
    tree2 = Tree([singles, loner])
    tree3 = Tree([tree1, tree2])

    for tree in tree1, tree2, tree3:
        oldest = tree.get_oldest()
        age = relativedelta(date.today(), oldest.birthdate)
        print(
            f"Oldest person: {oldest.name}; Age: {age.years} years, "
            f"{age.months} months")


if __name__ == '__main__':
    main()
