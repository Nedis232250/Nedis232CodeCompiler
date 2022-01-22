import os

variables = []
functions = []


def run_code_std():
    code_value = input("Nedis232Scriptt 1.0 > ")

    split_code = code_value.split(":")
    function_split_code = code_value.split(";")

    if split_code[0] == "print":
        print(split_code[1])
    elif split_code[0] == "input":
        input_val = input(split_code[1] + " ")

        input_string = split_code[2] + ":" + input_val

        variables.append(input_string)
        print(variables)
    elif split_code[0] == "template_print":
        var_names = []
        var_values = []
        var_len = len(variables)
        template_string = ""

        for i in range(len(variables)):
            template_split_code = split_code[1].split("$")
            var_split = variables[i].split(":")
            var_name_str = "{" + var_split[0] + "}"
            var_names.append(var_name_str)
            var_values.append(var_split[1])

            for j in range(len(template_split_code)):
                if template_split_code[j] == var_names[i]:
                    template_split_code[j] = var_values[i]

                template_string += template_split_code[j]

        if len(template_split_code) <= 2:
            print(template_string)
    elif code_value == "clear:":
        command = "clear"
        if os.name in ("nt", "dos"):
            command = "cls"
        os.system(command)
    elif split_code[0] == "var":
        var_string = split_code[1] + ":" + split_code[2]
        variables.append(var_string)
    elif split_code[0] == "def_var":
        extract_var = ""
        var_string = ""
        for i in range(len(variables)):
            extract_var = variables[i].split(":")
            if extract_var[0] == split_code[1]:
                variables.pop(i)
                var_string += split_code[1] + ":" + split_code[2]
                variables.append(var_string)

        print(variables)
    elif split_code[0] == "num":
        print(eval(split_code[1]))
    elif code_value == "run:":
        pass
