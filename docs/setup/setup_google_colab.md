# 🚀 Google Colab Setup Guide

This guide will help you run the course notebooks on Google Colab for free, without any local setup.

---

## ✨ Why Use Google Colab?

- ✅ **Free GPU/TPU access** (for advanced models)
- ✅ **No installation required** - runs in browser
- ✅ **Pre-installed libraries** - most Python packages ready
- ✅ **Easy sharing** - collaborate with teammates
- ✅ **Auto-save** - linked to Google Drive
- ✅ **Works on any device** - even Chromebooks!

---

## 🎯 Quick Start (5 minutes)

### Step 1: Access the Repository

1. Go to the GitHub repository
2. Navigate to any notebook (`.ipynb` file)
3. Click **"Open in Colab"** button (if available)

**OR**

1. Go to [Google Colab](https://colab.research.google.com/)
2. Click **File → Open Notebook**
3. Select **GitHub** tab
4. Paste repository URL or search for the repo
5. Select the notebook you want to open

### Step 2: Connect to Runtime

1. In Colab, click **Connect** (top right)
2. Wait for connection (usually <30 seconds)
3. You're ready to code! 🎉

### Step 3: Run Setup Cell

Every notebook starts with a setup cell:

```python
# Run this cell first!
import sys
import os

# Check if running in Colab
if 'google.colab' in sys.modules:
    # Clone repository (if needed)
    !git clone https://github.com/[username]/bike-availability-data-science.git
    %cd bike-availability-data-science
    
    # Install requirements
    !pip install -q -r requirements.txt

# Add project root to path
project_root = os.path.abspath("..")
if project_root not in sys.path:
    sys.path.append(project_root)

print("✅ Setup complete!")
```

---

## 📁 Working with Files in Colab

### Uploading Files

```python
from google.colab import files

# Upload a file
uploaded = files.upload()
```

### Downloading Files

```python
from google.colab import files

# Download a file
files.download('results.csv')
```

### Mounting Google Drive

To persist data across sessions:

```python
from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')

# Access files
import os
os.chdir('/content/drive/MyDrive/bike-project')
```

---

## 💾 Saving Your Work

### Auto-Save to Google Drive

**Recommended Method**:
1. **File → Save a copy in Drive**
2. Work from the Drive copy
3. Changes auto-save every few minutes

### Download to Local

1. **File → Download → Download .ipynb**
2. Save to your computer
3. Commit to your GitHub repository

### Save to GitHub

```python
# In Colab, after making changes
from google.colab import drive
drive.mount('/content/drive')

# Then use git commands
!git add notebook.ipynb
!git commit -m "Update from Colab"
!git push
```

---

## 🔧 Installing Additional Packages

Most packages are pre-installed, but if you need more:

```python
# Install a single package
!pip install package-name

# Install from requirements.txt
!pip install -r requirements.txt

# Install specific version
!pip install pandas==2.0.0

# Install quietly (less output)
!pip install -q package-name
```

---

## 📊 Common Colab Operations

### Check Python Version

```python
!python --version
```

### Check GPU Availability

```python
import torch
print("GPU available:", torch.cuda.is_available())

# Or simpler
!nvidia-smi
```

### View System Info

```python
# Check RAM
!cat /proc/meminfo | grep MemTotal

# Check CPU
!cat /proc/cpuinfo | grep "model name" | head -n 1

# Check disk space
!df -h
```

### Run Shell Commands

```python
# Use ! for shell commands
!ls -la
!pwd
!wget https://example.com/data.csv
```

---

## 🚨 Common Issues & Solutions

### Issue 1: Session Disconnected

**Cause**: Idle timeout (90 minutes) or 12-hour maximum session  
**Solution**: 
- Reconnect and re-run cells
- Use Google Drive to persist data
- Consider Colab Pro for longer sessions

```python
# Add this to prevent timeout
import time
while True:
    print("Keep alive...")
    time.sleep(60)
```

### Issue 2: Runtime Crashed

**Cause**: Out of memory  
**Solution**:
```python
# Clear memory
import gc
gc.collect()

# Use smaller batches
# Process data in chunks
```

### Issue 3: Package Not Found

**Solution**:
```python
!pip install package-name
import importlib
importlib.reload(module_name)
```

### Issue 4: File Not Found

**Solution**:
```python
# Check current directory
!pwd

# List files
!ls -la

# Make sure you're in the right directory
import os
os.chdir('/content/bike-availability-data-science')
```

---

## ⚡ Tips for Better Performance

### 1. Use GPU Runtime (Free!)

1. **Runtime → Change runtime type**
2. Select **GPU** or **TPU**
3. Click **Save**
4. Good for: Deep learning, large computations

### 2. Clear Output Regularly

1. **Edit → Clear all outputs**
2. Reduces notebook size
3. Faster loading

### 3. Organize with Sections

```python
#@title Section Title { display-mode: "form" }

# Your code here
# Code will be collapsible
```

### 4. Use Forms for Parameters

```python
#@title Training Parameters
learning_rate = 0.001 #@param {type:"number"}
num_epochs = 100 #@param {type:"slider", min:10, max:500, step:10}
model_type = "RandomForest" #@param ["RandomForest", "XGBoost", "LinearRegression"]
```

### 5. Hide Code Cells

```python
#@title Load Data { display-mode: "form" }

import pandas as pd
df = pd.read_csv('data.csv')
print(f"Loaded {len(df)} records")
```

---

## 🔐 Handling API Keys in Colab

### Method 1: Environment Variables (Recommended)

```python
import os
from google.colab import userdata

# Store in Colab secrets:
# Click 🔑 icon in left sidebar → Add secret
API_KEY = userdata.get('MY_API_KEY')
```

### Method 2: Uploaded File

```python
# Upload a file with your API key
from google.colab import files
uploaded = files.upload()

# Read the key
with open('api_key.txt', 'r') as f:
    API_KEY = f.read().strip()
```

### ⚠️ Never Do This:

```python
# ❌ DON'T hardcode API keys!
API_KEY = "sk-1234567890abcdef"  # Anyone can see this!
```

---

## 📱 Using Colab on Mobile

1. Install **Google Colab** app (iOS/Android)
2. Open notebooks from Drive
3. View outputs and run cells
4. Limited editing on mobile

---

## 🎓 Colab Pro (Optional)

**Free Tier Limits**:
- 90 min idle timeout
- 12 hour maximum session
- Standard GPU/RAM

**Colab Pro Benefits** (~$10/month):
- Longer runtimes
- More RAM
- Faster GPUs
- Background execution

**Worth it if**: You're running long training jobs or large datasets

---

## 🔗 Useful Resources

- [Colab Welcome Notebook](https://colab.research.google.com/notebooks/welcome.ipynb)
- [Colab FAQ](https://research.google.com/colaboratory/faq.html)
- [Colab Markdown Guide](https://colab.research.google.com/notebooks/markdown_guide.ipynb)
- [Keyboard Shortcuts](https://colab.research.google.com/notebooks/shortcuts.ipynb)

---

## ⌨️ Essential Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl + Enter` | Run current cell |
| `Shift + Enter` | Run cell and move to next |
| `Ctrl + M + B` | Insert cell below |
| `Ctrl + M + A` | Insert cell above |
| `Ctrl + M + D` | Delete cell |
| `Ctrl + M + Y` | Convert to code cell |
| `Ctrl + M + M` | Convert to markdown cell |
| `Ctrl + /` | Comment/uncomment |
| `Tab` | Auto-complete |

---

## ✅ Setup Checklist

Before starting each module:

- [ ] Connected to Colab runtime
- [ ] Ran setup cell
- [ ] Installed required packages
- [ ] Verified data access
- [ ] Mounted Drive (if needed)
- [ ] Saved a copy to Drive

---

## 🎯 Best Practices

1. **Save frequently** - Auto-save isn't instant
2. **Use descriptive filenames** - Easy to find later
3. **Clear outputs** before saving - Smaller file size
4. **Document as you go** - Add markdown cells
5. **Test with small data first** - Before full runs
6. **Download important results** - Don't rely only on Colab
7. **Use version control** - Commit to GitHub regularly

---

**Happy Coding in the Cloud! ☁️🚀**
