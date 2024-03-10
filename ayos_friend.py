def do_calc(initial, a_ds):
    months = a_ds[0]
    commission = a_ds[1]
    percent_rate = a_ds[2]/100
    for month in range(1, months+1):
        initial += initial * (percent_rate / 12)
        initial += commission
    return initial


def calculateRetirement(start_age, initial, working, retired):
    print("Age {:3d} month {:2d} you have ${:.2f}".format(start_age//12, start_age%12, initial))
    working_acc_balance = do_calc(initial=initial, a_ds=working)
    retired_acc_balance = do_calc(initial=initial, a_ds=retired)
    print(f"Retirement account balance while working: {working_acc_balance}")
    print(f"Retirement account balance while retired: {retired_acc_balance}")

if __name__ == "__main__":
    calculateRetirement(327, 21_345, (489, 1000, 4.5), (384, -4000, 1))
