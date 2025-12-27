def vehicle_details(v_id, v_name, price, year_of_purchase):
    result = (
        f"v_id: {v_id}\n"
        f"v_name: {v_name}\n"
        f"price: {price}\n"
        f"year_of_purchase: {year_of_purchase}\n"
    )
    return result

if __name__ == "__main__":
    v_id = "143"
    v_name = "mustang"
    price = "6000"
    year_of_purchase = "2001"
    print(vehicle_details(v_id, v_name, price, year_of_purchase))
