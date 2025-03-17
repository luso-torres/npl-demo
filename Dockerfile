FROM jupyter/tensorflow-notebook

USER root

# Update system packages and install necessary libraries for SentencePiece
RUN apt-get update && apt-get install -y \
    libprotobuf-dev protobuf-compiler && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Switch back to the notebook user for security
USER $NB_UID

# Install Python packages
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir \
    transformers \
    sentencepiece \
    pydub \
    pysrt

# Fix permissions for the notebook user
RUN fix-permissions "/home/${NB_USER}"

COPY lyrics/input_lyrics.txt translator.ipynb audiodub.ipynb lyrics_generator.ipynb sub_generator.ipynb./