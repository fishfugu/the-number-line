---
date: 2025-03-25
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

# Review of Thesis Direction, Scope and Plan

## 1. Introduction & Motivation

1. **Elliptic Curves and Cryptography**  
   - Briefly introduce elliptic curves over finite fields - why they are central to modern cryptography.  
   - Highlight Discrete Logarithm Problem (DLP) - compare it to more “classical” factorisation-based RSA approach.  
   - State main questions we want to address: primarily point counting, its importance, and cryptanalytic landscape.

<!-- more -->

2. **Scope & Objectives**  
   - Lay out what we will (and will not) cover.  
   - Focus on mathematics and theoretical underpinnings (Hasse’s Theorem, structure of \( E(F_q) \), etc.) more than hardcore algorithmic-optimisation side.  
   - NOTE: not diving into engineering-level computational aspects.

---

## 2. Foundations: Elliptic Curves over Finite Fields
1. **Basic Definitions**  
   - Define elliptic curve E over field \( F_q \); talk about the group law, projective space vs. affine space.  
   - Provide high-level geometric intuition - e.g., how we visualise curves over real numbers or over the complex plane vs. over a finite field.  

2. **Finite Fields (Review)**  
   - Recap of \( F_q (q = p^n) \) construction, properties of Frobenius endomorphism, extension fields, and why these matter for elliptic curves.  
   - (Possibly) Touch on Galois theory just enough to show how F_q-extensions factor in, particularly for advanced point-counting methods.  

