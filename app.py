"""Streamlit chat UI.  Run: streamlit run app.py"""
import json
import streamlit as st
import bot

st.set_page_config(page_title="Great.cards assistant", page_icon="💳")
st.title("💳 Great.cards card assistant")
st.caption(f"LLM: {bot.PROVIDER}/{bot.MODEL} · prompt: {bot.PROMPT_NAME} · "
           f"amount guardrail: {'on' if bot.STRICT else 'off'}")

if "history" not in st.session_state:
    st.session_state.history, st.session_state.view = [], []

with st.sidebar:
    st.markdown("**Try:** `I spend 15k a month on Amazon and 8k on groceries. Which card?`")
    show_raw = st.toggle("Show raw tool calls", value=True)
    if st.button("New chat"):
        st.session_state.history, st.session_state.view = [], []
        st.rerun()

for m in st.session_state.view:
    with st.chat_message(m["role"]):
        st.markdown(m["text"])
        for w in m.get("warnings", []):
            st.warning(w)
        if show_raw and m.get("tools"):
            with st.expander(f"Tool calls ({len(m['tools'])})"):
                for t in m["tools"]:
                    st.code(f"{t['name']}({json.dumps(t['args'], ensure_ascii=False)})  [{t['ms']} ms]")
                    st.code(t["result"][:4000], language="json")

if prompt := st.chat_input("Describe your spending…"):
    st.session_state.view.append({"role": "user", "text": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Checking cards…"):
            try:
                res = bot.ask_sync(st.session_state.history, prompt)
                st.session_state.view.append({"role": "assistant", "text": res.reply,
                                              "warnings": res.warnings, "tools": res.tool_calls})
            except Exception as e:
                st.session_state.view.append({"role": "assistant", "text": f"Error: {bot.explain(e)}"})
    st.rerun()