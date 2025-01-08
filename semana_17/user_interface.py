import PySimpleGUI as sg

def show_category_window(finance_manager):
    category_win = True
    layout = [
        [sg.Text("Please add a new category name:")],
        [sg.Input(key=finance_manager.headings[1])],
        [sg.Button("Add")],
    ]
    window = sg.Window("Category", layout)
    my_categories = sg.user_settings_get_entry('category_list', [])

    while category_win:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            category_win = False
        elif event == "Add":
            new_category = values[finance_manager.headings[1]]
            if new_category not in my_categories:
                my_categories.append(new_category)
                sg.user_settings_set_entry('category_list', my_categories)
                sg.popup('Category saved')
            else:
                sg.popup('Category already exists')
            window.close()
            return my_categories
    window.close()

def show_income_window(finance_manager, input_category):
    income_win = True
    if not finance_manager.validate_category(input_category):
        return None

    layout = [
        [sg.Text("Income Name")],
        [sg.Input(key=finance_manager.headings[0])],
        [sg.Text("Income Category")],
        [sg.Input(key=finance_manager.headings[1])],
        [sg.Text("Income Amount")],
        [sg.Input(key=finance_manager.headings[3])],
        [sg.Button("Add")],
    ]

    window = sg.Window("Income", layout)

    while income_win:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            income_win = False
        elif event == "Add":
            existing_category = sg.user_settings_get_entry('category_list', None)
            new_category = values[finance_manager.headings[1]]
            if new_category not in existing_category:
                sg.popup("Error: Please enter an existing category.")
                continue
            else:
                window.close()
                new_entry = [values[finance_manager.headings[0]], values[finance_manager.headings[1]], "In", values[finance_manager.headings[3]]]
            return new_entry


def show_expense_window(finance_manager, input_category):
    expense_win = True
    if not finance_manager.validate_category(input_category):
        return None

    layout = [
        [sg.Text("Expense Name")],
        [sg.Input(key=finance_manager.headings[0])],
        [sg.Text("Expense Category")],
        [sg.Input(key=finance_manager.headings[1])],
        [sg.Text("Expense Amount")],
        [sg.Input(key=finance_manager.headings[3])],
        [sg.Button("Add")],
    ]

    window = sg.Window("Expense", layout)


    while expense_win:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            expense_win = False
        elif event == "Add":

            existing_category = sg.user_settings_get_entry('category_list', None)
            new_category = values[finance_manager.headings[1]]
            if new_category not in existing_category:
                sg.popup("Error: Please enter an existing category.")
                continue
            else:
                window.close()
                new_entry = [values[finance_manager.headings[0]], values[finance_manager.headings[1]], "Out", values[finance_manager.headings[3]]]
            return new_entry
