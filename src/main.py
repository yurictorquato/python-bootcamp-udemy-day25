import csv
from pathlib import Path


def main() -> None:
    """Função principal do programa."""
    file_csv = Path("weather_data.csv")

    with Path.open(file_csv) as file:
        data = csv.reader(file)
        next(data)  # pula a primeira linha (cabeçalho)

        temperatures: list[int] = [int(row[1]) for row in data]
        print(temperatures)


if __name__ == "__main__":
    main()
