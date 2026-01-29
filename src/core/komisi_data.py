"""
Komisi (Commission) data for DPR RI period 2024-2029.

This module contains information about the 13 DPR commissions and their
scope of responsibilities, as well as mappings from aspiration categories
to relevant commissions.

Reference: https://id.wikipedia.org/wiki/Komisi_DPR_RI
"""

from typing import Dict, List


# List of all 13 DPR RI Commissions (2024-2029)
KOMISI_LIST = [
    "Komisi I",
    "Komisi II", 
    "Komisi III",
    "Komisi IV",
    "Komisi V",
    "Komisi VI",
    "Komisi VII",
    "Komisi VIII",
    "Komisi IX",
    "Komisi X",
    "Komisi XI",
    "Komisi XII",
    "Komisi XIII",
]


# Detailed information about each Komisi
KOMISI_INFO: Dict[str, Dict[str, any]] = {
    "Komisi I": {
        "ruang_lingkup": ["Pertahanan", "Luar Negeri", "Komunikasi dan Informatika", "Intelijen"],
        "mitra_kerja": [
            "Kementerian Pertahanan",
            "Kementerian Luar Negeri", 
            "Kementerian Komunikasi dan Digital",
            "TNI (AD, AL, AU)",
            "Badan Intelijen Negara (BIN)",
            "Badan Siber dan Sandi Negara (BSSN)",
            "Lemhannas",
            "Bakamla",
            "Wantannas",
            "Dewan Pers",
            "Komisi Penyiaran Indonesia (KPI)",
            "Komisi Informasi Pusat",
            "Lembaga Sensor Film",
        ],
    },
    "Komisi II": {
        "ruang_lingkup": ["Pemerintah Dalam Negeri", "Pertanahan", "Pemberdayaan Aparatur"],
        "mitra_kerja": [
            "Kementerian Dalam Negeri",
            "Kementerian PAN-RB",
            "Kementerian ATR/BPN",
            "KPU",
            "DKPP",
            "Bawaslu",
            "Ombudsman RI",
            "BKN",
            "LAN",
            "ANRI",
            "Otorita IKN",
            "BNPP",
        ],
    },
    "Komisi III": {
        "ruang_lingkup": ["Penegakan Hukum"],
        "mitra_kerja": [
            "Kejaksaan Agung",
            "Kepolisian RI",
            "KPK",
            "PPATK",
            "BNN",
            "Mahkamah Agung",
            "Mahkamah Konstitusi",
            "Komisi Yudisial",
        ],
    },
    "Komisi IV": {
        "ruang_lingkup": ["Pertanian", "Kehutanan", "Kelautan"],
        "mitra_kerja": [
            "Kementerian Pertanian",
            "Kementerian Kehutanan",
            "Kementerian Kelautan dan Perikanan",
            "Bulog",
            "BRGM",
            "Badan Pangan Nasional",
            "Badan Karantina Indonesia",
        ],
    },
    "Komisi V": {
        "ruang_lingkup": ["Infrastruktur", "Perhubungan"],
        "mitra_kerja": [
            "Kementerian Pekerjaan Umum",
            "Kementerian Perumahan dan Kawasan Pemukiman",
            "Kementerian Perhubungan",
            "Kementerian Desa dan PDT",
            "Kementerian Transmigrasi",
            "BMKG",
            "Basarnas",
        ],
    },
    "Komisi VI": {
        "ruang_lingkup": ["Perdagangan", "Kawasan Perdagangan dan Pengawasan Persaingan Usaha", "BUMN"],
        "mitra_kerja": [
            "Kementerian Perdagangan",
            "Kementerian Koperasi",
            "Danantara",
            "BPKN",
            "KPPU",
            "BP Batam",
            "BPK Sabang",
            "Dekopin",
        ],
    },
    "Komisi VII": {
        "ruang_lingkup": ["Perindustrian", "UMKM", "Ekonomi Kreatif", "Pariwisata"],
        "mitra_kerja": [
            "Kementerian Perindustrian",
            "Kementerian Pariwisata",
            "Kementerian Ekonomi Kreatif",
            "Kementerian UMKM",
            "BSN",
            "LPP RRI",
            "LPP TVRI",
            "LKBN Antara",
        ],
    },
    "Komisi VIII": {
        "ruang_lingkup": ["Agama", "Sosial", "Pemberdayaan Perempuan dan Perlindungan Anak"],
        "mitra_kerja": [
            "Kementerian Agama",
            "Kementerian Sosial",
            "Kementerian PPPA",
            "Kementerian Haji dan Umrah",
            "BNPB",
            "KPAI",
            "Baznas",
            "BWI",
            "BPKH",
        ],
    },
    "Komisi IX": {
        "ruang_lingkup": ["Kesehatan", "Ketenagakerjaan", "Jaminan Sosial"],
        "mitra_kerja": [
            "Kementerian Kesehatan",
            "Kementerian Ketenagakerjaan",
            "BNSP",
            "Kementerian Kependudukan",
            "Kementerian Perlindungan Pekerja Migran",
            "BPOM",
            "BPJS Kesehatan",
            "BPJS Ketenagakerjaan",
            "Badan Gizi Nasional",
        ],
    },
    "Komisi X": {
        "ruang_lingkup": ["Pendidikan", "Olahraga", "Sains", "Teknologi"],
        "mitra_kerja": [
            "Kementerian Pendidikan Dasar dan Menengah",
            "Kementerian Pendidikan Tinggi, Sains, dan Teknologi",
            "Kementerian Kebudayaan",
            "Kementerian Pemuda dan Olahraga",
            "Perpustakaan Nasional",
            "BRIN",
            "BPS",
        ],
    },
    "Komisi XI": {
        "ruang_lingkup": ["Keuangan", "Perencanaan Pembangunan Nasional", "Moneter", "Sektor Jasa Keuangan"],
        "mitra_kerja": [
            "Kementerian Keuangan",
            "Bappenas",
            "Bank Indonesia",
            "OJK",
            "LKPP",
            "BPK",
            "LPS",
            "BPKP",
            "LPEI",
        ],
    },
    "Komisi XII": {
        "ruang_lingkup": ["Energi dan Sumber Daya Mineral", "Lingkungan Hidup", "Investasi"],
        "mitra_kerja": [
            "Kementerian ESDM",
            "Kementerian Lingkungan Hidup",
            "Kementerian Investasi/BKPM",
            "BPH Migas",
            "SKK Migas",
            "Dewan Energi Nasional",
            "Bapeten",
            "BIG",
        ],
    },
    "Komisi XIII": {
        "ruang_lingkup": ["Reformasi Regulasi", "Hak Asasi Manusia"],
        "mitra_kerja": [
            "Kementerian Hukum",
            "Kementerian HAM",
            "Kementerian Sekretariat Negara",
            "Kementerian Imigrasi dan Pemasyarakatan",
            "Komnas HAM",
            "LPSK",
            "BNPT",
            "BPIP",
            "Setjen DPD RI",
            "Setjen MPR RI",
            "Kantor Staf Presiden",
        ],
    },
}


