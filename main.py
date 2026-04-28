from utils import get_data, clean_data, generate_excel
from config import URL, PATH_FILE


def main():
    df = get_data(URL)

    df = clean_data(df)
    print(df.head())

    generate_excel(df, PATH_FILE)


if __name__ == "__main__":
    main()
