import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


class Visualize:
    def __init__(self):
        pass

    def plotly_bar(self, data, x, y, title):
        figure = px.bar(data, y=y, x=x,
                        title=title, height=800)
        figure.show()

    def go_bar(self, data, plot_attributes):
        fig = go.Figure()

        for attr in plot_attributes:
            fig.add_trace(go.Bar(
                x=data[attr['x']],
                y=data[attr['y']],
                name=attr['name'],
                marker_color=attr['color']
            ))

        fig.update_layout(barmode='group', xaxis_tickangle=-45)
        fig.show()

    def px_pie(self, df, columns, title):
        values = []

        for col in columns:
            values.append(df[col].sum())

        fig, ax1 = plt.subplots(facecolor='white')

        ax1.pie(values, labels=columns,
                shadow=True, startangle=90)
        ax1.axis('equal')
        ax1.set(title=title)

        plt.show()
