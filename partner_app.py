import streamlit as st
import pandas as pd

# --- 1. CONFIGURATION & STYLING ---
st.set_page_config(layout="wide", page_title="MMTC-PAMP Partner Integrations", page_icon="❄️")

# Load Custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

# --- 2. STATE MANAGEMENT (Simulating Database) ---

# [Snowflake Connection Setup]
# To connect, ensure you have a .streamlit/secrets.toml file configured (locally)
# or are running inside Streamlit in Snowflake.
try:
    conn = st.connection("snowflake")
    session = conn.session()
    st.sidebar.success("Connected to Snowflake ❄️")
except Exception as e:
    st.sidebar.warning("Offline Mode ⚠️")

# Initialize the partner list (Data from your mappings.json / script.js)
if 'partners' not in st.session_state:
    st.session_state.partners = [
        {"id": "P-001", "name": "Paytm", "category": "GAP Partner", "sub_process": "BM", "status": True, "commission": "1.85%", "settlement": "T-1", "source": "Email", "email": "reports@paytm.com", "txn_mappings": [], "header_mappings": []},
        {"id": "P-002", "name": "PhonePe", "category": "GAP Partner", "sub_process": "CEM", "status": True, "commission": "1.85%", "settlement": "T-1", "source": "SFTP", "email": "reports@phonepe.com", "txn_mappings": [], "header_mappings": []},
        {"id": "P-003", "name": "Google Pay", "category": "GAP Partner", "sub_process": "BM", "status": True, "commission": "1.45%", "settlement": "T-1", "source": "Email", "email": "reports@googlepay.com", "txn_mappings": [], "header_mappings": []},
        {"id": "P-004", "name": "ABC", "category": "GAP Partner", "sub_process": "BM", "status": True, "commission": "0.75% / 1.55%", "settlement": "T-1", "source": "Email", "email": "reports@abc.com", "txn_mappings": [], "header_mappings": []},
        {"id": "P-005", "name": "Jupiter", "category": "GAP Partner", "sub_process": "BM", "status": True, "commission": "1.50%", "settlement": "T-1", "source": "Email", "email": "reports@jupiter.com", "txn_mappings": [], "header_mappings": []},
        {"id": "P-006", "name": "Payworld", "category": "GAP Partner", "sub_process": "BM", "status": True, "commission": "1.25%", "settlement": "T-1", "source": "Email", "email": "reports@payworld.com", "txn_mappings": [], "header_mappings": []},
        {"id": "P-007", "name": "JosAlukkas", "category": "GAP Partner", "sub_process": "CEM", "status": True, "commission": "1.40%", "settlement": "T-1", "source": "SFTP", "email": "reports@josalukkas.com", "txn_mappings": [], "header_mappings": []},
        {"id": "P-008", "name": "Money Boxx", "category": "GAP Partner", "sub_process": "CEM", "status": True, "commission": "1.4%/1.5%", "settlement": "T-1", "source": "SFTP", "email": "reports@moneyboxx.com", "txn_mappings": [], "header_mappings": []},
        {"id": "P-009", "name": "ABCD", "category": "GAP Partner", "sub_process": "CEM", "status": True, "commission": "1.50%", "settlement": "T-1", "source": "SFTP", "email": "reports@abcd.com", "txn_mappings": [], "header_mappings": []},
        {"id": "P-010", "name": "BKS", "category": "GAP Partner", "sub_process": "CEM", "status": True, "commission": "1.30%", "settlement": "T-1", "source": "SFTP", "email": "reports@bks.com", "txn_mappings": [], "header_mappings": []},
        {"id": "P-011", "name": "Direct Sales", "category": "GAP Partner", "sub_process": "CEM", "status": True, "commission": "-", "settlement": "T-1", "source": "SFTP", "email": "reports@directsales.com", "txn_mappings": [], "header_mappings": []},
        {"id": "P-012", "name": "Batuk", "category": "GAP Partner", "sub_process": "CEM", "status": True, "commission": "0.65%", "settlement": "T-1", "source": "SFTP", "email": "reports@batuk.com", "txn_mappings": [], "header_mappings": []},
        {"id": "P-013", "name": "Innopay", "category": "GAP Partner", "sub_process": "CEM", "status": True, "commission": "1.30%", "settlement": "T-1", "source": "SFTP", "email": "reports@innopay.com", "txn_mappings": [], "header_mappings": []},
        {"id": "P-014", "name": "TCC", "category": "GAP Partner", "sub_process": "CEM", "status": True, "commission": "1.50%", "settlement": "T-1", "source": "SFTP", "email": "reports@tcc.com", "txn_mappings": [], "header_mappings": []},
        {"id": "P-015", "name": "Incred Money", "category": "GAP Partner", "sub_process": "CEM", "status": True, "commission": "1.50%", "settlement": "T-1", "source": "SFTP", "email": "reports@incredmoney.com", "txn_mappings": [], "header_mappings": []},
        {"id": "P-016", "name": "OCL", "category": "GAP Partner", "sub_process": "CEM", "status": True, "commission": "-", "settlement": "T-1", "source": "SFTP", "email": "reports@ocl.com", "txn_mappings": [], "header_mappings": []},
        {"id": "P-017", "name": "Fincart", "category": "GAP Partner", "sub_process": "CEM", "status": True, "commission": "1.30%", "settlement": "T-1", "source": "SFTP", "email": "reports@fincart.com", "txn_mappings": [], "header_mappings": []},
        {"id": "P-018", "name": "Koshex", "category": "GAP Partner", "sub_process": "BM", "status": True, "commission": "1.45%", "settlement": "T-1", "source": "Email", "email": "reports@koshex.com", "txn_mappings": [], "header_mappings": []},
        {"id": "P-019", "name": "Nivesh", "category": "GAP Partner", "sub_process": "CEM", "status": True, "commission": "0.65%", "settlement": "T-1", "source": "SFTP", "email": "reports@nivesh.com", "txn_mappings": [], "header_mappings": []},
        {"id": "P-020", "name": "Paynav", "category": "GAP Partner", "sub_process": "BM", "status": True, "commission": "1.40%", "settlement": "T-1", "source": "Email", "email": "reports@paynav.com", "txn_mappings": [], "header_mappings": []},
        {"id": "P-021", "name": "Yourly", "category": "GAP Partner", "sub_process": "CEM", "status": True, "commission": "1.40%", "settlement": "T-1", "source": "SFTP", "email": "reports@yourly.com", "txn_mappings": [], "header_mappings": []},
        {"id": "P-022", "name": "JustPe", "category": "GAP Partner", "sub_process": "CEM", "status": True, "commission": "1.40%", "settlement": "T-1", "source": "SFTP", "email": "reports@justpe.com", "txn_mappings": [], "header_mappings": []},
        {"id": "P-023", "name": "Vittem Money", "category": "GAP Partner", "sub_process": "CEM", "status": True, "commission": "0.75%", "settlement": "T-1", "source": "SFTP", "email": "reports@vittemmoney.com", "txn_mappings": [], "header_mappings": []}
    ]

    # Populate default mappings for all partners
    default_txn = [{"partner": "WeBuy", "internal": "Buy"}, {"partner": "WeSell", "internal": "Sell"}]
    default_headers = [{"internal": "customer_id_internal", "partner": "ClientRefID"}, {"internal": "order_total_gross", "partner": "TotalTransactionValue"}]
    
    for p in st.session_state.partners:
        p['txn_mappings'] = [m.copy() for m in default_txn]
        p['header_mappings'] = [m.copy() for m in default_headers]

