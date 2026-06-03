"""Input validation utilities"""

def validate_numeric(value, field_name, min_val=0, max_val=None):
    """Validate numeric input"""
    try:
        num = float(value)
        if num < min_val:
            return None, f"{field_name} must be >= {min_val}"
        if max_val is not None and num > max_val:
            return None, f"{field_name} must be <= {max_val}"
        return num, None
    except ValueError:
        return None, f"{field_name} must be a valid number"

def validate_binary(value, field_name):
    """Validate binary (0/1) input"""
    try:
        num = float(value)
        if num not in [0, 1]:
            return None, f"{field_name} must be 0 or 1"
        return num, None
    except ValueError:
        return None, f"{field_name} must be 0 or 1"

def validate_range(value, field_name, min_val, max_val):
    """Validate value within range"""
    try:
        num = float(value)
        if num < min_val or num > max_val:
            return None, f"{field_name} must be between {min_val} and {max_val}"
        return num, None
    except ValueError:
        return None, f"{field_name} must be a valid number"
