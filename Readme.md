# Affine Cypher Decoder

An Affine Cypher is a Cypher that generates an encoded string using the formula
```C = aP + b```
P is the original String
a is a simple integer
b is a simple integer


It can be decoded with the following formula
```P = aC + b```

This Python Script is based around the basic algorithm for a Affine Cypher, and uses a brute force method and dictionary tester to make sure that it is decoding a valid english string. The task was given from [r/dailyprogrammer](https://www.reddit.com/r/dailyprogrammer/comments/6k123x/20170629_challenge_321_intermediate_affine_cipher/) as task on reddit and uses the dictionary provided by them.
