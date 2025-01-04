print("Hi Dawoud")
print("Imported Success")

print("Ahmed Dawoud")
letter = "a"
if letter in "Ahmed":
    print("PPPPP")
else:
    print(False)


## Missing it all up
import dowhy
from dowhy import CausalModel
import pandas as pd
import numpy as np

# Step 1: Install dowhy
# You can install dowhy using pip:
# !pip install dowhy

# Step 2: Define your causal graph
causal_graph = """
digraph {
    U[label="Unobserved Confounders"];
    X -> Y;
    X -> Z;
    Z -> Y;
    U -> X;
    U -> Y;
}
"""

# Step 3: Load your data
data_dict = {
    "X": np.random.normal(size=1000),
    "Z": np.random.normal(size=1000),
    "Y": np.random.normal(size=1000),
}
data = pd.DataFrame(data_dict)

# Step 4: Create a causal model
model = CausalModel(data=data, treatment="X", outcome="Y", graph=causal_graph)

# Step 5: Identify the causal effect
identified_estimand = model.identify_effect()

# Step 6: Estimate the causal effect
estimate = model.estimate_effect(
    identified_estimand, method_name="backdoor.linear_regression"
)

# Step 7: Refute the causal effect
refutation = model.refute_estimate(
    identified_estimand, estimate, method_name="placebo_treatment_refuter"
)

# Print the results
print(estimate)
print(refutation)
