import json

# Bounding box of gmina Tarczyn (slightly expanded)
LON_MIN, LON_MAX = 20.665, 20.960
LAT_MIN, LAT_MAX = 51.915, 52.040
W, H = 1400, 780

def lon_to_x(lon):
    return (lon - LON_MIN) / (LON_MAX - LON_MIN) * W

def lat_to_y(lat):
    return (LAT_MAX - lat) / (LAT_MAX - LAT_MIN) * H

def coord(lon, lat):
    return f"{lon_to_x(lon):.1f},{lat_to_y(lat):.1f}"

# Gmina boundary (simplified from Nominatim)
boundary_coords = [
    (20.6851,51.9589),(20.7059,51.9452),(20.7220,51.9445),(20.7327,51.9452),
    (20.7429,51.9475),(20.7534,51.9441),(20.7899,51.9525),(20.8161,51.9460),
    (20.8289,51.9427),(20.8466,51.9314),(20.8600,51.9289),(20.8727,51.9293),
    (20.8789,51.9300),(20.8933,51.9324),(20.9150,51.9336),(20.9245,51.9366),
    (20.9290,51.9402),(20.9273,51.9441),(20.9336,51.9476),(20.9353,51.9505),
    (20.9367,51.9522),(20.9354,51.9552),(20.9360,51.9578),(20.9370,51.9601),
    (20.9384,51.9613),(20.9374,51.9633),(20.9372,51.9651),(20.9364,51.9669),
    (20.9378,51.9680),(20.9379,51.9692),(20.9385,51.9705),(20.9380,51.9718),
    (20.9381,51.9734),(20.9379,51.9753),(20.9392,51.9779),(20.9420,51.9799),
    (20.9429,51.9818),(20.9393,51.9803),(20.9375,51.9840),(20.9271,51.9868),
    (20.9053,51.9951),(20.8983,51.9985),(20.8892,51.9989),(20.8884,52.0042),
    (20.8830,52.0079),(20.8775,52.0117),(20.8720,52.0156),(20.8690,52.0195),
    (20.8665,52.0217),(20.8586,52.0224),(20.8466,52.0243),(20.8370,52.0297),
    (20.8241,52.0270),(20.7981,52.0126),(20.7814,52.0039),(20.7503,51.9860),
    (20.7359,51.9851),(20.7173,51.9847),(20.6991,51.9814),(20.6949,51.9783),
    (20.6948,51.9772),(20.6956,51.9763),(20.6966,51.9753),(20.6971,51.9745),
    (20.6942,51.9707),(20.6972,51.9598),(20.6851,51.9589)
]
boundary_path = " ".join([f"{'M' if i==0 else 'L'}{coord(lon,lat)}" for i,(lon,lat) in enumerate(boundary_coords)]) + "Z"

# CORRECTED A50 red variant route - goes THROUGH Świętochów, higher latitude
# Based on careful analysis of TRAKT PDF maps ark06 and ark07
a50_route = [
    (20.665, 51.957),   # entry from west
    (20.695, 51.958),   # near Wólka Jeżewska (south of it)
    (20.720, 51.957),   # near Bystrzanów area
    (20.745, 51.959),   # continuing east
    (20.770, 51.961),   # approaching Świętochów
    (20.783, 51.962),   # THROUGH Świętochów
    (20.800, 51.963),   # east of Świętochów
    (20.820, 51.964),   # approaching S7 interchange
    (20.845, 51.965),   # Węzeł Tarczyn PD (interchange)
    (20.865, 51.963),   # east of interchange
    (20.885, 51.960),   # continuing east
    (20.905, 51.957),   # between villages
    (20.925, 51.955),   # continuing
    (20.945, 51.953),   # near Zawodne
    (20.960, 51.952),   # exit east
]
a50_path = " ".join([f"{'M' if i==0 else 'L'}{coord(lon,lat)}" for i,(lon,lat) in enumerate(a50_route)])

