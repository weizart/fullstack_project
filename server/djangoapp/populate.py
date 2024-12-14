from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name":"NISSAN", "description":"Great cars. Japanese technology"},
        {"name":"Mercedes", "description":"Great cars. German technology"},
        {"name":"Audi", "description":"Great cars. German technology"},
        {"name":"Kia", "description":"Great cars. Korean technology"},
        {"name":"Toyota", "description":"Great cars. Japanese technology"},
    ]
    car_make_instances = []
    for data in car_make_data:
            car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description']))
    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
      {"name":"Pathfinder", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "dealer_id": 1, "price": 50000.00, "engine": "V6", "transmission": "Automatic"},
      {"name":"Qashqai", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "dealer_id": 1, "price": 45000.00, "engine": "4-cylinder", "transmission": "CVT"},
      {"name":"XTRAIL", "type":"SUV", "year": 2023, "car_make":car_make_instances[0], "dealer_id": 1, "price": 47000.00, "engine": "4-cylinder", "transmission": "CVT"},
      {"name":"A-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1], "dealer_id": 2, "price": 55000.00, "engine": "4-cylinder", "transmission": "Automatic"},
      {"name":"C-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1], "dealer_id": 2, "price": 65000.00, "engine": "4-cylinder", "transmission": "Automatic"},
      {"name":"E-Class", "type":"SUV", "year": 2023, "car_make":car_make_instances[1], "dealer_id": 2, "price": 75000.00, "engine": "6-cylinder", "transmission": "Automatic"},
      {"name":"A4", "type":"SUV", "year": 2023, "car_make":car_make_instances[2], "dealer_id": 3, "price": 60000.00, "engine": "4-cylinder", "transmission": "Automatic"},
      {"name":"A5", "type":"SUV", "year": 2023, "car_make":car_make_instances[2], "dealer_id": 3, "price": 65000.00, "engine": "4-cylinder", "transmission": "Automatic"},
      {"name":"A6", "type":"SUV", "year": 2023, "car_make":car_make_instances[2], "dealer_id": 3, "price": 70000.00, "engine": "6-cylinder", "transmission": "Automatic"},
      {"name":"Sorrento", "type":"SUV", "year": 2023, "car_make":car_make_instances[3], "dealer_id": 4, "price": 45000.00, "engine": "4-cylinder", "transmission": "Automatic"},
      {"name":"Carnival", "type":"SUV", "year": 2023, "car_make":car_make_instances[3], "dealer_id": 4, "price": 50000.00, "engine": "V6", "transmission": "Automatic"},
      {"name":"Cerato", "type":"Sedan", "year": 2023, "car_make":car_make_instances[3], "dealer_id": 4, "price": 35000.00, "engine": "4-cylinder", "transmission": "Automatic"},
      {"name":"Corolla", "type":"Sedan", "year": 2023, "car_make":car_make_instances[4], "dealer_id": 5, "price": 30000.00, "engine": "4-cylinder", "transmission": "CVT"},
      {"name":"Camry", "type":"Sedan", "year": 2023, "car_make":car_make_instances[4], "dealer_id": 5, "price": 35000.00, "engine": "4-cylinder", "transmission": "Automatic"},
      {"name":"Kluger", "type":"SUV", "year": 2023, "car_make":car_make_instances[4], "dealer_id": 5, "price": 45000.00, "engine": "V6", "transmission": "Automatic"},
    ]
    for data in car_model_data:
            CarModel.objects.create(
                name=data['name'], 
                car_make=data['car_make'], 
                type=data['type'], 
                year=data['year'],
                dealer_id=data['dealer_id'],
                price=data['price'],
                engine=data['engine'],
                transmission=data['transmission']
            )
