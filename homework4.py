cars = {
  "car1" : {
    "name" : "Noble M400",
    "color": "black",
    "year" : "2006"
  },
  "car2" : {
    "name" : "Jaguar XFR",
    "color": "blue",
    "year" : "2009"
  },
  "car3" : {
    "name" : "Lexus LC",
    "color": "white",
    "year" : "2019"
  }
}
filtered = filter(lambda car: car['year'] == '2009', cars.values())
for car in filtered:
    print(car['name'])