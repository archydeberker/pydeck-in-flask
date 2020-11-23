import pydeck as pdk

LONDON = [51.50, -0.12]


def plot_3d_map(df):
    """
    Plots a map with a dot at latitude `x` with longitude `y` and height `z`
    """
    df["colour"] = df["chargeDeviceStatus"].map({"In service": [10, 200, 20], "Out of service": [200, 20, 20]})
    print(df)
    geojson = pdk.Layer(
        "ScatterplotLayer",
        get_position=["longitude", "latitude"],
        get_radius=20,
        color="red",
        data=df,
        opacity=0.3,
        stroke_min_width=10,
        filled=True,
        auto_highlight=True,
        pickable=True,
        tooltip=True,
        get_fill_color="colour",
        get_line_color=[0, 0, 0],
        radius_min_pixels=10,
        radius_max_pixels=100,
    )
    # Set the viewport location
    view_state = pdk.ViewState(
        longitude=LONDON[1], latitude=LONDON[0], zoom=5, min_zoom=5, max_zoom=15, pitch=89, bearing=0
    )

    return pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=view_state,
        layers=[geojson],
        tooltip={"html": "{name}<br/>" "", "style": {"backgroundColor": "steelblue", "color": "white"}},
        width="70%",
        height=200,
    )


def clean_html(html):
    html = html.replace("100vw", "100%").replace("100vw", "100%")
    return html
