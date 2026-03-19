import streamlit as st
from streamlit_flow import streamlit_flow
from streamlit_flow.elements import StreamlitFlowNode

st.set_page_config(layout="wide")
st.title("Poppy AI - Universal Canvas")

# Initialize the canvas state to remember your cards
if 'nodes' not in st.session_state:
    st.session_state.nodes = [
        StreamlitFlowNode("1", (50, 50), {'content': 'Main Project Board'}, 'input', 'right')
    ]

# Sidebar for User Input
with st.sidebar:
    st.header("Add New Card")
    input_type = st.selectbox("Type", ["Research", "YouTube", "Draft", "Idea"])
    content = st.text_area("Paste content or link here:")
    
    if st.button("Add to Canvas"):
        new_id = str(len(st.session_state.nodes) + 1)
        # Places the new card slightly offset from the last one
        new_node = StreamlitFlowNode(new_id, (100 + (len(st.session_state.nodes)*20), 100), {'content': f"[{input_type}] {content}"}, 'default', 'left')
        st.session_state.nodes.append(new_node)
        st.rerun()

# Display the Canvas
streamlit_flow("canvas", st.session_state.nodes, [])
