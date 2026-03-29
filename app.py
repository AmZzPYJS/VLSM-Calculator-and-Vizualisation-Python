import streamlit as st
import pandas as pd
import math
import ipaddress

st.title("VLSM Calculator & Visualizer")
st.markdown("### Fait par Amîn Mezouer")

reseau_base = st.text_input("Réseau de base (ex: 192.168.1.0/24)")

nombre_sous_reseaux = st.number_input(
    "Nombre de sous-réseaux",
    min_value=1,
    max_value=10,
    value=3
)

liste_hotes = []

st.subheader("Besoins en hôtes")

for i in range(nombre_sous_reseaux):
    nb = st.number_input(
        f"Sous-réseau {i+1}",
        min_value=1,
        value=10,
        key=i
    )
    liste_hotes.append(nb)

def calcul_vlsm(reseau, besoins_hotes):
    besoins_hotes.sort(reverse=True)

    reseau_ip = ipaddress.ip_network(reseau, strict=False)
    ip_courante = int(reseau_ip.network_address)

    resultats = []

    for h in besoins_hotes:
        taille = h + 2
        bits = math.ceil(math.log2(taille))
        taille_sous_reseau = 2 ** bits
        cidr = 32 - bits

        sous_reseau = ipaddress.ip_network((ip_courante, cidr), strict=False)

        resultats.append({
            "Hôtes demandés": h,
            "CIDR": f"/{cidr}",
            "Masque": str(sous_reseau.netmask),
            "Réseau": str(sous_reseau.network_address),
            "Première IP": str(list(sous_reseau.hosts())[0]),
            "Dernière IP": str(list(sous_reseau.hosts())[-1]),
            "Broadcast": str(sous_reseau.broadcast_address)
        })

        ip_courante += taille_sous_reseau

    return pd.DataFrame(resultats)

if st.button("Calculer VLSM"):

    if reseau_base:

        tableau_resultat = calcul_vlsm(reseau_base, liste_hotes)
        st.subheader("Résultat")
        st.dataframe(tableau_resultat)

        st.subheader("Découpage du réseau")
        couleurs = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFA07A"]

        for i in range(len(tableau_resultat)):
            st.markdown(
                f"""
                <div style="
                    background-color:{couleurs[i % len(couleurs)]};
                    padding:15px;
                    margin:5px;
                    border-radius:10px;
                    text-align:center;
                    color:black;
                    font-weight:bold;">
                    {tableau_resultat.iloc[i]['Réseau']} {tableau_resultat.iloc[i]['CIDR']}
                </div>
                """,
                unsafe_allow_html=True
            )

    else:
        st.error(":warning: Veuillez entrer un réseau valide")

