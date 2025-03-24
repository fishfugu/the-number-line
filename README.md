# The Number Line

Welcome to **The Number Line**, a knowledge base dedicated to mathematical communication, with a focus on elliptic curves and number theory.

## 🚀 Getting Started

### 1️⃣ Install Dependencies

Ensure you have Python and MkDocs installed:

```bash
pip install mkdocs-material
```

_(Or install via Homebrew if preferred: `brew install mkdocs-material`)_

### 2️⃣ Running the Site Locally

To preview the site on your computer:

```bash
mkdocs serve
```

Then visit `http://127.0.0.1:8000/`.

### 3️⃣ Adding Content

- All pages are in the `docs/` directory as Markdown files (`.md`).
- Use KaTeX for maths equations:
  ```md
  $$ y^2 = x^3 + ax + b $$
  ```
- Update `mkdocs.yml` to add new pages to the navigation:
  ```yaml
  nav:
    - Home: index.md
    - Introduction: introduction.md
    - New Topic: new-topic.md
  ```

### 4️⃣ Deploying the Site

After making changes, push them to GitHub and deploy:

```bash
git add .
git commit -m "Updated content"
git push origin main
mkdocs gh-deploy
```

---

## Converting files to PDF using pandoc

```bash
pandoc --from=markdown+tex_math_single_backslash \
       --to=pdf \
       --pdf-engine=pdflatex \
       --output=output.pdf \
       docs/blog/posts/summary-spielman-spectral-algebraic-graph-theory-text.md
```

## 🤝 Contributing

Contributions are welcome! If you’d like to improve **The Number Line**, here’s how:

### 1️⃣ Fork the Repository

Click the **Fork** button at the top right of this GitHub repo to create your own copy.

### 2️⃣ Clone Your Fork

Download your forked repository to your local machine:

```bash
git clone https://github.com/your-username/the-number-line.git
cd the-number-line
```

### 3️⃣ Create a New Branch

Before making changes, create a separate branch:

```bash
git checkout -b feature-new-topic
```

### 4️⃣ Make Your Changes

- Add or edit Markdown files in `docs/`
- Update `mkdocs.yml` if necessary
- Run `mkdocs serve` to preview changes locally

### 5️⃣ Commit and Push

Once happy with your changes:

```bash
git add .
git commit -m "Added new topic on XYZ"
git push origin feature-new-topic
```

### 6️⃣ Open a Pull Request

- Go to **your fork** on GitHub
- Click **New Pull Request**
- Select `main` as the target branch
- Add a description of your changes and submit the PR

I’ll review and merge your contribution!

---

## 📜 License

This project is licensed under the MIT License.

---

## ❓ FAQ

### **Q: How do I add a new topic?**

A: Create a new `.md` file in the `docs/` directory and update `mkdocs.yml` to include it in the navigation.

### **Q: How do I contribute if I'm new to GitHub?**

A: Follow the steps in the **Contributing** section above. If you need help, open an issue!

### **Q: What mathematical notation is supported?**

A: The site uses **KaTeX** for rendering math equations.

### **Q: Where can I see a preview before deploying?**

A: Run `mkdocs serve` locally and visit `http://127.0.0.1:8000/`.

---

## 🛠 Troubleshooting

### **Issue: MkDocs command not found**

- Ensure MkDocs is installed using `pip install mkdocs-material`.
- If using Homebrew, try `brew install mkdocs-material`.

### **Issue: KaTeX not rendering properly**

- Check that `pymdownx.arithmatex` is enabled in `mkdocs.yml`.
- Ensure your equations are wrapped properly in `$$`.

### **Issue: GitHub Pages not updating**

- Ensure `gh-pages` branch exists.
- Try running `mkdocs gh-deploy` again.
- Check your GitHub repository settings under **Pages**.

---

## 🚀 Roadmap

### 🔹 Phase 1: Initial Setup (✅ Complete)

- Set up MkDocs with Material theme
- Enable KaTeX for math notation
- Deploy to GitHub Pages

### 🔹 Phase 2: Content Expansion

- Add structured sections on elliptic curves
- Include interactive visualizations (Future goal)
- Add deeper content on number theory connections

### 🔹 Phase 3: Multimedia Integration

- Start a blog section
- Integrate YouTube content
- Explore podcast hosting options
