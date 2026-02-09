import streamlit as st

# Säulen-Datenbank mit Empfehlungen
COLUMN_DATABASE = {
    "Affinity": {
        "HisTag": {
            "columns": [
                {
                    "name": "HisTrap HP (Cytiva, 17524801)",
                    "binding_capacity": "~40 mg/mL",
                    "features": "Ni-Sepharose High Performance, Standard for most His-Tag proteins",
                    "best_for": "Routine purifications, good balance between purity and capacity"
                },
                {
                    "name": "PureCube Ni-INDIGO (Cube-Biotech, 75306)",
                    "binding_capacity": "~80 mg/mL",
                    "features": "6% highly cross-linked agarose, tolerates EDTA and DTT to 20mM",
                    "best_for": "Routine purifications, proteins where high EDTA and DTT amounts are needed"
                },
                {
                    "name": "HiTrap TALON Crude (Cytiva, 29048565)",
                    "binding_capacity": "~20 mg/mL",
                    "features": "Loaded with Cobalt(II) instead of Nickel, Crude technically means that no pre-clearing of the lysate is needed",
                    "best_for": "Weak nickel binding proteins"
                }
            ]
        },
        "GSTag": {
            "columns": [
                {
                    "name": "GSTrap HP (Cytiva, 17528201)",
                    "binding_capacity": "~10 mg/mL",
                    "features": "One-step purifications of glutathione S-Transferase (GST) tagged proteins, Mild elution conditions",
                    "best_for": "GST-fusion Proteins, mild elution preserves protein antigenicity and function"
                }
            ]
        },
        "Strep-Tag / Strep-Tag II": {
            "columns": [
                {
                    "name": "Strep-Tactin® 4Flow® high capacity (IBA, 2-1257-001)",
                    "binding_capacity": "~20 mg/mL",
                    "features": "Elution with 2.5mM d-Desthiobiotin, binding of Biotin possible - therefore use biotin blocking if necessary",
                    "best_for": "Purification of Strep-tag®II and Twin-Strep-tag® fusion proteins"
                },
                {
                    "name": "Strep-Tactin®XT 4Flow® (IBA, 2-5023-001)",
                    "binding_capacity": "~11 mg/mL",
                    "features": "Outstanding target purity (>95%) and high binding affinity, best for low expressing proteins, elution with 50mM Biotin",
                    "best_for": "Purification of Strep-tag®II and Twin-Strep-tag® fusion proteins"
                }
            ]
        },
        "FLAG-Tag": {
            "columns": [
                {
                    "name": "Anti-FLAG M2 Affinity Gel (Sigma)",
                    "binding_capacity": ">600 μg/mL",
                    "features": "Monoclonal anti-FLAG antibody, mild elution with FLAG peptide",
                    "best_for": "Standard FLAG-Tag purification"
                },
                {
                    "name": "Anti-FLAG M1 Agarose (Sigma)",
                    "binding_capacity": "~400 μg/mL",
                    "features": "Ca2+-dependent binding, EDTA elution possible",
                    "best_for": "When peptide elution should be avoided"
                }
            ]
        },
        "MYC-Tag": {
            "columns": [
                {
                    "name": "c-Myc Agarose (Thermo/Pierce)",
                    "binding_capacity": "~200 μg/mL",
                    "features": "Anti-c-Myc antibody coupled",
                    "best_for": "Standard c-Myc (EQKLISEEDL) purification"
                },
                {
                    "name": "c-Myc Magnetic Beads (Thermo)",
                    "binding_capacity": "Variable",
                    "features": "Magnetic beads for fast isolation",
                    "best_for": "Small volumes, Co-IP experiments"
                }
            ]
        },
        "Antibody": {
            "subtypes": {
                "IgG1 (human)": [
                    {
                        "name": "Protein A HP (GE/Cytiva)",
                        "binding": "Very strong",
                        "features": "Highest affinity for human IgG1",
                        "best_for": "Standard choice for human IgG1"
                    },
                    {
                        "name": "Protein G HP (GE/Cytiva)",
                        "binding": "Strong",
                        "features": "Broad species reactivity",
                        "best_for": "Alternative to Protein A"
                    }
                ],
                "IgG2 (human)": [
                    {
                        "name": "Protein A HP (GE/Cytiva)",
                        "binding": "Medium-strong",
                        "features": "Weaker binding than IgG1, higher elution volumes needed",
                        "best_for": "Works, but not optimal"
                    },
                    {
                        "name": "Protein G HP (GE/Cytiva)",
                        "binding": "Strong",
                        "features": "Better binding than Protein A for IgG2",
                        "best_for": "Preferred for human IgG2"
                    },
                    {
                        "name": "Protein A/G (Thermo)",
                        "binding": "Strong",
                        "features": "Combines both binding domains",
                        "best_for": "When IgG subtype is mixed or unknown"
                    }
                ],
                "IgG3 (human)": [
                    {
                        "name": "Protein G HP (GE/Cytiva)",
                        "binding": "Very strong",
                        "features": "Best choice for IgG3",
                        "best_for": "Standard for IgG3"
                    },
                    {
                        "name": "Protein A HP (GE/Cytiva)",
                        "binding": "Weak",
                        "features": "Not recommended for IgG3",
                        "best_for": "Avoid for IgG3"
                    }
                ],
                "IgG4 (human)": [
                    {
                        "name": "Protein A HP (GE/Cytiva)",
                        "binding": "Strong",
                        "features": "Good binding",
                        "best_for": "Standard choice"
                    },
                    {
                        "name": "Protein G HP (GE/Cytiva)",
                        "binding": "Strong",
                        "features": "Also good binding",
                        "best_for": "Alternative to Protein A"
                    }
                ],
                "Mouse IgG1": [
                    {
                        "name": "Protein G HP (GE/Cytiva)",
                        "binding": "Very strong",
                        "features": "Best binding for Mouse IgG1",
                        "best_for": "Standard for Mouse IgG1"
                    },
                    {
                        "name": "Protein A HP (GE/Cytiva)",
                        "binding": "Medium",
                        "features": "Works, but weaker",
                        "best_for": "If Protein G not available"
                    }
                ],
                "Mouse IgG2a": [
                    {
                        "name": "Protein A HP (GE/Cytiva)",
                        "binding": "Very strong",
                        "features": "Excellent binding",
                        "best_for": "Standard choice"
                    },
                    {
                        "name": "Protein G HP (GE/Cytiva)",
                        "binding": "Strong",
                        "features": "Also good",
                        "best_for": "Alternative"
                    }
                ],
                "Mouse IgG2b": [
                    {
                        "name": "Protein A HP (GE/Cytiva)",
                        "binding": "Strong",
                        "features": "Good binding",
                        "best_for": "Standard choice"
                    },
                    {
                        "name": "Protein G HP (GE/Cytiva)",
                        "binding": "Very strong",
                        "features": "Best binding",
                        "best_for": "Preferred for Mouse IgG2b"
                    }
                ],
                "Mouse IgG3": [
                    {
                        "name": "Protein A HP (GE/Cytiva)",
                        "binding": "None/very weak",
                        "features": "NOT recommended",
                        "best_for": "Avoid!"
                    },
                    {
                        "name": "Protein G HP (GE/Cytiva)",
                        "binding": "Weak",
                        "features": "Suboptimal",
                        "best_for": "Only if no alternative"
                    },
                    {
                        "name": "Anti-Mouse IgG Agarose",
                        "binding": "Strong",
                        "features": "Specific for Mouse IgG",
                        "best_for": "BEST choice for Mouse IgG3"
                    }
                ],
                "Rat IgG": [
                    {
                        "name": "Protein G HP (GE/Cytiva)",
                        "binding": "Strong",
                        "features": "Good binding for most Rat IgG",
                        "best_for": "Standard choice"
                    },
                    {
                        "name": "Protein A HP (GE/Cytiva)",
                        "binding": "Weak-medium",
                        "features": "Subtype-dependent",
                        "best_for": "Not first choice"
                    }
                ]
            }
        }
    },
    "Size Exclusion": {
        "columns": [
            {
                "name": "Superdex 200 Increase 10/300 GL",
                "separation_range": "10 - 600 kDa",
                "best_for": "Standard for most proteins, good resolution"
            },
            {
                "name": "Superdex 75 Increase 10/300 GL",
                "separation_range": "3 - 70 kDa",
                "best_for": "Smaller proteins, peptides, better resolution in lower MW range"
            },
            {
                "name": "Superose 6 Increase 10/300 GL",
                "separation_range": "5 - 5000 kDa",
                "best_for": "Large protein complexes, virus-like particles"
            },
            {
                "name": "Superdex 200 Increase 3.2/300",
                "separation_range": "10 - 600 kDa",
                "best_for": "Analytical runs, small sample amounts"
            },
            {
                "name": "HiLoad Superdex 200 pg 16/600",
                "separation_range": "10 - 600 kDa",
                "best_for": "Preparative runs, larger volumes, higher resolution"
            }
        ]
    }
}

