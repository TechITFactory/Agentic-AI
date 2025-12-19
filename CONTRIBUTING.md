# Contributing to Agentic AI Course

Thank you for your interest in contributing! This course is designed to be a comprehensive, production-ready resource for aspiring AI/ML engineers.

## 🎯 Course Philosophy

**"Minimum DS + Maximum Practical"**

Everything we add should:
- ✅ Be immediately applicable in real projects
- ✅ Follow production best practices
- ✅ Include working, tested code
- ✅ Have clear, practical explanations
- ✅ Focus on what companies actually use

## 🚀 Ways to Contribute

### 1. Report Issues

Found a bug or unclear explanation?
- Use GitHub Issues
- Include section number and specific problem
- Provide screenshots if relevant

### 2. Improve Documentation

- Fix typos or unclear explanations
- Add clarifying examples
- Improve code comments
- Translate content (future)

### 3. Add Code Examples

- New algorithms implementations
- Alternative approaches
- Performance comparisons
- Edge case handling

### 4. Create Labs/Exercises

- Hands-on coding exercises
- Real-world problem scenarios
- Progressive difficulty challenges

### 5. Enhance Existing Content

- Better explanations
- More efficient code
- Additional best practices
- Updated dependencies

## 📋 Contribution Guidelines

### Code Standards

**Python Code**:
- Follow PEP 8 style guide
- Use type hints for function signatures
- Include docstrings for all functions/classes
- Add inline comments for complex logic
- Test all code before submitting

**Example**:
```python
def train_model(X_train: np.ndarray, y_train: np.ndarray) -> RandomForestClassifier:
    """
    Train a Random Forest classifier.
    
    Args:
        X_train: Training features (n_samples, n_features)
        y_train: Training labels (n_samples,)
    
    Returns:
        Trained RandomForestClassifier model
    """
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model
```

### Documentation Standards

**Lesson Structure**:
1. Clear learning objectives
2. Concept explanation (2-3 paragraphs)
3. Code example with comments
4. Common mistakes/pitfalls
5. Key takeaways

