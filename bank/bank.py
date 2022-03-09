from datetime import date, datetime, timedelta


def rupiah_format(number: int, decimal=2) -> str:
    rupiah = "{:,}".format(number)
    rupiah = rupiah.replace(",", ".")
    return f"Rp. {rupiah}"


class Bank:
    def __init__(self, name: str, address: str, code: str, contact_email: str) -> None:
        self.name = name
        self.address = address
        self.code = code
        self.contact_email = contact_email

    def __str__(self) -> str:
        return "+=========Bank Detail=========+\nName\t\t: {}\nAddress\t\t: {}\nBank Code\t: {}\nContact Email\t: {}".format(
            self.name, self.address, self.code, self.contact_email
        )


class Account:
    def __init__(
        self,
        name: str,
        date_birth: date,
        bank,
        date_created: datetime,
        transaction_list: list,
    ) -> None:
        self.name = name
        self.date_birth = date_birth
        self.bank = bank
        self.date_created = date_created
        self.transaction_list = transaction_list

    def __str__(self) -> str:
        return "+=======Account Details=======+\nName\t\t: {}\nDate of Birth\t: {}\nDate Created\t: {}".format(
            self.name,
            self.date_birth.strftime("%d/%m/%Y"),
            self.date_created.strftime("%d/%m/%y at %H:%M"),
        )

    def history_transaction(self) -> str:
        history = "+====Transaction History======+\n"
        for transaction in self.transaction_list:
            history += str(transaction) + "\n"
        history += "+=============================+\n"
        history += "Total balance\t: " + str(self.calculate_balance())
        return history

    def calculate_balance(self) -> str:
        total_balance = 0
        for transaction in self.transaction_list:
            if transaction.is_debit:
                total_balance += transaction.total
            else:
                total_balance -= transaction.total
        return rupiah_format(total_balance)


class Transaction:
    def __init__(self, is_debit: bool, total: int, date_created: datetime) -> None:
        self.is_debit = is_debit
        self.total = total
        self.date_created = date_created

    def __str__(self) -> str:
        if self.is_debit:
            return (
                "+ "
                + rupiah_format(self.total)
                + "\t"
                + self.date_created.strftime("%d/%m/%y at %H:%M")
            )
        return (
            "- "
            + rupiah_format(self.total)
            + "\t"
            + self.date_created.strftime("%d/%m/%y at %H:%M")
        )


# Input Data
bca_bank = Bank(
    "Bank Central Asia", "Jl. M.H Thamrin No. 1", "014", "contact@bca.co.id"
)
list_transaction = [
    Transaction(True, 200000, datetime.now() - timedelta(50)),
    Transaction(True, 30000, datetime.now() - timedelta(49)),
    Transaction(False, 10000, datetime.now() - timedelta(48)),
    Transaction(True, 90000, datetime.now() - timedelta(48)),
    Transaction(True, 12000, datetime.now() - timedelta(55)),
    Transaction(False, 19000, datetime.now() - timedelta(66)),
]

basori_account = Account(
    "Akbar Basori", datetime(1992, 8, 2), bca_bank, datetime.now(), list_transaction
)

# Print result
print(basori_account)
print(basori_account.bank)
print(basori_account.history_transaction())
