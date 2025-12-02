# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import matplotlib.pyplot as plt
import pandas as pd
import os

def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    _FILE = "files/input/shipping-data.csv"
    _DOCS = "docs/"
    _WAREHOUSE = "docs/shipping_per_warehouse.png"
    _MODE = "docs/mode_of_shipment.png"
    _AVERAGE = "docs/average_customer_rating.png"
    _WEIGHT = "docs/weight_distribution.png"

    def load_data():
        df = pd.read_csv(_FILE)
        return df

    load_data().head()

    def create_visual_for_shipping_per_warehouse(df):
        df = df.copy()
        plt.figure()
        counts = df.Warehouse_block.value_counts()
        counts.plot.bar(
            title = "Shipping per Warehouse",
            xlabel = "Warehouse block",
            ylabel = "Record Count",
            color = "tab:blue",
            fontsize=8
        )
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        os.makedirs(_DOCS, exist_ok=True)
        plt.savefig(_WAREHOUSE)

    df = load_data()
    create_visual_for_shipping_per_warehouse(df)

    def create_visual_for_mode_of_shipment(df):
        df = df.copy()
        plt.figure()
        counts = df.Mode_of_Shipment.value_counts()
        counts.plot.pie(
            title = "Mode of shipment",
            wedgeprops=dict(width=0.35),
            ylabel = "",
            colors = ["tab:blue", "tab:orange", "tab:green"],
            fontsize=8
        )
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        os.makedirs(_DOCS, exist_ok=True)
        plt.savefig(_MODE)

    df = load_data()
    create_visual_for_mode_of_shipment(df)

    def create_visual_for_average_customer_rating(df):
        df = df.copy()
        plt.figure()
        df = (
            df[["Mode_of_Shipment", "Customer_rating"]]
            .groupby("Mode_of_Shipment")
            .describe()
        )
        df.columns = df.columns.droplevel()
        df = df[["mean", "min", "max"]]

        colors = [
            "tab:green" if value >= 3.0 else "tab:orange" for value in df["mean"].values
        ]

        plt.barh(
            y=df.index.values,
            width=df["max"].values -1,
            left=df["min"].values,
            color = colors,
            height=0.5,
            alpha=0.8,
        )

        os.makedirs(_DOCS, exist_ok=True)
        plt.savefig(_AVERAGE)

    df = load_data()
    create_visual_for_average_customer_rating(df)

    def create_visual_for_weight_distribution(df):
        df = df.copy()
        plt.figure()
        df.Weight_in_gms.plot.hist(
            title="Shipped Weight Distribution",
            color = "tab:orange",
            edgecolor="white"
        )    

        os.makedirs(_DOCS, exist_ok=True)
        plt.savefig(_WEIGHT)

    df = load_data()
    create_visual_for_weight_distribution(df)

