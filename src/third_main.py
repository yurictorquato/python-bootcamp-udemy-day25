import pandas as pd


def main() -> None:
    """Função principal do programa."""
    data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251019.csv")

    colors = data["Primary Fur Color"]

    black = 0
    red = 0
    gray = 0

    for color in colors:
        if color == "Black":
            black += 1
        elif color == "Cinnamon":
            red += 1
        elif color == "Gray":
            gray += 1

    data_dict = {
        "Fur Color": ["black", "red", "gray"],
        "Count": [black, red, gray]
    }

    df = pd.DataFrame(data_dict)
    df.to_csv("squirre_colors.csv")


def teacher_solution() -> None:
    """Função que mostra a solução da professora."""
    data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251019.csv")

    colors = data["Primary Fur Color"]

    black_squirrels = len(data[colors == "black"])
    red_squirrels = len(data[colors == "red"])
    gray_squirrels = len(data[colors == "Gray"])

    data_dict = {
        "Fur Color": ["black", "red", "grat"],
        "Count": [black_squirrels, red_squirrels, gray_squirrels],
    }

    df = pd.DataFrame(data_dict)
    df.to_csv("squirre_colors_teacher_solution.csv")


if __name__ == "__main__":
    main()
    teacher_solution()
