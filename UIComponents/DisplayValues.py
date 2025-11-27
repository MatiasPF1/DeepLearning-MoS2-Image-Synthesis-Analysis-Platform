from dash import Input, Output, html


def register_display_values_callback(app):    
    @app.callback(
        Output('values-display-content', 'children'),
        Input('mat-name', 'value'),
        Input('pixel-size', 'value'),
        Input('metal-atom', 'value'),
        Input('lattice-const', 'value'),
        Input('img-size', 'value'),
        Input('chal-atom', 'value'),
        Input('sub-atom-metal', 'value'),
        Input('metal-sub-conc', 'value'),
        Input('metal-vac-conc', 'value'),
        Input('sub-atom-chal', 'value'),
        Input('chal-sub-conc', 'value'),
        Input('vac-one-conc', 'value'),
        Input('vac-two-conc', 'value'),
        Input('sub-two-conc', 'value'),
        Input('sub-one-conc', 'value'),
        Input('voltage', 'value'),
        Input('aperture', 'value'),
        Input('defocus', 'value'),
        Input('dwell-time', 'value'),
        Input('cs3-mean', 'value'),
        Input('cs3-std', 'value'),
        Input('cs5-mean', 'value'),
        Input('cs5-std', 'value'),
        Input('adf-angle-min', 'value'),
        Input('adf-angle-max', 'value'),
        Input('src-size-mean', 'value'),
        Input('defoc-spread-mean', 'value'),
        Input('probe-cur-mean', 'value'),
        Input('src-size-std', 'value'),
        Input('defoc-spread-std', 'value'),
        Input('probe-cur-std', 'value'),
    )
    def update_values_display(mat_name, pixel_size, metal_atom, lattice_const, img_size, chal_atom,
                             sub_atom_metal, metal_sub_conc, metal_vac_conc, sub_atom_chal,
                             chal_sub_conc, vac_one_conc, vac_two_conc, sub_two_conc, sub_one_conc,
                             voltage, aperture, defocus, dwell_time,
                             cs3_mean, cs3_std, cs5_mean, cs5_std,
                             adf_angle_min, adf_angle_max,
                             src_size_mean, defoc_spread_mean, probe_cur_mean,
                             src_size_std, defoc_spread_std, probe_cur_std):
        
        # Create rows for each parameter with label and value
        rows = []
        
        # Material Properties Section
        rows.append(html.Div([html.H6("Material Properties", style={"fontWeight": "bold", "marginTop": "15px"})]))
        rows.append(html.Div([html.Span("Material Name: "), html.Span(mat_name or "-", className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Pixel Size: "), html.Span(pixel_size or "-", className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Metal Atom #: "), html.Span(metal_atom or "-", className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Lattice Constant: "), html.Span(lattice_const or "-", className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Image Size: "), html.Span(img_size or "-", className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Chalcogen Atom #: "), html.Span(chal_atom or "-", className="value-text")], className="value-row"))
        
        # Metal Site Defects
        rows.append(html.Div([html.H6("Metal Site Defects", style={"fontWeight": "bold", "marginTop": "15px"})]))
        rows.append(html.Div([html.Span("Sub. Atom #: "), html.Span(sub_atom_metal or "-", className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Sub. Conc: "), html.Span(metal_sub_conc or "-", className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Vacancy Conc: "), html.Span(metal_vac_conc or "-", className="value-text")], className="value-row"))
        
        # Chalcogen Site Defects
        rows.append(html.Div([html.H6("Chalcogen Site Defects", style={"fontWeight": "bold", "marginTop": "15px"})]))
        rows.append(html.Div([html.Span("Sub. Atom #: "), html.Span(sub_atom_chal or "-", className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Sub. Conc: "), html.Span(chal_sub_conc or "-", className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Vacancy One: "), html.Span(vac_one_conc or "-", className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Vacancy Two: "), html.Span(vac_two_conc or "-", className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Sub. Two: "), html.Span(sub_two_conc or "-", className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Sub. One: "), html.Span(sub_one_conc or "-", className="value-text")], className="value-row"))
        
        # Microscope Settings
        rows.append(html.Div([html.H6("Microscope Settings", style={"fontWeight": "bold", "marginTop": "15px"})]))
        rows.append(html.Div([html.Span("Voltage: "), html.Span(voltage or "-", className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Aperture: "), html.Span(aperture or "-", className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Defocus: "), html.Span(defocus or "-", className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Dwell Time: "), html.Span(dwell_time or "-", className="value-text")], className="value-row"))
        
        # Aberration Coefficients
        rows.append(html.Div([html.H6("Aberration Coefficients", style={"fontWeight": "bold", "marginTop": "15px"})]))
        rows.append(html.Div([html.Span("Cs3 Mean: "), html.Span(cs3_mean or "-", className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Cs3 Std: "), html.Span(cs3_std or "-", className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Cs5 Mean: "), html.Span(cs5_mean or "-", className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Cs5 Std: "), html.Span(cs5_std or "-", className="value-text")], className="value-row"))
        
        # ADF Settings
        rows.append(html.Div([html.H6("ADF Settings", style={"fontWeight": "bold", "marginTop": "15px"})]))
        rows.append(html.Div([html.Span("Angle Min: "), html.Span(adf_angle_min or "-", className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Angle Max: "), html.Span(adf_angle_max or "-", className="value-text")], className="value-row"))
        
        # Gaussian Parameters
        rows.append(html.Div([html.H6("Gaussian Parameters", style={"fontWeight": "bold", "marginTop": "15px"})]))
        rows.append(html.Div([html.Span("Src Size Mean: "), html.Span(src_size_mean or "-", className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Src Size Std: "), html.Span(src_size_std or "-", className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Defoc Spread Mean: "), html.Span(defoc_spread_mean or "-", className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Defoc Spread Std: "), html.Span(defoc_spread_std or "-", className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Probe Cur Mean: "), html.Span(probe_cur_mean or "-", className="value-text")], className="value-row"))
        rows.append(html.Div([html.Span("Probe Cur Std: "), html.Span(probe_cur_std or "-", className="value-text")], className="value-row"))
        
        return rows
