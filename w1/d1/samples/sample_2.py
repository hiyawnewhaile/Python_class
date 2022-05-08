#sample function
#accept a list of integers as its input
#output a new list consisting of any positive integers

#sample input: [1,-3,9,-2,7]
def sample_function_name(input_list):
    output_list = []
    
    for i in range(0, len(input_list)):
        if input_list[i] >= 0:
            output_list.append(input_list[i])


    return output_list


print(sample_function_nam([1,-3,9,-2,7]))