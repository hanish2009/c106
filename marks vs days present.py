import plotly.express as px
import numpy as np
import csv

def plotFigure(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x="Days Present", y="Marks In Percentage")
        fig.show()

def getDataSource(data_path):
    days_present = []
    marks_in_percentage = []

    with open(data_path) as f:
        csv_reader = csv.DictReader(f)

        for row in csv_reader:
            days_present.append(float(row["Days Present"]))
            marks_in_percentage.append(float(row["Marks In Percentage"]))

    return {"x": days_present, "y": marks_in_percentage}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between Marks and Days Present is --> ", correlation[0, 1])

def setup():
    data_path = "Student Marks vs Days Present.csv"
    data_source = getDataSource(data_path)

    plotFigure(data_path)
    findCorrelation(data_source)

setup()