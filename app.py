import streamlit as st

st.set_page_config(page_title="Note Taking App", layout="centered")

st.title("📒 Note Taking App")

# Initialize session state for notes
if "notes" not in st.session_state:
    st.session_state.notes = []

# Input fields
lesson = st.text_input("📚 Lesson Name")
content = st.text_area("📝 Notes", height=200)

# Save note
if st.button("💾 Save Note"):
    if lesson and content:
        st.session_state.notes.append({"lesson": lesson, "content": content})
        st.success("Note saved!")
    else:
        st.warning("Please fill in both fields.")

# Copy content
if st.button("📋 Copy Note Content"):
    if content:
        st.code(content, language="markdown")
        st.toast("Copied! (Use Ctrl+C manually here)", icon="✅")
    else:
        st.warning("Nothing to copy!")

st.markdown("---")
st.subheader("📚 Saved Notes")

# Display saved notes
for i, note in enumerate(st.session_state.notes):
    with st.expander(f"📘 {note['lesson']}"):
        st.markdown(note["content"])
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button(f"📋 Copy", key=f"copy_{i}"):
                st.code(note["content"], language="markdown")
                st.toast("Copied! (Use Ctrl+C manually here)", icon="✅")
        with col2:
            if st.button(f"🗑️ Delete", key=f"del_{i}"):
                st.session_state.notes.pop(i)
                st.experimental_rerun()