# Mapping from aspiration categories to relevant Komisi(s)
# Categories that span multiple commissions have multiple entries
CATEGORY_TO_KOMISI: Dict[str, List[str]] = {
    "Ekonomi": ["Komisi VI", "Komisi XI", "Komisi VII"],
    "Pendidikan": ["Komisi X"],
    "Kesehatan": ["Komisi IX"],
    "Infrastruktur": ["Komisi V"],
    "Pertanian": ["Komisi IV"],
    "Kelautan": ["Komisi IV"],
    "Energi": ["Komisi XII"],
    "Hukum": ["Komisi III", "Komisi XIII"],
    "Teknologi": ["Komisi X", "Komisi I"],
    "Sosial": ["Komisi VIII"],
    "Lingkungan": ["Komisi XII", "Komisi IV"],
    "Pertahanan": ["Komisi I"],
    "Keuangan": ["Komisi XI"],
    "Industri": ["Komisi VII"],
    "Perdagangan": ["Komisi VI"],
    "Pariwisata": ["Komisi VII"],
}


def get_relevant_komisi(category: str) -> List[str]:
    """
    Get the list of relevant Komisi for a given aspiration category.
    
    Args:
        category: The category of the aspiration
        
    Returns:
        List of relevant Komisi names. Returns all Komisi if category not found.
    """
    return CATEGORY_TO_KOMISI.get(category, KOMISI_LIST)


def get_primary_komisi(category: str) -> str:
    """
    Get the primary (first) Komisi for a given aspiration category.
    
    Args:
        category: The category of the aspiration
        
    Returns:
        The primary Komisi name
    """
    komisi_list = get_relevant_komisi(category)
    return komisi_list[0] if komisi_list else "Komisi I"


def get_komisi_scope(komisi: str) -> List[str]:
    """
    Get the scope/areas of responsibility for a Komisi.
    
    Args:
        komisi: Name of the Komisi (e.g., "Komisi I")
        
    Returns:
        List of scope areas
    """
    info = KOMISI_INFO.get(komisi, {})
    return info.get("ruang_lingkup", [])


def get_komisi_partners(komisi: str) -> List[str]:
    """
    Get the partner institutions for a Komisi.
    
    Args:
        komisi: Name of the Komisi (e.g., "Komisi I")
        
    Returns:
        List of partner institution names
    """
    info = KOMISI_INFO.get(komisi, {})
    return info.get("mitra_kerja", [])
