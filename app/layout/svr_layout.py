from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

regression_svr = dbc.Card(          
    children=[
        html.H2(html.B(html.P("Support Vector Regressor", className="card-text"))),
        html.Hr(style={'borderWidth': "0.5vh", "borderColor": "grey"}),

        html.Div(
            [
                    html.H4(html.B("Paramètres généraux")),html.Br(),
                    dbc.Row(
                        [
                            dbc.Col(
                            [
                            dbc.Label("Taille de l'échantillon test", html_for="svr_test_size",style={'font-weight': 'bold'}),
                                ],width=3
                        ),
                        dbc.Col(
                            [
                            dcc.Slider(id='svr_test_size',min=0.1,max=0.5,step=0.1,value=0.3,tooltip={"placement": "bottom", "always_visible": True}),
                            ],width=2
                        ),
                        dbc.Col(
                            width=2
                        ),
                        dbc.Col(
                            [
                            html.B("Random state "),html.I("par défaut=42"),html.P(" Contrôle le brassage appliqué aux données avant d'appliquer le fractionnement. Passer un int pour une sortie reproductible sur plusieurs appels de fonction.", className="card-text"),
                            ],width=3
                        ),
                        dbc.Col(
                            [
                            dcc.Input(id="svr_random_state", type="number", placeholder="input with range",min=1,max=42, step=1,value=42),html.Br(),html.Br(),
                            ],width=1
                        )
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Label("Centrer réduire",  html_for="svr_centrer_reduire",style={'font-weight': 'bold'}),
                            ], width=3
                        ),
                        dbc.Col(
                            [
                            dbc.Checklist(
                                id="svr_centrer_reduire",
                                options=[{"value":"yes"}]
                            )
                            ],width=1
                        )
                    ]
                ),
                html.Br(),
                dbc.Row(
                        [
                            dbc.Col(
                                [
                                html.B("shuffle "),html.I("par défaut shuffle=True"),html.Br(),html.P("s'il faut ou non mélanger les données avant de les diviser.", className="card-text"),
                                ], width=3
                            ),
                            dbc.Col(
                            [
                                dcc.Dropdown(
                                    id='svr_shuffle',
                                    options=[
                                        {'label': 'True', 'value': 'True'},
                                        {'label': 'False', 'value': 'False'},
                                    ],
                                    value = 'True'
                                )
                                ], width=1
                                ),
                            dbc.Col(
                                width=2
                                ),
                            ]
                            ),
                html.Br(),
                html.Hr(style={'borderWidth': "0.5vh", "borderColor": "grey"}),
            ]
        ),

        html.Div(
            [
                # Div des paramètres sur la gauche
                html.Div(
                    children = 
                    [
                        html.H4(html.B("Optimisation des hyperparamètres :")),html.Br(),

                        html.B("GridSearchCV_number_of_folds "),html.I("par défaut=5"),html.Br(),

                        html.P("Selectionner le nombre de fois que vous souhaitez réaliser la validation croisée pour l'optimisation des hyperparamètres.", className="card-text"),
                        dcc.Input(id="svr_gridCV_k_folds", type="number", placeholder="input with range",min=1,max=100, step=1,value=5),html.Br(),html.Br(),
                    
                        html.B("GridSearchCV_scoring "),html.I("par défaut = 'MSE'"),html.Br(),
                        html.P("Selectionner la méthode de scoring pour l'optimisation des hyperparamètres."),
                        dcc.Dropdown(
                            id='svr_gridCV_scoring',
                            options=[
                               {'label': "MSE", 'value': "neg_mean_squared_error"},
                               {'label': "RMSE", 'value': "RMSE"},
                               {'label': "MAE", 'value': "neg_mean_absolute_error"}
                            ],
                            value = 'neg_mean_squared_error'
                        ),html.Br(),html.Br(),

                        html.B("GridSearchCV_njobs "),html.I("par défaut=-1"),html.Br(),
                        html.P("Selectionner le nombre de coeurs (-1 = tous les coeurs)", className="card-text"),
                        dcc.Dropdown(
                            id="svr_GridSearchCV_njobs",
                            options= [{'label': 'None', 'value': 'None'}] + [{'label': -1, 'value': -1}] + [{'label':i, 'value':i} for i in range(1,33)],
                            value = -1
                        ),html.Br(),html.Br(),

                        dbc.Button("valider GridSearchCV",color ="info",id='svr_button_GridSearchCV',n_clicks=0),
                        
                        html.Br(),html.Hr(),




                        # Fit predict
                        html.H4(html.B("Performance du modèle sur le jeu de test :")),html.Br(),
                        html.Br(),html.Br(),

                        # Paramètres de l'algo
                        dbc.Row(
                            [
                                # Type du noyau
                                dbc.Col(
                                    [
                                        dbc.Label("Type de noyau (kernel)", html_for="svr_kernel_selection",style={'font-weight': 'bold'}),
                                        dcc.Dropdown(
                                            id='svr_kernel_selection',
                                            options=[
                                                {'label': 'linéaire', 'value': 'linear'},
                                                {'label': 'polynomial', 'value': 'poly'},
                                                {'label': 'RBF', 'value': 'rbf'},
                                                {'label': 'Sigmoïde', 'value': 'sigmoid'},
                                            ],
                                            value = 'rbf'
                                        ),
                                    ],
                                ),

                                # Degré pour noyau polynomial
                                dbc.Col(
                                    [
                                        dbc.Label("Degré (pour noyau polynomial)", html_for="svr_kernel_selection",style={'font-weight': 'bold'}),
                                        dbc.Input(id='svr_degre',type='number',min=0,max=4,step=1,value=0,),
                                    ],
                                )
                            ]
                        ),

                        html.Br(),
                        dbc.Row(
                            [
                                # Paramètre de régularisation
                                dbc.Col(
                                    [
                                        dbc.Label("Régularisation (C)", html_for="svr_regularisation_selection",style={'font-weight': 'bold'}),
                                        dbc.Input(id='svr_regularisation_selection',type='number',min=0,max=100,step=0.1,value=0.1,),
                                    ],
                                ),
                            ],style={'margin-bottom': '1em'}
                        ),

                        dbc.Row(
                            [
                                # Epsilon 
                                dbc.Col(
                                    [
                                        dbc.Label("Epsilon (ε)",html_for='svr_epsilon',style={'font-weight': 'bold'}),
                                        dbc.Input(id='svr_epsilon',type='number',value=0.1,min=0,max=100,step=0.1),
                                    ],
                                )
                            ]
                        ),
                        html.Br(),
                        dbc.Button("Valider fit & predict", color="danger",id='smv_button',n_clicks=0),

                        html.Br(),html.Hr(),


                        # Validation Croisée

                        html.H4(html.B("Validation croisée :")),html.Br(),

                        html.B("cv_number_of_folds "),html.I("par défaut=5"),html.Br(),
                        html.P("Selectionner le nombre de fois que vous souhaitez réaliser la validation croisée.", className="card-text"),
                        dcc.Input(id="svr_cv_number_of_folds", type="number", placeholder="input with range",min=1,max=100, step=1,value=5),html.Br(),html.Br(),

                        html.B("cv_scoring "),html.I("par défaut = 'MSE'"),html.Br(),
                        html.P("Selectionnez la méthode de scoring pour la validation croisée."),
                        dcc.Dropdown(
                            id='svr_cv_scoring',
                            options=[
                                {'label': "MSE", 'value': "MSE"},
                                {'label': "RMSE", 'value': "RMSE"},
                                {'label': "MAE", 'value': "MAE"},
                            ],
                            value = 'MSE'
                        ),html.Br(),html.Br(),

                        dbc.Button("Valider K-Fold Cross-Validation",id='svr_button_CrossValidation', color="success", n_clicks=0),
                    ],className='col-6'
                ),
                # Div des résultats sur la droite 
                html.Div(
                    [
                        html.H3(html.B("Résultats :")),
                        dcc.Loading(
                            children=[html.Div(id="res_svr_GridSearchCV")], 
                            type="default"
                        ),html.Hr(style={'borderWidth': "0.5vh", "borderColor": "grey"}),
                        
                        dcc.Loading(
                            children=[html.Div(id="res_svr_FitPredict")], 
                            type="default"
                        ),html.Hr(style={'borderWidth': "0.5vh", "borderColor": "grey"}),

                        dcc.Loading(
                            children = [html.Div(id="res_svr_CrossValidation")],
                            type = "default"
                        ),html.Hr(style={'borderWidth': "0.5vh", "borderColor": "grey"})
                    ],
                    className='col-6'
                )
            ],className="row"
        ),
    ],
    body=True
)