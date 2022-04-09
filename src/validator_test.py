from src.validator import Validator


class TestValidator:
    @staticmethod
    def test_should_fail_on_value_none():
        body = {"field": None}
        required_fields = ["field"]
        isValid = Validator.is_body_valid(body, required_fields)
        assert not isValid

    @staticmethod
    def test_should_fail_on_missing_required_field():
        body = {"field": "value"}
        required_fields = ["required_field"]
        isValid = Validator.is_body_valid(body, required_fields)
        assert not isValid

    @staticmethod
    def test_should_fail_on_missing_required_field_and_value_none():
        body = {"field": None}
        required_fields = ["required_field"]
        isValid = Validator.is_body_valid(body, required_fields)
        assert not isValid

    @staticmethod
    def test_should_suceed_on_all_fields_present_and_no_none_value():
        body = {"field": "test", "required_field": "123"}
        required_fields = ["required_field", "field"]
        isValid = Validator.is_body_valid(body, required_fields)
        assert isValid
