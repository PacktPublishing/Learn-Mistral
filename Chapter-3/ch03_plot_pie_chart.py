import numpy as np
import matplotlib.pyplot as plt

logits = {
    'guitar': 2.5,
    'melody': 2.2,
    'whisper': 1.4,
    'sunset': 1.3,
    'avalanche': 0.3,
    'elephant': 0.2
}

def softmax(logits):
    exp_logits = np.exp(logits)
    probabilities = exp_logits / np.sum(exp_logits)
    return probabilities

def plot_pie_chart_with_probabilities(logits):
    words = list(logits.keys())
    logit_values = np.array(list(logits.values()))

    # Calculate probabilities using softmax
    probabilities = softmax(logit_values)

    # Sort the probabilities and corresponding words in descending order
    sorted_indices = np.argsort(probabilities)
    sorted_probabilities = probabilities[sorted_indices]
    sorted_words = [words[i] for i in sorted_indices]

    # Create color shades of grey
    colors = plt.cm.Greys(np.linspace(0.3, 0.9, len(sorted_probabilities)))

    # Plot the pie chart
    fig, ax = plt.subplots(figsize=(6, 6))
    wedges, texts = ax.pie(sorted_probabilities, startangle=90, colors=colors, wedgeprops=dict(width=0.4))

    # Create a legend with words and probabilities in percentage
    legend_labels = [f'{word}: {prob*100:.2f}%' for word, prob in zip(sorted_words, sorted_probabilities)]
    ax.legend(wedges, legend_labels, title="Words", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    # Draw the surrounding circle with scores from 0 to 100
    circle_radius = 1.1
    angles = np.linspace(0, 2 * np.pi, 100)
    ax.plot(circle_radius * np.cos(angles), circle_radius * np.sin(angles), color='black')

    # Annotate the circle with scores from 0 to 100
    for i in range(10, 110, 10):
        angle = np.deg2rad(90 - (i * 3.6))  # 3.6 degrees per 10% increment
        x = (circle_radius+0.1) * np.cos(angle)
        y = (circle_radius+0.1) * np.sin(angle)
        ax.text(x, y, f'{i}', ha='center', va='center', fontsize=10, color='black')


    # Set the title and display the chart
    ax.set_title('Logit Probabilities', fontsize=16)
    plt.show()

plot_pie_chart_with_probabilities(logits)