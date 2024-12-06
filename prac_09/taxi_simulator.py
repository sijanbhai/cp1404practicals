from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """Taxi simulator program."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4),
    ]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    while True:
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == "q":
            break
        elif choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                total_bill += drive_taxi(current_taxi)
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(taxis):
    """Allow the user to choose a taxi from the list."""
    print("Taxis available:")
    display_taxis(taxis)
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid input")
    return None


def drive_taxi(taxi):
    """Drive the selected taxi and return the cost of the trip."""
    try:
        distance = float(input("Drive how far? "))
        trip_cost = taxi.get_fare()
        distance_driven = taxi.drive(distance)
        trip_cost = taxi.get_fare() - trip_cost
        print(f"Your {taxi.name} trip cost you ${trip_cost:.2f}")
        return trip_cost
    except ValueError:
        print("Invalid distance")
        return 0.0


def display_taxis(taxis):
    """Display the list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == "__main__":
    main()