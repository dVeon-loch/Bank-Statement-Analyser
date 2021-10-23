from parsing.statement_parser import StatementParser
import pandas
import pdfplumber


class ParserCapitec(StatementParser):

    def get_info(self):
        with pdfplumber.open("account_statement.pdf") as pdf:
            first_page = pdf.pages[0]
            page_text = first_page.extract_text()
            text_array = (page_text.splitlines())
            name = text_array[3][:text_array[3].find("Tax")].strip().title()
            address = text_array[4].title()
            from_date=text_array[12][text_array[12].rfind(":")+2:]
            to_date=text_array[13][text_array[13].rfind(":")+2:]
            dict = {'Name': name, 'Address': address, 'From_Date': from_date, 'To_Date': to_date}
            return pandas.Series(dict).to_frame('Info')
    def get_data(self):
        pass


def main():
    print(ParserCapitec.get_info(ParserCapitec))


if __name__ == '__main__':
    main()
