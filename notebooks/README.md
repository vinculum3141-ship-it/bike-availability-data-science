# Notebook folder

## 📓 Notebook Naming Convention (Important)
Inside each module folder:
```
M2_01_amsterdam_open_data_demo.ipynb
M2_02_knmi_weather_api_demo.ipynb
M2_03_merge_datasets.ipynb
M2_04_hands_on_exercises.ipynb
```

This ensures:
- Clear learning flow
- Easy grading
- Easy navigation

## 🧠 Notebook Template (Starter Cell)
Every notebook should start with:
```python
# Notebook Setup (Run First)

import sys
import os

if "google.colab" in sys.modules:
    !pip install -r ../requirements.txt

project_root = os.path.abspath("..")
sys.path.append(project_root)
```
