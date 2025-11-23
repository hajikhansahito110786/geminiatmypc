def find_capital():
    country_capitals = {
        "usa": "Washington, D.C.",
        "india": "New Delhi",
        "japan": "Tokyo",
        "germany": "Berlin",
        "france": "Paris",
        "uk": "London",
        "canada": "Ottawa",
        "australia": "Canberra",
        "china": "Beijing",
        "brazil": "Brasília",
        "russia": "Moscow",
        "italy": "Rome",
        "spain": "Madrid",
        "mexico": "Mexico City",
        "south africa": "Pretoria",
        "egypt": "Cairo",
        "argentina": "Buenos Aires",
        "greece": "Athens",
        "new zealand": "Wellington",
        "switzerland": "Bern",
    }

    country = input("Enter a country name: ").strip().lower()

    if country in country_capitals:
        print(f"The capital of {country.title()} is {country_capitals[country]}.")
    else:
        print(f"Sorry, I don't have information for the capital of {country.title()}.")

if __name__ == "__main__":
    find_capital()
