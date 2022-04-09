class Validator:
    @staticmethod
    def is_body_valid(body, required_fields):
        def is_none(value):
            return value is None

        def body_contains(value):
            return value in body

        are_field_values_none = map(is_none, body.values())
        contains_required_field = map(body_contains, required_fields)

        values_contains_none = any(are_field_values_none)
        are_fields_valid = all(contains_required_field)

        return are_fields_valid and not values_contains_none
