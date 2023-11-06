def cumulative_sum(input_list):
    if not input_list:
        return []

    cumulative_result = [input_list[0]]

    for i in range(1, len(input_list)):
        if isinstance(input_list[i], (int, float)):
            cumulative_result.append(cumulative_result[i - 1] + input_list[i])
        elif isinstance(input_list[i], str):
            cumulative_result.append(cumulative_result[i - 1] + " " + input_list[i])

    return cumulative_result


# Voorbeelden van het gebruik van de functie met zowel getallen als strings:
num_list = [1, 2, 3, 4, 5]
str_list = ["a", "b", "c", "d", "e"]

result_num = cumulative_sum(num_list)
result_str = cumulative_sum(str_list)

print("Cumulatieve som van getallen:", result_num)
print("Cumulatieve som van strings:", result_str)

