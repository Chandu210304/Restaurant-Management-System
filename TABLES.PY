class Table:
    def __init__(self, table_id, status='Available'):
        self.__table_id = table_id
        self.__status = status

    def reserve(self):
        if self.__status == 'Available':
            self.__status = 'Reserved'
            print(f"Table {self.__table_id} reserved.")
        else:
            print(f"Table {self.__table_id} is already reserved.")

class TableManager:
    def __init__(self):
        self.tables = [Table(i) for i in range(1, 6)]  # 5 tables initially

    def manage_tables(self):
        for table in self.tables:
            print(f"Table {table._Table__table_id} is {table._Table__status}")
        
        table_id = int(input("Enter table id to reserve: "))
        if 1 <= table_id <= len(self.tables):
            self.tables[table_id - 1].reserve()
        else:
            print("Invalid table id.")
