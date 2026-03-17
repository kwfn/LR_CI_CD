class RefuelError(Exception):
    """Исключение при попытке залить слишком много топлива."""
    def __init__(self, message: str = "Вы пытаетесь залить слишком много бензина!"):
        self.message = message
        super().__init__(self.message)


class InsufficientFuelError(Exception):
    """Исключение при недостаточном количестве топлива для поездки."""
    def __init__(self, message: str = "Не доедем жеж..."):
        self.message = message
        super().__init__(self.message)


class Car:
    def __init__(self, model: str, fuel_capacity: float) -> None:
        self._model = model
        self._max_fuel_capacity: float = fuel_capacity
        self._fuel_in_tank: float = 0

    def get_current_fuel_level(self) -> float:
        return self._fuel_in_tank

    def refuel_car(self, fuel_quantity: float):
        if self._max_fuel_capacity - self._fuel_in_tank < fuel_quantity:
            error_message = "Вы пытаетесь залить слишком много бензина!"
            raise RefuelError(error_message)
        self._fuel_in_tank += fuel_quantity

    def drive(self, distance_km: float):
        # Считаем, что расход 8 литров на 100 км
        fuel_burned = 8 * (distance_km / 100)
        if self._fuel_in_tank < fuel_burned:
            error_message = "Не доедем жеж..."
            raise InsufficientFuelError(error_message)
        self._fuel_in_tank -= fuel_burned
        return self.get_current_fuel_level()
