# CSCA48-MultiSet_ADT
Created a MultiSet ADT using SkipList ADT.


# SkipList ADT:

* In computer science, a skip list is a data structure that allows fast search within an ordered sequence of elements. Fast search is made possible by maintaining a linked hierarchy of subsequences, each skipping over fewer elements. Searching starts in the sparsest subsequence until two consecutive elements have been found, one smaller and one larger than the element searched for. Via the linked hierarchy these two elements link to elements of the next sparsest subsequence where searching is continued until finally we are searching in the full sequence. The elements that are skipped over may be chosen probabilistically [2] or deterministically,[3] with the former being more common.


# MultiSet ADT:
* In mathematics, a multiset (or bag) is a generalization of the concept of a set that, unlike a set, allows multiple instances of the multiset's elements. The multiplicity of an element is the number of instances of the element in a specific multiset.

  For example, an infinite number of multisets exist which contain elements a and b, varying only by multiplicity:

* The unique set {a, b} contains only elements a and b, each having multiplicity 1
* In multiset {a, a, b}, a has multiplicity 2 and b has multiplicity 1
* In multiset {a, a, a, b, b, b}, a and b both have multiplicity 3


# Please Note:

* My MultiSet works little differently as planned from the given instruction. The serach process works fine, but my SkipList works differently when it comes to insertion and delete. Since my SkipList Nodes can go foward, back, down, and up. We do not require the need to BOTTOM MOST Node. My ADT will auto delete all the Nodes iff one Node from the TOP or from the BOTTOM is deleted. This is a helpful features but surely takes up processing time.
