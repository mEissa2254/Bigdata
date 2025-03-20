<<<<<<< HEAD
# Bigdata
=======
# Student Information Analysis Project

This project analyzes student information to derive insights and predictions about career outcomes.

## Project Execution

1. **Create the Dockerfile** (see Dockerfile in this repository)

2. **Build the Docker image:**
>>>>>>> 7743e38 (Intial commit)
>>>>>>>  sh
   docker build -t bd-a1 .
   
2. **Run the container:**
   sh
   docker run -it bd-a1
   
3. **Inside the container, start the pipeline**
   sh
   python3 load.py dataset.csv
   
4.  **Run the final script on the local machine to copy results:**
   ```sh
   bash final.sh
