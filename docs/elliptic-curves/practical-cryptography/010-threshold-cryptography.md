# Threshold Cryptography: A Trustless Approach to Collective Agreement

## **Overview**

Here we will explore the concept of using **[public key cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography)** to allow a group of systems or people to **[collectively agree](https://www.sciencedirect.com/topics/computer-science/collective-agreement)** to unlock or decrypt something. Let's assume the core requirements of such a system are:

- A **[minimum number of participants](https://blog.pantherprotocol.io/threshold-cryptography-an-overview/#:~:text=After%20setting%20the%20number%20of,at%20least%20two%20more%20people.)** (t-of-n) must agree to unlock access.
- No participant ever reveals their **[private key](https://www.techtarget.com/searchsecurity/definition/private-key)** to another party.
- The system must be **[trustless](https://medium.com/@Ukeziebenezer/unlocking-societal-benefits-the-shift-from-trust-to-trustless-in-finance-505e3309d524#:~:text=Trustless%20systems%20aim%20to%20reduce,and%20transactions%20directly%20between%20parties.)**, meaning no single party should be able to compromise security.

Now, let's break down some of the various cryptographic techniques that can achieve this goal, their applications, trade-offs, and practical implementations.

---

## **Potential Use Cases**

There are a range of real-world scenarios in which such a system is beneficial, including:

- **[Banking and Investment Accounts](https://research.csiro.au/blockchainpatterns/general-patterns/security-patterns/multiple-authorization/):** Multi-signature authorisation for financial transactions where multiple stakeholders must approve access to funds.
- **[Data Recovery & Secure Storage](https://docs.rubrik.com/en-us/saas/qauth/quorum_authorization.html):** Protecting sensitive data so that a quorum of authorised parties must agree before it can be accessed.
- **[Secure Voting & Decision-Making Systems](https://eprints.qut.edu.au/250712/):** Cryptographically enforcing collective approval processes in decentralised systems.
- **[Blockchain & Smart Contracts](https://www.investopedia.com/tech/what-dao/):** Multi-party authorisation of transactions or governance decisions in decentralised networks.

---

## **Exploring Possible Approaches**

We initially investigated several cryptographic techniques to solve this problem:

### **1. [Shamir’s Secret Sharing (SSS) + Public Key Cryptography](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing#:~:text=SSS%20is%20used%20to%20secure,is%20needed%2C%20called%20the%20threshold.)**

- **General Idea:** The private key is split into multiple shares, and a quorum of shares is needed to reconstruct the key.
- **Used In Practice For:** Secure key backup and recovery, threshold decryption.
- **Why It's Not Appropriate For Our Use-Case:** Once the secret is reconstructed, secrecy is lost—making it unsuitable for a fully trustless system.

### **2. [Threshold RSA / Threshold Decryption](https://www.cs.ox.ac.uk/files/269/Thesis.pdf)**

- **General Idea:** The RSA private key is split across multiple participants who collaboratively perform decryption without reconstructing the full key.
- **Used In Practice For:** Secure messaging, threshold decryption.
- **Why It's Not Appropriate For Our Use-Case:** Not all implementations support **[Distributed Key Generation (DKG)](https://scryptplatform.medium.com/distributed-key-generation-3ef41ced01ed)**, meaning the private key might exist in full at some point.

### **3. [Threshold ECDSA](https://internetcomputer.org/docs/current/developer-docs/smart-contracts/signatures/t-ecdsa/) / [Schnorr Signatures](https://internetcomputer.org/docs/current/developer-docs/smart-contracts/signatures/t-schnorr#:~:text=Schnorr%20signatures%20are%20a%20type,be%20used%20on%20the%20network.)**

- **General Idea:** Multiple participants collectively generate a valid **[cryptographic signature](https://www.techtarget.com/searchsecurity/definition/digital-signature)** without reconstructing the [private key](https://www.preveil.com/blog/public-and-private-key/).
- **Used In Practice For:** Multi-signature wallets, secure transaction approvals.
- **Why We Chose this for our Use-Case:** Supports **[DKG](https://docs.skale.network/technology/dkg-bls)**, making it fully [trustless](https://www.morpher.com/blog/benefits-of-a-trustless-blockchain), and works well for [access control mechanisms](https://www.sciencedirect.com/science/article/pii/S2772918423000036).

### **4. [Multi-Party Computation (MPC) Approaches](https://www.fireblocks.com/what-is-mpc/#:~:text=In%20a%20general%20sense%2C%20MPC,any%20otherwise%20related%20secret%20information)**

- **General Idea:** A group of participants jointly computes a function without revealing individual inputs.
- **Used In Practice For:** Privacy-preserving computations, advanced cryptographic protocols.
- **Why We Didn’t Focus on this for our Use-Case:** High computational complexity and performance overhead.

---

## **Choosing Between Threshold ECDSA and Threshold Schnorr**

Both Threshold ECDSA and Threshold Schnorr allow t-of-n participants to collectively sign a message. The main differences are:

| Approach              | Can Unlock Access? | Keeps Keys Private? | Works Without Trusted Third Party? | Best For                                       |
| --------------------- | ------------------ | ------------------- | ---------------------------------- | ---------------------------------------------- |
| **Threshold ECDSA**   | ✅ Yes             | ✅ Yes              | ✅ Yes                             | Cryptographic signing & access control         |
| **Threshold Schnorr** | ✅ Yes             | ✅ Yes              | ✅ Yes                             | More efficient signing in multi-party settings |

Threshold Schnorr (e.g., **FROST**) is more efficient and flexible than ECDSA, which is why we focused on it for this use-case.

---

## **Why [Distributed Key Generation (DKG)](https://uwspace.uwaterloo.ca/items/05ecf041-a600-4ea1-8f76-c8a8cb3f14f7) Matters**

### **Why Avoid [Centralised Key Generation](https://www.researchgate.net/publication/339545481_A_Centralized_Key_Management_Scheme_Based_on_McEliece_PKC_for_Space_Network)?**

A major security risk exists if a full private key is ever generated before being "split" into shares. This would allow a single party to keep a copy of the key, breaking the trustless property.

### **What is [Distributed Key Generation (DKG)](https://www.usenix.org/conference/usenixsecurity23/presentation/das)?**

DKG allows a group to **[collectively generate a public-private keypair](https://eprint.iacr.org/2019/114.pdf)** without any single party ever having access to the full private key. The key is never assembled in one place, preventing compromise.

### **[How Does DKG Work?](<https://en.wikipedia.org/wiki/Distributed_key_generation#:~:text=Distributed%20key%20generation%20(DKG)%20is,rely%20on%20Trusted%20Third%20Parties.>)**

1. **Each participant generates a private share** independently.
2. **Participants exchange cryptographic commitments** to verify correctness.
3. **The collective public key is computed** from these shares, ensuring trustlessness.

Also see: [Asynchronous Distributed Private-Key Generators](https://eprint.iacr.org/2009/355.pdf)

### **Which Cryptosystems Support DKG?**

| Cryptosystem                  | Supports DKG? | Key Type   |
| ----------------------------- | ------------- | ---------- |
| **Threshold Schnorr (FROST)** | ✅ Yes        | Signing    |
| **Threshold ECDSA (GG20)**    | ✅ Yes        | Signing    |
| **Threshold RSA**             | ⚠️ Sometimes  | Decryption |
| **Paillier Cryptosystem**     | ⚠️ Sometimes  | Decryption |

---

## **How Threshold Signing Works Without Leaking Private Keys**

### **Key Insight: Partial Signatures Reveal Nothing**

Each participant computes a **[partial signature](https://eprint.iacr.org/2009/336.pdf)** without [exposing their private key share](https://www.researchgate.net/publication/2422330_Exposing_an_RSA_Private_Key_Given_a_Small_Fraction_of_its_Bits). This works because:

1. **Each signer picks a fresh random nonce** \( k_i \) per request.
2. **They commit to their nonce**: \( R_i = g^{k_i} \).
3. **They compute their partial signature**:

   $$ S_i = k_i + c \cdot x_i $$

   where \( c \) is a challenge computed from the message.
   s

4. **Aggregation ensures security**:

   $$ S = S_1 + S_2 + ... + S_t $$

   The final signature is valid, but the private key remains unknown.

### **Why is This Secure?**

- The function \( S_i = f(x_i) \) is **[one-way](https://en.wikipedia.org/wiki/One-way_function)** and non-invertible.
- Even if multiple signatures are observed, \( x_i \) **cannot** be derived.
- The aggregated signature is indistinguishable from a Schnorr signature created from a single private key input.

For more details on how this works, mathematically, and why it is secure, please see [The Mathematics Behind Threshold Cryptography](020-mathematics-of-threshold.md)

---

## **Practical Considerations**

### **How Many Participants Can Be in a Pool?**

There is no strict limit, but communication overhead grows with \( n \). Common useage examples are:

- **\( t = 3, n = 5 \)** (small teams)
- **\( t = 10, n = 100 \)** (large governance models)

but, theoretically, pools of participants and the number of people required to atisfy a request for partial signatures are only limited by considerations of performance.

### **How Agreement Works in Practice**

- Participants **sign in any order**, asynchronously.
- Each signer **sends only their partial signature** (which, importantly, still maintains the secrecy of the private key used)
- The final signature is computed once \( t \) shares are collected.

### **Who Sends What to Whom?**

- A requester broadcasts **a signing request**.
- Each signer computes their **partial signature** (if they wish too sign the request as "correct" or "passed")
- Partial signatures are **aggregated into a valid Schnorr signature**.
- The system **verifies** the final signature before unlocking access.

---

## Further Reading on Threshold Crytography

- [The Flexible Round-Optimized Schnorr Threshold (FROST) Protocol for Two-Round Schnorr Signatures](https://datatracker.ietf.org/doc/rfc9591/): This document specifies the Flexible Round-Optimized Schnorr Threshold (FROST) signing protocol. FROST signatures can be issued after a threshold number of entities cooperate to compute a signature, allowing for improved distribution of trust and redundancy with respect to a secret key. FROST depends only on a prime-order group and cryptographic hash function. This document specifies a number of ciphersuites to instantiate FROST using different prime- order groups and hash functions. This document is a product of the Crypto Forum Research Group (CFRG) in the IRTF.

- [FROST: Flexible Round-Optimized Schnorr Threshold Signatures](https://eprint.iacr.org/2020/852): Unlike signatures in a single-party setting, threshold signatures require cooperation among a threshold number of signers each holding a share of a common private key. Consequently, generating signatures in a threshold setting imposes overhead due to network rounds among signers, proving costly when secret shares are stored on network-limited devices or when coordination occurs over unreliable networks. In this work, we present FROST, a Flexible Round-Optimized Schnorr Threshold signature scheme that reduces network overhead during signing operations while employing a novel technique to protect against forgery attacks applicable to similar schemes in the literature.

- [GG20: Gennaro-Goldfeder Threshold ECDSA](https://eprint.iacr.org/2020/540): ... we show how to build a tailored protocol for threshold ECDSA with minimal overhead... We present a highly efficient protocol with a non-interactive online phase allowing for players to asynchronously participate in the protocol without the need to be online simultaneously. We benchmark our protocols and find that our protocol simultaneously reduces the rounds and computations of current protocols, while adding significant functionality: identifiable abort and noninteractivity.

### Practical Application

- [_Thetacrypt: A Distributed Service for Threshold Cryptography_](https://arxiv.org/html/2502.03247v1#S3): This paper introduces Thetacrypt, a library designed to integrate various threshold schemes into a unified codebase. It offers a practical approach to building distributed systems that utilise threshold cryptography.

  - Also see: [the GitHub repo for Thetacrypt - Threshold Cryptography Distributed Service in Rust](https://github.com/cryptobern/thetacrypt)

- [_Threshold Cryptography_](https://link.springer.com/referenceworkentry/10.1007/978-1-4419-5906-5_330?utm_source=chatgpt.com): This entry in the Encyclopedia of Cryptography and Security offers an overview of threshold cryptography, discussing its motivation, fundamental problems, and applications.

- [_Threshold Cryptosystems from Threshold Fully Homomorphic Encryption_](https://www.iacr.org/archive/crypto2018/10993213/10993213.pdf?utm_source=chatgpt.com): This paper explores threshold cryptosystems with non-interactive decentralized key generation, providing insights into advanced threshold encryption schemes.

- [_Multi-Party Threshold Signature Scheme_](https://github.com/bnb-chain/tss-lib): This is an implementation of multi-party {t,n}-threshold ECDSA (Elliptic Curve Digital Signature Algorithm) based on Gennaro and Goldfeder CCS 2018 1 and EdDSA (Edwards-curve Digital Signature Algorithm) following a similar approach.