**Markdown Style**:
- Use headers consistently (# for title, ## for sections)
- Include code blocks with language hints
- Add visual separators between major sections
- Keep paragraphs short (3-5 sentences max)

### Lab/Exercise Standards

Each lab should include:
- **README.md**: Clear instructions and learning objectives
- **starter.py**: Template with TODOs for students
- **solution.py**: Complete working solution
- **data/**: Sample dataset if needed
- **Expected Output**: What success looks like

### Testing Requirements

Before submitting:
- ✅ Code runs without errors
- ✅ All imports work
- ✅ Results are reproducible
- ✅ Documentation is clear
- ✅ No security vulnerabilities

## 🔄 Pull Request Process

### 1. Fork and Clone

```bash
# Fork on GitHub first, then:
git clone https://github.com/YOUR_USERNAME/Agentic-AI.git
cd Agentic-AI
```

### 2. Create Branch

```bash
git checkout -b feature/your-feature-name
# Examples:
# - feature/add-xgboost-tutorial
# - fix/pandas-example-typo
# - docs/improve-section-5-readme
```

### 3. Make Changes

- Follow code and documentation standards
- Test thoroughly
- Update relevant READMEs
- Keep commits focused and atomic

### 4. Commit

```bash
# Stage changes
git add .

# Commit with descriptive message
git commit -m "Add XGBoost hyperparameter tuning example"

# Good commit messages:
# - "Fix typo in Section 2 README"
# - "Add data leakage demonstration"
# - "Improve FastAPI error handling"
# - "Update requirements.txt with latest versions"
```

### 5. Push and Create PR

```bash
git push origin feature/your-feature-name
```

Then create Pull Request on GitHub with:
- **Title**: Clear, descriptive
- **Description**: What changes and why
- **Related Issues**: Link to issue if applicable
- **Testing**: How you tested the changes

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code improvement

## Testing Done
- [ ] Tested locally
- [ ] All code runs without errors
- [ ] Documentation reviewed

## Related Issues
Fixes #(issue number)
```

## 🎓 Content Contribution Guidelines

### Adding a New Lesson

1. **Follow Section Structure**:
   ```
   sections/XX-section-name/
   ├── XX-lesson-name.md
   └── code/
       └── example.py
   ```

2. **Lesson Format**:
   ```markdown
   # Lesson Title
   
   ## Overview
   Brief introduction
   
   ## Concept Explanation
   Main content
   
   ## Code Example
   ```python
   # Working code
   ```
   
   ## Common Mistakes
   Pitfalls to avoid
   
   ## Key Takeaways
   Summary bullets
   ```

3. **Update Section README** to include new lesson

### Adding a New Lab

1. **Create Lab Directory**:
   ```
   sections/XX-section/labs/lab_name/
   ├── README.md
   ├── starter.py
   ├── solution.py
   └── data/
   ```

2. **Lab README Should Include**:
   - Learning objectives
   - Problem description
   - Step-by-step instructions
   - Expected output
   - Time estimate

3. **Code Requirements**:
   - Starter has clear TODOs
   - Solution is well-commented
   - Both run without errors

### Adding a New Section

Discuss with maintainers first via GitHub Issues.

Required:
- Section README
- At least 3 lessons with code
- One lab or mini-project
- Integration with course flow

## 🐛 Bug Reports

### What to Include

- **Section/File**: Where the bug is
- **Description**: What's wrong
- **Expected Behavior**: What should happen
- **Actual Behavior**: What actually happens
- **Steps to Reproduce**: How to see the bug
- **Environment**: Python version, OS, etc.

### Example Bug Report

```markdown
**Section**: 02-python-for-ai
**File**: code/pandas_examples.py

**Description**: Code fails when running with pandas 2.1.0

**Expected**: Examples should run successfully

**Actual**: 
```
AttributeError: 'DataFrame' object has no attribute 'append'
```

**Steps**:
1. Install pandas 2.1.0
2. Run `python pandas_examples.py`
3. Error occurs at line 45

**Environment**: Python 3.11, pandas 2.1.0, macOS
```

## 📝 Style Guidelines

### Code Comments

```python
# Good: Explains WHY
# Use StandardScaler because features have different ranges
scaler = StandardScaler()

# Bad: Explains WHAT (obvious from code)
# Create a StandardScaler
scaler = StandardScaler()
```

### Documentation Tone

- ✅ Conversational and friendly
- ✅ Practical and example-driven
- ✅ Clear and concise
- ❌ Academic or overly formal
- ❌ Unnecessarily complex
- ❌ Vague or handwavy

### Code Naming

```python
# Good
def calculate_precision_recall(y_true, y_pred):
    ...

# Bad
def calc_pr(yt, yp):
    ...
```

## ⚖️ License

By contributing, you agree that your contributions will be licensed under the same license as the project.

## 🤝 Code of Conduct

### Our Standards

- ✅ Be respectful and inclusive
- ✅ Accept constructive criticism
- ✅ Focus on what's best for students
- ✅ Show empathy towards others

### Unacceptable Behavior

- ❌ Harassment or discrimination
- ❌ Trolling or inflammatory comments
- ❌ Personal or political attacks
- ❌ Publishing others' private information

## 🎯 Priority Areas

Looking for contribution ideas? These areas need help:

1. **High Priority**:
   - Complete Section 3 (data science fundamentals)
   - Build Section 4 (ML algorithms)
   - Create Section 6 (Kubernetes deployment)

2. **Medium Priority**:
   - Finish Section 2 (Python tutorials)
   - Expand Section 5 (more serving patterns)
   - Add more labs across sections

3. **Nice to Have**:
   - Additional code examples
   - Alternative approaches
   - Performance optimizations
   - Translations

## 📞 Questions?

- **General Questions**: Use GitHub Discussions
- **Bug Reports**: Use GitHub Issues
- **Feature Requests**: Use GitHub Issues with [Feature Request] tag
- **Security Issues**: Email (provide email here)

## 🎉 Recognition

Contributors will be:
- Listed in README acknowledgments
- Credited in relevant sections
- Thanked in release notes

## 📚 Resources for Contributors

### Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)

### Tools

- [Black](https://black.readthedocs.io/) - Python code formatter
- [Flake8](https://flake8.pycqa.org/) - Python linter
- [MyPy](https://mypy.readthedocs.io/) - Type checker

### Course Structure

Review [DEVELOPMENT.md](./DEVELOPMENT.md) for current status and roadmap.

---

Thank you for helping make this course better! 🚀

Your contributions help aspiring AI/ML engineers build real-world skills and launch their careers.
