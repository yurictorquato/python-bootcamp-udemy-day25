from typing import Any

import pandas as pd


def main() -> None:
    """Função principal do programa."""
    data: pd.DataFrame = pd.read_csv("weather_data.csv")
    # print(data["temp"])

    data_dict: dict[str, Any] = data.to_dict()
    # print(data_dict)

    temp_list: list = data["temp"].to_list()

    average: int | float = round(sum(temp_list) / len(temp_list), 2)
    print(f"A média das temperaturas é {average}")

    print(
        data["temp"].mean()
    )  # faz a  mesma coisa do código acima, mas usando o pandas

    print(f"A temperatura máxima é de: {data['temp'].max()}")

    # Get data in columns
    print(data["condition"])
    print(data.condition)

    # Get data in row
    print(data[data.day == "Monday"])  # obtém a linha inteira

    print(data["day"][0])
    print(data.day[0])

    print(data[data.temp == 24])
    print(data[data.temp == data.temp.max()])
    print(data[data["temp"] == data["temp"].max()])

    monday = data[data.day == "Monday"]
    print(monday.condition)

    fahrenheit: int | float = (monday["temp"][0] * (9 / 5)) + 32
    print(f"{monday['temp'][0]} graus celsius é igual a {fahrenheit} graus fahrenheit")

    # Create a dataframe from scratch
    data_dict_students: dict[str, list[str] | list[int]] = {
        "students": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65],
    }

    data_students = pd.DataFrame(data_dict_students)
    print(data_students)

    data_students.to_csv("data_students.csv")


if __name__ == "__main__":
    main()
