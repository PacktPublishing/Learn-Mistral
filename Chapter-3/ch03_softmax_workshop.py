import numpy as np

def softmax(logits, temperature=1.0):
    # Convert logits to a NumPy array
    logit_values = np.array(list(logits.values()))
    # Apply temperature scaling
    scaled_logits = logit_values / temperature
    # Calculate the exponential of each logit
    exp_logits = np.exp(scaled_logits)
    # Normalize by dividing by the sum of all exponentials
    probabilities = exp_logits / np.sum(exp_logits)
    return probabilities


def sort_logits_by_probability(logits, temperature=1.0):
    probabilities = softmax(logits, temperature)
    # Sort indices based on probabilities in descending order
    sorted_indices = np.argsort(probabilities)[::-1]
    sorted_logits = np.array(list(logits.items()))[sorted_indices]
    sorted_probabilities = probabilities[sorted_indices]
    return sorted_logits, sorted_probabilities


def top_k(logits, k, temperature=1.0):
    sorted_logits, sorted_probabilities = sort_logits_by_probability(logits, temperature)
    # Keep only the top k logits
    top_k_logits = sorted_logits[:k]
    top_k_probabilities = sorted_probabilities[:k]
    return top_k_logits, top_k_probabilities

def top_p(logits, p, temperature=1.0):
    sorted_logits, sorted_probabilities = sort_logits_by_probability(logits, temperature)
    # Calculate the cumulative probabilities
    cumulative_prob = np.cumsum(sorted_probabilities)
    # Find the smallest set of logits where the cumulative probability exceeds p
    cutoff_index = np.argmax(cumulative_prob >= p)
    top_p_logits = sorted_logits[:cutoff_index + 1]
    top_p_probabilities = sorted_probabilities[:cutoff_index + 1]
    return top_p_logits, top_p_probabilities

def min_p(logits, p, temperature=1.0):
    return top_p(logits, 1-p, temperature)


# Example logits
logits = {
    'guitar': 2.5,
    'melody': 2.2,
    'whisper': 1.4,
    'sunset': 1.3,
    'avalanche': 0.3,
    'elephant': 0.2
}

temperature = 0.7
p = 0.7
min_p_value = 0.3
k = 3

# Softmax probabilities
probabilities = softmax(logits, temperature)
print("Softmax probabilities:", probabilities)

# Top k logits and probabilities
top_k_logits, top_k_probabilities = top_k(logits, k, temperature)
print("\nTop k logits and probabilities:")
for (word, logit), prob in zip(top_k_logits, top_k_probabilities):
    print(f'{word}: Logit = {logit}, Probability = {prob*100:.2f}%')

# Top p logits and probabilities
top_p_logits, top_p_probabilities = top_p(logits, p, temperature)
print("\nTop p logits and probabilities:")
for (word, logit), prob in zip(top_p_logits, top_p_probabilities):
    print(f'{word}: Logit = {logit}, Probability = {prob*100:.2f}%')

# Min p logits and probabilities
min_p_logits, min_p_probabilities = min_p(logits, min_p_value, temperature)
print("\nMin p logits and probabilities:")
for (word, logit), prob in zip(min_p_logits, min_p_probabilities):
    print(f'{word}: Logit = {logit}, Probability = {prob*100:.2f}%')
