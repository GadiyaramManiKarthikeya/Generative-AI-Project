import streamlit as st
import random

st.title(" AI Fashion Designer")
st.write("Generate AI-based outfit ideas, patterns, and style recommendations.")

colors = ["Red", "Blue", "Black", "White", "Pink", "Yellow", "Green", "Purple"]
patterns = ["Floral", "Geometric", "Abstract", "Striped", "Polka Dots", "Digital Print"]
outfits = ["Dress", "Kurta", "Top", "Saree", "Shirt", "Hoodie", "Gown", "Skirt"]
styles = ["Modern", "Traditional", "Fusion", "Party Wear", "Casual", "Elegant", "Designer"]
fabrics = ["Cotton", "Silk", "Chiffon", "Denim", "Rayon", "Linen"]

def generate_design():
    return {
        "Outfit": random.choice(outfits),
        "Style": random.choice(styles),
        "Color": random.choice(colors),
        "Pattern": random.choice(patterns),
        "Fabric": random.choice(fabrics)
    }

if st.button("Generate Fashion Design"):
    design = generate_design()
    st.subheader(" AI-Generated Fashion Idea")
    st.write(f"**Outfit Type:** {design['Outfit']}")
    st.write(f"**Style:** {design['Style']}")
    st.write(f"**Color:** {design['Color']}")
    st.write(f"**Pattern:** {design['Pattern']}")
    st.write(f"**Fabric:** {design['Fabric']}")

st.write("---")
st.caption("AI Fashion Designer  Generative AI Project")