# Villages with correct names from OSM Overpass API
places = [
    ("Tarczyn", 20.834, 51.980, "town"),
    # Villages near/on the A50 route (most affected)
    ("Świętochów", 20.783, 51.962, "village"),  # ON THE ROUTE
    ("Bystrzanów", 20.732, 51.953, "village"),
    ("Wólka Jeżewska", 20.695, 51.954, "village"),
    ("Parcele-Jeżewice", 20.766, 51.955, "hamlet"),
    ("Rembertów", 20.840, 51.959, "village"),
    ("Cieśle", 20.821, 51.955, "hamlet"),
    ("Stefanówka", 20.867, 51.951, "village"),
    ("Brominy", 20.862, 51.952, "hamlet"),
    ("Wylezin", 20.882, 51.954, "village"),
    ("Racibory", 20.910, 51.949, "village"),
    ("Nowe Racibory", 20.915, 51.952, "hamlet"),
    # Villages south of route
    ("Natalin", 20.688, 51.941, "village"),
    ("Kornelówka", 20.706, 51.941, "village"),
    ("Michrów-Stefów", 20.755, 51.938, "village"),
    ("Michrówek", 20.777, 51.946, "village"),
    ("Michrów", 20.792, 51.941, "village"),
    ("Księżowola", 20.837, 51.939, "village"),
    ("Kopana", 20.858, 51.942, "village"),
    ("Stara Kopana", 20.853, 51.946, "hamlet"),
    ("Pawłowice", 20.878, 51.944, "village"),
    ("Kawęczyn", 20.906, 51.941, "village"),
    ("Wilcza Wólka", 20.931, 51.939, "village"),
    ("Zawodne", 20.948, 51.950, "village"),
    ("Kocerany", 20.823, 51.937, "village"),
    ("Podole", 20.850, 51.925, "village"),
    ("Kruszew", 20.784, 51.923, "village"),
    ("Aleksandrów", 20.717, 51.925, "village"),
    ("Załęże Duże", 20.738, 51.932, "village"),
    # Villages north of route
    ("Werdun", 20.726, 51.958, "village"),
    ("Many", 20.714, 51.966, "village"),
    ("Suchostruga", 20.734, 51.965, "village"),
    ("Suchodół", 20.774, 51.980, "village"),
    ("Jeżewice", 20.752, 51.973, "village"),
    ("Nosy", 20.795, 51.989, "village"),
    ("Marianka", 20.802, 51.980, "village"),
    ("Drozdy", 20.815, 51.976, "village"),
    ("Jeziorzany", 20.822, 51.970, "village"),
    ("Komorniki", 20.850, 51.977, "village"),
    ("Józefowice", 20.850, 51.979, "village"),
    ("Gładków", 20.869, 51.973, "village"),
    ("Ruda", 20.871, 51.979, "village"),
    ("Gąski", 20.881, 51.967, "village"),
    ("Prace Małe", 20.888, 51.979, "village"),
    ("Prace Duże", 20.913, 51.973, "village"),
    ("Borowiec", 20.728, 51.980, "village"),
    ("Zaręby", 20.735, 51.996, "village"),
    # Northern villages
    ("Przypki", 20.811, 52.007, "village"),
    ("Wola Przypkowska", 20.833, 52.009, "village"),
    ("Grzędy", 20.849, 52.009, "village"),
    ("Kotorydz", 20.869, 52.000, "village"),
    ("Marylka", 20.890, 51.991, "village"),
    ("Korzeniówka", 20.902, 51.995, "village"),
    ("Złotokłos", 20.905, 52.005, "village"),
    ("Henryków-Urocze", 20.923, 51.999, "village"),
    ("Kolonia Jeziorzany", 20.842, 51.966, "hamlet"),
]

# S7 road
s7_route = [(20.838, 52.040), (20.840, 52.010), (20.842, 51.980), (20.844, 51.965), (20.846, 51.940), (20.848, 51.915)]
s7_path = " ".join([f"{'M' if i==0 else 'L'}{coord(lon,lat)}" for i,(lon,lat) in enumerate(s7_route)])

