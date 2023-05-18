class Store:
    def __init__(self, shop_name, vendor_name, vendor_kind):
        self.__shop_name = shop_name
        self.__vendor_name = vendor_name
        self.__vendor_kind = vendor_kind
        self.__sales_dict = {}
        self.__vendor_sales_dict = {}

    def get_shop_name(self):
        return self.__shop_name

    def set_shop_name(self, shop_name):
        self.__shop_name = shop_name

    def get_vendor_name(self):
        return self.__vendor_name

    def set_vendor_name(self, vendor_name):
        self.__vendor_name = vendor_name

    def get_vendor_kind(self):
        return self.__vendor_kind

    def set_vendor_kind(self, vendor_kind):
        self.__vendor_kind = vendor_kind

    def store_sales_amount(self):
        total_sales = sum(self.__sales_dict.values())
        return total_sales

    def vendor_sales_amount(self, vendor_name, vendor_kind):
        key = (vendor_name, vendor_kind)
        if key in self.__sales_dict:
            return self.__sales_dict[key]
        else:
            return 0

    def add_sale(self, vendor_name, vendor_kind, amount):
        key = (vendor_name, vendor_kind)
        if key in self.__sales_dict:
            self.__sales_dict[key] += amount
        else:
            self.__sales_dict[key] = amount
        if vendor_name in self.__vendor_sales_dict:
            self.__vendor_sales_dict[vendor_name] += amount
        else:
            self.__vendor_sales_dict[vendor_name] = amount

    def __str__(self):
        output = f"Total sales for {self.get_shop_name()}: {self.store_sales_amount()}\n"
        output += "Sales by vendor:\n"
        for vendor_name, amount in self.__vendor_sales_dict.items():
            output += f"{vendor_name} - {amount}\n"
        return output


stores_dict = {}

while True:
    shop_name = input("Enter store name (or type 'exit' to quit): ")
    if shop_name.lower() == 'exit':
        break
    vendor_name = input("Enter vendor name: ")
    vendor_kind = input("Enter vendor kind (tv, computer, white_goods, other): ")
    sales_amount = float(input("Enter sales amount: "))

    if shop_name in stores_dict:
        stores_dict[shop_name].add_sale(vendor_name, vendor_kind, sales_amount)
    else:
        store = Store(shop_name, vendor_name, vendor_kind)
        store.add_sale(vendor_name, vendor_kind, sales_amount)
        stores_dict[shop_name] = store

for store in stores_dict.values():
    print(store)
