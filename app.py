import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')

# 2. Ventes par produit 

figure2 = px.bar(
    données,
    x='produit',
    y='qte',
    title='Ventes par produit (quantité)',
    color='produit'
)

figure2.write_html('ventes-par-produit.html')
print('ventes-par-produit.html généré avec succès !')


# 3. Chiffre d’affaires par produit

# Calcul du CA
données['ca'] = données['qte'] * données['prix']

figure3 = px.bar(
    données,
    x='produit',
    y='ca',
    title="Chiffre d'affaires par produit",
    color='produit'
)

figure3.write_html('ca-par-produit.html')
print('ca-par-produit.html généré avec succès !')

