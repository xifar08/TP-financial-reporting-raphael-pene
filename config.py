"""Configuration file for the project"""

URL = "https://minio.lab.sspcloud.fr/fabienhos/td-reporting-financial/financial_data.parquet"

PATH_FILE = "template/template_reporting.xlsx"

CONFIG = [
        # Répartition PP/PM
        {'row': 8, 'formule': 'COUNTIF', 'args': [('B', 'PP')]},
        {'row': 9, 'formule': 'COUNTIF', 'args': [('B', 'PM')]},
        {'row': 10, 'formule': 'SUM', 'args': ['E8:E9']},
        
        # Scores V/O/R
        {'row': 14, 'formule': 'COUNTIFS', 'args': [('B', 'PP'), ('D', 'V')]},
        {'row': 15, 'formule': 'COUNTIFS', 'args': [('B', 'PP'), ('D', 'O')]},
        {'row': 16, 'formule': 'COUNTIFS', 'args': [('B', 'PP'), ('D', 'R')]},
        {'row': 17, 'formule': 'COUNTIFS', 'args': [('B', 'PP'), ('D', 'M')]},
        
        # DRC Complet
        {'row': 22, 'formule': 'COUNTIFS', 'args': [('B', 'PP'), ('G', "VRAI")]},
        {'row': 23, 'formule': 'COUNTIFS', 'args': [('B', 'PM'), ('G', "VRAI")]},
        {'row': 24, 'formule': 'SUM', 'args': ['E22:E23']},
        # Focus V/O avec DRC
        {'row': 28, 'formule': 'COUNTIFS', 'args': [('B', 'PP'), ('D', 'V')]},
        {'row': 29, 'formule': 'COUNTIFS', 'args': [('B', 'PM'), ('D', 'V')]},
        {'row': 30, 'formule': 'SUM', 'args': ['E28:E29']},
    ]
