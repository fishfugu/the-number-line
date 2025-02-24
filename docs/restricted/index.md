<script src="../assets/restricted.js"></script>

# The Number Line

## Restricted Access Area

This section of The Number Line site is designed to be a resticted access area.

But don't get too excited. All we're keeping here is notes on what needs to be done, and plans for the future site... so if you've got in here because you were super interested, and "hacked" your way in (it wasn't hard, was it?)... have at it!! :-)

### Other Restricted Pages

- [Notes on Animation](animation-notes.md)

## The Big TODO list

[ ] TODO: move the old site over to here

- [ ] TODO: _Elliptic Curves_ by Anthony W. Knapp.
  - [x] Get it from UNE
  - [ ] read it

### Section Elliptic Curves 101

- [ ] TODO: on the "point-addition" page - inmentions the idea of "the inflection point on curve where it shifts from -ve curvature to +ve curvature" - explore this idea in terms of the first and second derivative, in the weierstrass form, and the fact it represents a "triple root"

- [ ] TODO: on "point addition page - redo "Examples of Torsion Points" and try put in 5P = -P. But first, work out how to add P + 4P = 5P. It's easy if you do 2P + 3P, or even P + 4P = P - 2P = -P... but how do simple add P to 4P, when the line make a tangent with P? Do you simply have to assume the association that the tangent crosses at -2P... and there for P + 4P = P - 2P = -P?

- [ ] TODO: on "point addition page - check 4P is marked properly (should it be -4P) - and exlpain in detail that this is being found by doubling points

- [ ] TODO: "where g is the generator of the group" needs a separate explainer section

### Threshold Crytography

- [mathematics-of-threshold.html](../elliptic-curves/practical-cryptography/020-mathematics-of-threshold.md) "Since exponentiation and addition in elliptic curve groups are **homomorphic**, this means" - needs explanation, reference and more research

- [mathematics-of-threshold.html](../elliptic-curves/practical-cryptography/020-mathematics-of-threshold.md) "where $ q $ is the order of the elliptic curve group" - the idea of `the order` needs explanation - a page - and references

- You can design a system where a predefined group of participants control access to signing operations, and additional members can be added dynamically if a quorum (threshold) of existing members approve the addition. Do we want to do more research into this aspect? This can be implemented using Threshold Signatures and Multi-Party Computation (MPC). See notes on topic...

- [mathematics-of-threshold.html](../elliptic-curves/practical-cryptography/020-mathematics-of-threshold.md): check section at bottom under Practical Considerations and link to references on important topics within that summary

## The LONG list of "Things to Read Later (maybe)":

### Quantum Crytography

- This chapter covers secret sharing, threshold cryptography, signature schemes, and finally quantum key distribution and quantum cryptography. https://documents.uow.edu.au/~jennie/WEB/WEB10/cryptoII.pdf

### Threhold Crytography

