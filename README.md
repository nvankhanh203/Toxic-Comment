Toxic Comment Classification

This repository contains a Toxic Comment Classification project using Natural Language Processing (NLP) and Deep Learning techniques.
The project includes data preprocessing, model training, and an interactive Chainlit-based application for inference.

📌 Project Overview

Task: Toxic / Non-toxic text classification

Techniques: Machine Learning, Deep Learning, BERT

Frameworks: PyTorch, Chainlit

Interface: Web-based (Chainlit)

⚙️ System Requirements

OS: Windows 10 / 11 (PowerShell recommended)

Python: 3.9 – 3.11

Git: Latest version

Git LFS: Required for large model files

Internet connection: Required for dependency installation

🔧 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/nvankhanh203/Toxic-Comment.git
cd Toxic-Comment

2️⃣ Install Git LFS (Required)

Large model files are managed using Git Large File Storage.

git lfs install
git lfs pull

3️⃣ Create or Use the Virtual Environment

If the virtual environment does not exist on your machine, create a new one:

python -m venv khanh_toxic


Activate the environment (Windows):

khanh_toxic\Scripts\Activate.ps1


If script execution is blocked, run once:

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned


You should see (khanh_toxic) in your terminal.

4️⃣ Install Required Dependencies
pip install -r requirements.txt

▶️ How to Run the Application

⚠️ Follow the steps in order from top to bottom

Step 1: Open PowerShell in the Project Root

Navigate to the folder that contains the khanh_toxic environment:

cd "YOUR_PROJECT_PATH"


Example:

cd "F:\khanh toxic comment"

Step 2: Activate the Virtual Environment
khanh_toxic\Scripts\Activate.ps1

Step 3: Navigate to the App Folder
cd app

Step 4: Run the Chainlit Application
chainlit run app.py -w


app.py: main application file

-w: auto-reload on code changes

Chainlit will output a local URL, for example:

http://localhost:8000


Open this link in your browser to use the application.

📂 Important: Update File Paths After Download

⚠️ Do NOT use absolute paths from another machine.

If your code contains paths like:

F:/khanh toxic comment/dataset_splited/train.csv


You must change them to match your local directory.

✅ Recommended (Portable Approach)
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "dataset_splited")
MODEL_PATH = os.path.join(BASE_DIR, "..", "model", "bert.pth")


This ensures the project works on different computers.

🧠 Jupyter Notebooks

The repository includes:

bert_for_toxic_comment.ipynb – BERT fine-tuning

ML_DL_Base_for_toxic_comment.ipynb – Traditional ML & DL models

These notebooks are for training, experiments, and analysis.

⚠️ Common Issues & Solutions
❌ Scripts execution is disabled

✔️ Run:

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

❌ ModuleNotFoundError

✔️ Activate the virtual environment
✔️ Run pip install -r requirements.txt

❌ FileNotFoundError

✔️ Check dataset/model paths
✔️ Update paths according to your local directory

📦 Large Model Files

model/bert.pth is larger than 100MB

Managed using Git LFS

After cloning:

git lfs pull

📄 License

This project is intended for educational and research purposes only.

👤 Author

Nguyễn Văn Khánh
AI / NLP Student
