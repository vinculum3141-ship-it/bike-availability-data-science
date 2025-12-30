# Contributing to Bike Availability Data Science Project

Thank you for participating in this course! This document provides guidelines for organizing your work and maintaining a professional project structure.

## 📝 General Guidelines

- Write clean, readable code with meaningful variable names
- Document your work with clear markdown cells in notebooks
- Test your code before committing
- Follow Python best practices (PEP 8)

## 🗂️ Project Organization

### Notebooks
- Place notebooks in the appropriate module folder
- Follow the naming convention: `M{module}_{number}_{description}.ipynb`
  - Example: `M2_01_data_acquisition_api.ipynb`
- Always include a setup cell at the beginning of each notebook

### Source Code
- Write reusable functions in `src/` modules
- Add docstrings to all functions and classes
- Keep functions focused and single-purpose
- Use type hints where appropriate

### Data
- Store raw data in `data/raw/`
- Store processed data in `data/processed/`
- Do NOT commit large datasets (add to .gitignore if needed)
- Document your data sources and transformations

## 💻 Code Style

### Python
```python
# Good
def calculate_bike_availability(station_data: pd.DataFrame) -> float:
    """
    Calculate the average bike availability for a station.
    
    Args:
        station_data: DataFrame with bike availability records
        
    Returns:
        Average availability as a float
    """
    return station_data['available_bikes'].mean()

# Avoid
def calc(d):
    return d['available_bikes'].mean()
```

### Notebooks
- Start with a title and description
- Use markdown to explain your approach
- Comment complex code sections
- Display results clearly with visualizations
- Summarize key findings at the end

## 🔄 Git Workflow

### Commit Messages
Use clear, descriptive commit messages:

```bash
# Good commit messages
git commit -m "Add data acquisition notebook for Amsterdam bike data"
git commit -m "Implement feature engineering for time-based features"
git commit -m "Fix bug in bike availability calculation"

# Avoid
git commit -m "update"
git commit -m "fix"
git commit -m "changes"
```

### Commit Frequency
- Commit after completing a logical unit of work
- Commit working code (make sure it runs without errors)
- Don't commit broken code or half-finished work

### What to Commit
✅ DO commit:
- Python scripts and notebooks
- Documentation and markdown files
- Configuration files
- Small reference datasets (<1MB)

❌ DON'T commit:
- Large datasets (>1MB)
- API keys or passwords
- Temporary files (.ipynb_checkpoints, __pycache__)
- Virtual environment folders

## 🧪 Testing Your Work

Before committing, verify:
1. All notebook cells run without errors (Kernel → Restart & Run All)
2. No hardcoded paths (use relative paths or config files)
3. No exposed API keys or credentials
4. Code follows the naming conventions
5. Markdown documentation is clear and complete

## 📊 Data Science Best Practices

### Experimentation
- Track your experiments (parameters, results, insights)
- Document failed approaches (learning opportunity!)
- Use version control for model iterations

### Reproducibility
- Set random seeds for reproducible results
- Document all dependencies in requirements.txt
- Include data preprocessing steps in notebooks

### Model Development
- Start simple (baseline model)
- Document model assumptions
- Validate on held-out test data
- Avoid data leakage

## 🎓 Learning Goals

Remember, the goal is to:
- Learn by doing (make mistakes and learn from them)
- Build a portfolio-worthy project
- Practice real-world data science workflows
- Develop good coding habits

## 🤝 Getting Help

If you're stuck:
1. Review the module materials
2. Check the documentation in `docs/`
3. Look at the project structure for guidance
4. Reach out to instructors or peers

## 📚 Additional Resources

- [PEP 8 Style Guide](https://pep8.org/)
- [Jupyter Notebook Best Practices](https://jupyter-notebook.readthedocs.io/)
- [Git Commit Message Guidelines](https://chris.beams.io/posts/git-commit/)

Happy learning! 🚴‍♀️📊