# Streamlit App
st.set_page_config(page_title="PhlippSelect", page_icon="🧪", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    /* Main background color with 50% opacity */
    .stApp {
        background-color: rgba(227, 229, 242, 0.5);
    }
    
    /* Style for selectbox */
    div[data-baseweb="select"] > div {
        background-color: rgb(230, 231, 232);
    }
    
    /* Style for expander boxes (column information) */
    .streamlit-expanderHeader {
        background-color: rgb(233, 228, 225) !important;
    }
    
    .streamlit-expanderContent {
        background-color: rgb(233, 228, 225) !important;
    }
    
    details {
        background-color: rgb(233, 228, 225) !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧪 PhlippSelect")
st.markdown("### A tool for optimal column selection in your lab")

# Session State initialisieren
if 'selections' not in st.session_state:
    st.session_state.selections = {}

# Hauptauswahl: Affinity oder Size Exclusion
st.markdown("---")
chrom_type = st.selectbox(
    "**Step 1: Choose chromatography type**",
    ["--- Please select ---", "Affinity", "Size Exclusion"],
    key="chrom_type"
)

if chrom_type == "Affinity":
    st.markdown("---")
    
    # Tag-Auswahl
    tag_type = st.selectbox(
        "**Step 2: Choose your affinity tag**",
        ["--- Please select ---", "HisTag", "GSTag", "Strep-Tag / Strep-Tag II", 
         "FLAG-Tag", "MYC-Tag", "Antibody"],
        key="tag_type"
    )
    
    if tag_type != "--- Please select ---":
        st.markdown("---")
        
        # Spezialfall: Antibody mit Subtypen
        if tag_type == "Antibody":
            st.info("⚠️ **Important:** The choice of the right column is highly dependent on the IgG subtype!")
            
            antibody_subtype = st.selectbox(
                "**Step 3: Choose antibody subtype**",
                ["--- Please select ---"] + list(COLUMN_DATABASE["Affinity"]["Antibody"]["subtypes"].keys()),
                key="antibody_subtype"
            )
            
            if antibody_subtype != "--- Please select ---":
                st.markdown("---")
                st.success(f"### 🎯 Recommended columns for {antibody_subtype}")
                
                columns = COLUMN_DATABASE["Affinity"]["Antibody"]["subtypes"][antibody_subtype]
                
                for idx, col in enumerate(columns, 1):
                    with st.expander(f"**Option {idx}: {col['name']}** - Binding: {col['binding']}", expanded=True):
                        st.markdown(f"**Binding strength:** {col['binding']}")
                        st.markdown(f"**Features:** {col['features']}")
                        st.markdown(f"**💡 Best for:** {col['best_for']}")
                        
                        # Visual warning for poor binding
                        if "weak" in col['binding'].lower() or "none" in col['binding'].lower():
                            st.warning("⚠️ Caution: Weak/no binding!")
                        elif "very strong" in col['binding'].lower():
                            st.success("✅ Very good binding!")
        
        # All other tags
        else:
            if tag_type in COLUMN_DATABASE["Affinity"]:
                columns = COLUMN_DATABASE["Affinity"][tag_type]["columns"]
                
                for idx, col in enumerate(columns, 1):
                    with st.expander(f"**Option {idx}: {col['name']}**", expanded=True):
                        st.markdown(f"**Binding Capacity:** {col['binding_capacity']}")
                        st.markdown(f"**Features:** {col['features']}")
                        st.markdown(f"**💡 Best for:** {col['best_for']}")

elif chrom_type == "Size Exclusion":
    st.markdown("---")
    st.success("### 🎯 Available SEC columns")
    
    st.info("**Tip:** Choose based on the expected size of your protein/complex")
    
    columns = COLUMN_DATABASE["Size Exclusion"]["columns"]
    
    for idx, col in enumerate(columns, 1):
        with st.expander(f"**{col['name']}** - Separation range: {col['separation_range']}", expanded=False):
            st.markdown(f"**Separation range:** {col['separation_range']}")
            st.markdown(f"**💡 Best for:** {col['best_for']}")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>💡 <b>Tip:</b> This tool is based on standard recommendations. Always consult 
    manufacturer specifications for specific requirements!</p>
    <p style='font-size: 0.8em;'>Developed for your lab 🧬</p>
</div>
""", unsafe_allow_html=True)