- [_Threshold Cryptosystems From Threshold Fully Homomorphic Encryption_](https://www.iacr.org/archive/crypto2018/10993213/10993213.pdf?utm_source=chatgpt.com): We develop a general approach to adding a threshold functionality to a large class of (non-threshold) cryptographic schemes. A threshold functionality enables a secret key to be split into a number of shares, so that only a threshold of parties can use the key, without reconstructing the key. We begin by constructing a threshold fully-homomorphic encryption scheme (ThFHE) from the learning with errors (LWE) problem. We next introduce a new concept, called a universal thresholdizer, from which many threshold systems are possible. We show how to construct a universal thresholdizer from our ThFHE. A universal thresholdizer can be used to add threshold functionality to many systems, such as CCA-secure public-key encryption (PKE), signature schemes, pseudorandom functions, and others primitives. In particular, by applying this paradigm to a (non-threshold) lattice signature system, we obtain the first single-round threshold signature scheme from LWE.

- [_Threshold Implementations of Cryptographic Functions Between Finite Abelian Groups_](https://eprint.iacr.org/2024/439?utm_source=chatgpt.com): Side-channel attacks pose a significant threat to the security of cryptographic hardware implementations and Threshold Implementation (TI) is a well-established countermeasure to mitigate those attacks...

- [Quasigroups](https://www.jstor.org/stable/1990259?seq=1): Introduction. A theory of non-associative algebras has been developed(') withbout any assumption of a substitute for the associative law, and the basic structure properties of such algebras have been shown to depend upon the possession of almost these same properties by related associative algebras. It seems natural then to attempt to obtain an analogous treatment of quasigroups. We shall present the results here. Most of the results in the literature on quasigroups do depend upon special associativity conditions(2) but no assumption of such conditions is necessary for our theorems.

- [Design and analyses of two basic protocols for use in TTP-based Key escrow](https://link.springer.com/chapter/10.1007/bfb0027933): In this paper, we study two basic protocols which are important in realizing TTP-based key escrow systems. A TTP-based key escrow system was studied in [3] under the scenario of multiple domains (e.g., countries), where a protocol based on verifiable secret sharing scheme was proposed to transfer a shared secret from one set of TTPs to another set of TTPs. However, the protocol only allows one step transfer, i.e., transfer a shared secret from set A to set B, but the same shared secret can not be further transferred from B to any other set.

- [Secret Sharing Homomorphisms: Keeping Shares of a Secret Secret (Extended Abstract)](https://link.springer.com/chapter/10.1007/3-540-47721-7_19): In 1979, Blackley and Shamir independently proposed schemes by which a secret can be divided into many shares which can be distributed to mutually suspicious agents. This paper describes a homomorphism property attained by these and several other secret sharing schemes which allows multiple secrets to be combined by direct computation on shares. This property reduces the need for trust among agents and allows secret sharing to be applied to many new problems. One application described here gives a method of verifiable secret sharing which is much simpler and more efficient than previous schemes. A second application is described which gives a fault-tolerant method of holding verifiable secret-ballot elections.

- [Efficient generation of shared RSA keys](https://link.springer.com/chapter/10.1007/bfb0052253): We describe efficient techniques for three (or more) parties to jointly generate an RSA key. At the end of the protocol an RSA modulus N = pq is publicly known. None of the parties know the factorization of N. In addition a public encryption exponent is publicly known and each party holds a share of the private exponent that enables threshold decryption. Our protocols are efficient in computation and communication.

- [Key escrow in mutually mistrusting domains](https://link.springer.com/chapter/10.1007/3-540-62494-5_14): In this paper we present a key escrow system which meets possible requirements for international key escrow, where different domains may not trust each other. In this system multiple third parties, who are trusted collectively but not individually, perform the dual role of providing users with key management services and providing authorised agencies in the relevant domains with warranted access to the users' communications. We propose two escrowed key agreement mechanisms, both designed for the case where the pair of communicating users are in different domains, in which the pair of users and all the third parties jointly generate a cryptographic key for end-to-end encryption. The fact that all entities are involved in the key generation process helps make it more difficult for deviant users to subvert the escrowed key by using a hidden ‘shadow-key’. The first mechanism makes use of a single set of key escrow agencies moderately trusted by mutually mistrusting domains. ! The second mechanism uses a transferable and verifiable secret sharing scheme to transfer key shares between two groups of key escrow agencies, where one group is in each domain.

- [Protocol failure in the escrowed encryption standard](https://dl.acm.org/doi/abs/10.1145/191177.191193): The Escrowed Encryption Standard (EES) defines a US Government family of cryptographic processors, popularly known as “Clipper” chips, intended to protect unclassified government and private-sector communications and data. A basic feature of key setup between pairs of EES processors involves the exchange of a “Law Enforcement Access Field” (LEAF) that contains an encrypted copy of the current session key. The LEAF is intended to facilitate government access to the cleartext of data encrypted under the system. Several aspects of the design of the EES, which employs a classified cipher algorithm and tamper-resistant hardware, attempt to make it infeasible to deploy the system without transmitting the LEAF. We evaluated the publicly released aspects of the EES protocols as well as a prototype version of a PCMCIA-based EES device. This paper outlines various techniques that enable cryptographic communication among EES processors without transmission of the valid LEAF. We identify two classes of techniques. The simplest allow communication only between pairs of “rogue” parties. The second, more complex methods permit rogue applications to take unilateral action to interoperate with legal EES users. We conclude with techniques that could make the fielded EES architecture more robust against these failures.

## Learning Outcomes

### The documented learning outcomes for this course

- demonstrate specialist knowledge and technical research skills in the planning, design and execution of a research project in a specialist area of study;
- demonstrate a theoretical knowledge of, and critically reflect on, scientific research as it relates to the specialist area of study;
- critically evaluate and theorise on issues contributing to the professional and ethical standards of practice expected in the specialist area of study;
- apply communication skills to convey methodologies, conclusions and professional decisions resulting from the project to audiences ranging from experts to those with no knowledge of the specialist area of study;
- demonstrate the ability to apply knowledge to new developments in the specialist area of study; and
- demonstrate an ability to plan and deliver research seminars.

### Assessments

Assessment 1
Research proposal.
No. Words: 2000

Assessment 2
Literature review.
No. Words: 4000

Assessment 3
Oral presentation.
