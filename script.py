import csv

csv_insurance_data = open('Data/insurance.csv')
insurance_data = csv.DictReader(csv_insurance_data)


# the average age of an insured person
def get_average_age(data):
    total_age = 0
    length = 0
    for x in data:
        try:
            age = int(x['age'])
            total_age += age
            length += 1
        except ValueError:
            pass
    average_age = total_age / length
    csv_insurance_data.seek(0)
    return int(round(average_age, 0))


# average age with one child insured
def average_age_with_one_child(data):
    total_age = 0
    total_people_with_one_child = 0
    for child in data:
        if child['children'] == '1':
            total_age += int(child['age'])
            total_people_with_one_child += 1
    average_age = total_age / total_people_with_one_child
    csv_insurance_data.seek(0)
    return int(round(average_age, 0))


# total smokers and non smokers
def is_smoker(data):
    total_smokers = 0
    non_smokers = 0
    for smoker in data:
        if smoker['smoker'] == 'yes':
            total_smokers += 1
        if smoker['smoker'] == 'no':
            non_smokers += 1
    csv_insurance_data.seek(0)
    return total_smokers, non_smokers


# the percent smokers make up
def avg_percent_smokers(data):
    num_smokers = is_smoker(data)[0]
    list_length = 0
    for _ in data:
        list_length += 1
    list_length = list_length - 1
    average = num_smokers / list_length
    percent = (average / list_length) * 100
    csv_insurance_data.seek(0)
    return round(percent, 2)


# area most people have this insurance
def area_from(data):
    north_west = 0
    north_east = 0
    south_east = 0
    south_west = 0

    for region in data:
        if region['region'] == 'northwest':
            north_west += 1
        if region['region'] == 'northeast':
            north_east += 1
        if region['region'] == 'southeast':
            south_east += 1
        if region['region'] == 'southwest':
            south_west += 1
    area_dic = {'North West': north_west,
                'North East': north_east,
                'South East': south_east,
                'South West': south_west}
    max_value = max(area_dic.values())
    max_key = max(area_dic, key=area_dic.get)
    csv_insurance_data.seek(0)
    return max_key, max_value


# difference in price between smokers and not smokers
def smoker_non_smoker_diff(data):
    smoker = is_smoker(data)[0]
    smoker_cost_total = 0
    non_smoker = is_smoker(data)[1]
    non_smoker_cost_total = 0
    for cost in data:
        if cost['smoker'] == 'yes':
            smoker_cost_total += float(cost['charges'])
        if cost['smoker'] == 'no':
            non_smoker_cost_total += float(cost['charges'])
    csv_insurance_data.seek(0)
    avg_smoker_cost = smoker_cost_total / smoker
    avg_non_smoker_cost = non_smoker_cost_total / non_smoker
    return round(avg_smoker_cost, 2), round(avg_non_smoker_cost, 2)


# percent difference between smokers and non Smokers
def smoker_non_smoker_percent_diff(data):
    avg_smoker_cost, avg_non_smoker_cost = smoker_non_smoker_diff(data)
    total_cost = 0
    for cost in data:
        try:
            temp_cost = float(cost['charges'])
            total_cost += temp_cost
        except ValueError:
            pass
    percent = ((avg_smoker_cost - avg_non_smoker_cost) / avg_non_smoker_cost) * 100
    csv_insurance_data.seek(0)
    return int(round(percent, 0))


# difference between sex
def sex_difference(data):
    num_of_male = 0
    num_of_female = 0
    total_cost_of_male = 0
    total_cost_of_female = 0
    for value in data:
        if value['sex'] == 'male':
            num_of_male += 1
            total_cost_of_male += float(value['charges'])
        if value['sex'] == 'female':
            num_of_female += 1
            total_cost_of_female += float(value['charges'])
    price_for_male = total_cost_of_male / num_of_male
    price_for_female = total_cost_of_female / num_of_female
    csv_insurance_data.seek(0)
    return round(price_for_male, 2), round(price_for_female, 2)


def price_difference_for_sex(data):
    male_price, female_price = sex_difference(data)
    return male_price - female_price


total_smokers, non_smokers = is_smoker(insurance_data)
area, num_people = area_from(insurance_data)
smoker_cost, non_smoker_cost = smoker_non_smoker_diff(insurance_data)
male_insurance_price, female_insurance_price = sex_difference(insurance_data)

print(
    f"The average price of an insured person is {get_average_age(insurance_data)}, The average age with one child is {average_age_with_one_child(insurance_data)}, \n"
    f"Smokers make up {avg_percent_smokers(insurance_data)}% of the total with {total_smokers} smokers and {non_smokers} non-smokers. \n"
    f"The price difference between smokers and non-smokers is {smoker_non_smoker_percent_diff(insurance_data)}% with the average price of a smoker ${smoker_cost}, Non-smoker ${non_smoker_cost} \n"
    f"The place with the most people insured is {area} with {num_people} people.\n"
    f"Your sex also plays a role in Price with male prices ${male_insurance_price} and female prices ${female_insurance_price} which is a difference of ${price_difference_for_sex(insurance_data)}")
