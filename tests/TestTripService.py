import pytest

from app.DependendClassCallDuringUnitTestException import DependendClassCallDuringUnitTestException
from app.UserNotLoggedInException import UserNotLoggedInException
from app.User import User
from app.TripService import TripService


class TestTripService:

    def test_should_not_raise_an_exception(self):
        # Given
        user = User()
        trip_service = TripService()

        with pytest.raises(Exception):
            trip_service.get_trips_by_user(user)