3. **Hasse’s Theorem**  
   - State the theorem and its immediate consequences (the bound on #E(F_q)).  
   - Highlight why bounding the number of points is crucial.  

---

## 3. Point-Counting Algorithms
*(This is where you can really dive in, comparing different algorithms is inherently “review and analysis.”)*

1. **Overview & Historical Context**  
   - The evolution from Schoof’s algorithm to the Schoof–Elkies–Atkin (SEA) algorithm.  
   - Explain that these algorithms compute #E(F_q) in polynomial time and are essential in choosing “secure” curves for ECC.  

2. **Schoof’s Algorithm**  
   - Outline the main idea: using division polynomials, computing E(F_q) mod small primes, etc.  
   - Discuss complexity and why it was such a groundbreaking improvement.  

3. **Schoof–Elkies–Atkin (SEA) Algorithm**  
   - Contrast with plain Schoof: using Elkies primes, Atkin primes to speed up the process.  
   - Provide a sense of how and why this algorithm is more efficient in practice.  

4. **Other Approaches**  
   - Mention related or advanced methods, possibly including p-adic or complex multiplication approaches to point counting.  
   - Clarify that these can get quite specialised (and can connect to deeper number-theoretic tools like Weil conjectures or zeta functions).  

5. **Why Point Counting Matters**  
   - Emphasise the “cryptographic parameter setting” angle: how #E(F_q) determines group sizes, security levels, etc.  
   - Link back to the broader theme of security: ensuring the curve order is prime (or nearly prime) so the discrete log problem remains hard.

---

## 4. Elliptic Curve Cryptography & Security
1. **Basics of ECC**  
   - Key generation, point multiplication, and the role of #E(F_q) in ensuring group order.  
   - Summarise the Discrete Log Problem specifically in E(F_q).  

2. **Attacks on ECC**  
   - Classic methods: Pollard’s Rho, Pohlig–Hellman, baby-step/giant-step, etc.  
   - Highlight how these attacks scale and how the group order (point count) influences the feasibility of these attacks.  
   - Note any specialised attacks (e.g., small subgroup attacks, special structure in the curve).  

3. **Post-Quantum Considerations (if desired)**  
   - Very briefly mention that quantum algorithms (like Shor’s algorithm) would solve discrete log in polynomial time on a quantum computer, but that for ECC the approach to “quantum-safe” cryptography is still an area of research.  
   - This can serve to contextualise “why might we keep pushing point counting, security analysis, etc.”

---

## 5. Advanced or Optional Topics
*(You can flexibly include or omit these based on time and advisor feedback.)*

1. **Weil Conjectures & Zeta Functions**  
   - Explain the connection: #E(F_q) can be encapsulated via the local zeta function, and Hasse’s Theorem is effectively a specific case of Weil’s bounds.  
   - This can give deeper insight into *why* counting points lines up with big results in algebraic geometry.

2. **Complex Multiplication**  
   - Show how CM can lead to the construction of curves with specific cryptographic properties.  
   - Often used in “endowed” curves or specialised cryptosystems.

3. **Pairing-based Cryptography**  
   - Outline how pairings (Weil pairing, Tate pairing) require knowledge of the group structure on E(F_q^n).  
   - This can lead to identity-based encryption or other advanced protocols, but also leads to new lines of attack in some cases.

---

## 6. Conclusion & Future Directions
1. **Summary of Findings**  
   - Recap the significance of point-counting algorithms in determining cryptographically secure elliptic curves.  
   - Summarise how the attacks interplay with the group order.  

2. **Open Problems & Emerging Areas**  
   - Any unresolved questions or deeper territory that goes beyond the Master’s thesis scope.  
   - For instance, advanced number-theoretic questions about curve constructions, or the interplay with post-quantum cryptography.

3. **Reflections on Implementation vs. Theory**  
   - Acknowledge the tension between pure mathematical aspects (e.g., bounding #E(F_q)) and the very practical question of how quickly and feasibly those computations can be done on real hardware.

---

# Is this Scope Too Large, Too Small, or Just Right?

1. **Core Components (Definitely “enough” for a Master’s Thesis)**  
   - A thorough literature review on point-counting algorithms (Schoof, SEA, etc.) plus an analysis of *why* these algorithms matter for selecting cryptographically secure curves is *definitely* enough to fill out a solid Master’s thesis.  
   - Coupled with a chapter on ECC fundamentals and standard attacks, you already have a robust project.

2. **Where the Scope Might Grow Too Large**  
   - If you add in-depth coverage of every advanced topic—Weil conjectures, complex multiplication, pairing-based crypto, post-quantum attacks, etc.—you can quickly balloon into something that’s more of a large-scale monograph than a typical Master’s thesis.  
   - It’s advisable to position the “advanced” sections as either short surveys or optional directions for future research rather than full-blown chapters.  

3. **Balancing Math vs. Implementation**  
   - You mention you don’t want to get too bogged down in the “raw computing details” of how quickly we can do modular arithmetic on a CPU or GPU. That’s perfectly fine—just be clear that your emphasis is on the mathematical and cryptanalytic reasoning, not on engineering optimisations.  
   - A small demonstration of how one might programmatically implement a simpler version of Schoof’s algorithm (to illustrate the mathematics) could still be a nice addition, but you don’t need to optimise it for large prime fields if that’s not your focus.

4. **Recommendation**  
   - Focus on the fundamentals, Hasse’s Theorem, and point-counting algorithms thoroughly.  
   - Include a dedicated chapter on the security landscape (attacks, cryptanalysis).  
   - Then, if you have space/time, add short sections on Weil/Zeta, CM, or pairings, but keep them more at a survey level to show how they connect to the bigger picture.  

With this approach, your thesis will be:
- Cohesive (starts with the basics, then delves into point-counting, then ties it all back to ECC security).  
- Manageable in size.  
- Still flexible enough to allow some interesting “optional” advanced topics to show broader context and your personal intellectual curiosity.

---

### Final Thoughts
- In short, the abstract you proposed is absolutely *viable* for a Master’s thesis. The big question is **depth** vs. **breadth**.  
- A strong recommendation is to *thoroughly* cover the “core” topics (ECC + point counting + attacks) and keep the big advanced items (Weil conjectures, complex multiplication, pairings) more *exploratory*.  
- This way, you neither undershoot nor overshoot. You’ll have a thoroughly researched, mathematically rich project that remains doable within typical Master’s-level timelines.