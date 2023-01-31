def calculatePay():
    # This first line is provided for you
    hrs = input('Enter Hours: ')
    try: 
        hrs = float(hrs)
    except:
        print('Please enter a number')

    rate = input('Enter Rate: ')
    try:
        rate = float(rate)
    except:
        print('Please enter a number')

    ot_rate = rate *1.5    
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
