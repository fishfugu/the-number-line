# The Weierstrass and more General Forms of Elliptic Curves

Taking the Weierstrass form of an elliptic curve and translating our \( x \)-values and \( y \)-values with specific functions, we can convert the Weierstrass form to a more general form (related to, but slightly extending, the equation defined in _Washington, L. C., 2008, p10, Equation 2.1_). The resulting curve remains an elliptic curve.

> **IMPORTANT:** This general form is not generally symmetrical around the \( x \)-axis. As such, the calculation of the additive inverse becomes less straightforward — a topic we explore further in subsequent sections.

However, as shown below, these translations never cause the additive inverse (_P_ and _P′ = –P_) to deviate from being vertically aligned.

---

## The Transformation Process

### 1. Starting with the Weierstrass Form

Begin with the standard equation for an elliptic curve in Weierstrass form:

$$
y^2 = x^3 + Ax + B \quad \text{ for some } A, B \in \mathbb{R}
$$

### 2. Translating the Coordinates

Apply translations to both the _x_-values and _y_-values using the following functions:

$$
x' = dx + f \quad \text{ for some } d, f \in \mathbb{R}
$$

$$
y' = dx + f \quad \text{ for some } d, f \in \mathbb{R}
$$

This yields a new equation for the elliptic curve:

```
(Insert new equation here)
```

Which can be rewritten in the form:

```
(Insert general form equation here)
```

with the following parameter definitions:

```
(Insert parameter details here)
```

### 3. Recognizing the Generalised Weierstrass Equation

The equation

```
(Insert equation here)
```

is recognized as the _generalised Weierstrass equation_ of an elliptic curve (Washington, L. C., 2008, p. 10, Equation 2.1). Notice that it is equivalent to the derived form except for the inclusion of an $x^3$ coefficient, $a_0$. By dividing the right-hand side by $a_0 = \frac{d^3}{b^2}$, the graph (when defined over the Real numbers) becomes vertically compressed towards the _x_-axis yet remains topologically unchanged. In other words, the derived equation and the generalised Weierstrass equation are isomorphic.

This correspondence suggests a method to reliably transform an elliptic curve from the general form back to the specific Weierstrass form.

---

## Step-by-Step Parameter Transformations

Each parameter in the equations influences the curve in visually intuitive ways when graphed on a 2-dimensional plane.

### Horizontal Adjustments

- **Changing $d$:**  
  The curve is squeezed or stretched horizontally.

- **Changing $f$:**  
  The curve shifts laterally along the _x_-axis.

- **Changing both $d$ and $f$ simultaneously:**  
  Animations include a faint dotted grid to illustrate how the space over which the curve is defined is transformed.

### Vertical Adjustments

- **Changing $b$:**  
  The curve is squeezed or stretched vertically.

- **Changing $c$:**  
  The curve slides up or down along the _y_-axis.

- **Changing $a$ (a particularly interesting case):**  
  The curve undergoes a vertical slide relative to its distance from the _y_-axis. At $x = 0$, there is no change, but the effect becomes more pronounced further from the axis—transforming squares into parallelograms (as seen with the shifting green grid points).

In every case, points that were originally vertically aligned remain so after the transformation. This consistency is key to understanding how the additive inverse is affected—a topic addressed in the next section.

---

## Combined Transformations

When all five parameters are altered simultaneously, the behavior of the curve is particularly interesting. Notice, for example, the line connecting $R$ and $R′ = -R = (P+Q)$, which remains perfectly vertical throughout the transformation.

---

## Interactive Visualizations

The online version of this content includes interactive animations to help visualize the following:

- **Horizontal and Vertical Scaling:**  
  Animations show the curve being squeezed, stretched, and shifted in both directions.

- **Grid Overlays:**  
  A faint dotted grid aids in understanding how the coordinate space transforms.

For the complete interactive experience, please visit:  
[Creative Arts – Expanding from Weierstrass to General Form](https://www.creativearts.com.au/article/expanding-weierstrass-to-general-form)
