def convert_to_json(data):
    result = []

    for row in data[1:]:
        json_object = {}
        for (index, column_name) in enumerate(data[0]):
            json_object[column_name] = row[index]
        result.append(json_object)
    return result
