def pack_calc(total_packs, cigs_smoked, cigs_per_pack = 20):
    total_cigs = total_packs * cigs_per_pack
    return (total_cigs - cigs_smoked + 19) // cigs_per_pack
def cig_calc(total_packs, cigs_smoked, cigs_per_pack = 20):
    total_cigs = total_packs * cigs_per_pack

    if (total_cigs - cigs_smoked) <= 0:
        return 0
    else:
        return (total_cigs - cigs_smoked)

def main():
    while True:
        total_packs = input("How many Cigarette packs do you have?: ")
        cigs_smoked = input("How many Cigarettes have you smoked?: ")

        try:
            total_packs = int(total_packs)
            cigs_smoked = int(cigs_smoked)

            if total_packs < 0 or cigs_smoked < 0:
                print("Please input an integer greater than 0.")
                continue
            break
        except ValueError:
            print("Please input a integer value for number of packs and cigs smoked.")

    packs_left = pack_calc(total_packs, cigs_smoked)
    cigs_left = cig_calc(total_packs, cigs_smoked)


    print(f"You have {packs_left} pack(s) and {cigs_left} cig(s) total left!")

if __name__ == "__main__":
    main()

