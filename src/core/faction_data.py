"""
Faction (Fraksi) data and ideology mapping for DPR Simulator.
"""

from typing import Dict

# Mapping of political factions to their general ideology/stance/persona key characteristics
FACTION_PERSONAS: Dict[str, str] = {
    "PDI-P": "Nasionalis, fokus pada 'Wong Cilik', ideologi Soekarno, proteksi sosial, persatuan nasional.",
    "Golkar": "Karyakekaryaan, fokus pada pembangunan ekonomi, stabilitas, teknokratik, pro-investasi.",
    "Gerindra": "Nasionalis, tegas, fokus pada pertahanan/keamanan, kemandirian pangan/energi, patriotik.",
    "PKB": "Nasionalis-Religius (basis NU), fokus pada pesantren, masyarakat pedesaan, toleransi, kesejahteraan ummat.",
    "Nasdem": "Restorasi Indonesia, perubahan, gagasan baru, anti-mahar politik, nasionalis-modern.",
    "PKS": "Agamis (Islam), kritis terhadap kebijakan pemerintah (objektif), fokus pada layanan publik, ketahanan keluarga, moralitas.",
    "Demokrat": "Nasionalis-Religius, fokus pada pertumbuhan ekonomi berkeadilan, stabilitas politik, pro-rakyat.",
    "PAN": "Nasionalis-Religius (basis Muhammadiyah), modernis, pro-bisnis/ekonomi pasar, reformis.",
    "PPP": "Agamis (Islam Tradisional), persatuan umat, pembangunan berazaskan nilai Islam.",
    "PSI": "Progresif, anak muda/millennial, anti-korupsi, anti-intoleransi, transparansi, gaya komunikasi lugas.",
    "Perindo": "Persatuan Indonesia, fokus pada UMKM, ekonomi kerakyatan, kesejahteraan keluarga.",
    "Hanura": "Hati Nurani Rakyat, fokus pada keadilan sosial, pembangunan daerah.",
    "Gelora": "Arah baru Indonesia, nasionalisme modern, visi Indonesia kekuatan dunia.",
    "Ummat": "Tegakkan keadilan, lawan kezaliman, berbasis nilai Islam yang tegas.",
    "PBB": "Islam moderat, kepastian hukum, hak asasi manusia.",
    "PKPI": "Nasionalis, persatuan, kesejahteraan prajurit/veteran.",
    "Garuda": "Gerakan perubahan, ekonomi kerakyatan, nasionalisme."
}

def get_faction_persona(faction: str) -> str:
    """Get the persona description for a given faction."""
    return FACTION_PERSONAS.get(faction, "Nasionalis, berorientasi pada kepentingan rakyat.")
