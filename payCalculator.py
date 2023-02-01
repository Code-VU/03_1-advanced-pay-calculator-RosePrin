def calculatePay():
    # This first line is provided for you
    try:
        hrs = float(input('Enter Hours: '))
    except:
        hrs = float(input('Error, please enter numeric input: '))

    try:
        rate = float(input('Enter Rate: '))
    except:
        rate = float(input('Error, please enter numeric input: '))

    ot_rate = rate * 1.5
    if hrs <= 40:
        print('Pay:', (hrs * rate))
    else:
        ot_hrs = hrs - 40
        print('Pay:', ((ot_hrs * ot_rate) + (rate * 40)))

    # end assignment

## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
