from utils import get_data, clean_data
from config import URL


def main():
    df = get_data(URL)

    df = clean_data(df)
    print(df.head())


if __name__ == "__main__":
    main()
