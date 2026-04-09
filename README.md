# 🌐 VLSM Calculator & Visualizer

An interactive web application that computes and visualizes **Variable Length Subnet Masking (VLSM)** addressing plans. Built with Python and Streamlit, it takes a base network and a list of host requirements, then outputs an optimized subnetting plan.

> Personal project — built to practice networking concepts and web app development with Streamlit

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Features

- Input: base network address (e.g., `192.168.1.0/24`) and host requirements per subnet
- Automatic VLSM calculation with optimal subnet allocation
- Visual representation of the addressing plan
- Subnet details: network address, broadcast, usable range, mask, CIDR notation
- Interactive Streamlit web interface — no installation needed for end users

## How VLSM works

VLSM allows subnets of different sizes within the same network, unlike fixed-length subnetting. The algorithm:

1. Sorts subnets by size (largest first)
2. Allocates the smallest power-of-2 block that fits each requirement
3. Assigns network addresses sequentially to avoid overlap

## Tech stack

| Component | Technology |
|-----------|-----------|
| Language | Python |
| Web framework | Streamlit |
| Networking | ipaddress (stdlib) |

## Getting started

```bash
git clone https://github.com/AmZzPYJS/VLSM-Calculator-and-Vizualisation-Python.git
cd VLSM-Calculator-and-Vizualisation-Python
pip install -r requirements.txt
streamlit run app.py
```

## What I learned

- Implementing VLSM subnetting logic from scratch using Python's `ipaddress` module
- Building interactive web applications with Streamlit (widgets, layouts, session state)
- Translating networking theory (subnet masks, CIDR, broadcast addresses) into working code
- Designing a user-friendly interface for a technical tool

## License

MIT
