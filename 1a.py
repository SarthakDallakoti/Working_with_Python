def main():
    try:
        incomeTax = float(input('Enter your income tax: '))

        if incomeTax < 0:
            raise ValueError

        taxBrackets = [
            {'lowerBound': 47500, 'percentage': 0.45},
            {'lowerBound': 7500, 'percentage': 0.4},
            {'lowerBound': 0, 'percentage': 0.2},
        ]

        income = 12500

        for bracket in taxBrackets:
            if (incomeTax > bracket['lowerBound']):
                incomeInBracket = incomeTax - bracket['lowerBound']
                income += (incomeInBracket) / bracket['percentage']
                incomeTax -= incomeInBracket

        print(f'{income:.2f}')
    except ValueError:
        print('Invalid amount!')
