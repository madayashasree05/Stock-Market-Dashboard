import plotly.graph_objects as go

def create_chart(data):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data['Close'],
            mode='lines',
            name='Close Price'
        )
    )

    return fig