# DK50 existing road
dk50_route = [(20.665, 51.938), (20.720, 51.935), (20.780, 51.932), (20.820, 51.935), (20.860, 51.930), (20.920, 51.928), (20.960, 51.930)]
dk50_path = " ".join([f"{'M' if i==0 else 'L'}{coord(lon,lat)}" for i,(lon,lat) in enumerate(dk50_route)])

# Railway
rail_route = [(20.665, 51.975), (20.720, 51.978), (20.780, 51.980), (20.830, 51.980), (20.870, 51.978), (20.920, 51.975), (20.960, 51.973)]
rail_path = " ".join([f"{'M' if i==0 else 'L'}{coord(lon,lat)}" for i,(lon,lat) in enumerate(rail_route)])

# Local roads
local_roads = [
    [(20.735, 51.975), (20.770, 51.968), (20.783, 51.962), (20.800, 51.963), (20.840, 51.959)],
    [(20.755, 51.938), (20.792, 51.941), (20.837, 51.939), (20.878, 51.944)],
    [(20.752, 52.000), (20.752, 51.973), (20.766, 51.955)],
    [(20.780, 51.980), (20.815, 51.976), (20.834, 51.980)],
    [(20.834, 51.980), (20.844, 51.965), (20.878, 51.944)],
    [(20.834, 51.980), (20.833, 52.009)],
    [(20.834, 51.980), (20.870, 51.979), (20.913, 51.973)],
    [(20.688, 51.941), (20.706, 51.941), (20.738, 51.932)],
]

# Forest areas
forests = [
    [(20.665,52.000), (20.710,52.005), (20.735,51.995), (20.740,51.980), (20.700,51.970), (20.665,51.975)],
    [(20.775,51.958), (20.810,51.962), (20.815,51.955), (20.795,51.945), (20.770,51.940), (20.758,51.948)],
    [(20.880,52.010), (20.930,52.015), (20.945,52.000), (20.920,51.990), (20.885,51.995)],
    [(20.900,51.960), (20.940,51.965), (20.960,51.955), (20.950,51.940), (20.910,51.945)],
    [(20.850,52.020), (20.870,52.025), (20.875,52.010), (20.855,52.010)],
]

# Water bodies
waters = [
    (20.688, 51.965, 8, 4),
    (20.878, 51.935, 6, 3),
    (20.905, 52.008, 7, 4),
    (20.810, 52.015, 5, 3),
    (20.790, 51.968, 4, 2),  # near Świętochów
]

# Build corridor paths
corridor_offset = 0.0035
danger_offset = 0.006
def make_area(route, offset):
    top = [(lon, lat + offset) for lon, lat in route]
    bot = list(reversed([(lon, lat - offset) for lon, lat in route]))
    path = " ".join([f"{'M' if i==0 else 'L'}{coord(lon,lat)}" for i,(lon,lat) in enumerate(top)])
    path += " " + " ".join([f"L{coord(lon,lat)}" for lon,lat in bot]) + " Z"
    return path

corridor_area = make_area(a50_route, corridor_offset)
danger_area = make_area(a50_route, danger_offset)

# ======= BUILD SVG =======
svg_parts = []
svg_parts.append(f'''<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" class="w-full h-auto rounded-xl"
     role="img" aria-label="Mapa wariantu czerwonego A50 przez gminę Tarczyn"
     style="font-family: -apple-system, 'Segoe UI', Arial, sans-serif;">
    <defs>
        <filter id="redGlow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur in="SourceGraphic" stdDeviation="4" result="blur"/>
            <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
        </filter>
        <filter id="redGlowStrong" x="-30%" y="-30%" width="160%" height="160%">
            <feGaussianBlur in="SourceGraphic" stdDeviation="8" result="blur"/>
            <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
        </filter>
        <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
            <feDropShadow dx="0" dy="1" stdDeviation="1" flood-opacity="0.3"/>
        </filter>
    </defs>

    <!-- Background outside gmina -->
    <rect width="{W}" height="{H}" fill="#e8e0d8"/>
    <!-- Gmina fill -->
    <path d="{boundary_path}" fill="#f2efe9" stroke="none"/>''')

