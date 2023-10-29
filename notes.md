
Tokens
- https://platform.openai.com/tokenizer
- rules of thumb: 
    - one token ~= 4 characters, which ~= 3/4 of a word
    - 100 tokens ~= 75 words
- token count of prompt + `max tokens` arg cannot exceed model's context length
    - as of Apr 2023:
        - most = 2048
        - newer = 4069

Temperature
- float. range: [0,2]
- lower = more deterministics (ex: 0.2)
- higher = more random (ex: 0.8)
- alt: can use `top_p` param, which uses nucleus sampling (vs sampling w/ temp)


Playground
- https://platform.openai.com/playground
