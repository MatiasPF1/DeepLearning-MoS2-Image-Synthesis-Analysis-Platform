from dash import Dash, html, Input, Output, State, dcc
import dash_bootstrap_components as dbc
import dash


#First Tab Components
from UIComponents.Navbar import navbar
from UIComponents.tabs import left_tabs
from UIComponents.MaterialProperties import material_properties
from UIComponents.MaterialProperties2 import metal_site_defects
from UIComponents.MaterialProperties3 import chalcogen_site_defects
from UIComponents.SettingsGeneration import generation_settings

#Second Tab Components 
from UIComponents.BasicMicroscopeSettings import Microscope_Settings
from UIComponents.aberrationCoeficcients import Abberation_Coeficients
from UIComponents.ADF_Settings import ADF_Settings
from UIComponents.GaussianParameters import Gaussian_Parameters

# Callback For Display Vallues Collumn 
from UIComponents.DisplayValues import register_display_values_callback


# 0-Main UI Layout
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    navbar,
    
    # Hidden storage component for parameters
    dcc.Store(id='parameters-store', storage_type='memory'),
    
    # Alert for validation messages
    html.Div(id='validation-alert', className='alert-container'),
    
    html.Div(
        [
            # Left side - Tabs and parameter panels
            html.Div(
                [
                    left_tabs(),

                    #Material Section Panels 
                    material_properties(),
                    metal_site_defects(),
                    chalcogen_site_defects(),

                    #Microscope Section Panels
                    Microscope_Settings(),
                    Abberation_Coeficients(),
                    ADF_Settings(),
                    Gaussian_Parameters(),
                ],
                className="tab-with-panel"
            ),
            # Right side - Generation settings and config
            generation_settings()
        ],
        className="section-container"
    )
])


# 1-Functions for Interactivity

# On/Off Button Functionality
@app.callback(
    #Button Outputs 
    Output("btn-material", "className"),
    Output("btn-microscope", "className"),

    #First Tab Outputs
    Output("material-panel", "style"),
    Output("metal-defects-panel", "style"),
    Output("metal-Chalcogen-panel", "style"),

    #Second Tab Outputs
    Output("microscope-panel", "style"),
    Output("aberration-panel", "style"),
    Output("ADF_Panel", "style"),
    Output("Gausian_Panel","style"),

    #Click Inputs by User
    Input("btn-material", "n_clicks"),
    Input("btn-microscope", "n_clicks"),
)
def toggle_buttons(material_clicks, microscope_clicks):
    # Styles for show/hide
    visible = {"display": "block"} # Show
    hidden = {"display": "none"} #Hide

    # 1-Default State(param-btn By Default Active)
    if not material_clicks and not microscope_clicks:
        return (
            "param-btn active-param-btn",    # Material active
            "param-btn",                     # Microscope inactive
            visible,                         # Material panel Visible
            visible,                         # Metal defects panel Visible
            visible,                         # Chalcogen defects panel Visible
            hidden,                          # Microscope panel Hidden
            hidden,                          # Aberration panel Hidden
            hidden,                          # ADF panel Hidden
            hidden                           # Gaussian Panel Hidden
        )

    # 2- User Selection of Button

    # Which button was clicked?
    ctx = dash.callback_context.triggered_id

    # If Material Button Clicked
    if ctx == "btn-material":
        return (
            "param-btn active-param-btn",
            "param-btn",
            visible,  # material
            visible,  # metal defects
            visible,  # chalcogen defects
            hidden,   # microscope is hidden
            hidden,   # aberration is hidden
            hidden,   # ADF is hidden 
            hidden    # gaussian is Hidden 
        )

    # If Microscope Button Clicked
    elif ctx == "btn-microscope":
        return (
            "param-btn",
            "param-btn active-param-btn",
            hidden,   # material is hidden
            hidden,   # metal defects is hidden
            hidden,   # chalcogen defects is hidden
            visible,  # microscope
            visible,  # aberration
            visible,  # ADF
            visible   # Gaussian
        )


