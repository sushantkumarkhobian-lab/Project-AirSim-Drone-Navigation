import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


BASE_NAME = "advanced_drone_navigation_analytics"
RESULTS_FOLDER = ""


LOWER_IS_BETTER = [
    "Actual_Time_Taken_Seconds",
    "Time_Error_Seconds",
    "Final_Position_Error_m",
    "Max_Position_Error_m",
    "Total_Distance_Travelled_m",
    "Battery_Used_Percent"
]

HIGHER_IS_BETTER = [
    "Average_Speed_mps",
    "Path_Efficiency_Percent",
    "Battery_Remaining_Percent"
]


def get_file_from_number(number):
    return f"{BASE_NAME}{number}.csv"


def load_csv(file):
    if not os.path.exists(file):
        print("File not found:", file)
        return None

    return pd.read_csv(file)


def clean_data(df):
    df = df.copy()

    df = df[
        ~df["Waypoint_No_or_Phase"].astype(str).isin(["TAKEOFF", "LANDING"])
    ]

    numeric_columns = LOWER_IS_BETTER + HIGHER_IS_BETTER

    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def get_winner(metric, value1, value2, label1, label2):
    if metric in LOWER_IS_BETTER:
        return label1 if value1 < value2 else label2

    if metric in HIGHER_IS_BETTER:
        return label1 if value1 > value2 else label2

    return "N/A"


def get_improvement_percent(metric, value1, value2):
    if value1 == 0 or value2 == 0:
        return 0

    if metric in LOWER_IS_BETTER:
        better = min(value1, value2)
        worse = max(value1, value2)

    elif metric in HIGHER_IS_BETTER:
        better = max(value1, value2)
        worse = min(value1, value2)

    else:
        return 0

    return ((worse - better) / worse) * 100


def create_clean_summary(df1, df2, label1, label2):
    metrics = [
        "Actual_Time_Taken_Seconds",
        "Time_Error_Seconds",
        "Final_Position_Error_m",
        "Max_Position_Error_m",
        "Total_Distance_Travelled_m",
        "Average_Speed_mps",
        "Battery_Used_Percent",
        "Battery_Remaining_Percent",
        "Path_Efficiency_Percent"
    ]

    rows = []

    for metric in metrics:
        if metric in df1.columns and metric in df2.columns:
            value1 = df1[metric].mean()
            value2 = df2[metric].mean()

            winner = get_winner(metric, value1, value2, label1, label2)
            improvement = get_improvement_percent(metric, value1, value2)

            rows.append([
                metric,
                round(value1, 4),
                round(value2, 4),
                winner,
                round(improvement, 2)
            ])

    summary = pd.DataFrame(
        rows,
        columns=[
            "Metric",
            label1,
            label2,
            "Better_Run",
            "Improvement_Percent"
        ]
    )

    path = os.path.join(RESULTS_FOLDER, "clean_comparison_summary.csv")
    summary.to_csv(path, index=False)

    return summary


def create_scorecard(summary, label1, label2):
    wins_1 = 0
    wins_2 = 0

    rows = []

    for _, row in summary.iterrows():
        metric = row["Metric"]
        winner = row["Better_Run"]

        if winner == label1:
            wins_1 += 1
        elif winner == label2:
            wins_2 += 1

        rows.append([metric, winner])

    if wins_1 > wins_2:
        overall = label1
    elif wins_2 > wins_1:
        overall = label2
    else:
        overall = "Tie"

    rows.append(["Overall Winner", overall])
    rows.append([f"{label1} Wins", wins_1])
    rows.append([f"{label2} Wins", wins_2])

    scorecard = pd.DataFrame(
        rows,
        columns=["Category", "Winner"]
    )

    path = os.path.join(RESULTS_FOLDER, "performance_scorecard.csv")
    scorecard.to_csv(path, index=False)

    return scorecard, overall, wins_1, wins_2


def plot_metric_line(df1, df2, label1, label2, metric, filename, ylabel):
    if metric not in df1.columns or metric not in df2.columns:
        return

    plt.figure(figsize=(10, 5))

    plt.plot(
        range(1, len(df1) + 1),
        df1[metric],
        marker="o",
        label=label1
    )

    plt.plot(
        range(1, len(df2) + 1),
        df2[metric],
        marker="o",
        label=label2
    )

    plt.xlabel("Navigation Step")
    plt.ylabel(ylabel)
    plt.title(metric.replace("_", " "))
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    path = os.path.join(RESULTS_FOLDER, filename)
    plt.savefig(path)
    plt.close()


def plot_summary_bar(summary, label1, label2):
    metrics = summary["Metric"]
    values1 = summary[label1]
    values2 = summary[label2]

    x = np.arange(len(metrics))
    width = 0.35

    plt.figure(figsize=(12, 6))

    plt.bar(x - width / 2, values1, width, label=label1)
    plt.bar(x + width / 2, values2, width, label=label2)

    plt.xticks(x, metrics, rotation=45, ha="right")
    plt.ylabel("Average Value")
    plt.title("Average Metric Comparison")
    plt.legend()
    plt.tight_layout()

    path = os.path.join(RESULTS_FOLDER, "average_metric_comparison_bar.png")
    plt.savefig(path)
    plt.close()