# Forests
for f in forests:
    path = " ".join([f"{'M' if i==0 else 'L'}{coord(lon,lat)}" for i,(lon,lat) in enumerate(f)]) + " Z"
    svg_parts.append(f'    <path d="{path}" fill="#c8ddb0" stroke="#a8c090" stroke-width="0.5" opacity="0.7"/>')

# Water
for lon, lat, rx, ry in waters:
    svg_parts.append(f'    <ellipse cx="{lon_to_x(lon):.1f}" cy="{lat_to_y(lat):.1f}" rx="{rx}" ry="{ry}" fill="#aad4e6" stroke="#88b8d0" stroke-width="0.5"/>')

# Boundary
svg_parts.append(f'    <path d="{boundary_path}" fill="none" stroke="#9a7b6a" stroke-width="2.5" stroke-dasharray="8,4" opacity="0.6"/>')

# Railway
svg_parts.append(f'    <path d="{rail_path}" fill="none" stroke="#888" stroke-width="2.5"/>')
svg_parts.append(f'    <path d="{rail_path}" fill="none" stroke="white" stroke-width="1.5" stroke-dasharray="6,6"/>')

# DK50
svg_parts.append(f'    <path d="{dk50_path}" fill="none" stroke="#e8c84a" stroke-width="4" stroke-linecap="round"/>')
svg_parts.append(f'    <path d="{dk50_path}" fill="none" stroke="#f0d860" stroke-width="2.5" stroke-linecap="round"/>')

# S7
svg_parts.append(f'    <path d="{s7_path}" fill="none" stroke="#d45050" stroke-width="5" stroke-linecap="round"/>')
svg_parts.append(f'    <path d="{s7_path}" fill="none" stroke="#e86060" stroke-width="3" stroke-linecap="round"/>')
svg_parts.append(f'    <path d="{s7_path}" fill="none" stroke="white" stroke-width="0.8" stroke-dasharray="8,6"/>')

# Local roads
for road in local_roads:
    path = " ".join([f"{'M' if i==0 else 'L'}{coord(lon,lat)}" for i,(lon,lat) in enumerate(road)])
    svg_parts.append(f'    <path d="{path}" fill="none" stroke="white" stroke-width="2.5" stroke-linecap="round"/>')
    svg_parts.append(f'    <path d="{path}" fill="none" stroke="#ddd" stroke-width="1.5" stroke-linecap="round"/>')

# A50 animated corridor
svg_parts.append(f'''
    <!-- ===== A50 RED VARIANT - ANIMATED ===== -->
    <path d="{danger_area}" fill="#dc2626" opacity="0.08">
        <animate attributeName="opacity" values="0.06;0.15;0.06" dur="2s" repeatCount="indefinite"/>
    </path>
    <path d="{corridor_area}" fill="#dc2626" opacity="0.25" filter="url(#redGlow)">
        <animate attributeName="opacity" values="0.2;0.45;0.2" dur="2s" repeatCount="indefinite"/>
    </path>
    <path d="{a50_path}" fill="none" stroke="#ef4444" stroke-width="4" stroke-linecap="round" filter="url(#redGlowStrong)">
        <animate attributeName="stroke" values="#ef4444;#fca5a5;#ef4444" dur="1.5s" repeatCount="indefinite"/>
        <animate attributeName="stroke-width" values="3;6;3" dur="1.5s" repeatCount="indefinite"/>
    </path>
    <path d="{a50_path}" fill="none" stroke="white" stroke-width="1" stroke-dasharray="8,6" opacity="0.5">
        <animate attributeName="opacity" values="0.5;0.15;0.5" dur="1.5s" repeatCount="indefinite"/>
    </path>''')

