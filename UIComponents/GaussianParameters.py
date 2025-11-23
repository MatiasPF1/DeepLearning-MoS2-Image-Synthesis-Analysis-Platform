from dash import html, dcc
'''
Second Part, Part 4
'''

def Gaussian_Parameters():
    return html.Div(
        [
            html.H4("Metal Site Defects", className="section-title"),
            html.P("Configure substitutions and vacancies on metal sites: Defects accept from 0 to 1.0 concentrations", className="section-subtitle"),

            html.Div(
                [
                    # Column 1
                    html.Div(
                        [
                            html.Label("Source Size Mean(nm)"),
                            dcc.Input(
                                type="number",
                                value=0,
                                className="input-field"
                            ),

                            html.Label("Defocus Spread Mean(A)"),
                            dcc.Input(
                                type="number",
                                value=0,
                                className="input-field"
                            ),

                            html.Label("Probe Current Mean(A)"),
                            dcc.Input(
                                type="number",
                                value=0,
                                className="input-field"
                            ),
                        ],
                        className="form-col"
                    ),

                    # Column 2
                    html.Div(
                        [
                            html.Label("Source Size Std(nm)"),
                            dcc.Input(
                                type="number",
                                value=0,
                                className="input-field"
                            ),

                            html.Label("Defocus Spread Stf(A)"),
                            dcc.Input(
                                type="number",
                                value=0,
                                className="input-field"
                            ),

                             html.Label("Probe Current Std(A)"),
                            dcc.Input(
                                type="number",
                                value=0,
                                className="input-field"
                            ),
                        ],
                        className="form-col"
                    )
                ],
                className="form-grid"
            )
        ],
        id="Gausian_Panel",
        className="Gausian_Panel"
    )