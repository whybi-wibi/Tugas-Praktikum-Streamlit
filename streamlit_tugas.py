import streamlit as st


# ========== HITUNG LUAS ========== #
def luas_segitiga(a, t):
    return (a * t) / 2

def luas_persegi_panjang(p, l):
    return p * l

def luas_jajar_genjang(a, t):
    return a * t


# ========== HITUNG KELILING ========== #

def keliling_segitiga(a, b, c):
    return a + b + c

def keliling_persegi_panjang(p, l):
    return 2 * (p + l)

def keliling_jajar_genjang(a, b):
    return 2 * (a + b)


# ========== DICTIONARY ========== #

hitungluas = {
    "Luas Segitiga": {
        "Fungsi": luas_segitiga,
        "Inputan": ['Alas', 'Tinggi'],
    },
    "Luas Persegi Panjang": {
        "Fungsi": luas_persegi_panjang,
        "Inputan": ['Panjang', 'Lebar'],
    },
    "Luas Jajar Genjang": {
        "Fungsi": luas_jajar_genjang,
        "Inputan": ['Alas', 'Tinggi'],
    }
}

hitungkeliling = {
    "Keliling Segitiga": {
        "Fungsi": keliling_segitiga,
        "Inputan": ['Sisi A', 'Sisi B', 'Sisi C'],
    },
    "Keliling Persegi Panjang": {
        "Fungsi": keliling_persegi_panjang,
        "Inputan": ['Panjang', 'Lebar'],
    },
    "Keliling Jajar Genjang": {
        "Fungsi": keliling_jajar_genjang,
        "Inputan": ['Sisi A', 'Sisi B'],
    }
}


# ========== STREAMLIT APP ========== #


def pilih_rumus(option):
    allRumus = {}

    if option == "Hitung Luas":
        allRumus = hitungluas
    elif option == "Hitung Keliling":
        allRumus = hitungkeliling
    return allRumus

st.title("Kalkulator Luas dan Keliling Bangun Datar")
opt = st.selectbox(
    "Pilih Jenis Perhitungan:",
    ("Hitung Luas", "Hitung Keliling")
)

allRumus = pilih_rumus(opt)
pilih_hitung = st.radio(
    label = "Pilih Hitung",
    options=allRumus.keys(),
    horizontal=True
)

inputs = [st.number_input(label, value=0.0) for label in allRumus[pilih_hitung]['Inputan']]

if st.button("Hitung"):
    hasil = allRumus[pilih_hitung]['Fungsi'](*inputs)
    st.markdown(f'<h2 style="color: green; text-align: center;">Hasil: {hasil}</h2>', 
                unsafe_allow_html=True)