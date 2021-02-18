
import valid


def get_class_widths():
    class_width_prompt = 'What is the width of the classes?: '
    number_of_classes_prompt = 'How many classes are there?: '
    starting_class_prompt = 'What is the very first lower class boundary?: '

    class_width = valid.get_int_selection(class_width_prompt)
    if class_width == False:
        return False

    number_of_classes = valid.get_int_selection(number_of_classes_prompt)
    if number_of_classes == False:
        return False

    starting_class_value = valid.get_int_selection(starting_class_prompt)
    if starting_class_value == False:
        return False

    class_list = []

    for x in range(number_of_classes):
        class_list.append(starting_class_value + (class_width / 2))
        starting_class_value = starting_class_value + class_width + 1

    
    return class_list


def get_values(class_list):
    value_list = []
    value_num = len(class_list)
    counter = 0
    print('Type in the frequency values below. You will be '
    ,'prompted {} times for your {} classes.'.format(value_num, value_num))
    for counter in range(value_num):
        user_input = valid.get_float_selection('What is the frequency for class {}?: '.format(counter +1))
        if user_input != False:
            value_list.append(user_input)
        
        else:
            return False
            
    return value_list


def get_estimated_xbar(value_list, class_list):
    multi_list = []
    for x in range(len(value_list)):
        multi_list.append(value_list[x] * class_list[x])

    multi_list_sum = sum(multi_list)
    frequency_sum = sum(value_list)
    return multi_list_sum / frequency_sum


def main_loop():

    while True:
        class_widths = get_class_widths()
        if class_widths == False:
            break
        values = get_values(class_widths)
        if values == False:
            break
        xbar = get_estimated_xbar(values, class_widths)
        print('----------------------------------------------------')
        print('Your Values: ')
        print(*values, ', ')
        print('Your class midpoint values:')
        print(*class_widths, ', ')
        print('Your estimated xbar is : ' + str(xbar))
        print('----------------------------------------------------')


