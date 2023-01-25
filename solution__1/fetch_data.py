import json
import requests


class VehicleAPIData:
    """this class retrieves the first five unique entries of the
    vehicle API data from swapi.dev/api/vehicles
    """

    _PAYLOAD: str = "https://swapi.dev/api/vehicles/"

    def __init__(self) -> None:
        self._manufacturers: set[str] = set()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}, ._get_payload_data(), _add_data(), list_manufacturers()"

    def __str__(self) -> str:
        return f"{self.__class__.__name__} -> {self._PAYLOAD}"

    @classmethod
    def _get_payload_data(cls) -> None:
        response = requests.get(cls._PAYLOAD)
        cls.data = response.json()

    def _add_data(self) -> None:
        for vehicle in self.data["results"]:
            self._manufacturers.add(vehicle["manufacturer"])

    def list_manufacturers(self) -> list[str]:
        obj = list(self._manufacturers)[:5]
        vehicles = json.dumps(obj)
        return vehicles


def main():
    api_data = VehicleAPIData()
    api_data._get_payload_data()
    api_data._add_data()
    print(api_data.list_manufacturers())


if __name__ == "__main__":
    main()
