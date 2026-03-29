import streamlit as st
import pandas as pd
import math
import ipaddress

st.title("VLSM Calculator & Visualizer")

reseau_choisis = st.text_input("Réseau de base (ex: 192.168.1.0/24)")

n = st.number_input("Nombre de sous-réseaux", min_value=1, max_value=10, value=3)

hotes = []

st.subheader("Besoins en hôtes")

for i in range(n):
    h = st.number_input(f"Sous-réseau {i+1}", min_value=1, value=10, key=i)
    hotes.append(h)

def calcul_vlsm(network, hosts):
    hosts.sort(reverse=True)
    net = ipaddress.ip_network(network, strict=False)

    ip = int(net.network_address)
    results = []

    for h in hosts:
        size = h + 2
        bits = math.ceil(math.log2(size))
        taille_masque = 2 ** bits
        cidr = 32 - bits

        subnet = ipaddress.ip_network((ip, cidr), strict=False)

        results.append({
            "Hôtes demandés": h,
            "CIDR": f"/{cidr}",
            "Masque": str(subnet.netmask),
            "Réseau": str(subnet.network_address),
            "Première IP": str(list(subnet.hosts())[0]),
            "Dernière IP": str(list(subnet.hosts())[-1]),
            "Broadcast": str(subnet.broadcast_address)
        })

        ip = ip + taille_masque

    return pd.DataFrame(results)

if st.button("Calculer VLSM"):
    if reseau_choisis:
        df = calcul_vlsm(reseau_choisis, hotes)
        st.subheader("Résultat")
        st.dataframe(df)

        st.subheader("Visualisation")
        st.bar_chart(df["Hôtes demandés"])
    else:
        st.error("Entre un réseau valide")