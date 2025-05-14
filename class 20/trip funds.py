def hotel_cost(nights):
    return 140* nights

def plane(cities):
    if 'colombo' == cities:
        return 180
    
    elif 'bandaranike' == cities:
        return 120
    
    elif 'mattala' == cities:
        return 200
    
    elif 'jaffna' == cities:
        return 210
    

def carcost(days):

    if days >= 7:
        return 40*days - 50
    
    elif days >=3:
        return 40*days - 30
    
    else:
        return 40* days
    
def tripcost(cities , nights , days, spending_money):
    return hotel_cost(nights) + plane(cities) + carcost(days) + spending_money

print(f'the total trip cost is {tripcost('colombo', 5, 6, 500)})