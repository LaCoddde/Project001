import pandas as pd
from tabulate import tabulate
from datetime import datetime
from habit_tracker import track_habit, Habit


def main():
    habits: list[Habit] = [
        track_habit("Coffee", datetime(2023, 1, 6, 8), cost=1, minutes_used=5),
        track_habit("Wasting time", datetime(2024, 2, 4, 10), cost=50, minutes_used=120),
        track_habit("Ordering", datetime(2023, 10, 1, 8), cost=30, minutes_used=40)
    ]

    df = pd.DataFrame(habits)

    print(tabulate(df, headers="keys", tablefmt="psql"))


if __name__ == '__main__':
    main()