# Interchange at Węzeł Tarczyn PD (where A50 crosses S7)
ix, iy = lon_to_x(20.845), lat_to_y(51.965)
svg_parts.append(f'''
    <!-- Węzeł Tarczyn PD -->
    <circle cx="{ix:.1f}" cy="{iy:.1f}" r="16" fill="none" stroke="#ef4444" stroke-width="2.5" opacity="0.7">
        <animate attributeName="r" values="14;20;14" dur="2s" repeatCount="indefinite"/>
        <animate attributeName="opacity" values="0.7;0.2;0.7" dur="2s" repeatCount="indefinite"/>
    </circle>
    <circle cx="{ix:.1f}" cy="{iy:.1f}" r="4" fill="#ef4444">
        <animate attributeName="fill" values="#ef4444;#fca5a5;#ef4444" dur="1.5s" repeatCount="indefinite"/>
    </circle>
    <text x="{ix:.0f}" y="{iy+28:.0f}" fill="#dc2626" font-size="9" font-weight="bold" text-anchor="middle">
        Węzeł Tarczyn PD
        <animate attributeName="fill" values="#dc2626;#f87171;#dc2626" dur="2s" repeatCount="indefinite"/>
    </text>''')

# Road labels
s7x, s7y = lon_to_x(20.850), lat_to_y(51.920)
dk50x, dk50y = lon_to_x(20.720), lat_to_y(51.932)
a50x, a50y = lon_to_x(20.730), lat_to_y(51.962)
plx, ply = lon_to_x(20.820), lat_to_y(51.972)

svg_parts.append(f'''
    <rect x="{s7x-12:.0f}" y="{s7y-9:.0f}" width="24" height="18" rx="3" fill="#d45050"/>
    <text x="{s7x:.0f}" y="{s7y+4:.0f}" fill="white" font-size="11" font-weight="bold" text-anchor="middle">S7</text>
    <rect x="{dk50x-18:.0f}" y="{dk50y-9:.0f}" width="36" height="18" rx="3" fill="#d4a820"/>
    <text x="{dk50x:.0f}" y="{dk50y+4:.0f}" fill="white" font-size="10" font-weight="bold" text-anchor="middle">DK50</text>
    <rect x="{a50x-16:.0f}" y="{a50y-10:.0f}" width="32" height="20" rx="3" fill="#dc2626">
        <animate attributeName="fill" values="#dc2626;#f87171;#dc2626" dur="1.5s" repeatCount="indefinite"/>
    </rect>
    <text x="{a50x:.0f}" y="{a50y+4:.0f}" fill="white" font-size="12" font-weight="bold" text-anchor="middle">A50</text>
    <rect x="{plx-75:.0f}" y="{ply-11:.0f}" width="150" height="18" rx="3" fill="#dc2626" opacity="0.85">
        <animate attributeName="opacity" values="0.85;0.4;0.85" dur="2s" repeatCount="indefinite"/>
    </rect>
    <text x="{plx:.0f}" y="{ply+3:.0f}" fill="white" font-size="11" font-weight="bold" text-anchor="middle" letter-spacing="1.5">PODWARIANT TARCZYN</text>''')

# Place labels
for name, lon, lat, ptype in places:
    x, y = lon_to_x(lon), lat_to_y(lat)
    if ptype == "town":
        svg_parts.append(f'''    <rect x="{x-3:.0f}" y="{y-3:.0f}" width="6" height="6" fill="#333" rx="1"/>
    <text x="{x:.0f}" y="{y+16:.0f}" fill="#222" font-size="14" font-weight="bold" text-anchor="middle"
          paint-order="stroke" stroke="#f2efe9" stroke-width="3">{name}</text>''')
    elif ptype == "village":
        svg_parts.append(f'''    <circle cx="{x:.1f}" cy="{y:.1f}" r="2.5" fill="#555"/>
    <text x="{x+5:.0f}" y="{y+4:.0f}" fill="#444" font-size="10" font-weight="500"
          paint-order="stroke" stroke="#f2efe9" stroke-width="2.5">{name}</text>''')
    else:
        svg_parts.append(f'''    <circle cx="{x:.1f}" cy="{y:.1f}" r="1.5" fill="#777"/>
    <text x="{x+4:.0f}" y="{y+3:.0f}" fill="#666" font-size="8"
          paint-order="stroke" stroke="#f2efe9" stroke-width="2">{name}</text>''')

