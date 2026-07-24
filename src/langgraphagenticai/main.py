import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit


def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph Agentic AI application.
    """

    # Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Failed to load UI.")
        return

    # Chat input
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else :
        user_message = st.chat_input("Enter your message")

    if not user_message:
        return

    try:
        # Initialize LLM
        obj_llm_config = GroqLLM(user_controls_input=user_input)
        model = obj_llm_config.get_llm_model()

        if model is None:
            st.error("Failed to initialize LLM.")
            return

        # Get selected use case
        usecase = user_input.get("selected_usecase")

        if not usecase:
            st.error("Please select a use case.")
            return

        # Build graph
        graph_builder = GraphBuilder(model)
        graph = graph_builder.setup_graph(usecase)

        # Display response
        display = DisplayResultStreamlit(
            usecase=usecase,
            graph=graph,
            user_message=user_message
        )
        display.display_result_on_ui()

    except Exception as e:
        st.exception(e)