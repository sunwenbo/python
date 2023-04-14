def city_country(city_name="zhangbei",country_name="zhangbei",person=""):
    if person:
        a = city_name + ',' + person + " "  + country_name
    else:
        a = city_name + ',' + country_name
    return a.title()
c = city_country(person="sunwenbo")
#b = city_country("beijing","zhongguo","sunwenbo")
print(c)