# 2-Parameter Input Validation and Storage
@app.callback(
    Output('parameters-store', 'data'),
    Output('validation-alert', 'children'),
    Input('generate-btn', 'n_clicks'),
    State('batch-size-dropdown', 'value'),
    
    # Material Properties States
    State('mat-name', 'value'),
    State('pixel-size', 'value'),
    State('metal-atom', 'value'),
    State('lattice-const', 'value'),
    State('img-size', 'value'),
    State('chal-atom', 'value'),
    
    # Metal Site Defects States
    State('sub-atom-metal', 'value'),
    State('metal-sub-conc', 'value'),
    State('metal-vac-conc', 'value'),
    
    # Chalcogen Site Defects States
    State('sub-atom-chal', 'value'),
    State('chal-sub-conc', 'value'),
    State('vac-one-conc', 'value'),
    State('vac-two-conc', 'value'),
    State('sub-two-conc', 'value'),
    State('sub-one-conc', 'value'),
    
    # Microscope Settings States
    State('voltage', 'value'),
    State('aperture', 'value'),
    State('defocus', 'value'),
    State('dwell-time', 'value'),
    
    # Aberration Coefficients States
    State('cs3-mean', 'value'),
    State('cs3-std', 'value'),
    State('cs5-mean', 'value'),
    State('cs5-std', 'value'),
    
    # ADF Settings States
    State('adf-angle-min', 'value'),
    State('adf-angle-max', 'value'),
    
    # Gaussian Parameters States
    State('src-size-mean', 'value'),
    State('defoc-spread-mean', 'value'),
    State('probe-cur-mean', 'value'),
    State('src-size-std', 'value'),
    State('defoc-spread-std', 'value'),
    State('probe-cur-std', 'value'),
    
    prevent_initial_call=True
)
def store_parameters(n_clicks, batch_size, mat_name, pixel_size, metal_atom, 
                     lattice_const, img_size, chal_atom, sub_atom_metal,
                     metal_sub_conc, metal_vac_conc, sub_atom_chal,
                     chal_sub_conc, vac_one_conc, vac_two_conc,
                     sub_two_conc, sub_one_conc,
                     voltage, aperture, defocus, dwell_time,
                     cs3_mean, cs3_std, cs5_mean, cs5_std,
                     adf_angle_min, adf_angle_max,
                     src_size_mean, defoc_spread_mean, probe_cur_mean,
                     src_size_std, defoc_spread_std, probe_cur_std):
    
    # If button not clicked, do nothing
    if not n_clicks:
        return dash.no_update, dash.no_update
    
    # Validate that all required inputs are provided
    required_values = [
    mat_name, pixel_size, metal_atom, lattice_const, img_size, chal_atom,
    voltage, aperture, defocus, dwell_time,
    cs3_mean, cs3_std, cs5_mean, cs5_std,
    adf_angle_min, adf_angle_max,
    src_size_mean, defoc_spread_mean, probe_cur_mean,
    src_size_std, defoc_spread_std, probe_cur_std
    ]
    
    # Check for missing or invalid inputs - if any missing, don't store
    for v in required_values:
        if v is None or v == '':
            return dash.no_update, dash.no_update
    
    # All inputs are valid - create parameter dictionary
    parameters = {
        'batch_size': batch_size,
        'material_properties': {
            'material_name': mat_name,
            'pixel_size': pixel_size,
            'metal_atom_number': metal_atom,
            'lattice_constant': lattice_const,
            'image_size': img_size,
            'chalcogen_atom_number': chal_atom
        },
        'metal_site_defects': {
            'substitution_atom_number': sub_atom_metal,
            'substitution_concentration': metal_sub_conc,
            'vacancy_concentration': metal_vac_conc
        },
        'chalcogen_site_defects': {
            'substitution_atom_number': sub_atom_chal,
            'substitution_concentration': chal_sub_conc,
            'vacancy_one_concentration': vac_one_conc,
            'vacancy_two_concentration': vac_two_conc,
            'substitution_two_concentration': sub_two_conc,
            'substitution_one_concentration': sub_one_conc
        },
        'microscope_settings': {
            'voltage': voltage,
            'aperture': aperture,
            'defocus': defocus,
            'dwell_time': dwell_time
        },
        'aberration_coefficients': {
            'cs3_mean': cs3_mean,
            'cs3_std': cs3_std,
            'cs5_mean': cs5_mean,
            'cs5_std': cs5_std
        },
        'adf_settings': {
            'angle_min': adf_angle_min,
            'angle_max': adf_angle_max
        },
        'gaussian_parameters': {
            'source_size_mean': src_size_mean,
            'defocus_spread_mean': defoc_spread_mean,
            'probe_current_mean': probe_cur_mean,
            'source_size_std': src_size_std,
            'defocus_spread_std': defoc_spread_std,
            'probe_current_std': probe_cur_std
        }
    }
    
    return parameters, ""


# Register display values callback
register_display_values_callback(app)


if __name__ == "__main__":
    app.run(debug=True)