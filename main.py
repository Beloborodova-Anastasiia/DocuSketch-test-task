import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path


class DrawingPlots:

    def draw_plot(self, file_path: Path) -> Path:
        dismissed_columns = ['name', 'gt_corners', 'rb_corners']
        df = pd.read_json(file_path)
        drawing_columns = df.keys().drop(dismissed_columns)
        for column in drawing_columns:
            plt.figure()
            plt.plot(df[column])
            plt.title(column)
            plt.savefig(f"plots/{column}")


def main() -> None:
    drawing = DrawingPlots()
    drawing.draw_plot("deviation.json")


if __name__ == '__main__':
    main()
