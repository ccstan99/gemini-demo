# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Gemini 101",
        page_icon=" 🌟",
    )

    st.write("# Welcome to the Gemini Demo! 🌟")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        This is the companion code for the Intro to AI + Gemini 101 workshops to quickly build and deploy Gemini-powered apps.
        **👈 Select a demo from the sidebar** for ideas and adapt for your own projects!
        ### Resources to continue learning:
        - [Gemini + AI Studio](https://ai.google.dev/) -- Prototyping environment with Gemini
        - [Gemini Quickstart Tutorials](https://ai.google.dev/tutorials/python_quickstart) -- Examples to build in different programming languages
        - [Streamlit Tutorials](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps) -- Build web apps calling LLMs
        - [Introduction to Generative AI](https://www.cloudskillsboost.google/paths/118) -- Google learning paths with videos & exercises
        - [DeepLearning.AI](https://www.deeplearning.ai/) -- Full specializations + many short 1-hour courses
        ### Feedback & stay in touch:
        - [Feedback survey](https://bit.ly/cheng2-slides)

      """
    )


if __name__ == "__main__":
    run()
