# The Additive Inverse on an Elliptic Curve

## **Definition of the Additive Inverse**

For every point \( P \) on an **Elliptic Curve**, there exists a point **\( P' \)** (often denoted **$-P$**) such that:
$$ P + P' = P + (-P) = P - P = \mathscr{O} $$

where **\( \mathscr{O} \)** is the **point at infinity**.

<div style="text-align: center;">
  <video width="640" height="360" controls>
    <source src="vid/additive-inverse.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</div>

---

## **The Inverse of the Inverse**

Clearly, the opposite applies. That is:
$$ -(-P) = P $$

---

## **Characteristic of 2 and 3**

It should also be noted that an **Elliptic Curve** defined on any field with **characteristic other than 2 or 3** can be **converted into the Weierstrass form**.

---

# **Weierstrass Form and Symmetry Around the X-Axis**

### **Equation of the Elliptic Curve in Weierstrass Form**

The **graph of an elliptic curve** in **Weierstrass form** ([Washington, L. C., 2008, pp. 9-11, Section 2.1](acknowledgements-bibliography.md)) is given by:
$$ y^2 = x^3 + Ax + B $$

where **\( A \)** and **\( B \)** are constants.

This equation exhibits **symmetry across the x-axis** due to several inherent properties.

---

### **Why is the Curve Symmetric?**

#### **1. Equation Form**

The equation:
$$ y^2 = x^3 + Ax + B $$

naturally defines symmetry about the **x-axis** because if **\( (x,y) \)** is a point on the curve, then **\( (x,-y) \)** must also be a point.

Since **\( y^2 \)** remains the same whether **\( y \)** or **\( -y \)** is used, this ensures symmetry.

#### **2. Even Function Relationship**

The function **\( y = x^2 \)** is an **even function**, meaning its graph is symmetric with respect to the **y-axis**.

For an elliptic curve, if you "swap" \( x \) and \( y \) in \( y = x^2 \), you obtain:
$$ y^2 = f(x) $$

which represents an elliptic curve when \( f(x) \) is a cubic function.

#### **3. Geometric Interpretation**

Geometrically, this symmetry means that:

- The curve **mirrors itself** across the **x-axis**.
- Any **vertical line** at a given \( x \) value intersects the curve at two points that are equidistant from the **x-axis** but on opposite sides.

---

## **The Role of Symmetry in Group Structure**

Symmetry plays a **critical role** in the **group law** for elliptic curves:

1. **Point Addition and the Inverse**

   - The **inverse of a point** \( (x, y) \) is **\( (x, -y) \)**.
   - This ensures that the **curve forms an abelian group**.

2. **Conversion to Weierstrass Form**
   - Any elliptic curve with **characteristic other than 2 or 3** can be converted to **Weierstrass form**.
   - This allows us to **use the symmetry** of the Weierstrass equation for most investigations.

### **Summary**

The **x-axis symmetry** in the Weierstrass equation is a **direct consequence** of:

- The **algebraic structure** of the equation.
- The fact that **\( y^2 \)** is always positive.
- The **group law**, which ensures that **\( (x, y) \) and \( (x, -y) \) always exist** in the curve’s structure.

---

# **The General Equation and Inversion**

### **More General Forms of an Elliptic Curve**

Less obviously, the **inverse by vertical line projection** also applies to some more **general equations** for elliptic curves.

A **general form** of an elliptic curve is:
$$ y^2 + a_1xy + a_3y = x^3 + a_2x^2 + a_4x + a_6 $$

([Washington, L. C., 2008, p. 10, Equation 2.1](acknowledgements-bibliography.md)) where **\( a_1, a_2, a_3, a_4, a_6 \)** are constants.

### **Computing the Inverse in General Form**

Given a point **\( P = (x,y) \)**, the inverse \( -P \) is:
$$ -P = (x, -y - a_1x - a_3) $$

This adjustment accounts for **linear terms in \( y \)** but still defines a point **vertically adjacent** to \( P \).

---

## **Exploring Transformations**

<div style="text-align: center;">
  <video width="640" height="360" controls>
    <source src="vid/general-equations.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</div>

In the animation above:

- **\( A \)** and **\( B \)** remain constant.
- All versions of the elliptic curve can be converted into **Weierstrass form**:
  $$ y^2 = x^3 + Ax + B $$

- The values are transformed as follows:
  $$ x\_{\text{new}} = dx + f $$

  $$ y\_{\text{new}} = ax\_{\text{new}} + by + c $$

The animation explores what happens to the **general transformed equation** when altering the values of:

- \( d, f, a, b, c \)  
  while keeping:
- \( A, B \), and the initial **P and Q** (and therefore \( R \) and \( R' = -R \)) **unchanged**.