def normalize_for_radar(summary, label1, label2):
    radar_metrics = [
        "Time_Error_Seconds",
        "Final_Position_Error_m",
        "Max_Position_Error_m",
        "Average_Speed_mps",
        "Battery_Used_Percent",
        "Path_Efficiency_Percent"
    ]

    labels = []
    file1_scores = []
    file2_scores = []

    for metric in radar_metrics:
        row = summary[summary["Metric"] == metric]

        if row.empty:
            continue

        value1 = float(row[label1].iloc[0])
        value2 = float(row[label2].iloc[0])

        if value1 == 0 and value2 == 0:
            score1 = 1
            score2 = 1

        elif metric in LOWER_IS_BETTER:
            max_value = max(value1, value2)
            score1 = 1 - (value1 / max_value)
            score2 = 1 - (value2 / max_value)

        else:
            max_value = max(value1, value2)
            score1 = value1 / max_value
            score2 = value2 / max_value

        labels.append(metric.replace("_", " "))
        file1_scores.append(score1)
        file2_scores.append(score2)

    return labels, file1_scores, file2_scores


def plot_radar_chart(summary, label1, label2):
    labels, scores1, scores2 = normalize_for_radar(summary, label1, label2)

    if len(labels) < 3:
        return

    scores1 += scores1[:1]
    scores2 += scores2[:1]

    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]

    plt.figure(figsize=(8, 8))
    ax = plt.subplot(111, polar=True)

    ax.plot(angles, scores1, marker="o", label=label1)
    ax.fill(angles, scores1, alpha=0.15)

    ax.plot(angles, scores2, marker="o", label=label2)
    ax.fill(angles, scores2, alpha=0.15)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    ax.set_title("Overall Performance Radar Chart")
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))

    path = os.path.join(RESULTS_FOLDER, "performance_radar_chart.png")
    plt.savefig(path, bbox_inches="tight")
    plt.close()


def create_analysis_report(summary, label1, label2, overall, wins_1, wins_2):
    lines = []

    lines.append("DRONE NAVIGATION COMPARISON REPORT")
    lines.append("=" * 45)
    lines.append(f"Compared Runs: {label1} vs {label2}")
    lines.append("")
    lines.append("SUMMARY")
    lines.append("-" * 45)
    lines.append(f"{label1} Wins: {wins_1}")
    lines.append(f"{label2} Wins: {wins_2}")
    lines.append(f"Overall Better Run: {overall}")
    lines.append("")

    lines.append("METRIC-WISE ANALYSIS")
    lines.append("-" * 45)

    for _, row in summary.iterrows():
        metric = row["Metric"]
        better = row["Better_Run"]
        improvement = row["Improvement_Percent"]

        lines.append(
            f"{metric}: {better} performed better "
            f"by approximately {improvement}%."
        )

    lines.append("")
    lines.append("INTERPRETATION")
    lines.append("-" * 45)
    lines.append(
        "Lower time error, final position error, maximum position error, "
        "travelled distance, and battery usage indicate better control quality."
    )
    lines.append(
        "Higher average speed, battery remaining, and path efficiency indicate "
        "better performance and energy efficiency."
    )

    report_text = "\n".join(lines)

    path = os.path.join(RESULTS_FOLDER, "analysis_report.txt")

    with open(path, "w") as file:
        file.write(report_text)

    print(report_text)


def main():
    global RESULTS_FOLDER

    print("Available file format:")
    print("advanced_drone_navigation_analytics1.csv")
    print("advanced_drone_navigation_analytics2.csv")
    print("advanced_drone_navigation_analytics3.csv")
    print()

    file1_num = input("Enter first file number: ")
    file2_num = input("Enter second file number: ")

    RESULTS_FOLDER = f"results{file1_num}{file2_num}"
    os.makedirs(RESULTS_FOLDER, exist_ok=True)

    file1 = get_file_from_number(file1_num)
    file2 = get_file_from_number(file2_num)

    label1 = f"File_{file1_num}"
    label2 = f"File_{file2_num}"

    df1 = load_csv(file1)
    df2 = load_csv(file2)

    if df1 is None or df2 is None:
        return

    df1 = clean_data(df1)
    df2 = clean_data(df2)

    summary = create_clean_summary(df1, df2, label1, label2)
    scorecard, overall, wins_1, wins_2 = create_scorecard(summary, label1, label2)

    plot_metric_line(df1, df2, label1, label2, "Actual_Time_Taken_Seconds",
                     "actual_time_comparison.png", "Actual Time Taken (seconds)")

    plot_metric_line(df1, df2, label1, label2, "Time_Error_Seconds",
                     "time_error_comparison.png", "Time Error (seconds)")

    plot_metric_line(df1, df2, label1, label2, "Final_Position_Error_m",
                     "final_position_error_comparison.png", "Final Position Error (m)")

    plot_metric_line(df1, df2, label1, label2, "Max_Position_Error_m",
                     "max_position_error_comparison.png", "Max Position Error (m)")

    plot_metric_line(df1, df2, label1, label2, "Average_Speed_mps",
                     "average_speed_comparison.png", "Average Speed (m/s)")

    plot_metric_line(df1, df2, label1, label2, "Battery_Remaining_Percent",
                     "battery_remaining_comparison.png", "Battery Remaining (%)")

    plot_summary_bar(summary, label1, label2)
    plot_radar_chart(summary, label1, label2)

    create_analysis_report(
        summary,
        label1,
        label2,
        overall,
        wins_1,
        wins_2
    )

    print(f"\nAll improved analysis files saved inside '{RESULTS_FOLDER}' folder.")


if __name__ == "__main__":
    main()