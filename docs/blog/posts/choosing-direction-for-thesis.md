---
date: 2025-03-24
categories:
  - UNE
  - Master of Scientific Studies
  - CRICOS CODE 000441G
  - Jelena Schmalz
  - SCI500
  - Research Methods in the Sciences
  - 2024 Literature Review
  - Elliptic Curves
tags:
  - scope
  - planning
authors:
  - fishfugu
---

# Choosing a Direction for the Masters Thesis

To help me focus my efforts, my thesis supervisor asked me to focus on which of the most general areas (the differen Fields and Rings on which Elliptic curves are defined) I would like to focus on for my thesis - as this will instruct the reqwuirements of the Literature Revieww I'm working on right now, and help to illuminate what I'm trying to achieve with my thesis.

<!-- more -->

Elliptic Curves (ECs) are wonderfully rich objects precisely because they behave very differently depending on the Field (or Ring) over which you consider them. Each choice (over the Reals \(\mathbb{R}\), a Finite Field \(\mathbb{F}_p\), the Rationals \(\mathbb{Q}\), or the Complex Numbers \(\mathbb{C}\)) opens the door to a slightly different set of questions and techniques. Below is an overview of how each path typically unfolds and what sort of research directions one might pursue.

---

## 1 Elliptic Curves over \(\mathbb{R}\)

### Themes
- **Visualisation and Real Geometry**  
  Easily visualised as a cubic curve in the plane with some real components (depending on whether the cubic has 0, 1, or 2 "real ovals"). Studied with real geometry and real analysis tools, though some of the deeper number-theoretic aspects might be “invisible” over \(\mathbb{R}\).

- **Elliptic Integrals**  
  The integral of a differential on an elliptic curve (when viewed as a real curve) leads to the notion of elliptic integrals, which connect to special functions in real analysis.

- **Directions**  
    1. Detailed geometric analysis of real points on the curve (the shape/topology of the real locus).  
    2. Connections to real-analytic functions, elliptic integrals, real analysis aspects of Weierstrass \(\wp\)-functions.  
    3. Further, might connect to some transcendence questions / real algebraic geometry.

### Pros / Cons
- **Pros**: More straightforward geometric intuition; direct connections to real-variable tools (good for hands-on “pictures” and real analysis).  
- **Cons**: Some deep arithmetical structure less prominent here. Results can be less “headline-making” in modern number theory compared to rational or finite-field settings - though there's still interesting real geometry to explore.

---

## 2 Elliptic Curves over a Finite Field \(\mathbb{F}_p\)

### Themes
- **Applications to Cryptography**  
  Biggest draw to studying ECs over finite fields is their application to public-key cryptography (Elliptic Curve Cryptography, ECC). Look at the group of \(\mathbb{F}_p\)-rational points and discrete-log-type problems.

- **Counting Points / Hasse’s Theorem**  
  A fundamental question is the number of points on the curve, captured by Hasse’s theorem
  $$ |\#E(\mathbb{F}_p) - (p+1)| \le 2\sqrt{p} $$
  leads to the study of zeta functions of the curve (local factors of its L-function), interplay with coding theory, etc.

- **Directions**  
    1. **Cryptographic aspects**: Security analysis, discrete log, isogenies, pairing-based cryptography.  
    2. **Computational number theory**: Algorithms for point counting (Schoof’s algorithm and improvements), fast group law computations.  
    3. **Algebraic geometry**: Weil conjectures in the simpler setting of elliptic curves, properties of the Frobenius endomorphism.

### Pros / Cons
- **Pros**: Active area. Lots of real-world applications / specialised computational tools; synergy with practical cryptography.  
- **Cons**: If you’re looking for very classical (or purely theoretical) number-theoretic questions like ranks, Mordell–Weil groups, BSD conjecture, you might find you have to shift to rational or complex curves.

---

## 3 Elliptic Curves over \(\mathbb{Q}\)

### Key Themes
- **Classical Arithmetic Geometry**  
  Mordell’s theorem states that \(E(\mathbb{Q})\) (the group of rational points) is finitely generated. Understanding the rank, torsion structure, and so forth leads to beautiful (and famously difficult) territory.

- **Birch and Swinnerton-Dyer (BSD) Conjecture**  
  One of the Clay Millennium Problems, the BSD conjecture, is intimately tied to elliptic curves over \(\mathbb{Q}\). It relates the rank of \(E(\mathbb{Q})\) to the behavior of an associated L-function \(L(E, s)\). Research in this area touches the deepest parts of modern arithmetic geometry.

- **Directions**  
    1. **Ranks, torsion subgroups, heights**: The group structure \(E(\mathbb{Q})\).
    2. **L-functions and BSD**: Special values of \(L\)-functions, p-adic L-functions, or Iwasawa theory.
    3. **Galois representations**: Torsion points of \(E\) reflect the Galois group of \(\mathbb{Q}\).

### Pros / Cons
- **Advantages**: It's the “classic, deep core” of elliptic curve theory. For number theory, big open problems (BSD), and advanced algebraic geometry, this is the choice.
- **Disadvantages**: Can be quite abstract, highly technical, and requires a solid background in advanced algebraic geometry, number theory, and the theory of modular forms. Progress can be slow and demands specialised knowledge.

---

## 4 Elliptic Curves over \(\mathbb{C}\)

### Themes
- **Complex Analysis and Geometry**  
  Every elliptic curve can be viewed as a torus \(\mathbb{C} / \Lambda\), where \(\Lambda\) is a 2D lattice in \(\mathbb{C}\). This viewpoint leads to classical theorems involving the Weierstrass \(\wp\)-function, elliptic functions, and the identification of elliptic curves with complex tori.

