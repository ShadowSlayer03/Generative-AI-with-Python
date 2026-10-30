seat_type = input("What train seat would you like to prefer? (Sleeper, AC, General, Luxury): ").lower()

match seat_type:
    case "sleeper":
        print("Features: Comfortable berths, fans, curtains, and affordable overnight travel.")
    case "ac":
        print("Features: Air-conditioned coaches, comfortable bedding, quiet environment, and privacy.")
    case "general":
        print("Features: Most affordable, non-reserved seating, crowded but economical.")
    case "luxury":
        print("Features: Premium experience with recliner seats, meals included, entertainment screens.")
    case _:
        print("Invalid choice. Please select from Sleeper, AC, General, or Luxury.")