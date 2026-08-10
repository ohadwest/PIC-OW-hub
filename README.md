# 🔬 Silicon Photonics Simulation Hub

Welcome to the **Silicon Photonics Simulation Hub**, a centralized portal providing interactive, web-based simulation tools for integrated photonics design and analysis.

This hub aggregates specialized simulation engines built with Python and Streamlit, offering researchers and engineers fast numerical solvers for optical waveguides and directional couplers.

---

## 🚀 Available Simulation Tools

### 1. 📐 [FDE Mode Solver (Standard)](https://pic-mode-solver-ohadwest.streamlit.app/)
* **Description:** Finite-Difference Eigenmode (FDE) solver for standard rectangular silicon/silicon-nitride waveguides.
* **Key Features:**
  * Calculates effective refractive index ($n_{\text{eff}}$), group index ($n_g$), and effective mode area ($A_{\text{eff}}$).
  * Generates 2D and 1D mode field distributions for quasi-TE and quasi-TM modes.

### 2. 🌀 [Advanced Mode Solver (Trapezoid & Bending)](https://pic-mode-solver-davanced-ohadwest.streamlit.app/)
* **Description:** Advanced mode solver handling complex waveguide geometries and curvature.
* **Key Features:**
  * Support for sidewall angles (trapezoidal cross-sections).
  * Conformal index transformation for Ring Resonator bending losses.
  * Complex refractive index distribution analysis.

### 3. ⚡ [Symmetric Directional Coupler Simulator](https://pic-coupler-simulator-ohadwest.streamlit.app/)
* **Description:** Supermode and Coupled-Mode Theory (CMT) analysis for symmetric directional couplers ($w_1 = w_2$).
* **Key Features:**
  * Calculates even and odd supermode field profiles.
  * Computes coupling coefficient ($\kappa$) and cross-over coupling length ($L_c$).
  * Interactive power transfer dynamics along the propagation distance.

### 4. 🌊 [Asymmetric Directional Coupler Simulator (ADC)](https://asymmetric-directional-coupler-ohadwest.streamlit.app/)
* **Description:** Coupler analysis for waveguides with unequal widths ($w_1 \neq w_2$).
* **Key Features:**
  * Evaluates phase mismatch ($\Delta\beta$) and maximum power conversion limit.
  * Wavelength/gap dispersion sweeps.
  * Supermode asymmetry visualization.

---

## 🛠️ Project Structure

```text
silicon-photonics-hub/
├── app.py              # Main Streamlit Portal App
├── requirements.txt    # Python dependencies
└── README.md           # Project Documentation
