class Calculator:
    calculation_type = 'Arithmetic Operations'

    @staticmethod
    def add(a, b):

        """Retuns the sum of two numbers"""
        return a + b
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
