import transformers as tf

generator = tf.pipeline(
    "text-generation",
    model="pierreguillou/gpt2-small-portuguese"
)

respostas = generator(
    "Dê uma dica de programação para iniciantes:",
    max_length=80,
    temperature=0.9,
    do_sample=True,
    num_return_sequences=3,
    pad_token_id=generator.tokenizer.eos_token_id
)

for i, resposta in enumerate(respostas):
    print(f"=== Dica {i+1} ===")
    print(resposta["generated_text"])
    print()

print("""
=== Análise ===
Com a temperature = 0.9, as respostas ficaram mais CRIATIVAS e variadas. 
Isso ocorre porque valores mais altos aumentam a aleatoriedade das palavras, 
evitando que o modelo gere textos repetitivos ou óbvios demais.
""")