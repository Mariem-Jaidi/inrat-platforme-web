import os
import streamlit as st
import rasterio
import numpy as np
import folium
from rasterio.crs import CRS
from streamlit_folium import st_folium
from folium.raster_layers import ImageOverlay
import geopandas as gpd
from rasterio.warp import transform_bounds

from governorates_data import (
    GOVERNORATES,
    get_governorate_keys_sorted,
    get_label,
    get_delegations,
    has_detailed_data,
    get_shapefile_name,
)
from theme import THEME_CSS

# --------------------------------------------------
# Configuration générale
# --------------------------------------------------

st.set_page_config(
    page_title="SIG Agricole — Tunisie",
    page_icon="🗺️",
    layout="wide",
)

st.markdown(THEME_CSS, unsafe_allow_html=True)

DATA_FOLDER = "data"
SHP_FOLDER = os.path.join(DATA_FOLDER, "shape")
RASTER_CRS = "EPSG:32632"

# --------------------------------------------------
# En-tête de la plateforme
# --------------------------------------------------

st.markdown(
    """
    <div class="platform-header">
        <div>
            <div class="eyebrow">Système d'information géographique &mdash; Aptitude des sols</div>
            <h1>Plateforme de visualisation cartographique</h1>
            <div class="subtitle-ar">منظومة المعلومات الجغرافية لملاءمة التربة الزراعية</div>
        </div>
        <div class="header-meta">
            <div class="org">République Tunisienne</div>
            Ministère de l'Agriculture<br>
            Direction des Sols
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# État de session
# --------------------------------------------------

if "show_basemap" not in st.session_state:
    st.session_state.show_basemap = True
if "selected_gov" not in st.session_state:
    st.session_state.selected_gov = "bizerte"
if "selected_region" not in st.session_state:
    st.session_state.selected_region = None

# --------------------------------------------------
# Barre latérale — Navigation administrative
# --------------------------------------------------

st.sidebar.markdown(
    """
    <div class="sidebar-brand">
        Navigation
        <small>Sélection de la zone d'étude</small>
    </div>
    """,
    unsafe_allow_html=True,
)

gov_keys = get_governorate_keys_sorted()
gov_labels = [get_label(k) for k in gov_keys]

default_gov_index = gov_keys.index("bizerte") if "bizerte" in gov_keys else 0

st.sidebar.markdown("### Gouvernorat")
selected_gov_label = st.sidebar.selectbox(
    "Choisir un gouvernorat",
    gov_labels,
    index=default_gov_index,
    label_visibility="collapsed",
)
selected_gov_key = gov_keys[gov_labels.index(selected_gov_label)]

if selected_gov_key != st.session_state.selected_gov:
    st.session_state.selected_gov = selected_gov_key
    st.session_state.selected_region = None

gov_info = GOVERNORATES[selected_gov_key]
delegations = get_delegations(selected_gov_key)
gov_has_data = has_detailed_data(selected_gov_key)

st.sidebar.markdown("### Délégation / région")
region_options = ["Toutes les délégations"] + delegations
selected_region = st.sidebar.selectbox(
    "Choisir une délégation",
    region_options,
    index=0,
    label_visibility="collapsed",
    key="region_selectbox",
)
st.session_state.selected_region = (
    None if selected_region == "Toutes les délégations" else selected_region
)

st.sidebar.markdown(
    f"""
    <div class="info-card" style="margin-top:4px;">
        <div class="card-title">Zone sélectionnée</div>
        <span class="region-pill active">{gov_info['label_fr']} · {gov_info['label_ar']}</span><br><br>
        <span class="region-pill">{selected_region}</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown("### Affichage")
show_basemap = st.sidebar.checkbox(
    "Fond de carte (OpenStreetMap)", value=st.session_state.show_basemap
)
if show_basemap != st.session_state.show_basemap:
    st.session_state.show_basemap = show_basemap
    st.rerun()

center_on_zone = st.sidebar.checkbox(
    "Centrer la carte sur la zone sélectionnée", value=True
)

# --------------------------------------------------
# Bandeau d'état des données
# --------------------------------------------------

if not gov_has_data:
    st.markdown(
        f"""
        <div class="data-banner">
            <span class="status-dot pending"></span>&nbsp;
            <b>Données détaillées non disponibles pour {gov_info['label_fr']}.</b>
            Les couches raster d'aptitude des sols et les limites de délégations
            n'ont été chargées à ce jour que pour le gouvernorat de <b>Bizerte</b>.
            La liste des {len(delegations)} délégations officielles de
            {gov_info['label_fr']} est néanmoins disponible ci-contre à titre de référence.
        </div>
        """,
        unsafe_allow_html=True,
    )

# ====================================================
# Mode 1 — Gouvernorat sans données détaillées
# ====================================================

if not gov_has_data:

    gov_shp_path = os.path.join(DATA_FOLDER, "decoupage_gouv", "decoupage_gouv.shp")

    col_map, col_side = st.columns([3, 1])

    with col_map:
        st.markdown(
            f'<p class="section-label">Carte — {gov_info["label_fr"]}</p>',
            unsafe_allow_html=True,
        )

        tiles = "OpenStreetMap" if st.session_state.show_basemap else None
        m = folium.Map(location=[34.0, 9.5], zoom_start=6, tiles=tiles)

        if os.path.exists(gov_shp_path):
            try:
                gdf = gpd.read_file(gov_shp_path)
                if gdf.crs != "EPSG:4326":
                    gdf = gdf.to_crs("EPSG:4326")

                row = gdf[gdf["Noms_Gouv"] == selected_gov_key]
                other = gdf[gdf["Noms_Gouv"] != selected_gov_key]

                folium.GeoJson(
                    other.to_json(),
                    name="Autres gouvernorats",
                    style_function=lambda x: {
                        "color": "#A9B3BF",
                        "weight": 1,
                        "fillOpacity": 0.03,
                        "fillColor": "#A9B3BF",
                    },
                ).add_to(m)

                if not row.empty:
                    folium.GeoJson(
                        row.to_json(),
                        name=gov_info["label_fr"],
                        style_function=lambda x: {
                            "color": "#1F4E5F",
                            "weight": 3,
                            "fillOpacity": 0.12,
                            "fillColor": "#1F4E5F",
                        },
                        tooltip=folium.GeoJsonTooltip(
                            fields=["gouvernora"], aliases=["Gouvernorat"]
                        ),
                    ).add_to(m)

                    if center_on_zone:
                        b = row.total_bounds
                        m.location = [(b[1] + b[3]) / 2, (b[0] + b[2]) / 2]
                        m.zoom_start = 9
            except Exception as e:
                st.error(f"Erreur lors du chargement des limites administratives : {e}")
        else:
            st.warning("Fichier des limites de gouvernorats introuvable.")

        folium.LayerControl(collapsed=True).add_to(m)
        st_folium(m, width=None, height=620, key=f"map_mode1_{selected_gov_key}")

    with col_side:
        st.markdown('<p class="section-label">Délégations</p>', unsafe_allow_html=True)
        st.caption(f"{len(delegations)} délégations officielles")
        for d in delegations:
            is_active = d == st.session_state.selected_region
            css_class = "region-pill active" if is_active else "region-pill"
            st.markdown(
                f'<div style="margin-bottom:6px;"><span class="{css_class}">{d}</span></div>',
                unsafe_allow_html=True,
            )

    st.stop()

# ====================================================
# Mode 2 — Gouvernorat avec données détaillées (Bizerte)
# ====================================================

tif_files = sorted(f for f in os.listdir(DATA_FOLDER) if f.lower().endswith(".tif"))

if len(tif_files) == 0:
    st.error("Aucun fichier TIFF trouvé dans le dossier 'data'.")
    st.stop()

st.sidebar.markdown("### Couche raster")
selected_tif = st.sidebar.selectbox(
    "Choisir une carte (variété / culture)",
    tif_files,
    label_visibility="collapsed",
)
filepath = os.path.join(DATA_FOLDER, selected_tif)

# --------------------------------------------------
# Lecture du raster
# --------------------------------------------------

with rasterio.open(filepath) as src:

    if src.crs is None:
        raster_crs = CRS.from_string(RASTER_CRS)
        crs_note = f"CRS non défini dans le fichier — {RASTER_CRS} appliqué par défaut"
    else:
        raster_crs = src.crs
        crs_note = f"CRS détecté : {raster_crs}"

    bounds = src.bounds
    bounds_wgs84 = transform_bounds(
        src_crs=raster_crs,
        dst_crs="EPSG:4326",
        left=bounds.left,
        bottom=bounds.bottom,
        right=bounds.right,
        top=bounds.top,
    )

    count = src.count

    if count >= 3:
        rgb = src.read([1, 2, 3])
        rgb = np.moveaxis(rgb, 0, -1)
        if rgb.max() > 1.0:
            rgb = rgb / 255.0
        rgb = np.clip(rgb, 0, 1)

        h, w, _ = rgb.shape
        colored = np.zeros((h, w, 4), dtype=np.float32)
        colored[:, :, :3] = rgb
        colored[:, :, 3] = 1.0

        is_dark = (rgb[:, :, 0] < 0.05) & (rgb[:, :, 1] < 0.05) & (rgb[:, :, 2] < 0.05)
        # Background is exactly RGB(240,240,240) = 0.941 — threshold 0.93 catches it cleanly
        is_light = (rgb[:, :, 0] > 0.93) & (rgb[:, :, 1] > 0.93) & (rgb[:, :, 2] > 0.93)
        background_mask = is_dark | is_light
        colored[background_mask, 3] = 0.0

        valid = rgb[:, :, 0].flatten()
        valid = valid[~np.isnan(valid)]
        valid = valid[~background_mask.flatten()]
        vmin, vmax = 0.0, 1.0
        raster_kind = "rgb"

    else:
        raster = src.read(1).astype(np.float32)
        nodata_value = src.nodata
        nodata_mask = (raster == nodata_value) if nodata_value is not None else np.isnan(raster)
        valid = raster[~nodata_mask]

        if len(valid) == 0:
            st.error("Toutes les valeurs du raster sont NoData.")
            st.stop()

        h, w = raster.shape
        colored = np.zeros((h, w, 4), dtype=np.float32)
        unique_vals = np.unique(valid)

        if set(unique_vals).issubset({1, 2, 3, 4}):
            color_map = {
                1: [139 / 255, 69 / 255, 19 / 255, 1.0],
                2: [255 / 255, 140 / 255, 0 / 255, 1.0],
                3: [255 / 255, 255 / 255, 0 / 255, 1.0],
                4: [0 / 255, 200 / 255, 0 / 255, 1.0],
            }
            for val, color in color_map.items():
                colored[raster == val] = color
            vmin, vmax = 1, 4
        else:
            vmin = float(np.nanmin(valid))
            vmax = float(np.nanmax(valid))
            bins = np.linspace(vmin, vmax, 5)
            mask = (raster <= bins[1]) & (~nodata_mask)
            colored[mask] = [139 / 255, 69 / 255, 19 / 255, 1.0]
            mask = (raster > bins[1]) & (raster <= bins[2]) & (~nodata_mask)
            colored[mask] = [255 / 255, 140 / 255, 0 / 255, 1.0]
            mask = (raster > bins[2]) & (raster <= bins[3]) & (~nodata_mask)
            colored[mask] = [255 / 255, 255 / 255, 0 / 255, 1.0]
            mask = (raster > bins[3]) & (~nodata_mask)
            colored[mask] = [0 / 255, 200 / 255, 0 / 255, 1.0]
        raster_kind = "classified"

# --------------------------------------------------
# Carte Folium
# --------------------------------------------------

center_lat = (bounds_wgs84[1] + bounds_wgs84[3]) / 2
center_lon = (bounds_wgs84[0] + bounds_wgs84[2]) / 2
tiles = "OpenStreetMap" if st.session_state.show_basemap else None

m = folium.Map(location=[center_lat, center_lon], zoom_start=12, tiles=tiles)

ImageOverlay(
    image=colored,
    bounds=[[bounds_wgs84[1], bounds_wgs84[0]], [bounds_wgs84[3], bounds_wgs84[2]]],
    opacity=1.0,
    interactive=True,
    name="Carte raster",
    overlay=True,
).add_to(m)

# --------------------------------------------------
# Limites administratives (délégations de Bizerte)
# --------------------------------------------------

shp_status = None
gdf_wgs84 = None

if os.path.exists(SHP_FOLDER):
    shp_files = [f for f in os.listdir(SHP_FOLDER) if f.lower().endswith(".shp")]
    default_shp = next((s for s in shp_files if "BZ32" in s.upper()), None)

    if shp_files:
        shp_to_use = default_shp or shp_files[0]
        shp_path = os.path.join(SHP_FOLDER, shp_to_use)

        try:
            gdf = gpd.read_file(shp_path)
            gdf_wgs84 = gdf.to_crs("EPSG:4326") if gdf.crs != "EPSG:4326" else gdf

            region_col = "ADM_DEL" if "ADM_DEL" in gdf_wgs84.columns else None
            highlight_gdf = None

            if region_col and st.session_state.selected_region:
                target_shp_name = get_shapefile_name(st.session_state.selected_region)
                match = gdf_wgs84[gdf_wgs84[region_col].str.upper() == target_shp_name]
                if not match.empty:
                    highlight_gdf = match

            folium.GeoJson(
                gdf_wgs84.to_json(),
                name=f"Délégations — {gov_info['label_fr']}",
                style_function=lambda x: {
                    "color": "#1F4E5F",
                    "weight": 2,
                    "fillOpacity": 0.04,
                    "opacity": 0.85,
                    "fillColor": "#1F4E5F",
                },
                highlight_function=lambda x: {"weight": 4, "color": "#B5552E"},
                tooltip=folium.GeoJsonTooltip(
                    fields=[region_col] if region_col else list(gdf_wgs84.columns)[:1],
                    aliases=["Délégation"],
                    localize=True,
                ),
            ).add_to(m)

            if highlight_gdf is not None and not highlight_gdf.empty:
                folium.GeoJson(
                    highlight_gdf.to_json(),
                    name="Délégation sélectionnée",
                    style_function=lambda x: {
                        "color": "#B5552E",
                        "weight": 4,
                        "fillOpacity": 0.18,
                        "fillColor": "#B5552E",
                    },
                ).add_to(m)

                if center_on_zone:
                    b = highlight_gdf.total_bounds
                    m.location = [(b[1] + b[3]) / 2, (b[0] + b[2]) / 2]
                    m.zoom_start = 13
            elif center_on_zone:
                b = gdf_wgs84.total_bounds
                m.location = [(b[1] + b[3]) / 2, (b[0] + b[2]) / 2]
                m.zoom_start = 11

            shp_status = ("ok", f"{len(gdf_wgs84)} délégations chargées — {shp_to_use}")

        except Exception as e:
            shp_status = ("error", str(e))
    else:
        shp_status = ("warning", "Aucun fichier .shp trouvé dans le dossier shape.")
else:
    shp_status = ("warning", "Dossier des limites administratives introuvable.")

folium.LayerControl(collapsed=True).add_to(m)

# --------------------------------------------------
# Affichage principal
# --------------------------------------------------

col1, col2 = st.columns([3, 1])

with col1:
    region_suffix = f" — {st.session_state.selected_region}" if st.session_state.selected_region else ""
    st.markdown(
        f'<p class="section-label">Carte interactive — {gov_info["label_fr"]}{region_suffix}</p>',
        unsafe_allow_html=True,
    )
    st_folium(m, width=None, height=640,
              key=f"map_mode2_{selected_gov_key}_{st.session_state.selected_region}_{selected_tif}")

with col2:
    st.markdown('<p class="section-label">Statistiques</p>', unsafe_allow_html=True)

    if len(valid) > 0:
        if raster_kind == "rgb":
            st.metric("Pixels exploitables", f"{len(valid):,}")
        else:
            mc1, mc2 = st.columns(2)
            with mc1:
                st.metric("Minimum", round(float(vmin), 2))
                st.metric("Moyenne", round(float(np.nanmean(valid)), 2))
            with mc2:
                st.metric("Maximum", round(float(vmax), 2))
                st.metric("Pixels valides", f"{len(valid):,}")

    st.markdown('<p class="section-label">Légende</p>', unsafe_allow_html=True)
    legend_items = [
        ("#8B4513", "Aptitude très faible"),
        ("#FF8C00", "Aptitude faible"),
        ("#FFFF00", "Aptitude moyenne"),
        ("#00C800", "Aptitude élevée"),
    ]
    legend_html = "".join(
        f'<div class="legend-row"><span class="legend-swatch" '
        f'style="background:{color};"></span>{label}</div>'
        for color, label in legend_items
    )
    st.markdown(f'<div class="info-card">{legend_html}</div>', unsafe_allow_html=True)

    st.markdown('<p class="section-label">Référentiel</p>', unsafe_allow_html=True)
    status_dot = "ok" if shp_status and shp_status[0] == "ok" else "pending"
    status_text = shp_status[1] if shp_status else "Non chargé"
    st.markdown(
        f"""
        <div class="info-card">
            <div style="margin-bottom:8px;"><span class="status-dot {status_dot}"></span>
            &nbsp;Limites administratives</div>
            <div style="font-size:12px; color:var(--slate-soft); margin-bottom:10px;">{status_text}</div>
            <div style="font-size:12px; color:var(--slate-soft); line-height:1.6;">
                Raster&nbsp;: {raster_crs}<br>
                Shapefile&nbsp;: EPSG:32632<br>
                Affichage&nbsp;: WGS84 (EPSG:4326)
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# --------------------------------------------------
# Galerie des cartes disponibles
# --------------------------------------------------

st.markdown("---")
st.markdown('<p class="section-label">Cartes disponibles — aperçu</p>', unsafe_allow_html=True)

image_files = sorted(
    f for f in os.listdir(DATA_FOLDER)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
)

if image_files:
    cols = st.columns(3)
    for i, file in enumerate(image_files):
        path = os.path.join(DATA_FOLDER, file)
        label = (
            os.path.splitext(file)[0]
            .replace("_(2)", "")
            .replace("c#U00e9r#U00e9ale", "Cereale")
            .replace("-removebg-preview", "")
            .replace("_", " ")
        )
        with cols[i % 3]:
            st.image(path, use_container_width=True)
            st.caption(label)
else:
    st.info("Aucune image disponible dans le dossier de données.")

# --------------------------------------------------
# Pied de page
# --------------------------------------------------

st.markdown(
    f"""
    <div class="platform-footer">
        <span>Plateforme SIG &mdash; Aptitude des sols agricoles</span>
        <span>{crs_note}</span>
    </div>
    """,
    unsafe_allow_html=True,
)