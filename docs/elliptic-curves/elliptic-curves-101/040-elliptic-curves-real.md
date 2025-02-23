# Elliptic Curves over \( \mathbb{R} \)

[Elliptic curves](https://mathworld.wolfram.com/EllipticCurve.html#:~:text=Formally%2C%20an%20elliptic%20curve%20over,%2C%20or%20a%20finite%20field.) have applications in various mathematical fields, including [**number theory**](https://mathworld.wolfram.com/NumberTheory.html#:~:text=Number%20theory%20is%20a%20vast,the%20properties%20of%20whole%20numbers.) and [**cryptography**](https://mathworld.wolfram.com/Cryptography.html).

---

<div style="float: left; margin-right: 15px;">
    <img src="img/ec-in-R.png" alt="graph showing two different Elliptic Curves in the Real numbers, one continuous, and one with 2 separate sections" width="300px">
</div>
## Definition

An **elliptic curve** over \( \mathbb{R} \) is defined by a [cubic equation](https://mathworld.wolfram.com/CubicEquation.html#:~:text=A%20cubic%20equation%20is%20an,solutions%20of%20a%20cubic%20equation.) of the form:
$$ y^2 = x^3 + Ax + B $$

where \( A \) and \( B \) are [real coefficients](https://mathworld.wolfram.com/Coefficient.html).

When these coefficients satisfy the condition:
$$ 4A^3 + 27B^2 \neq 0 $$

the curve is [**non-singular**](https://mathworld.wolfram.com/Determinant.html).

Elliptic curves that do not satisfy this condition are called **singular elliptic curves**.

### **The Weierstrass Equation**

In the form:
$$ y^2 = x^3 + Ax + B $$

an elliptic curve is said to be in the **Weierstrass Equation form**.

There are [more general equations that define elliptic curves](https://mathworld.wolfram.com/EllipticCurve.html) over \( \mathbb{R} \) ([Washington, L. C., 2008, pp. 35-42, Section 2.5](acknowledgements-bibliography.md)). However, elliptic curves can be [**converted** into the Weierstrass Equation form](https://crypto.stanford.edu/pbc/notes/elliptic/weier.html) when defined across fields with [a characteristic other than **2 or 3**](https://mathworld.wolfram.com/EllipticCurve.html).

---

## Animation of ECs in the Weierstrass form

See below, an animation of different elliptic curves in the Weierstrass Form, for varying values of the coefficients A and B (in the equation \( y^2 = x^3 + Ax + B \)):

<div style="text-align: center;">
  <video width="640" height="360" controls>
    <source src="vid/weierstrass-form.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</div>

---

<div style="float: left; margin-right: 15px;">
    <img src="img/geometry.jpg" alt="graph showing two different Elliptic Curves in the Real numbers, one continuous, and one with 2 separate sections" width="250px">
</div>

## Geometric Features

### **Discriminant and Shape**

The shape of an elliptic curve in Weierstrass form depends on the **discriminant**:
$$ \Delta = -16(4A^3 + 27B^2) $$

([Washington, L. C., 2008, pp. 9-11, Section 2.1](acknowledgements-bibliography))

---

<div style="float: right; margin-left: 15px;">
    <img src="img/geometry2.jpg" alt="graph showing two different Elliptic Curves in the Real numbers, one continuous, and one with 2 separate sections" width="250px">
</div>

- If **\( \Delta < 0 \)**, the curve is a **single, connected loop**.  
  The cubic equation: \( x^3 + Ax + B = 0 \) has **one real solution**.

- If **\( \Delta > 0 \)**, the curve consists of **two disjoint loops**.  
  The cubic equation: \( x^3 + Ax + B = 0 \) has **three real solutions**.

**Note:** The definition of these "loops" will become clearer once we introduce the concept of [**the point at infinity**](projective-plane). For now, we accept that the far end of each curve **connects at infinity**.

### **Symmetry**

Every elliptic curve in Weierstrass form is **symmetric** about the **x-axis**.  
If \( (x, y) \) is on the curve, then so is \( (x, -y) \).

---

<div style="float: right; margin-left: 15px;">
    <img src="img/group-law.jpg" alt="graph showing two different Elliptic Curves in the Real numbers, one continuous, and one with 2 separate sections" width="300px">
</div>

## Group Law: Addition of Points

Elliptic curves over \( \mathbb{R} \) form a **group** under the operation of **point addition**.

If **\( P \)** and **\( Q \)** are points on the curve, their sum **\( P + Q \)** is defined **geometrically** by:

- Drawing a **line through \( P \) and \( Q \)**.
- Finding its **third intersection point** with the curve.
- Reflecting that point over the **x-axis**.

---

<div style="float: left; margin-right: 15px;">
    <img src="img/group-law-2.png" alt="graph showing two different Elliptic Curves in the Real numbers, one continuous, and one with 2 separate sections" width="300px">
</div>

### **Special Cases in Point Addition**

#### When \( P = Q \)

When \( P = Q \) (i.e the points you are adding together are equal), as described above under "Group Law":
$$ P + Q = 2P $$

so the equation for the gradient:
$$ m = \frac{ y_Q - y_P }{ x_Q - x_P } $$

no longer makes any sense - because:
$$ x_Q - x_P = 0 $$

and therefore, the denominator would be 0.

So we need to find the slope of E:
$$ m = \frac{ x_P^2 + a }{ 2 y_P } $$

([Washington, L. C., 2008, pp13-14, Section 2.2](acknowledgements-bibliography.md))

The concept of finding the slope of an Elliptic Curve will be further explored in [the section on "Formal Derivatives"](slope-of-elliptic-curve.md). For now, we will simply say that we use the derivative for finding the slope at a point on the curve.

#### When \( y = 0 \)

That is: the tangent to the curve E is a vertical line.

So:
$$ 2P = \text{"the point at infinity"} $$

It can also be shown, related to the definition of addition for elliptic curves, that any straight line that passes through 3 points on the curve (\( P \), \( Q \) and \( R \)) represents the fact that:
$$ P + Q + R = 0 $$

For this, and many related reasons, the "point at infinity" is taken to be the "additive neutral element" for the Group defined for Elliptic Curves ([Washington, Section 2.3, pp18-20](acknowledgements-bibliography.md)).

NOTE: When defined in \( \mathbb{R} \), it can easily be shown that, if the tangent line to the curve \( E \) is anything other than vertical, [it will intersect with E (in the Affine plane), at another point](line-connecting-p-q-intersect-third-point.md).

---

## Applications

### **[Cryptography](https://en.wikipedia.org/wiki/Cryptography)**

Elliptic curves over \( \mathbb{R} \) serve as **simpler models** for understanding more **complex cryptographic schemes** over finite fields and rings, including those used in **Elliptic Curve Cryptography (ECC)**.

### **[Theoretical Mathematics](https://en.wikipedia.org/wiki/Algebraic_geometry)**

Elliptic curves are studied for their properties in **algebraic geometry** and **number theory**.

---

## Challenges & Considerations

### **[Visualisation](https://mathworld.wolfram.com/EllipticCurve.html#:~:text=Informally%2C%20an%20elliptic%20curve%20is,form%20of%20an%20elliptic%20curve.)**

Unlike elliptic curves over finite fields (used in cryptography), curves over \( \mathbb{R} \) can be **graphically represented**, making visual learning **more intuitive**.

### **[Complexity in Handling](<https://math.libretexts.org/Under_Construction/Purgatory/Book%3A_Active_Calculus_(Boelkins_et_al.)/01%3A_Understanding_the_Derivative/1.07%3A_Limits_Continuity_and_Differentiability>)**

While real-number elliptic curves are **easier to visualise**, they introduce complexities in ensuring **mathematical rigor**, especially concerning:

- **Limits**
- **Continuity**
- **Differentiability**