# Navigation State
if 'current_view' not in st.session_state:
    st.session_state.current_view = 'list' # options: 'list', 'mapping'
if 'show_add_form' not in st.session_state:
    st.session_state.show_add_form = False
if 'selected_partner_index' not in st.session_state:
    st.session_state.selected_partner_index = None

# --- 3. HELPER FUNCTIONS ---

def toggle_add_form():
    st.session_state.show_add_form = not st.session_state.show_add_form

def open_mapping(index):
    st.session_state.selected_partner_index = index
    st.session_state.current_view = 'mapping'
    st.rerun()

def close_mapping():
    st.session_state.current_view = 'list'
    st.session_state.selected_partner_index = None

def save_new_partner():
    # Retrieve data from session state keys
    new_p = {
        "id": st.session_state.new_id,
        "name": st.session_state.new_name,
        "category": st.session_state.new_cat,
        "sub_process": st.session_state.new_sub,
        "status": True,
        "commission": st.session_state.new_comm,
        "settlement": st.session_state.new_cycle,
        "source": st.session_state.new_source,
        "email": st.session_state.new_email,
        "txn_mappings": [],
        "header_mappings": []
    }
    st.session_state.partners.append(new_p)
    st.session_state.show_add_form = False
    st.rerun()

def delete_mapping_row(type_, index):
    p_idx = st.session_state.selected_partner_index
    if type_ == 'txn':
        st.session_state.partners[p_idx]['txn_mappings'].pop(index)
    else:
        st.session_state.partners[p_idx]['header_mappings'].pop(index)

