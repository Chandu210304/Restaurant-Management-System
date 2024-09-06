class Staff:
    def __init__(self, staff_id, name, position):
        self.__staff_id = staff_id
        self.__name = name
        self.__position = position

    def promote(self):
        self.__position = "Manager"
        print(f"{self.__name} promoted to {self.__position}.")

class StaffManager:
    def __init__(self):
        self.staff_list = [
            Staff(1, 'John Doe', 'Waiter'),
            Staff(2, 'Jane Smith', 'Chef')
        ]

    def manage_staff(self):
        for staff in self.staff_list:
            print(f"{staff._Staff__name} - {staff._Staff__position}")
        
        promote_staff_id = int(input("Enter staff id to promote: "))
        if 1 <= promote_staff_id <= len(self.staff_list):
            self.staff_list[promote_staff_id - 1].promote()
        else:
            print("Invalid staff id.")
