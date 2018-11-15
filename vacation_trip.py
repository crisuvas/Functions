def hotel_cost(nights):
    return 140 * nights


def plane_ride_cost(city):
    if city == "Guadalajara":
        return 450
    elif city == "Monterrey":
        return 1450
    elif city == "CDMX":
        return 530
    elif city == "Tlaquepaque":
        return 234


def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost


def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money


print(trip_cost("Guadalajara", 8, 5400))