- **Connection to Modular Forms**  
  The theory of elliptic curves over \(\mathbb{C}\) includes the idea of how the \(j\)-invariant parameterizes complex elliptic curves (via moduli). This is deeply intertwined with the theory of modular forms and the geometry of the upper half-plane.

- **Directions**  
    1. **Complex tori**: The shape and classification of elliptic curves via lattice quotients.  
    2. **Elliptic functions**: Studying the \(\wp\)-function and other special functions of complex analysis.  
    3. **Moduli spaces**: Studying the moduli space of elliptic curves, the connection to modular curves, and advanced aspects of algebraic geometry over \(\mathbb{C}\).

### Pros / Cons
- **Pros**: Interplay with complex analysis (the theory of elliptic functions is classical and elegant). Very geometric viewpoint; many important foundational results are first proven over \(\mathbb{C}\).  
- **Cons**: If ultimate aim is something purely arithmetic (like rational points or finite fields), might have to shift from the complex-analytic viewpoint eventually. Great for geometry and classical complex function theory.

---

## Notes on Decision

### **Broader research interests**
- **cryptography** or **computational aspects**, go with **finite fields**.  
- **classical number theory** / connect to famous conjectures, go with **\(\mathbb{Q}\)**.  
- **geometery** or analytical side (elliptic integrals, special functions) but still real / complex tools, go with **\(\mathbb{R}\)** or **\(\mathbb{C}\)**.

This encourages me towards **\(\mathbb{Q}\)**

But I don't want to ignore my experience in Software Development / Engineering - which would encourage me towards **finite fields**.

### **Tools to master**
- **Over \(\mathbb{R}\) and \(\mathbb{C}\)**: deeper into real/complex analysis, geometric viewpoints, and classical function theory.  
- **Over \(\mathbb{Q}\) and \(\mathbb{F}_p\)**: focus more on algebraic geometry, arithmetic, number theory, and possibly computational/cryptographic methods.

This encourages me towards: **\(\mathbb{Q}\) and \(\mathbb{F}_p\)**.

### **Jelena's expertise / interests**
- **Cryptographery / computational number theory**: might do best with finite fields.
- **Classical pure maths / rational points or L-functions**: \(\mathbb{Q}\) might be better.

This is an open question for me.

### **Post-Thesis direction**
- **Industry or applied paths**: finite fields and cryptography are a natural fit.  
- **Academic career in pure math**: elliptic curves over \(\mathbb{Q}\) or \(\mathbb{C}\) (and their deep theoretical frameworks) can provide a rich foundation.

My "emotional" / immediate reaction to this... pushes me towards **\(\mathbb{Q}\) or \(\mathbb{C}\)**.

But again - I don't want to be _silly_ and _ignore_ the value of picking a direction with lots of real-world drivers behind it. I do have a lot of experience as a programmer - and while I took up my Maths study to try to focus on more academic, and pure studies... Even as an academic study, choosing a direction that has direct real-world applications can be a good idea.

If I _were_ to go down the \(\mathbb{F}_p\), I would actually be very interested in somewhat of an "historical" / chronological approach to my thesis... that is:
- how did we get to where we are with modern crytogrtaphy (right from the begginning)?
- comparisons with the the fast factorisation question and RSA crytography

---

## General Thoughts

So if we look at the 4 sections above as giving a point each to each of the foci... and a \( 1 \over 2 \) point when the recommendation is split...

That's 2 points for \(\mathbb{Q}\), \( 1 \over 2 \) point for \(\mathbb{F}_p\), and \( 1 \over 2 \) point for \(\mathbb{C}\).

So that either decides it for \(\mathbb{Q}\) - OR, if I give 2 points to Jelena's advice, it could still swing the result either way.

- There is no single “best” choice; each domain has its own powerful techniques and famous open questions.  
- A research path can use multiple viewpoints (e.g., might start with a complex-analytic viewpoint of an elliptic curve but ultimately investigate its \(\mathbb{Q}\)-rational properties).

### Current strategy

- sample each perspective briefly - e.g., read about Hasse’s theorem in the finite-field case, look at the rank problem over \(\mathbb{Q}\), see how a complex torus is formed from a lattice in \(\mathbb{C}\)—and see what resonates.

---

## Current Reading

For each section:

1. **\(\mathbb{R}\)**: [Greenhill, Alfred George. The Applications of Elliptic Functions (1892)](https://ia601304.us.archive.org/11/items/cu31924001588395/cu31924001588395.pdf)

2. **\(\mathbb{F}\)**: [Koblitz, Neal. “Elliptic Curve Cryptosystems.” Mathematics of Computation 48 (1987)](https://www.jstor.org/stable/pdf/2007884.pdf?refreqid=fastly-default%3A9f30ab2ed4e65d3ce2b7425d4d08fdb4&ab_segments=&initiator=&acceptTC=1) - "[stable URL](https://www.jstor.org/stable/2007884)"

3. **\(\mathbb{Q}\)**: [Silverman, Joseph H. The Arithmetic of Elliptic Curves, Graduate Texts in Mathematics, Vol. 106 (Springer, 1986)](http://www.pdmi.ras.ru/~lowdimma/BSD/Silverman-Arithmetic_of_EC.pdf)

4. **\(\mathbb{C}\)**: Lang, Serge. Elliptic Functions, 2nd ed., Graduate Texts in Mathematics, Vol. 112 (Springer, 1987) - but I haven't been able to get a copyt of this yet... so... 