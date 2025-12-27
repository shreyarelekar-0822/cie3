from vehicle import vehicle_details

def test_vehicle_details():
    expected_output = (
        "v_id:143\n"
        "v_name:mustang\n"
        "price:6000\n"
        "year_of_purchase:2001\n"
    )
    assert vehicle_details("143", "mustang", 6000, "2001") == expected_output
