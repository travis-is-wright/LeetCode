class LuckyTicket():
    def isLucky(self, ticket):
        first_three = str(ticket)[:3]
        last_three = str(ticket)[-3:]
        first_sum = 0
        last_sum = 0

        for val in first_three:
            first_sum += int(val)

        for val in last_three:
            last_sum += int(val)

        if first_sum == last_sum:
            return "YES"
        else:
            return "NO"

if __name__ == "__main__":
    lucky = LuckyTicket()
    ticket = 155022
    ticket2 = 405027

    print(lucky.isLucky(ticket))
    print(lucky.isLucky(ticket2))