def add_mapping_row(type_, val1, val2):
    p_idx = st.session_state.selected_partner_index
    if type_ == 'txn':
        st.session_state.partners[p_idx]['txn_mappings'].append({"partner": val1, "internal": val2})
    else:
        st.session_state.partners[p_idx]['header_mappings'].append({"internal": val1, "partner": val2})

def save_mappings():
    st.success("Mappings saved successfully!")

# --- 4. UI LAYOUT ---

# Sidebar (Navigation)
with st.sidebar:
    st.image("assets/mmtclogo.png")
    st.markdown("### ")
    
    # Custom Menu Buttons
    if st.button("👥 Partners", type="primary"):
        st.session_state.current_view = 'list'
    # if st.button("📊 Analytics", width="stretch"):
    #     pass
    if st.button("⚙️ Settings"):
        pass

# --- VIEW 1: PARTNER LIST & ADD FORM ---
if st.session_state.current_view == 'list':
    
    # Header Section
    col_h1, col_h2 = st.columns([6, 1])
    col_h1.title("Partner Integrations22")
    col_h2.button("➕ Add New Partner", on_click=toggle_add_form, key="btn_add_partner")

    # A. The "Add New Partner" Form (Hidden/Shown based on toggle)
    if st.session_state.show_add_form:
        with st.container():
            st.subheader("New Integration Setup")
            
            # Row 1
            c1, c2, c3 = st.columns(3)
            c1.text_input("Partner Name", key="new_name", placeholder="e.g. Acme Logistics")
            cat = c2.selectbox("Process Category", ["GAP Partner", "Ecommerce Partner"], key="new_cat")
            
            # Dynamic Sub-process logic
            sub_opts = ["CEM", "BM"] if cat == "GAP Partner" else ["Sell", "Buy"]
            c3.selectbox("Sub-Process", sub_opts, key="new_sub")

            # Row 2
            c4, c5, c6 = st.columns(3)
            c4.text_input("Commission Rates", key="new_comm", placeholder="5%")
            c5.text_input("Settlement Cycle", key="new_cycle", value="T-1")
            c6.selectbox("Source Type", ["Email", "SFTP", "API"], key="new_source")

            # Row 3
            c7, c8, c9 = st.columns(3)
            c7.text_input("MMTC Partner ID", key="new_id", placeholder="P-00X")
            c8.text_input("Recipient Email", key="new_email")
            
            # Form Buttons
            b_col1, b_col2 = st.columns([8, 1])
            with b_col2:
                st.button("Cancel", key="btn_cancel", on_click=toggle_add_form)
            st.button("Create Partner", key="btn_create", type="primary", on_click=save_new_partner)

    # B. The Data Table
    # Note: We convert the list of dicts to a DataFrame for display
    df_partners = pd.DataFrame(st.session_state.partners)
    
    # Rename for cleaner UI display
    display_df = df_partners[['id', 'name', 'category', 'sub_process', 'status']].copy()
    display_df.columns = ["ID", "Partner Name", "Category", "Sub-Process", "Active"]

    st.markdown("### Existing Partners")
    
    # We use Data Editor to allow the "Active" toggle to be interactive
    edited_df = st.data_editor(
        display_df,
        column_config={
            "Active": st.column_config.CheckboxColumn(
                "Status",
                help="Toggle status",
                default=False,
            ),
            "Category": st.column_config.TextColumn(
                "Process Category",
                width="medium",
            ),
        },
        disabled=["ID", "Partner Name", "Category", "Sub-Process"],
        hide_index=True,
        width="stretch",
        key="partner_table"
    )

    # Update the session state with edited status
    for idx, row in edited_df.iterrows():
        st.session_state.partners[idx]['status'] = row['Active']

    # Interaction: Selection Logic
    # Since Streamlit tables don't have row-click events yet, we use a Selectbox helper
    st.info("👇 Select a partner below to Configure Mapping or Edit details.")
    
    sel_col1, sel_col2 = st.columns([3, 1])
    selected_partner_name = sel_col1.selectbox("Select Partner to Configure", [p['name'] for p in st.session_state.partners])
    
    if sel_col2.button("Open Configuration ➔", type="primary", key="btn_open_config"):
        # Find index of selected name
        idx = next((i for i, item in enumerate(st.session_state.partners) if item["name"] == selected_partner_name), None)
        if idx is not None:
            open_mapping(idx)


