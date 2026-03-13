from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="pierreguillou/gpt2-small-portuguese"
)

print("=== Assistente de Estudos de Programação ===")
print("Digite 'sair' a qualquer momento para encerrar o programa.\n")

contador = 0

while True:
    pergunta = input("Sua dúvida: ")
    
    if pergunta.strip().lower() == 'sair':
        print(f"\nEncerrando... Você fez um total de {contador} pergunta(s). Bons estudos!")
        break
        
    contador += 1
    
    prompt = f"Pergunta sobre programação: {pergunta}\nExplicação simples e direta:"

    resposta = generator(
        prompt,
        max_new_tokens=80, 
        pad_token_id=generator.tokenizer.eos_token_id,
        truncation=True
    )
    
    print(f"\nProfessor ({contador}ª pergunta):")
    print(resposta[0]["generated_text"])
    print("-" * 50)