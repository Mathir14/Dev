the problem has two methods,
in encode, we have to shorten the given url
in decode, we have to take that shorten url and expand it to it's original form by
cracking the encode

though a valid and full fledged url shortener isn't in my expertise at this stage,
the main goal is to transform it in some way during encode
and reverse that transformation to return the original url during decode

even a simple [::-1] works for that
