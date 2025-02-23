# The Mathematics Behind Threshold Cryptography

## **How Does Aggregation Work Without Revealing the Private Key?**

[**Threshold cryptography**](https://medium.com/@kyodo-tech/threshold-encryption-for-secure-multi-party-collaboration-72e168052da7) is a field that enhances the security and reliability of cryptographic systems by [distributing trust among multiple parties](https://csrc.nist.gov/projects/threshold-cryptography). In a (t,n)-threshold scheme, [any t out of n participants can collaboratively perform a cryptographic operation](https://documents.uow.edu.au/~jennie/WEB/WEB10/cryptoII.pdf), such as decryption or signing, while fewer than t participants cannot.

In a threshold cryptography system such as **[Threshold Schnorr](https://eprint.iacr.org/2023/445.pdf)**, a group of participants contribute to a signature without ever revealing their individual private key shares. This is done through a process called **[signature aggregation](https://crypto.stanford.edu/~dabo/papers/aggsurvey.pdf)**, which ensures that:

1. a minimum number of participants (t-of-n) can generate a valid signature, and
2. no single participant ever knows the full private key, and
3. the system remains secure even if some participants are compromised.

### **Step 1: Individual Key Shares**

Each participant \( i \) holds a private key share \( x_i \), a randomly chosen number:

$$ x_i \in \mathbb{Z_q} $$

where \( q \) is the order of the elliptic curve group.

Each participant also has a corresponding public key share:

$$ X_i = g^{x_i} $$

where \( g \) is the generator of the group.

### **Step 2: Aggregated Public Key**

The collective public key is obtained by summing the individual public keys:

$$ X = X_1 + X_2 + ... + X_n $$

Since exponentiation and addition in elliptic curve groups are **homomorphic**, this means:

$$ X = g^{(x_1 + x_2 + ... + x_n)} $$

### **Step 3: Partial Signatures**

!!! note "Why does this help?"

    Having calculated \( S_i \), it can be freely and openly shared with anyone. Knowing \( S_i \) does not allow anyone to (easily, or in a reasonable amount of time) calculate \( k_i \), \( c \), or (moost importantly, in a way) \( x_i \).

    And so, the value of \( S_i \) can be safely sent to the requester of the response (or anyone else), giving nothing away about your private key, in the process.

    For some background information on why calculating these things is "hard", or "practically impossible", see our previous article on [the Distrete Logarithm Problem](discrete-logarithm.html).

Each participant generates a **random nonce** \( k_i \) per signing request:

$$ R_i = g^{k_i} $$

Each participant then computes their **partial signature**:

$$ S_i = k_i + c \cdot x_i $$

where \( c \) is a challenge computed from the message:

$$ c = H(X, R, m) $$

and \( H \) is a secure cryptographic hash function.

### **Step 4: Aggregation of Signatures**

Once at least **t** participants respond, their partial signatures are summed:

$$ S = S_1 + S_2 + ... + S_t $$

Similarly, their nonce commitments are summed:

$$ R = R_1 + R_2 + ... + R_t $$

### **Step 5: Final Signature**

The final Schnorr signature is:

$$ (R, S) $$

!!! note "Why this is important"

    The fact that \( x \) CAN NOT be calculated (not because it's not "part of the process" but because no one ever has the right information to do so), is important. It means that no person, or service, in this process can ever calculate the "collective private key" for the group.

which is equivalent to a normal Schnorr signature using the full (but never explicitly computed) private key:

$$ x = x_1 + x_2 + ... + x_t $$

### **Step 6: Verification**

To verify the aggregated signature, the verifier checks:

$$ g^S = R \cdot g^{cX} $$

If the equation holds, the signature is valid, proving that the group collectively signed the message without exposing any individual \( x_i \), either to each other, or the requester of the signature.

## **Why Does This Work?**

The security of this system relies on:

- **[The Discrete Log Problem (DLP)](../../elliptic-curves-101/discrete-logarithm.html)**: Given \( g^x \), it is infeasible to compute \( x \) in polynomial time.
- **Random Nonces**: Since each signing request uses fresh random nonces, an attacker cannot link signatures to extract private keys.
- **One-Way Hashing**: The challenge \( c \) is derived from the message, making replay attacks impossible.

Since **no single participant is ever capable of reconstructing the private key**, the system remains trustless and secure.

---

## More on Threshold Cryptography in General

This page is intended as a "break out" from [this site's main explainer on Threshold Crytography](threshold_crypto_explainer.html). If you have come from there, to read this more detailed material, please [click here to return to the main explainer](threshold_crypto_explainer.html).

## Further Reading on the Maths Behind Threshold Cryptography

- [Cryptography 101: Threshold Signatures](https://medium.com/@francomangone18/cryptography-101-threshold-signatures-ac63c412122a): This article will be solely dedicated to explaining one such example, where we’ll combine the usual _signing techniques_ with _polynomials_, to create an interesting _hybrid scheme_. We’ll be working in the context of _elliptic curves_, and use \( G \) and \( H \) to denote group generators for a group \( \mathbb{G} \).

- [_Threshold Schemes for Cryptographic Primitives_](https://nvlpubs.nist.gov/nistpubs/ir/2019/NIST.IR.8214.pdf?utm_source=chatgpt.com): from [the National Institute of Standards and Technology (NIST)](https://www.nist.gov/), this publication provides an overview of implementing cryptographic primitives using threshold schemes. It discusses how multiple components can collaboratively achieve security goals, even when some are compromised.

- [_Threshold Cryptosystems: A Comprehensive Survey_](https://arxiv.org/abs/2311.05514?utm_source=chatgpt.com): reviews threshold digital signatures, covering both conventional and [post-quantum cryptography](https://en.wikipedia.org/wiki/Post-quantum_cryptography) settings. It examines various signature families, their applications, and potential future research directions.
