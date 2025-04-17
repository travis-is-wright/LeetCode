class ClockHandCalc:
    def calculate_hands_angles(self, hour: int, minutes: int) -> (float, float):
        if not 0 <= hour <= 23:
            raise ValueError("Hours must be between 0 and 23!")
        if not 0 <= minute <= 59:
            raise ValueError("Minutes must be between 0 and 59!")

        if hour > 12:
            hour -= 12

        hour_angle = (30 * hour) + (minute * 0.5)
        minute_angle = (6 * minute)

        return hour_angle, minute_angle

if __name__ == "__main__":
    clockhandcalc = ClockHandCalc()

    hour = int(input("Hour: "))
    minute = int(input("Minute: "))

    hour_angle, minute_angle = clockhandcalc.calculate_hands_angles(hour, minute)

    print(f"Angle of Hour Hand: {hour_angle}°")
    print(f"Angle of Minute Hand: {minute_angle}°")
