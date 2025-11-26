from dash import html, dcc




'''
Second Part, Part 1
'''

def Microscope_Settings():
    return html.Div(
        [
            html.H4("Basic Microscope Settings", className="section-title"),
            html.P("Configure electron microscope operational parameters", className="section-subtitle"),

            html.Div(
                [
                    # Column 1
                    html.Div(
                        [
                            html.Label("Voltage(kV)"),
                            dcc.Input(
                                id="voltage",
                                type="text",
                                className="input-field"
                            ),

                            html.Label("Aperture"),
                            dcc.Input(
                                id="aperture",
                                type="number",
                                className="input-field"
                            ),
                        ],
                        className="form-col"
                    ),

                    # Column 2
                    html.Div(
                        [
                            html.Label("Defocus(df)"),
                            dcc.Input(
                                id="defocus",
                                type="number",
                                className="input-field"
                            ),

                            html.Label("Dwell Time"),
                            dcc.Input(
                                id="dwell-time",
                                type="number",
                                className="input-field"
                            ),
                        ],
                        className="form-col"
                    )
                ],
                className="form-grid"
            )
        ],
        id="microscope-panel",
        className="microscope-panel"
    )
