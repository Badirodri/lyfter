import PySimpleGUI as sg
from models import FinanceManager
from user_interface import show_category_window, show_expense_window, show_income_window

def show_main_window():
    finance_manager = FinanceManager()
    finance_manager.table_data = sg.user_settings_get_entry('my_table', [])
    layout = [
        [sg.Table(finance_manager.table_data, finance_manager.headings, key='table_data')],
        [sg.Button("Add Category")],
        [sg.Text("Please add a new category before continue")],
        [sg.Text("")],
        [sg.Button("Add Income"), sg.Button("Add Expense"), sg.Exit()],
    ]

    window = sg.Window("Financial Management", layout)
    main_win = True
    while main_win:
        sg.user_settings_set_entry('my_table', finance_manager.table_data)
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            main_win = False
        elif event == "Add Category":
            show_category_window(finance_manager)
        elif event == "Add Income":
            input_category = sg.user_settings_get_entry('category_list', None)
            if not input_category:
                sg.popup("Please add a new category first.")
                show_category_window(finance_manager)
            else:
                new_data = show_income_window(finance_manager, input_category)
                if new_data:
                    finance_manager.table_data.append(new_data)
                    window['table_data'].update(values=finance_manager.table_data)
        elif event == "Add Expense":
            input_category = sg.user_settings_get_entry('category_list', None)
            if not input_category:
                sg.popup("Please add a new category first.")
                show_category_window(finance_manager)
            else:
                new_data = show_expense_window(finance_manager, input_category)
                if new_data:
                    finance_manager.table_data.append(new_data)
                    window['table_data'].update(values=finance_manager.table_data)

    window.close()

if __name__ == "__main__":
    show_main_window()