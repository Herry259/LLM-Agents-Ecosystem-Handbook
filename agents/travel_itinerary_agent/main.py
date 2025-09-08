"""
Travel Itinerary Agent
----------------------

This script collects basic trip information from the user and returns a
synthetic itinerary.  It demonstrates how an agent might reason about
destinations, dates and activities without connecting to external services.

All data (flights, hotels, activities) is hard‑coded for demonstration
purposes.  You can extend the dictionaries below or replace them with
live API calls for a production‑ready agent.
"""

import datetime as dt
from typing import List, Dict, Any


# Sample data for flights, hotels and activities for a few destinations
SAMPLE_DATA: Dict[str, Dict[str, Any]] = {
    "Paris": {
        "flights": [
            {"airline": "AirDemo", "departure": "09:00", "arrival": "13:00"},
            {"airline": "FlyMock", "departure": "14:00", "arrival": "18:00"},
        ],
        "hotels": ["Hotel Lumière", "Château Demo", "Budget Inn Paris"],
        "activities": [
            "Visit the Eiffel Tower",
            "Explore the Louvre Museum",
            "Stroll along the Seine and have a picnic",
            "Enjoy a café in Montmartre",
        ],
    },
    "Tokyo": {
        "flights": [
            {"airline": "NipponAir", "departure": "11:00", "arrival": "22:00"},
            {"airline": "SushiSky", "departure": "23:00", "arrival": "10:00 (+1)"},
        ],
        "hotels": ["Hotel Sakura", "Shinjuku Stay", "Capsule Haven"],
        "activities": [
            "Visit Senso‑ji Temple in Asakusa",
            "Explore Akihabara’s electronics district",
            "Walk through the Shinjuku Gyoen National Garden",
            "Enjoy sushi at Tsukiji Outer Market",
        ],
    },
    "New York": {
        "flights": [
            {"airline": "SkyNYC", "departure": "08:00", "arrival": "12:00"},
            {"airline": "FreedomAir", "departure": "15:00", "arrival": "19:00"},
        ],
        "hotels": ["Central Park Hotel", "Times Square Lodge", "Brooklyn B&B"],
        "activities": [
            "Visit the Statue of Liberty",
            "Walk through Central Park",
            "Tour the Metropolitan Museum of Art",
            "See a Broadway show",
        ],
    },
}


def choose_flight(flights: List[Dict[str, str]]) -> Dict[str, str]:
    """Pick the first flight option.  In a real agent, you would choose based on price and convenience."""
    return flights[0]


def choose_hotel(hotels: List[str]) -> str:
    """Pick the first hotel.  You could add logic for budget or star rating."""
    return hotels[0]


def plan_daily_activities(available: List[str], days: int, preferences: List[str]) -> List[List[str]]:
    """Generate a list of activities for each day based on user preferences."""
    itinerary = []
    idx = 0
    for _ in range(days):
        day_plan = []
        for pref in preferences:
            for activity in available:
                if pref.lower() in activity.lower() and activity not in day_plan:
                    day_plan.append(activity)
                    break
        # Fill remaining slots with random activities if needed
        while len(day_plan) < 2 and idx < len(available):
            act = available[idx]
            if act not in day_plan:
                day_plan.append(act)
            idx += 1
        itinerary.append(day_plan)
    return itinerary


def main() -> None:
    print("Welcome to the Travel Itinerary Agent!")
    destination = input("Where would you like to go? (Paris, Tokyo, New York) ").strip().title()
    if destination not in SAMPLE_DATA:
        print(f"Sorry, I don't have data for {destination}. Try one of: {', '.join(SAMPLE_DATA.keys())}.")
        return
    dep_date_str = input("Enter your departure date (YYYY-MM-DD): ").strip()
    ret_date_str = input("Enter your return date (YYYY-MM-DD): ").strip()
    try:
        dep_date = dt.datetime.strptime(dep_date_str, "%Y-%m-%d")
        ret_date = dt.datetime.strptime(ret_date_str, "%Y-%m-%d")
    except Exception:
        print("Invalid date format.")
        return
    num_days = (ret_date - dep_date).days
    if num_days <= 0:
        print("Return date must be after departure date.")
        return
    prefs_input = input("Preferred activities (comma-separated, e.g. museums, food, sightseeing): ").strip()
    preferences = [p.strip() for p in prefs_input.split(",") if p.strip()]

    data = SAMPLE_DATA[destination]
    flight = choose_flight(data["flights"])
    hotel = choose_hotel(data["hotels"])
    itinerary = plan_daily_activities(data["activities"], num_days, preferences)

    print("\n--- Your Travel Itinerary ---")
    print(f"Destination: {destination}")
    print(f"Flight: {flight['airline']} departing at {flight['departure']} and arriving at {flight['arrival']}")
    print(f"Hotel: {hotel}\n")
    for i in range(num_days):
        day_date = dep_date + dt.timedelta(days=i)
        print(f"Day {i+1} ({day_date.strftime('%Y-%m-%d')}):")
        for act in itinerary[i]:
            print(f"  - {act}")
        print()
    print("Enjoy your trip!")


if __name__ == "__main__":
    main()