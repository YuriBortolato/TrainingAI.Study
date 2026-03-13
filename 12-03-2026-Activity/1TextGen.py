import transformers

generator = transformers.pipeline(
    "text-generation",
    model="pierreguillou/gpt2-small-portuguese"
)

limite_tokens = 120

resposta_prog = generator(
    "Explique de forma bem resumida o que é programação:",
    max_new_tokens=limite_tokens,
    pad_token_id=generator.tokenizer.eos_token_id,
    truncation=True
)

resposta_bd = generator(
    "Explique de forma bem resumida o que é banco de dados:",
    max_new_tokens=limite_tokens,
    pad_token_id=generator.tokenizer.eos_token_id,
    truncation=True
)

resposta_ia = generator(
    "Explique de forma bem resumida o que é inteligência artificial:",
    max_new_tokens=limite_tokens,
    pad_token_id=generator.tokenizer.eos_token_id,
    truncation=True
)

print("=== Programação ===")
print(resposta_prog[0]["generated_text"])

print("\n=== Banco de Dados ===")
print(resposta_bd[0]["generated_text"])

print("\n=== Inteligência Artificial ===")
print(resposta_ia[0]["generated_text"])