# version 0.012_v (April_21st_2022)

import csv
import time


class Audit:
    def __init__(self):
        self.bank_record = None
        self.manual_record = None
        self.p = ""
        self.description = ""
        pass

    def run_engine(self, bank_file, manual_file):
        print("Initializing Engine...0%")
        self.description += "Initializing Engine...0%\n"
        csvReader1 = csv.reader(bank_file)
        csvReader2 = csv.reader(manual_file)
        self.bank_record = []
        self.manual_record = []
        time.sleep(1)
        # Bank Record
        for row in csvReader1:
            self.bank_record.append(row)
        # Manual Record
        for vow in csvReader2:
            self.manual_record.append(vow)

        # Bank Record
        d, k = self.checker(self.bank_record)
        if d == "valid":
            print("Bank required Columns are provided")
            print("Successful...10%")
            self.description += "Bank required Columns are provided\n"
            self.description += "Successful...10%\n"
            pass
        else:
            print("Error from Bank Record__")
            print("program Terminated....")
            self.description += "Error from Bank Record__\n"
            self.description += "program Terminated....\n"
            return self.description
        # manual Record
        d, k = self.checker(self.manual_record)
        if d == "valid":
            print("Manual Booking required Columns are provided")
            print("Successful...16%")
            self.description += "Manual Booking required Columns are provided\n"
            self.description += "Successful...16%\n"
        else:
            print("Error from Manual Record__")
            print("program Terminated....")
            self.description += "Error from Manual Record__\n"
            self.description += "program Terminated....\n"
            return self.description
        time.sleep(1)
        # Bank Record Indexes
        bank_record_index = self.get_id_index(self.bank_record)
        # manual Record Indexes
        manual_record_index = self.get_id_index(self.manual_record)

        # Bank Record Range check
        d, idListB, debitListB, dateListB, creditListB, balanceListB, error = self.table_range(self.bank_record,
                                                                                               bank_record_index)
        if d:
            print("Error from Bank Record__")
            print(error)
            print("program Terminated....")
            self.description += "Error from Bank Record__\n"
            self.description += f"{error}\n"
            self.description += "program Terminated....\n"
            return self.description
        else:
            print("SUCCESS___the number of columns under each rows in Bank Record match")
            self.description += "SUCCESS___the number of columns under each rows in Bank Record match\n"
            pass
        time.sleep(1)
        # Manual Record Range check
        d, idListM, debitListM, dateListM, creditListM, balanceListM, error = self.table_range(self.manual_record,
                                                                                               manual_record_index)
        if d:
            print("Error from Manual Record__")
            print(error)
            print("program Terminated....")
            self.description += "Error from Manual Record__\n"
            self.description += f"{error}\n"
            self.description += "program Terminated....\n"

            return self.description
        else:
            print("SUCCESS___the number of columns under each rows in Manual Record match")
            self.description += "SUCCESS___the number of columns under each rows in Manual Record match\n"
            pass
        time.sleep(1)
        # Bank Record's Value Checker
        d, list_of_errors = self.values_validator(self.bank_record, bank_record_index)
        if d:
            print("Error from Bank Record__")
            print("We've found one or more data mismatch in places where string value was provide instead of a digit value.")
            print(list_of_errors)
            print("program Terminated....")
            self.description += "Error from Bank Record__"
            self.description += "We've found one or more data mismatch in places where string value was provide instead of a digit value.\n"
            self.description += f"{list_of_errors}\n"
            self.description += "program Terminated....\n"
            return self.description
        else:
            print('no value mismatch found in Bank statement.__success')
            self.description += "no value mismatch found in Bank statement.__success\n"
            pass
        time.sleep(1)
        # Manual Record's Value Checker
        d, list_of_errors = self.values_validator(self.manual_record, manual_record_index)
        if d:
            print("Error from Manual Record__")
            print("We've found one or more data mismatch in places where string value was provide instead of a digit value.")
            print(list_of_errors)
            print("program Terminated....")
            self.description += "Error from Manual Record__\n"
            self.description += "We've found one or more data mismatch in places where string value was provide instead of a digit value.\n"
            self.description += f"{list_of_errors}\n"
            self.description += "program Terminated....\n"

            return self.description
        else:
            print('no value mismatch found in Manual Book keeping.__success')
            self.description += "no value mismatch found in Manual Book keeping.__success\n"
            pass
        time.sleep(1)
        # Bank Record Range check
        d, idListB, debitListB, dateListB, creditListB, balanceListB, error = self.table_range(self.bank_record,
                                                                                               bank_record_index)
        if d:
            print("Error from Bank Record__")
            print(error)
            print("program Terminated....")
            self.description += "Error from Bank Record__\n"
            self.description += f"{error}\n"
            self.description += "program Terminated....\n"
            return self.description
        else:
            print("SUCCESS___the number of columns under each rows in Bank Record match")
            self.description += "SUCCESS___the number of columns under each rows in Bank Record match\n"
            pass
        time.sleep(1)
        # Manual Record Range check
        d, idListM, debitListM, dateListM, creditListM, balanceListM, error = self.table_range(self.manual_record,
                                                                                               manual_record_index)
        if d:
            print("Error from Manual Record__")
            print(error)
            print("program Terminated....")
            self.description += "Error from Manual Record__\n"
            self.description += f"{error}\n"
            self.description += "program Terminated....\n"
            return self.description
        else:
            print("SUCCESS___the number of columns under each rows in Manual Record match")
            self.description += "SUCCESS___the number of columns under each rows in Manual Record match\n"
        time.sleep(3)
        # duo range checker
        if len(idListM) != len(idListB):
            print('The number Of rows in both record are not equal to each other. There is or there are missing rows in one of the dataset')
            print(f'Height of Bank Record: {len(idListB)} rows')
            print(f'Height of Manual Record: {len(idListB)} rows')
            print("The Auditing Engine would continue with it's instantiation of events to give you a full detailed report of where the origin of the data mismatch began")
            self.description += "The number Of rows in both record are not equal to each other. There is or there are missing rows in one of the dataset\n"

            self.description += f"Height of Manual Record: {len(idListB)} rows\n"
            self.description += "The Auditing Engine would continue with it's instantiation of events to give you a full detailed report of where the origin of the data mismatch began\n"
            if len(idListM) > len(idListB):
                print("Since manual book keeping record is greater than the range of the Bank Statement, please note that extra copies of illegitimate transactions has been added to the Manual ledger by the accounting personnel")
                self.description += "Since manual book keeping record is greater than the range of the Bank Statement, please note that extra copies of illegitimate transactions has been added to the Manual ledger by the accounting personnel\n"
            else:
                print("Since manual book keeping record is less than the range of the actual Bank Statement, please note that extra copies of legitimate transactions has been omitted from the Manual ledger by the accounting personnel")
                self.description += "Since manual book keeping record is less than the range of the actual Bank Statement, please note that extra copies of legitimate transactions has been omitted from the Manual ledger by the accounting personnel \n"
        else:
            print("SUCCESS___the number of rows under both Bank Record and Manual Book Keeping. DataSET prove testing completed. \n Auditing In process...20%(System would go ahead to check for financial frauds. Stay tuned(-*-)")
            self.description += "SUCCESS___the number of rows under both Bank Record and Manual Book Keeping. DataSET prove testing completed. \n Auditing In process...20%(System would go ahead to check for financial frauds. Stay tuned(-*-) \n"
        # Bank Trial Balancing
        d, error = self.trial_balancer(self.bank_record, bank_record_index)
        if d:
            print("Error from Bank Record__")
            print(error)
            self.description += "Error from Bank Record__\n"
            self.description += f"{error}\n"
        else:
            print("Auditing In Process...35%")
            self.description += "Auditing In Process...35%\n"
        time.sleep(2)
        # Manual Trial Balancing
        d, error = self.trial_balancer(self.manual_record, manual_record_index)
        if d:
            print("Error from Manual Record__")
            print(error)
            self.description += "Error from Manual Record__\n"
            self.description += f"{error}\n"

        else:
            print("Auditing In Process...40%")
            self.description += "Auditing In Process...40%\n"
        time.sleep(1)
        # Bank Record Total Balance
        bankTotalBalance = 0
        TotalCredit = 0
        TotalDebit = 0
        for x in range(len(creditListB)):
            if x > 0:
                TotalCredit += float(creditListB[x])

        for x in range(len(debitListB)):
            if x > 0:
                TotalDebit += float(debitListB[x])

        for x in range(len(balanceListB)):
            if x > 0:
                bankTotalBalance += float(balanceListB[x])
        time.sleep(1)
        # Manual Record Total Balance
        manualTotalBalance = 0
        for x in range(len(balanceListM)):
            if x > 0:
                manualTotalBalance += float(balanceListM[x])

        if manualTotalBalance == bankTotalBalance:
            print(f"Total Bank Balance: {bankTotalBalance}")
            print(f"Total Manual Booking Balance: {manualTotalBalance}")
            print(f"Total Deposit: {TotalCredit}")
            print(f"Total Expenses: {TotalDebit}")
            print('(0) errors found at this instance.')
            self.description += f"Total Bank Balance: {bankTotalBalance}\n"
            self.description += f"Total Manual Booking Balance: {manualTotalBalance}\n"
            self.description += f"Total Deposit: {TotalCredit}\n"
            self.description += f"Total Expenses: {TotalDebit}\n"
            self.description += f"(0) errors found at this instance.\n"
        else:
            print(f"Total Bank Balance: {bankTotalBalance}")
            print(f"Total Manual Booking Balance: {manualTotalBalance}")
            print(f"Total Deposit: {TotalCredit}")
            print(f"Total Expenses: {TotalDebit}")
            print("___!!!Invalid Balance. There have been a fraudulent misappropriation of finances from the manual book keeping. The Bank balance and the ledger balance do not correlate. Check the further information listed below for a more detailed tracking!!!")
            self.description += f"Total Bank Balance: {bankTotalBalance}\n"
            self.description += f"Total Manual Booking Balance: {manualTotalBalance}\n"
            self.description += f"Total Deposit: {TotalCredit}\n"
            self.description += f"Total Expenses: {TotalDebit}\n"
            self.description += f"___!!!Invalid Balance. There have been a fraudulent misappropriation of finances from the manual book keeping. The Bank balance and the ledger balance do not correlate. Check the further information listed below for a more detailed tracking!!!\n"

        time.sleep(1)
        # ID Errors
        idErrors = []
        pen = False
        for xRow in range(len(idListB)):
            row = xRow
            bankInstance = None
            manualInstance = None
            try:
                bankInstance = idListB[row]
                manualInstance = idListM[row]
            except:
                print(f"Coordinates {row + 1}:{manual_record_index['id']} under manual is not available")
                self.description += f"Coordinates {row + 1}:{manual_record_index['id']} under manual is not available"
                break

            if str(bankInstance).lower() != str(manualInstance).lower():
                pen = True
                idErrors.append(f"Error on row {row}: column{manual_record_index['id']}")
            else:
                pass
        if pen is True:
            print(f"\n List of Errors Under Id: {len(idErrors)} errors.(type: data mismatch)")
            print(idErrors)
            print("Error is as a result in both bank statement and manual ledger value not bring proportional to each other")
            self.description += f"\n List of Errors Under Id: {len(idErrors)} errors.(type: data mismatch)\n"
            self.description += f"\n{idErrors}"
            self.description += f"\nError is as a result in both bank statement and manual ledger value not bring proportional to each other"
        else:
            print('No errors found under the id columns...55%')
            self.description += f"No errors found under the id columns...55%\n"

        time.sleep(1)
        # Date Errors
        pen = False
        dateErrors = []
        for xRow in range(len(dateListB)):
            row = xRow
            bankInstance = None
            manualInstance = None
            try:
                bankInstance = dateListB[row]
                manualInstance = dateListM[row]
            except:
                print(f"Coordinates {row + 1}:{manual_record_index['date']} under manual is not available")
                self.description += f"Coordinates {row + 1}:{manual_record_index['date']} under manual is not available"
                break

            if str(bankInstance).lower() != str(manualInstance).lower():
                dateErrors.append(f"Error on row {row + 1}: column {manual_record_index['date']}(type: data mismatch)")
                pen = True
            else:
                pass
        if pen is True:
            print(f"List of Errors Under Date: {len(dateErrors)} errors.")
            print(dateErrors)
            print("Error is as a result in both bank statement and manual ledger value not bring proportional to each other")
            self.description += f"List of Errors Under Date: {len(dateErrors)} errors.\n"
            self.description += f"{dateErrors}\n"
            self.description += "Error is as a result in both bank statement and manual ledger value not bring proportional to each other\n"

        else:
            print("No Errors found in date column...67.65%")
            self.description += f"No Errors found in date column...67.65%\n"

        time.sleep(1)
        # Credit or Deposit Errors
        pen = False
        creditErrors = []
        for xRow in range(len(creditListB)):
            row = xRow
            bankInstance = None
            manualInstance = None
            try:
                if row > 0:
                    bankInstance = creditListB[row]
                    manualInstance = creditListM[row]
            except:
                print(f"Coordinates {row + 1}:{manual_record_index['credit']} under manual is not available")
                self.description += f"Coordinates {row + 1}:{manual_record_index['credit']} under manual is not available\n"
                break
            if bankInstance != manualInstance:
                pen = True
                creditErrors.append(f"Error on row {row}: column{manual_record_index['credit']}")
            else:
                pass
        if pen is True:
            print(f"\n List of Errors Under Credit: {len(creditErrors)} errors.(type: data mismatch)")
            print(creditErrors)
            print("Error is as a result in both bank statement and manual ledger value not bring proportional to each other")
            self.description += f"\n List of Errors Under Credit: {len(creditErrors)} errors.(type: data mismatch)\n"
            self.description += f"{creditErrors}\n"
            self.description += f"Error is as a result in both bank statement and manual ledger value not bring proportional to each other\n"

        else:
            print('No errors found under Credit...78.9%')
            self.description += f"No errors found under Credit...78.9%\n"

        time.sleep(1)
        # debit or expenses error
        pen = False
        debitErrors = []
        for xRow in range(len(debitListB)):
            row = xRow
            bankInstance = None
            manualInstance = None
            try:
                if row > 0:
                    bankInstance = debitListB[row]
                    manualInstance = debitListM[row]
            except:
                print(f"Coordinates {row + 1}:{manual_record_index['debit']} under manual is not available")
                self.description += f"Coordinates {row + 1}:{manual_record_index['debit']} under manual is not available\n"
                break
            if bankInstance != manualInstance:
                pen = True
                debitErrors.append(f"Error on row {row}: column {manual_record_index['debit']}")

            else:
                pass
        if pen is True:
            print(f"\n List of Errors Under Debit: {len(debitErrors)} errors.")
            print(debitErrors)
            print("Error is as a result in both bank statement and manual ledger value not bring proportional to each other")
            self.description += f"\n List of Errors Under Debit: {len(debitErrors)} errors.\n"
            self.description += f"{debitErrors}\n"
            self.description += f"Error is as a result in both bank statement and manual ledger value not bring proportional to each other\n"

        else:
            print('no error found under debit column...85%')
            self.description += f"no error found under debit column...85%\n"

        time.sleep(1)
        # balances error
        balanceErrors = []
        pen = False
        for xRow in range(len(balanceListB)):
            row = xRow
            bankInstance = None
            manualInstance = None
            try:
                if row > 0:
                    bankInstance = balanceListB[row]
                    manualInstance = balanceListM[row]
            except:
                print(f"Coordinates {row + 1}:{manual_record_index['balance']} under manual is not available")
                self.description += f"Coordinates {row + 1}:{manual_record_index['balance']} under manual is not available\n"
                break

            if bankInstance != manualInstance:
                pen = True
                balanceErrors.append(f"Error on row {row}: column{manual_record_index['balance']}")
            else:
                pass

        if pen is True:
            print(f"\n List of Errors Under Balance: {len(balanceErrors)} errors.")
            print(balanceErrors)
            print("Error is as a result in both bank statement and manual ledger value not bring proportional to each other")
            self.description += f"\n List of Errors Under Balance: {len(balanceErrors)} errors.\n"
            self.description += f"{balanceErrors}\n"
            self.description += f"Error is as a result in both bank statement and manual ledger value not bring proportional to each other\n"
            return self.description
        else:
            print("No errors found under Balance...98.99")
            time.sleep(3)
            print("Evaluation Successfully Completed. (0) errors found...100%")
            self.description += f"No errors found under Balance...98.99\n"
            self.description += f"Evaluation Successfully Completed. (0) errors found...100%\n"
            return self.description

    def run_engine_address(self, bank_file_address, manual_file_address):
        try:
            bank_file = open(bank_file_address)
            manual_file = open(manual_file_address)

        except FileNotFoundError:
            self.description += f"Incorrect Address Provided. Recheck the address you provided.\n"
            self.description += f"program Terminated....\n"

            print("Incorrect Address Provided. Recheck the address you provided.")
            print("program Terminated....")

            return self.description

        print("Initializing Engine...0%")
        self.description += "Initializing Engine...0%\n"
        csvReader1 = csv.reader(bank_file)
        csvReader2 = csv.reader(manual_file)
        self.bank_record = []
        self.manual_record = []
        time.sleep(1)
        # Bank Record
        for row in csvReader1:
            self.bank_record.append(row)
        # Manual Record
        for vow in csvReader2:
            self.manual_record.append(vow)

        # Bank Record
        d, k = self.checker(self.bank_record)
        if d == "valid":
            print("Bank required Columns are provided")
            print("Successful...10%")
            self.description += "Bank required Columns are provided\n"
            self.description += "Successful...10%\n"
            pass
        else:
            print("Error from Bank Record__")
            print("program Terminated....")
            self.description += "Error from Bank Record__\n"
            self.description += "program Terminated....\n"
            return self.description
        # manual Record
        d, k = self.checker(self.manual_record)
        if d == "valid":
            print("Manual Booking required Columns are provided")
            print("Successful...16%")
            self.description += "Manual Booking required Columns are provided\n"
            self.description += "Successful...16%\n"
        else:
            print("Error from Manual Record__")
            print("program Terminated....")
            self.description += "Error from Manual Record__\n"
            self.description += "program Terminated....\n"
            return self.description
        time.sleep(1)
        # Bank Record Indexes
        bank_record_index = self.get_id_index(self.bank_record)
        # manual Record Indexes
        manual_record_index = self.get_id_index(self.manual_record)

        # Bank Record Range check
        d, idListB, debitListB, dateListB, creditListB, balanceListB, error = self.table_range(self.bank_record,
                                                                                               bank_record_index)
        if d:
            print("Error from Bank Record__")
            print(error)
            print("program Terminated....")
            self.description += "Error from Bank Record__\n"
            self.description += f"{error}\n"
            self.description += "program Terminated....\n"
            return self.description
        else:
            print("SUCCESS___the number of columns under each rows in Bank Record match")
            self.description += "SUCCESS___the number of columns under each rows in Bank Record match\n"
            pass
        time.sleep(1)
        # Manual Record Range check
        d, idListM, debitListM, dateListM, creditListM, balanceListM, error = self.table_range(self.manual_record,
                                                                                               manual_record_index)
        if d:
            print("Error from Manual Record__")
            print(error)
            print("program Terminated....")
            self.description += "Error from Manual Record__\n"
            self.description += f"{error}\n"
            self.description += "program Terminated....\n"

            return self.description
        else:
            print("SUCCESS___the number of columns under each rows in Manual Record match")
            self.description += "SUCCESS___the number of columns under each rows in Manual Record match\n"
            pass
        time.sleep(1)
        # Bank Record's Value Checker
        d, list_of_errors = self.values_validator(self.bank_record, bank_record_index)
        if d:
            print("Error from Bank Record__")
            print(
                "We've found one or more data mismatch in places where string value was provide instead of a digit value.")
            print(list_of_errors)
            print("program Terminated....")
            self.description += "Error from Bank Record__"
            self.description += "We've found one or more data mismatch in places where string value was provide instead of a digit value.\n"
            self.description += f"{list_of_errors}\n"
            self.description += "program Terminated....\n"
            return self.description
        else:
            print('no value mismatch found in Bank statement.__success')
            self.description += "no value mismatch found in Bank statement.__success\n"
            pass
        time.sleep(1)
        # Manual Record's Value Checker
        d, list_of_errors = self.values_validator(self.manual_record, manual_record_index)
        if d:
            print("Error from Manual Record__")
            print(
                "We've found one or more data mismatch in places where string value was provide instead of a digit value.")
            print(list_of_errors)
            print("program Terminated....")
            self.description += "Error from Manual Record__\n"
            self.description += "We've found one or more data mismatch in places where string value was provide instead of a digit value.\n"
            self.description += f"{list_of_errors}\n"
            self.description += "program Terminated....\n"

            return self.description
        else:
            print('no value mismatch found in Manual Book keeping.__success')
            self.description += "no value mismatch found in Manual Book keeping.__success\n"
            pass
        time.sleep(1)
        # Bank Record Range check
        d, idListB, debitListB, dateListB, creditListB, balanceListB, error = self.table_range(self.bank_record,
                                                                                               bank_record_index)
        if d:
            print("Error from Bank Record__")
            print(error)
            print("program Terminated....")
            self.description += "Error from Bank Record__\n"
            self.description += f"{error}\n"
            self.description += "program Terminated....\n"
            return self.description
        else:
            print("SUCCESS___the number of columns under each rows in Bank Record match")
            self.description += "SUCCESS___the number of columns under each rows in Bank Record match\n"
            pass
        time.sleep(1)
        # Manual Record Range check
        d, idListM, debitListM, dateListM, creditListM, balanceListM, error = self.table_range(self.manual_record,
                                                                                               manual_record_index)
        if d:
            print("Error from Manual Record__")
            print(error)
            print("program Terminated....")
            self.description += "Error from Manual Record__\n"
            self.description += f"{error}\n"
            self.description += "program Terminated....\n"
            return self.description
        else:
            print("SUCCESS___the number of columns under each rows in Manual Record match")
            self.description += "SUCCESS___the number of columns under each rows in Manual Record match\n"
        time.sleep(3)
        # duo range checker
        if len(idListM) != len(idListB):
            print(
                'The number Of rows in both record are not equal to each other. There is or there are missing rows in one of the dataset')
            print(f'Height of Bank Record: {len(idListB)} rows')
            print(f'Height of Manual Record: {len(idListB)} rows')
            print(
                "The Auditing Engine would continue with it's instantiation of events to give you a full detailed report of where the origin of the data mismatch began")
            self.description += "The number Of rows in both record are not equal to each other. There is or there are missing rows in one of the dataset\n"

            self.description += f"Height of Manual Record: {len(idListB)} rows\n"
            self.description += "The Auditing Engine would continue with it's instantiation of events to give you a full detailed report of where the origin of the data mismatch began\n"
            if len(idListM) > len(idListB):
                print(
                    "Since manual book keeping record is greater than the range of the Bank Statement, please note that extra copies of illegitimate transactions has been added to the Manual ledger by the accounting personnel")
                self.description += "Since manual book keeping record is greater than the range of the Bank Statement, please note that extra copies of illegitimate transactions has been added to the Manual ledger by the accounting personnel\n"
            else:
                print(
                    "Since manual book keeping record is less than the range of the actual Bank Statement, please note that extra copies of legitimate transactions has been omitted from the Manual ledger by the accounting personnel")
                self.description += "Since manual book keeping record is less than the range of the actual Bank Statement, please note that extra copies of legitimate transactions has been omitted from the Manual ledger by the accounting personnel \n"
        else:
            print(
                "SUCCESS___the number of rows under both Bank Record and Manual Book Keeping. DataSET prove testing completed. \n Auditing In process...20%(System would go ahead to check for financial frauds. Stay tuned(-*-)")
            self.description += "SUCCESS___the number of rows under both Bank Record and Manual Book Keeping. DataSET prove testing completed. \n Auditing In process...20%(System would go ahead to check for financial frauds. Stay tuned(-*-) \n"
        # Bank Trial Balancing
        d, error = self.trial_balancer(self.bank_record, bank_record_index)
        if d:
            print("Error from Bank Record__")
            print(error)
            self.description += "Error from Bank Record__\n"
            self.description += f"{error}\n"
        else:
            print("Auditing In Process...35%")
            self.description += "Auditing In Process...35%\n"
        time.sleep(2)
        # Manual Trial Balancing
        d, error = self.trial_balancer(self.manual_record, manual_record_index)
        if d:
            print("Error from Manual Record__")
            print(error)
            self.description += "Error from Manual Record__\n"
            self.description += f"{error}\n"

        else:
            print("Auditing In Process...40%")
            self.description += "Auditing In Process...40%\n"
        time.sleep(1)
        # Bank Record Total Balance
        bankTotalBalance = 0
        TotalCredit = 0
        TotalDebit = 0
        for x in range(len(creditListB)):
            if x > 0:
                TotalCredit += float(creditListB[x])

        for x in range(len(debitListB)):
            if x > 0:
                TotalDebit += float(debitListB[x])

        for x in range(len(balanceListB)):
            if x > 0:
                bankTotalBalance += float(balanceListB[x])
        time.sleep(1)
        # Manual Record Total Balance
        manualTotalBalance = 0
        for x in range(len(balanceListM)):
            if x > 0:
                manualTotalBalance += float(balanceListM[x])

        if manualTotalBalance == bankTotalBalance:
            print(f"Total Bank Balance: {bankTotalBalance}")
            print(f"Total Manual Booking Balance: {manualTotalBalance}")
            print(f"Total Deposit: {TotalCredit}")
            print(f"Total Expenses: {TotalDebit}")
            print('(0) errors found at this instance.')
            self.description += f"Total Bank Balance: {bankTotalBalance}\n"
            self.description += f"Total Manual Booking Balance: {manualTotalBalance}\n"
            self.description += f"Total Deposit: {TotalCredit}\n"
            self.description += f"Total Expenses: {TotalDebit}\n"
            self.description += f"(0) errors found at this instance.\n"
        else:
            print(f"Total Bank Balance: {bankTotalBalance}")
            print(f"Total Manual Booking Balance: {manualTotalBalance}")
            print(f"Total Deposit: {TotalCredit}")
            print(f"Total Expenses: {TotalDebit}")
            print(
                "___!!!Invalid Balance. There have been a fraudulent misappropriation of finances from the manual book keeping. The Bank balance and the ledger balance do not correlate. Check the further information listed below for a more detailed tracking!!!")
            self.description += f"Total Bank Balance: {bankTotalBalance}\n"
            self.description += f"Total Manual Booking Balance: {manualTotalBalance}\n"
            self.description += f"Total Deposit: {TotalCredit}\n"
            self.description += f"Total Expenses: {TotalDebit}\n"
            self.description += f"___!!!Invalid Balance. There have been a fraudulent misappropriation of finances from the manual book keeping. The Bank balance and the ledger balance do not correlate. Check the further information listed below for a more detailed tracking!!!\n"

        time.sleep(1)
        # ID Errors
        idErrors = []
        pen = False
        for xRow in range(len(idListB)):
            row = xRow
            bankInstance = None
            manualInstance = None
            try:
                bankInstance = idListB[row]
                manualInstance = idListM[row]
            except:
                print(f"Coordinates {row + 1}:{manual_record_index['id']} under manual is not available")
                self.description += f"Coordinates {row + 1}:{manual_record_index['id']} under manual is not available"
                break

            if str(bankInstance).lower() != str(manualInstance).lower():
                pen = True
                idErrors.append(f"Error on row {row}: column{manual_record_index['id']}")
            else:
                pass
        if pen is True:
            print(f"\n List of Errors Under Id: {len(idErrors)} errors.(type: data mismatch)")
            print(idErrors)
            print(
                "Error is as a result in both bank statement and manual ledger value not bring proportional to each other")
            self.description += f"\n List of Errors Under Id: {len(idErrors)} errors.(type: data mismatch)\n"
            self.description += f"\n{idErrors}"
            self.description += f"\nError is as a result in both bank statement and manual ledger value not bring proportional to each other"
        else:
            print('No errors found under the id columns...55%')
            self.description += f"No errors found under the id columns...55%\n"

        time.sleep(1)
        # Date Errors
        pen = False
        dateErrors = []
        for xRow in range(len(dateListB)):
            row = xRow
            bankInstance = None
            manualInstance = None
            try:
                bankInstance = dateListB[row]
                manualInstance = dateListM[row]
            except:
                print(f"Coordinates {row + 1}:{manual_record_index['date']} under manual is not available")
                self.description += f"Coordinates {row + 1}:{manual_record_index['date']} under manual is not available"
                break

            if str(bankInstance).lower() != str(manualInstance).lower():
                dateErrors.append(f"Error on row {row + 1}: column {manual_record_index['date']}(type: data mismatch)")
                pen = True
            else:
                pass
        if pen is True:
            print(f"List of Errors Under Date: {len(dateErrors)} errors.")
            print(dateErrors)
            print(
                "Error is as a result in both bank statement and manual ledger value not bring proportional to each other")
            self.description += f"List of Errors Under Date: {len(dateErrors)} errors.\n"
            self.description += f"{dateErrors}\n"
            self.description += "Error is as a result in both bank statement and manual ledger value not bring proportional to each other\n"

        else:
            print("No Errors found in date column...67.65%")
            self.description += f"No Errors found in date column...67.65%\n"

        time.sleep(1)
        # Credit or Deposit Errors
        pen = False
        creditErrors = []
        for xRow in range(len(creditListB)):
            row = xRow
            bankInstance = None
            manualInstance = None
            try:
                if row > 0:
                    bankInstance = creditListB[row]
                    manualInstance = creditListM[row]
            except:
                print(f"Coordinates {row + 1}:{manual_record_index['credit']} under manual is not available")
                self.description += f"Coordinates {row + 1}:{manual_record_index['credit']} under manual is not available\n"
                break
            if bankInstance != manualInstance:
                pen = True
                creditErrors.append(f"Error on row {row}: column{manual_record_index['credit']}")
            else:
                pass
        if pen is True:
            print(f"\n List of Errors Under Credit: {len(creditErrors)} errors.(type: data mismatch)")
            print(creditErrors)
            print(
                "Error is as a result in both bank statement and manual ledger value not bring proportional to each other")
            self.description += f"\n List of Errors Under Credit: {len(creditErrors)} errors.(type: data mismatch)\n"
            self.description += f"{creditErrors}\n"
            self.description += f"Error is as a result in both bank statement and manual ledger value not bring proportional to each other\n"

        else:
            print('No errors found under Credit...78.9%')
            self.description += f"No errors found under Credit...78.9%\n"

        time.sleep(1)
        # debit or expenses error
        pen = False
        debitErrors = []
        for xRow in range(len(debitListB)):
            row = xRow
            bankInstance = None
            manualInstance = None
            try:
                if row > 0:
                    bankInstance = debitListB[row]
                    manualInstance = debitListM[row]
            except:
                print(f"Coordinates {row + 1}:{manual_record_index['debit']} under manual is not available")
                self.description += f"Coordinates {row + 1}:{manual_record_index['debit']} under manual is not available\n"
                break
            if bankInstance != manualInstance:
                pen = True
                debitErrors.append(f"Error on row {row}: column {manual_record_index['debit']}")

            else:
                pass
        if pen is True:
            print(f"\n List of Errors Under Debit: {len(debitErrors)} errors.")
            print(debitErrors)
            print(
                "Error is as a result in both bank statement and manual ledger value not bring proportional to each other")
            self.description += f"\n List of Errors Under Debit: {len(debitErrors)} errors.\n"
            self.description += f"{debitErrors}\n"
            self.description += f"Error is as a result in both bank statement and manual ledger value not bring proportional to each other\n"

        else:
            print('no error found under debit column...85%')
            self.description += f"no error found under debit column...85%\n"

        time.sleep(1)
        # balances error
        balanceErrors = []
        pen = False
        for xRow in range(len(balanceListB)):
            row = xRow
            bankInstance = None
            manualInstance = None
            try:
                if row > 0:
                    bankInstance = balanceListB[row]
                    manualInstance = balanceListM[row]
            except:
                print(f"Coordinates {row + 1}:{manual_record_index['balance']} under manual is not available")
                self.description += f"Coordinates {row + 1}:{manual_record_index['balance']} under manual is not available\n"
                break

            if bankInstance != manualInstance:
                pen = True
                balanceErrors.append(f"Error on row {row}: column{manual_record_index['balance']}")
            else:
                pass

        if pen is True:
            print(f"\n List of Errors Under Balance: {len(balanceErrors)} errors.")
            print(balanceErrors)
            print(
                "Error is as a result in both bank statement and manual ledger value not bring proportional to each other")
            self.description += f"\n List of Errors Under Balance: {len(balanceErrors)} errors.\n"
            self.description += f"{balanceErrors}\n"
            self.description += f"Error is as a result in both bank statement and manual ledger value not bring proportional to each other\n"
            return self.description
        else:
            print("No errors found under Balance...98.99")
            time.sleep(3)
            print("Evaluation Successfully Completed. (0) errors found...100%")
            self.description += f"No errors found under Balance...98.99\n"
            self.description += f"Evaluation Successfully Completed. (0) errors found...100%\n"
            return self.description

    def get_id_index(self, record):
        self.p = {'id': record[0].index("id"), 'credit': record[0].index("credit"), 'debit': record[0].index("debit"),
                  'balance': record[0].index("balance"), 'date': record[0].index("date"), }
        return self.p

    def checker(self, record):
        document_status = {'id': 0, 'credit': 0, 'debit': 0, 'balance': 0, 'date': 0, }
        for x in record[0]:
            if 'id' == str(x).lower():
                document_status['id'] += 1

            elif 'credit' == str(x).lower():
                document_status['credit'] += 1

            elif 'debit' == str(x).lower():
                document_status['debit'] += 1

            elif 'balance' == str(x).lower():
                document_status['balance'] += 1

            elif 'date' == str(x).lower():
                document_status['date'] += 1

            else:
                pass

        if document_status['id'] == 1 and document_status['credit'] == 1 and document_status['debit'] == 1 and \
                document_status['balance'] == 1 and document_status['date'] == 1:
            self.p = "valid"
            print("_____All required required columns are provided...")
            return self.p, "_____All required required columns are provided..."

        elif document_status['id'] == 0 or document_status['credit'] == 0 or document_status['debit'] == 0 or \
                document_status['balance'] == 0 or document_status['date'] == 0:
            print('Check your dataset correctly, one of the required column (ID, DATE, CREDIT, DEBIT, OR BALANCE) is not provided in the data given. Please check your dataset and ensure it is updated correctly!')
            return 'invalid', 'Check your dataset correctly, one of the required column (ID, DATE, CREDIT, DEBIT, OR BALANCE) is not provided in the data given. Please check your dataset and ensure it is updated correctly!'

        elif document_status['id'] > 1 or document_status['credit'] > 1 or document_status['debit'] > 1 or \
                document_status['balance'] > 1 or document_status['date'] == 1:
            print(
                'Check your dataset correctly, one of this column (ID, DATE, CREDIT, DEBIT, OR BALANCE) appears to have one or multiple duplicate')
            return 'invalid', 'Check your dataset correctly, one of this column (ID, DATE, CREDIT, DEBIT, OR BALANCE) appears to have one or multiple duplicate'

    def values_validator(self, record, record_indexes):
        self.p = False
        list_of_miss_match = []
        for row in range(len(record)):
            if row > 0:
                try:
                    float(record[row][record_indexes['credit']]) + 34.44
                except ValueError:
                    self.p = True
                    list_of_miss_match.append(f"Error at [{row + 1}:{record_indexes['credit'] + 1}]")
                try:
                    float(record[row][record_indexes['debit']]) + 34.44
                except ValueError:
                    self.p = True
                    list_of_miss_match.append(f"Error at [{row + 1}:{record_indexes['debit'] + 1}]")
                try:
                    float(record[row][record_indexes['balance']]) + 34.44
                except ValueError:
                    self.p = True
                    list_of_miss_match.append(f"Error at [{row + 1}:{record_indexes['balance'] + 1}]")
            else:
                pass
        return self.p, list_of_miss_match

    def trial_balancer(self, record, record_indexes):
        self.p = False
        for xRow in range(len(record)):
            row = xRow
            if row > 1:
                if float(record[row][record_indexes['credit']]) == 0 and float(record[row][record_indexes['debit']]) > 0:
                    newBalance = float(record[row - 1][record_indexes['balance']]) - float(
                        record[row][record_indexes['debit']])
                    if newBalance != float(record[row][record_indexes['balance']]):
                        self.p = True
                        return self.p, f"Error! previous balance doesn't match up with summation of entities on row {record.index(record[row])}"
                    else:
                        pass
                elif float(record[row][record_indexes['debit']]) == 0 and float(record[row][record_indexes['credit']]) > 0:
                    newBalance = float(record[row-1][record_indexes['balance']]) + float(
                        record[row][record_indexes['credit']])
                    if newBalance != float(record[row][record_indexes['balance']]):
                        self.p = True
                        return self.p, f"Error! previous balance in summation with entities on row {record.index(record[row])} doesn't match."
                    else:
                        pass
                else:
                    self.p = True
                    return self.p, f"Error!There is an incorrect credit or debit value on row {record[row]}, please check it up and ensure that only one transaction type can occur at an instance!"
            else:
                pass
        return self.p, "Trial Balance Successfully Checked"

    def table_range(self, record, index):
        self.p = False
        idRange = []
        dateRange = []
        creditRange = []
        debitRange = []
        balanceRange = []
        for row in record:
            try:
                idRange.append(row[index['id']])
            except IndexError:
                print(f"Missing Values from row [{record.index(row)+1}]")
                pass
            try:
                dateRange.append(row[index['date']])
            except IndexError:
                print(f"Missing Values from row [{record.index(row)+1}]")
                pass
            try:
                creditRange.append(row[index['credit']])
            except IndexError:
                print(f"Missing Values from row [{record.index(row)+1}]")
                pass
            try:
                debitRange.append(row[index['debit']])
            except IndexError:
                print(f"Missing Values from row [{record.index(row)+1}]")
                pass
            try:
                balanceRange.append(row[index['balance']])
            except IndexError:
                print(f"Missing Values from row [{record.index(row)+1}]")
                pass
        gen = 1
        if len(debitRange) == len(balanceRange):
            if len(debitRange) == len(creditRange):
                if len(debitRange) == len(dateRange):
                    if len(dateRange) == len(idRange):
                        gen = 400
        if gen == 400:
            self.p = False
            return self.p, idRange, debitRange, dateRange, creditRange, balanceRange, 'successful'
        else:
            self.p = True
            return self.p, idRange, debitRange, dateRange, creditRange, balanceRange, 'Error, The number of rows under each columns are not equal, check the last row and ensure the values were provided'


Audit().run_engine_address('bank2.csv', 'bank.csv')
