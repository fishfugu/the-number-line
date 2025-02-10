# The Discrete Logarithm Problem

The [**Discrete Logarithm Problem**](https://mathworld.wolfram.com/DiscreteLogarithm.html) is a foundational problem in the field of **cryptography** and **number theory**.

---

![abstract representation of cogs representing the discrete logarithm problem](img/log-cogs.png)

## Definition

The **Discrete Logarithm Problem** involves finding an integer \( x \) given the equation:
$$ g^x \equiv h \mod p $$

where:

- \( g \) is a known [**base**](https://mathworld.wolfram.com/Base.html#:~:text=The%20word%20%22base%22%20in%20mathematics,in%20which%20logarithms%20are%20defined.)
- \( h \) is a known **result**
- \( p \) is a [**prime number**](<https://mathworld.wolfram.com/PrimeNumber.html#:~:text=A%20prime%20number%20(or%20prime,other%20than%201%20and%20itself.)>) (or the [order of the group](https://mathworld.wolfram.com/GroupOrder.html) in more general settings)

In reference to the idea of [operations on sets of elements](set-group-ring-field.md), the operation:
$$ g^h $$

refers to applying the operation (in this case, multiplication `*`) **h** times. That is:
$$ g^h = g \times g \times g \times \dots \times g \quad \text{(h times)} $$

In the case of **elliptic curves**, we often refer to the same problem, in terms of the `+` operation:
$$ gh = h + h + h + \dots + h \quad \text{(h times)} $$

But the complexity of reversing the operation is still referred to as the **Discrete Logarithm Problem**.

---

## Context

### [**Group Theory**](https://mathworld.wolfram.com/GroupTheory.html#:~:text=Group%20theory%20is%20a%20powerful,in%20physics%2C%20especially%20quantum%20mechanics.)

The problem is defined within the context of [**cyclic groups**](https://mathworld.wolfram.com/GroupTheory.html#:~:text=Group%20theory%20is%20a%20powerful,in%20physics%2C%20especially%20quantum%20mechanics.), where the operations are performed under [**modular arithmetic**](<https://mathworld.wolfram.com/ModularArithmetic.html#:~:text=Modular%20arithmetic%20is%20the%20arithmetic,or%20seconds%20on%20a%20clock).>).

### [**Cryptography**](https://mathworld.wolfram.com/Cryptography.html)

The **Discrete Logarithm Problem** is crucial in the security of [cryptographic protocols](https://mathworld.wolfram.com/Diffie-HellmanProtocol.html), particularly in [**public key cryptography**](https://mathworld.wolfram.com/Public-KeyCryptography.html), such as:

- [**Diffie-Hellman key exchange**](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)
- [**Elliptic Curve Cryptography (ECC)**](https://planetmath.org/ellipticcurvecryptography)

---

## Difficulty

The **"discrete"** part of the name emphasizes that this problem is concerned with **integers**, unlike its continuous counterpart in real numbers.

The complexity of finding \( k \) in the equation:
$$ kP \equiv Q $$

(for multiplication on an elliptic curve) is what makes it valuable for cryptography.

There are **no known efficient (polynomial time) algorithms** for solving it in general cases, making it a **computationally hard problem**.

For applications in cryptography, we seek groups where the **Discrete Logarithm Problem** is **computationally difficult** to solve.

---

## Application

### [**Security**](https://nap.nationalacademies.org/resource/other/deps/illustrating-math/interactive/mathematics-of-internet-security.html)

The [difficulty of the **Discrete Logarithm Problem**](https://math.mit.edu/classes/18.783/2022/LectureNotes9.pdf) underpins the security of various [**encryption systems**](https://en.wikipedia.org/wiki/Encryption) and [**digital signatures**](https://en.wikipedia.org/wiki/Digital_signature), where:

- It is **easy to compute** exponentiation.
- It is **hard to reverse** (i.e., compute the logarithm).
- This provides [**cryptographic security**](https://en.wikipedia.org/wiki/Public-key_cryptography).

---

## Further Study

For an interesting investigation of the **algebra** behind the **Discrete Logarithm Problem**, and its importance in **Applied Cryptography**, check out:

🔗 [Leandro Junes' YouTube playlist: The Discrete Logarithm Problem](https://www.youtube.com/watch?v=n41Z0c9Jm4Y&list=PL1xkDS1G9As7E_fPaLaFchq1a27I9a5tO)
