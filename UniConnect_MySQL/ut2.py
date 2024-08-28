def validate_param_format(input_str):
    # Split the string into two parts using the '=' delimiter
    parts = input_str.split('=')

    # Check if there are exactly two parts and neither part is empty
    if len(parts) == 2 and parts[0] and parts[1]:
        name = parts[0]
        value = f"{parts[1]}"
        return name, value
    else:
        raise ValueError("Input must be in the format 'name=value'")


def parse_param(line_arg):
    args = line_arg.split()
    param_dict = {}
    for param in args:
        if '=' not in param:
            continue  # skip if there's no '=' in parameter
        name, value = param.split('=', 1)

        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]  # Remove the surrounding quotes
            value = value.replace('\\"', '"')  # Replace escaped quotes
            value = value.replace('_', ' ')  # Replace underscores with spaces
        elif '.' in value and value.replace('.', '', 1).isdigit():
            # Float case: check if it is a valid float
            try:
                value = float(value)
            except ValueError:
                continue  # Skip if not a valid float
        elif value.isdigit():
            # Integer case
            value = int(value)
        else:
            continue  # Skip if it doesn't match any valid pattern

        param_dict[name] = value

    return param_dict


def create_object_with_param(args):
    arg = args.split()
    class_name = args[0]
    attributes = parse_param(args)
    # new_object = create_object(class_name)
    # if
    for name, value in attributes.items():
