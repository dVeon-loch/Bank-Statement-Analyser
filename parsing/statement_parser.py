from abc import ABC, abstractmethod


class StatementParser(ABC):
    """
    Abstract blueprint class for all bank specific parser implementations
    """

    @abstractmethod
    def get_info(self):
        """
        This method should extract the basic info from a bank statement, e.g. name, address, starting date, ending date.
        returns a Pandas dataframe containing this info
        """
        pass

    @abstractmethod
    def get_data(self):
        """
        This method should extract the important raw data from a bank statement, e.g. transaction date, description, amount (can be positive or negative), balance
        returns a Pandas dataframe
        :return:
        """
        pass
