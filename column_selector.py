import streamlit as st

# Säulen-Datenbank mit Empfehlungen
COLUMN_DATABASE = {
    "Affinity": {
        "HisTag": {
            "columns": [
                {
                    "name": "HisTrap HP (GE/Cytiva)",
                    "binding_capacity": "40 mg/mL",
                    "features": "Standard für die meisten His-Tag Proteine, Ni-Sepharose High Performance",
                    "best_for": "Routine Reinigungen, gute Balance zwischen Reinheit und Kapazität"
                },
                {
                    "name": "HisTrap FF (GE/Cytiva)",
                    "binding_capacity": "40 mg/mL",
                    "features": "Fast Flow, größere Partikel für schnellere Durchflussraten",
                    "best_for": "Große Volumina, weniger druckempfindliche Systeme"
                },
                {
                    "name": "TALON Crude (Takara)",
                    "binding_capacity": "10-15 mg/mL",
                    "features": "Co2+ statt Ni2+, geringere unspezifische Bindung",
                    "best_for": "Rohextrakte mit vielen kontaminierenden Proteinen"
                },
                {
                    "name": "Ni-NTA Superflow (Qiagen)",
                    "binding_capacity": "50 mg/mL",
                    "features": "Sehr hohe Kapazität, NTA-Chelatierung",
                    "best_for": "Maximale Ausbeute bei begrenztem Probenmaterial"
                }
            ]
        },
        "GSTag": {
            "columns": [
                {
                    "name": "GSTrap HP (GE/Cytiva)",
                    "binding_capacity": "10 mg GST/mL",
                    "features": "Glutathione Sepharose 4B, Standard für GST-Fusion",
                    "best_for": "Standard GST-Fusionsproteine"
                },
                {
                    "name": "GST SpinTrap (GE/Cytiva)",
                    "binding_capacity": "10 mg/mL",
                    "features": "Spin-Format für kleine Volumina",
                    "best_for": "Schnelle Reinigung kleiner Mengen, kein FPLC nötig"
                }
            ]
        },
        "Strep-Tag": {
            "columns": [
                {
                    "name": "StrepTrap HP (GE/Cytiva)",
                    "binding_capacity": "600 μg/mL",
                    "features": "Strep-Tactin Sepharose, milde Elution",
                    "best_for": "Standard Strep-Tag (WSHPQFEK)"
                },
                {
                    "name": "Strep-Tactin XT 4Flow (IBA)",
                    "binding_capacity": "2-3 mg/mL",
                    "features": "Höhere Kapazität, für Twin-Strep-Tag optimiert",
                    "best_for": "Twin-Strep-Tag, höhere Ausbeuten"
                }
            ]
        },
        "Strep-Tag II": {
            "columns": [
                {
                    "name": "Strep-Tactin XT (IBA)",
                    "binding_capacity": "2-3 mg/mL",
                    "features": "Optimiert für Strep-Tag II (WSHPQFEK), milde Elution mit Biotin",
                    "best_for": "Standard für Strep-Tag II, sehr sanfte Bedingungen"
                },
                {
                    "name": "MagStrep Type3 XT (IBA)",
                    "binding_capacity": "~1 mg/mL",
                    "features": "Magnetische Beads, kein Säulenlauf nötig",
                    "best_for": "Kleine Volumina, Hochdurchsatz-Screening"
                }
            ]
        },
        "FLAG-Tag": {
            "columns": [
                {
                    "name": "Anti-FLAG M2 Affinity Gel (Sigma)",
                    "binding_capacity": ">600 μg/mL",
                    "features": "Monoklonaler Anti-FLAG Antikörper, milde Elution mit FLAG-Peptid",
                    "best_for": "Standard FLAG-Tag Reinigung"
                },
                {
                    "name": "Anti-FLAG M1 Agarose (Sigma)",
                    "binding_capacity": "~400 μg/mL",
                    "features": "Ca2+-abhängige Bindung, EDTA-Elution möglich",
                    "best_for": "Wenn Peptid-Elution vermieden werden soll"
                }
            ]
        },
        "MYC-Tag": {
            "columns": [
                {
                    "name": "c-Myc Agarose (Thermo/Pierce)",
                    "binding_capacity": "~200 μg/mL",
                    "features": "Anti-c-Myc Antikörper gekoppelt",
                    "best_for": "Standard c-Myc (EQKLISEEDL) Reinigung"
                },
                {
                    "name": "c-Myc Magnetic Beads (Thermo)",
                    "binding_capacity": "Variable",
                    "features": "Magnetische Beads für schnelle Isolation",
                    "best_for": "Kleine Volumina, Co-IP Experimente"
                }
            ]
        },
        "Antibody": {
            "subtypes": {
                "IgG1 (human)": [
                    {
                        "name": "Protein A HP (GE/Cytiva)",
                        "binding": "Sehr stark",
                        "features": "Höchste Affinität für human IgG1",
                        "best_for": "Standard-Wahl für human IgG1"
                    },
                    {
                        "name": "Protein G HP (GE/Cytiva)",
                        "binding": "Stark",
                        "features": "Breite Spezies-Reaktivität",
                        "best_for": "Alternative zu Protein A"
                    }
                ],
                "IgG2 (human)": [
                    {
                        "name": "Protein A HP (GE/Cytiva)",
                        "binding": "Mittel-stark",
                        "features": "Schwächere Bindung als IgG1, höhere Elutionsvolumen nötig",
                        "best_for": "Funktioniert, aber nicht optimal"
                    },
                    {
                        "name": "Protein G HP (GE/Cytiva)",
                        "binding": "Stark",
                        "features": "Bessere Bindung als Protein A für IgG2",
                        "best_for": "Bevorzugt für human IgG2"
                    },
                    {
                        "name": "Protein A/G (Thermo)",
                        "binding": "Stark",
                        "features": "Kombiniert beide Bindungsdomänen",
                        "best_for": "Wenn IgG-Subtyp gemischt oder unbekannt"
                    }
                ],
                "IgG3 (human)": [
                    {
                        "name": "Protein G HP (GE/Cytiva)",
                        "binding": "Sehr stark",
                        "features": "Beste Wahl für IgG3",
                        "best_for": "Standard für IgG3"
                    },
                    {
                        "name": "Protein A HP (GE/Cytiva)",
                        "binding": "Schwach",
                        "features": "Nicht empfohlen für IgG3",
                        "best_for": "Vermeiden bei IgG3"
                    }
                ],
                "IgG4 (human)": [
                    {
                        "name": "Protein A HP (GE/Cytiva)",
                        "binding": "Stark",
                        "features": "Gute Bindung",
                        "best_for": "Standard-Wahl"
                    },
                    {
                        "name": "Protein G HP (GE/Cytiva)",
                        "binding": "Stark",
                        "features": "Ebenfalls gute Bindung",
                        "best_for": "Alternative zu Protein A"
                    }
                ],
                "Mouse IgG1": [
                    {
                        "name": "Protein G HP (GE/Cytiva)",
                        "binding": "Sehr stark",
                        "features": "Beste Bindung für Mouse IgG1",
                        "best_for": "Standard für Mouse IgG1"
                    },
                    {
                        "name": "Protein A HP (GE/Cytiva)",
                        "binding": "Mittel",
                        "features": "Funktioniert, aber schwächer",
                        "best_for": "Wenn Protein G nicht verfügbar"
                    }
                ],
                "Mouse IgG2a": [
                    {
                        "name": "Protein A HP (GE/Cytiva)",
                        "binding": "Sehr stark",
                        "features": "Exzellente Bindung",
                        "best_for": "Standard-Wahl"
                    },
                    {
                        "name": "Protein G HP (GE/Cytiva)",
                        "binding": "Stark",
                        "features": "Ebenfalls gut",
                        "best_for": "Alternative"
                    }
                ],
                "Mouse IgG2b": [
                    {
                        "name": "Protein A HP (GE/Cytiva)",
                        "binding": "Stark",
                        "features": "Gute Bindung",
                        "best_for": "Standard-Wahl"
                    },
                    {
                        "name": "Protein G HP (GE/Cytiva)",
                        "binding": "Sehr stark",
                        "features": "Beste Bindung",
                        "best_for": "Bevorzugt für Mouse IgG2b"
                    }
                ],
                "Mouse IgG3": [
                    {
                        "name": "Protein A HP (GE/Cytiva)",
                        "binding": "Keine/sehr schwach",
                        "features": "NICHT empfohlen",
                        "best_for": "Vermeiden!"
                    },
                    {
                        "name": "Protein G HP (GE/Cytiva)",
                        "binding": "Schwach",
                        "features": "Suboptimal",
                        "best_for": "Nur wenn keine Alternative"
                    },
                    {
                        "name": "Anti-Mouse IgG Agarose",
                        "binding": "Stark",
                        "features": "Spezifisch für Mouse IgG",
                        "best_for": "BESTE Wahl für Mouse IgG3"
                    }
                ],
                "Rat IgG": [
                    {
                        "name": "Protein G HP (GE/Cytiva)",
                        "binding": "Stark",
                        "features": "Gute Bindung der meisten Rat IgG",
                        "best_for": "Standard-Wahl"
                    },
                    {
                        "name": "Protein A HP (GE/Cytiva)",
                        "binding": "Schwach-mittel",
                        "features": "Subtyp-abhängig",
                        "best_for": "Nicht erste Wahl"
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
                "best_for": "Standard für die meisten Proteine, gute Auflösung"
            },
            {
                "name": "Superdex 75 Increase 10/300 GL",
                "separation_range": "3 - 70 kDa",
                "best_for": "Kleinere Proteine, Peptide, bessere Auflösung im unteren MW-Bereich"
            },
            {
                "name": "Superose 6 Increase 10/300 GL",
                "separation_range": "5 - 5000 kDa",
                "best_for": "Große Proteinkomplexe, Virus-ähnliche Partikel"
            },
            {
                "name": "Superdex 200 Increase 3.2/300",
                "separation_range": "10 - 600 kDa",
                "best_for": "Analytische Läufe, geringe Probenmengen"
            },
            {
                "name": "HiLoad Superdex 200 pg 16/600",
                "separation_range": "10 - 600 kDa",
                "best_for": "Präparative Läufe, größere Volumina, höhere Auflösung"
            }
        ]
    }
}

# Streamlit App
st.set_page_config(page_title="Chromatography Column Selector", page_icon="🧪", layout="wide")

st.title("🧪 Chromatography Column Selector")
st.markdown("### Ein Tool zur optimalen Säulenauswahl für euer Labor")

# Session State initialisieren
if 'selections' not in st.session_state:
    st.session_state.selections = {}

# Hauptauswahl: Affinity oder Size Exclusion
st.markdown("---")
chrom_type = st.selectbox(
    "**Schritt 1: Wähle die Chromatographie-Art**",
    ["--- Bitte wählen ---", "Affinity", "Size Exclusion"],
    key="chrom_type"
)

if chrom_type == "Affinity":
    st.markdown("---")
    
    # Tag-Auswahl
    tag_type = st.selectbox(
        "**Schritt 2: Wähle deinen Affinity Tag**",
        ["--- Bitte wählen ---", "HisTag", "GSTag", "Strep-Tag", "Strep-Tag II", 
         "FLAG-Tag", "MYC-Tag", "Antibody"],
        key="tag_type"
    )
    
    if tag_type != "--- Bitte wählen ---":
        st.markdown("---")
        
        # Spezialfall: Antibody mit Subtypen
        if tag_type == "Antibody":
            st.info("⚠️ **Wichtig:** Die Wahl der richtigen Säule ist stark vom IgG-Subtyp abhängig!")
            
            antibody_subtype = st.selectbox(
                "**Schritt 3: Wähle den Antikörper-Subtyp**",
                ["--- Bitte wählen ---"] + list(COLUMN_DATABASE["Affinity"]["Antibody"]["subtypes"].keys()),
                key="antibody_subtype"
            )
            
            if antibody_subtype != "--- Bitte wählen ---":
                st.markdown("---")
                st.success(f"### 🎯 Empfohlene Säulen für {antibody_subtype}")
                
                columns = COLUMN_DATABASE["Affinity"]["Antibody"]["subtypes"][antibody_subtype]
                
                for idx, col in enumerate(columns, 1):
                    with st.expander(f"**Option {idx}: {col['name']}** - Bindung: {col['binding']}", expanded=True):
                        st.markdown(f"**Bindungsstärke:** {col['binding']}")
                        st.markdown(f"**Features:** {col['features']}")
                        st.markdown(f"**💡 Best for:** {col['best_for']}")
                        
                        # Visuelle Warnung bei schlechter Bindung
                        if "schwach" in col['binding'].lower() or "keine" in col['binding'].lower():
                            st.warning("⚠️ Vorsicht: Schwache/keine Bindung!")
                        elif "sehr stark" in col['binding'].lower():
                            st.success("✅ Sehr gute Bindung!")
        
        # Alle anderen Tags
        else:
            st.success(f"### 🎯 Empfohlene Säulen für {tag_type}")
            
            if tag_type in COLUMN_DATABASE["Affinity"]:
                columns = COLUMN_DATABASE["Affinity"][tag_type]["columns"]
                
                for idx, col in enumerate(columns, 1):
                    with st.expander(f"**Option {idx}: {col['name']}**", expanded=True):
                        st.markdown(f"**Binding Capacity:** {col['binding_capacity']}")
                        st.markdown(f"**Features:** {col['features']}")
                        st.markdown(f"**💡 Best for:** {col['best_for']}")

elif chrom_type == "Size Exclusion":
    st.markdown("---")
    st.success("### 🎯 Verfügbare SEC-Säulen")
    
    st.info("**Tipp:** Wähle basierend auf der erwarteten Größe deines Proteins/Komplexes")
    
    columns = COLUMN_DATABASE["Size Exclusion"]["columns"]
    
    for idx, col in enumerate(columns, 1):
        with st.expander(f"**{col['name']}** - Trennbereich: {col['separation_range']}", expanded=False):
            st.markdown(f"**Trennbereich:** {col['separation_range']}")
            st.markdown(f"**💡 Best for:** {col['best_for']}")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>💡 <b>Tipp:</b> Dieses Tool basiert auf Standard-Empfehlungen. Bei speziellen Anforderungen 
    immer zusätzlich die Herstellerangaben konsultieren!</p>
    <p style='font-size: 0.8em;'>Entwickelt für euer Labor 🧬</p>
</div>
""", unsafe_allow_html=True)
