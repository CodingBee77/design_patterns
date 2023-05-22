from annual import Annual
from annual_student import AnnualStudent
from annual_corporate import AnnualCorporate
from monthly import Monthly
from monthly_corporate import MonthlyCorporate
from datetime import datetime


def main():
    sub1 = MonthlyCorporate('Bob', datetime.today())
    sub2 = AnnualStudent('Carol', datetime.today())
    sub3 = MonthlyCorporate('Ted', datetime.today())
    sub4 = AnnualStudent('Carol', datetime.today())

    print('\nDiscounted subscriptions: \n')
    print(
        f'Subscriber: {sub1.subscriber}, Cost: {sub1.price}, Expiration: '
        f'{sub1.expiration}')
    print(
        f'Subscriber: {sub2.subscriber}, Cost: {sub2.price}, Expiration: '
        f'{sub2.expiration}')
    print(
        f'Subscriber: {sub3.subscriber}, Cost: {sub3.price}, Expiration: '
        f'{sub3.expiration}')
    print(
        f'Subscriber: {sub4.subscriber}, Cost: {sub4.price}, Expiration: '
        f'{sub4.expiration}')

    print('\nNormal subscriptions: \n')
    sub5 = Monthly('Fred', datetime.today())
    sub6 = Annual('Wilma', datetime.today())

    print(
        f'Subscriber: {sub5.subscriber}, Cost: {sub5.price}, Expiration: '
        f'{sub5.expiration}')
    print(
        f'Subscriber: {sub6.subscriber}, Cost: {sub6.price}, Expiration: '
        f'{sub6.expiration}')


if __name__ == "__main__":
    main()
