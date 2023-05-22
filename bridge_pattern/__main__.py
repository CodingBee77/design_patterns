from annual import Annual
from monthly import Monthly
from discount import NoDiscount, StudentDiscount, CorporateDiscount
from datetime import datetime


def main():
    sub1 = Monthly('Bob', datetime.today(), StudentDiscount)
    sub2 = Annual('Carol', datetime.today(), CorporateDiscount)
    sub3 = Annual('Ted', datetime.today(), NoDiscount)

    print(
        f'Subscription: {sub1.subscriber}, Cost: {sub1.price}, Expiration: '
        f'{sub1.expiration}')
    print(
        f'Subscription: {sub2.subscriber}, Cost: {sub2.price}, Expiration: '
        f'{sub2.expiration}')
    print(
        f'Subscription: {sub3.subscriber}, Cost: {sub3.price}, Expiration: '
        f'{sub3.expiration}')


if __name__ == "__main__":
    main()
