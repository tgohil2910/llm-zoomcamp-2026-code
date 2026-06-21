def calculate_gpt54mini_price(input_tokens, output_tokens):
    INPUT_PRICE_PER_MILLION = 0.15
    OUTPUT_PRICE_PER_MILLION = 0.60

    input_cost = (input_tokens / 1_000_000) * INPUT_PRICE_PER_MILLION
    output_cost = (output_tokens / 1_000_000) * OUTPUT_PRICE_PER_MILLION
    total_cost = input_cost + output_cost

    return {
        "input_cost": input_cost,
        "output_cost": output_cost,
        "total_cost": total_cost,
    }

result = calculate_gpt54mini_price(652, 33)
print("Total cost: $", round(result["total_cost"], 8))