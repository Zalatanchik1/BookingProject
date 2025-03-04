import allure

from core.models.booking import BookingResponse
from pydantic import ValidationError

@allure.feature('Test creating booking')
@allure.story('Positive: creating booking with custom data')
def test_create_booking_with_custom_data(api_client):
    booking_data = {
        "firstname" : "Jim",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
        },
        "additionalneeds" : "Breakfast"
    }

    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f"Response validation failed{e}")

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']['checkout'] == booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == booking_data['additionalneeds']


@allure.feature('Test creating booking')
@allure.story('Positive: creating booking with custom data and bookingdates')
def test_create_booking_with_custom_data_and_bookingdates(api_client, generate_random_booking_data):
    response = api_client.create_booking(generate_random_booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f"Response validation failed{e}")

    assert response['booking']['firstname'] == generate_random_booking_data['firstname']
    assert response['booking']['lastname'] == generate_random_booking_data['lastname']
    assert response['booking']['totalprice'] == generate_random_booking_data['totalprice']
    assert response['booking']['depositpaid'] == generate_random_booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == generate_random_booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']['checkout'] == generate_random_booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == generate_random_booking_data['additionalneeds']