from dash import Dash, html,dcc,Input,Output,callback
from PIL import Image
import base64


#using direct image file path
image_path='C:\\Users\\Admin\\Desktop\\DSAIL\\assets\\puppy3.jpg'

#using pillow to read the image
pil_img=Image.open('C:\\Users\\Admin\\Desktop\\DSAIL\\assets\\puppy3.jpg')

#using base64 to encode and decode
def b64_image(image_filename):
    with open(image_filename,'rb') as f:
        image=f.read()
    return 'data:image,'+base64.b64encode(image).decode('utf-8')

#intialize the app
app=Dash(__name__)

#app layout
app.layout=html.Div([html.H1("MY DASH APP",style={'text-align':'center','color':'blue'}),
                     html.H2('dash puppies',style={'color':'red'}),
                     html.Img(src=image_path),
                     html.Img(src=app.get_asset_url('my_image.png')),
                     html.Img(src=pil_img),
                    
                     html.Br(),
                     html.Br(),
                     html.Div([
                         html.Label("first feature"),
                         dcc.Dropdown(["long ears","medim nose","short legs"],
                         value='long ears',
                         id="feature_one"),
                         
                         html.Br(),
                         html.Label("second feature"),
                         dcc.Dropdown(["long ears","medim nose","short legs"],
                         value='short legs',
                         id="feature_two"),
                         
                         html.Br(),
                         html.Label("third feature"),
                         dcc.Dropdown(["long ears","medim nose","short legs"],
                         value='medim nose',
                         id="feature_three"),
                         
                         html.Br(),
                         html.Button('SAVE',id='save-button',n_clicks=0),
                         html.Div(id='container')
                     ])
])
@callback(
    Output('container', 'children'),
    [Input('feature_one', 'value'),
     Input('feature_two', 'value'),
     Input('feature_three', 'value'),
     Input('save-button', 'n_clicks')
           ]
)
def update_inputs(selected_value1):
    print(selected_value1)
    return {selected_value1}

def update_input(selected_value2):
    print(selected_value2)
    return{selected_value2}

def updated_input(selected_value3):
    print(selected_value3)
    return{selected_value3}





#running the app
if __name__=='__main__':
    app.run_server(debug=True)

