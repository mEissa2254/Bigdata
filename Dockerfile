# Use Ubuntu as the base image
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /home/doc-bd-a1

# Update package lists and install necessary packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-venv \
    && rm -rf /var/lib/apt/lists/* 


# Create a virtual environment
RUN python3 -m venv /opt/venv

# Activate the virtual environment and install Python packages
RUN . /opt/venv/bin/activate && \
    pip3 install \
    pandas \
    numpy \
    seaborn \
    matplotlib \
    scikit-learn \
    scipy

# Copy the dataset into the container
COPY load.py dpre.py eda.py vis.py model.py /home/doc-bd-a1/

COPY dataset.csv /home/doc-bd-a1/

# Set the default command to open bash shell
CMD ["/bin/bash"]