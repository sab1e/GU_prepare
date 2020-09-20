CREATE_TABLE = {
    'categories': """
        CREATE TABLE IF NOT EXISTS categories (
        category_name TEXT PRIMARY KEY NOT NULL,
        category_description TEXT NOT NULL
        );""",
    'units': """
        CREATE TABLE IF NOT EXISTS units (
        unit TEXT PRIMARY KEY NOT NULL
        );""",
    'positions': """
        CREATE TABLE IF NOT EXISTS positions (
        position TEXT PRIMARY KEY NOT NULL
        );""",
    'goods': """
        CREATE TABLE IF NOT EXISTS goods (
        good_id INTEGER PRIMARY KEY NOT NULL,
        good_name TEXT NOT NULL,
        good_unit TEXT,
        good_cat TEXT,
        FOREIGN KEY (good_unit) REFERENCES units(unit),
        FOREIGN KEY (good_cat) REFERENCES categories(category_name)
        );""",
    'employees': """
        CREATE TABLE IF NOT EXISTS employees (
        employee_id INTEGER PRIMARY KEY NOT NULL,
        employee_fio TEXT NOT NULL,
        employee_position TEXT, 
        FOREIGN KEY (employee_position) REFERENCES positions(position)
        )""",
    'vendors': """
        CREATE TABLE IF NOT EXISTS vendors(
        vendor_id INTEGER PRIMARY KEY NOT NULL,
        vendor_name TEXT NOT NULL,
        vendor_ownerchipform TEXT NOT NULL,
        vendor_address TEXT NOT NULL,
        vendor_phone TEXT NOT NULL,
        vendor_email TEXT NOT NULL
        )""",
}
