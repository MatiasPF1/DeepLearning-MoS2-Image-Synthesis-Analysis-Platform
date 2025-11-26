from dash import html, dcc

def material_properties():
    return html.Div(
        [
            html.H4("Basic Material Properties", className="section-title"),
            html.P("Define the fundamental properties of your material sample", className="section-subtitle"),

            html.Div(
                [
                    # Column 1
                    html.Div(
                        [
                            html.Label("Material Name"),
                            dcc.Input(
                                id="mat-name",
                                type="text",
                                value="MoS2",
                                className="input-field"
                            ),

                            html.Label("Pixel Size (Å)"),
                            dcc.Input(
                                id="pixel-size",
                                type="number",
                                className="input-field"
                            ),

                            html.Label("Metal Site Atom Number"),
                            dcc.Input(
                                id="metal-atom",
                                type="number",
                                className="input-field"
                            )
                        ],
                        className="form-col"
                    ),

                    # Column 2
                    html.Div(
                        [
                            html.Label("Lattice Constant a (Å)"),
                            dcc.Input(
                                id="lattice-const",
                                type="number",
                                className="input-field"
                            ),

                            html.Label("Image Size (pixels)"),
                            dcc.Input(
                                id="img-size",
                                type="number",
                                className="input-field"
                            ),

                            html.Label("Chalcogen Site Atom Number"),
                            dcc.Input(
                                id="chal-atom",
                                type="number",
                                className="input-field"
                            )
                        ],
                        className="form-col"
                    )
                ],
                className="form-grid"
            )
        ],
        id="material-panel",
        className="material-panel"
    )