# Gmina label, directions, legend, scale, compass
glx, gly = lon_to_x(20.810), lat_to_y(52.015)
scale_px = (1/71.5) * 2 / (LON_MAX - LON_MIN) * W

svg_parts.append(f'''
    <text x="{glx:.0f}" y="{gly:.0f}" fill="rgba(100,70,50,0.15)" font-size="28" font-weight="bold"
          text-anchor="middle" letter-spacing="8">GMINA TARCZYN</text>

    <text x="15" y="{lat_to_y(51.957):.0f}" fill="#999" font-size="11">← Sochaczew</text>
    <text x="{W-15}" y="{lat_to_y(51.952):.0f}" fill="#999" font-size="11" text-anchor="end">Mińsk Maz. →</text>
    <text x="{lon_to_x(20.840):.0f}" y="18" fill="#999" font-size="11" text-anchor="middle">↑ Warszawa</text>

    <rect x="15" y="{H-115}" width="230" height="105" rx="6" fill="rgba(255,255,255,0.92)" stroke="#ccc" stroke-width="1"/>
    <text x="28" y="{H-95}" fill="#333" font-size="12" font-weight="bold">LEGENDA</text>
    <line x1="28" y1="{H-78}" x2="58" y2="{H-78}" stroke="#ef4444" stroke-width="4"/>
    <rect x="28" y="{H-83}" width="30" height="10" fill="#ef4444" opacity="0.25" rx="2"/>
    <text x="68" y="{H-74}" fill="#555" font-size="10">Wariant czerwony A50</text>
    <line x1="28" y1="{H-60}" x2="58" y2="{H-60}" stroke="#d45050" stroke-width="4"/>
    <text x="68" y="{H-56}" fill="#555" font-size="10">Droga ekspresowa S7</text>
    <line x1="28" y1="{H-42}" x2="58" y2="{H-42}" stroke="#e8c84a" stroke-width="3"/>
    <text x="68" y="{H-38}" fill="#555" font-size="10">Droga krajowa DK50</text>
    <line x1="28" y1="{H-24}" x2="45" y2="{H-24}" stroke="#888" stroke-width="2.5"/>
    <line x1="45" y1="{H-24}" x2="58" y2="{H-24}" stroke="white" stroke-width="1.5" stroke-dasharray="3,3"/>
    <text x="68" y="{H-20}" fill="#555" font-size="10">Linia kolejowa</text>
    <path d="M28,{H-10} L58,{H-10}" fill="none" stroke="#9a7b6a" stroke-width="2" stroke-dasharray="5,3"/>
    <text x="68" y="{H-6}" fill="#555" font-size="10">Granica gminy</text>

    <line x1="{W-180}" y1="{H-20}" x2="{W-180+scale_px:.0f}" y2="{H-20}" stroke="#333" stroke-width="2"/>
    <line x1="{W-180}" y1="{H-25}" x2="{W-180}" y2="{H-15}" stroke="#333" stroke-width="1.5"/>
    <line x1="{W-180+scale_px:.0f}" y1="{H-25}" x2="{W-180+scale_px:.0f}" y2="{H-15}" stroke="#333" stroke-width="1.5"/>
    <text x="{W-180+scale_px/2:.0f}" y="{H-26}" fill="#333" font-size="10" text-anchor="middle">2 km</text>

    <g transform="translate({W-40},40)">
        <circle cx="0" cy="0" r="16" fill="rgba(255,255,255,0.8)" stroke="#999" stroke-width="0.5"/>
        <polygon points="0,-12 -3,2 0,-1 3,2" fill="#333"/>
        <polygon points="0,12 -3,-2 0,1 3,-2" fill="#bbb"/>
        <text x="0" y="-17" fill="#333" font-size="9" font-weight="bold" text-anchor="middle">N</text>
    </g>
</svg>''')

print("\n".join(svg_parts))