# --- VIEW 2: MAPPING DETAILS ---
elif st.session_state.current_view == 'mapping':
    
    current_partner = st.session_state.partners[st.session_state.selected_partner_index]
    
    # Header
    m_col1, m_col2 = st.columns([6, 1])
    m_col1.title(f"Mapping: {current_partner['name']}")
    m_col1.caption("Configure transaction and header mappings for this partner.")
    
    with m_col2:
        st.button("💾 Save", type="primary", on_click=save_mappings, key="btn_save_mapping")
    st.button("← Back to List", on_click=close_mapping)

    # --- SECTION A: Transaction Type Mapping ---
    with st.container():
        st.subheader("Transaction Type Mapping")
        
        # Table Header
        h1, h2, h3, h4 = st.columns([3, 1, 3, 1])
        h1.markdown("**Partner Type**")
        h3.markdown("**Internal Type**")
        st.divider()

        # Existing Rows
        if current_partner['txn_mappings']:
            for i, mapping in enumerate(current_partner['txn_mappings']):
                r1, r2, r3, r4 = st.columns([3, 1, 3, 1])
                r1.code(mapping['partner'])
                r2.markdown("➡️")
                r3.code(mapping['internal'])
                r4.button("🗑️", key=f"del_txn_{i}", on_click=delete_mapping_row, args=('txn', i))
        else:
            st.markdown("*No mappings configured yet.*")

        # Add New Row
        st.markdown("#### Add New Transaction Pair")
        ar1, ar2, ar3, ar4 = st.columns([3, 1, 3, 1])
        new_pt = ar1.text_input("Partner Type", key="new_pt", placeholder="e.g. WeBuy")
        ar2.markdown("➡️")
        new_it = ar3.selectbox("Internal Type", ["Buy", "Sell", "Refund"], key="new_it")
        if ar4.button("➕ Add", key="add_txn_btn"):
            if new_pt:
                add_mapping_row('txn', new_pt, new_it)
                st.rerun()

    # --- SECTION B: Header Mapping ---
    with st.container():
        st.subheader("Header Mapping")
        st.markdown("Map internal IT system headers to the partner's required headers.")
        
        # Table Header
        hh1, hh2, hh3, hh4 = st.columns([3, 1, 3, 1])
        hh1.markdown("**Internal IT Header**")
        hh3.markdown("**Partner Header**")
        st.divider()

        # Existing Rows
        if current_partner['header_mappings']:
            for i, mapping in enumerate(current_partner['header_mappings']):
                hr1, hr2, hr3, hr4 = st.columns([3, 1, 3, 1])
                hr1.code(mapping['internal'])
                hr2.markdown("➡️")
                hr3.code(mapping['partner'])
                hr4.button("🗑️", key=f"del_head_{i}", on_click=delete_mapping_row, args=('header', i))
        else:
            st.markdown("*No header mappings configured yet.*")

        # Add New Row
        st.markdown("#### Add New Header Pair")
        ahr1, ahr2, ahr3, ahr4 = st.columns([3, 1, 3, 1])
        new_ih = ahr1.selectbox("Internal Header", ["customer_id", "order_total", "tax_vat", "shipping_addr"], key="new_ih")
        ahr2.markdown("➡️")
        new_ph = ahr3.text_input("Partner Header", key="new_ph", placeholder="e.g. ClientRefID")
        if ahr4.button("➕ Add", key="add_head_btn"):
            if new_ph:
                add_mapping_row('header', new_ih, new_ph)
                st.rerun()