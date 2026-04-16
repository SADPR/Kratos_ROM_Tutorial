# Kratos ROM Tutorial Series

Welcome to the **Kratos ROM Tutorial Series**. This workspace is dedicated to following the comprehensive video series showcasing the capabilities of the **Kratos Multiphysics Reduced Order Model (ROM)** applications.

---

## 📺 Course Overview
This series provides a step-by-step guide to implementing and utilizing Reduced Order Models within the Kratos Multiphysics framework. 

> [!NOTE]
> We will be proceeding **part by part**, exploring the various features and methodologies required to build efficient ROMs.

### 🔗 Resources
- **YouTube Playlist:** [Rom Tutorial Series](https://youtube.com/playlist?list=PLJZAo1kyATsUA8U4hex36P4HLAr0KJWH_&si=JWoR7MNrDq11Q9tJ)
- **Official Documentation:** [Kratos Multiphysics ROM Application](https://github.com/KratosMultiphysics/Kratos/tree/master/applications/RomApplication)

---

## 🚀 Part 1: Introduction to Snapshots & POD
**Part 1** serves as the foundation for the entire series. It introduces the core concepts and the initial steps required to start a ROM project.

### What we cover in this part:
- 💡 **General Introduction**: Understanding the motivation behind Reduced Order Modeling.
- 📸 **Snapshots Collection**: Learning how to store and organize the full-order model (FOM) data.
- 📉 **Proper Orthogonal Decomposition (POD)**: An overview of how to extract the dominant modes from the snapshot matrix.

### Files Included:
- [RomApp_Tutorial_1.pptx](file:///home/kratos/Kratos_ROM_Tutorial/RomTutorial_part1/RomApp_Tutorial_1.pptx): Supporting presentation for the lecture.

---

## 🏗️ Part 2: Beam Simulation & Data Preparation
**Part 2** moves into practical application by setting up a structural simulation of a beam. This part is crucial for understanding how to prepare a Kratos project for ROM training.

### What we cover in this part:
- 📐 **Structural Setup**: Reviewing the `beam` GiD project and the `MainKratos.py` solver script.
- 📂 **FOM Execution**: Running the Full Order Model to generate baseline behavior data.
- 🔧 **Snapshot Manager Integration**: Configuring the project to automatically collect data for training.

### Key Files in `RomTutorial_part2`:
- **[beam.gid](file:///home/kratos/Kratos_ROM_Tutorial/RomTutorial_part2/beam.gid/)**: The Kratos structural project directory.
- **[RomApp_Tutorial_2.pptx](file:///home/kratos/Kratos_ROM_Tutorial/RomTutorial_part2/RomApp_Tutorial_2.pptx)**: Lecture slides for this module.

---

## 🤖 Part 3: The ROM Manager
**Part 3** introduces the `RomManager`, a high-level utility in the Kratos `RomApplication` designed to simplify and automate the workflow of creating, training, and testing Reduced Order Models.

### What we cover in this part:
- ⚙️ **RomManager Configuration**: Setting up the manager with custom parameters for training and testing stages.
- 🔢 **Parameterization (mu vectors)**: Defining parameter spaces to explore different simulation scenarios (e.g., varying loads).
- 🔄 **Automation**: Streamlining the transition from Full Order Model (FOM) data collection to ROM execution.

### Key Files in `RomTutorial_part3`:
- **[ROM folder](file:///home/kratos/Kratos_ROM_Tutorial/RomTutorial_part3/ROM/)**: Contains the `MainKratos.py` script utilizing the `RomManager`.
- **[RomApp_Tutorial_3.pptx](file:///home/kratos/Kratos_ROM_Tutorial/RomTutorial_part3/RomApp_Tutorial_3.pptx)**: Lecture slides for this module.

---

## 🌊 Part 4: Fluid Dynamics ROM
**Part 4** applies the ROM methodology to fluid mechanics. This part explores the complexities of fluid flow simulations and how to parameterize material properties like viscosity in a reduced order context.

### What we cover in this part:
- 🧪 **Fluid Simulation Setup**: Reviewing the `fluid` GiD project and the `FluidModelPart`.
- 💧 **Viscosity Parameterization**: Dynamically updating `DYNAMIC_VISCOSITY` during training.
- 💨 **Velocity and Pressure ROM**: Training snapshots for multiple nodal unknowns (`VELOCITY_X`, `VELOCITY_Y`, and `PRESSURE`).

### Key Files in `RomTutorial_part4`:
- **[fluid.gid](file:///home/kratos/Kratos_ROM_Tutorial/RomTutorial_part4/fluid.gid/)**: The Kratos fluid project directory.
- **[ROM_2 folder](file:///home/kratos/Kratos_ROM_Tutorial/RomTutorial_part4/ROM_2/)**: Automated scripts for the fluid ROM workflow.
- **[RomApp_Tutorial_4.pptx](file:///home/kratos/Kratos_ROM_Tutorial/RomTutorial_part4/RomApp_Tutorial_4.pptx)**: Lecture slides for this module.

---

## 📈 Part 5: Error Estimation & Databases
**Part 5** focuses on the quantitative analysis of ROM accuracy. It introduces tools for managing snapshot databases and calculating errors between the Full Order Model (FOM) and the Reduced Order Model (ROM).

### What we cover in this part:
- 📊 **Snapshot Database Management**: Learning how to retrieve and manipulate snapshot matrices using the `RomManager` database interface.
- 📐 **Error Norms**: Implementing numerical checks (like the Frobenius norm) to validate the precision of the ROM.
- 🔍 **Model Validation**: Testing the ROM against unseen parameter sets (`mu_test`) to ensure generalization.

### Key Files in `RomTutorial_part5`:
- **[ROM folder](file:///home/kratos/Kratos_ROM_Tutorial/RomTutorial_part5/ROM/)**: Scripts for database extraction and error analysis.
- **[RomApp_Tutorial_5.pptx](file:///home/kratos/Kratos_ROM_Tutorial/RomTutorial_part5/RomApp_Tutorial_5.pptx)**: Lecture slides for this module.

---

## 📊 Part 6: Custom Simulations & QoIs
**Part 6** explores how to extend the default simulation behavior in Kratos to extract specific **Quantities of Interest (QoIs)**. This is essential for comparing FOM and ROM results based on specific physical metrics rather than just global error norms.

### What we cover in this part:
- 🛠️ **Simulation Customization**: Implementing a custom `Kratos` simulation class to add user-defined logic.
- 📍 **QoI Extraction**: Capturing specific data (e.g., vertical velocity at a probe point) during the simulation steps.
- 📉 **Visual Comparison**: Using `matplotlib` to visualize and compare the performance of the FOM and ROM for the selected QoIs.

### Key Files in `RomTutorial_part6`:
- **[ROM_2 folder](file:///home/kratos/Kratos_ROM_Tutorial/RomTutorial_part6/ROM_2/)**: Contains scripts for custom simulation and QoI plotting.
- **[RomApp_Tutorial_6.pptx](file:///home/kratos/Kratos_ROM_Tutorial/RomTutorial_part6/RomApp_Tutorial_6.pptx)**: Lecture slides for this module.

---

## 🔬 Part 7: Hyper-Reduction (HROM) Fundamentals
**Part 7** delves into the theoretical foundations of **Hyper-Reduced Order Modeling (HROM)**. While ROM significantly reduces the number of degrees of freedom, non-linear terms often still require integration over the entire mesh—a challenge known as the "Galerkin Bottleneck."

### What we cover in this part:
- 📉 **The Galerkin Bottleneck**: Understanding why non-linearities can hinder ROM performance.
- 🧪 **ECM Theory**: An introduction to the **Empirical Cubature Method (ECM)** for approximating non-linear terms using only a subset of elements.
- ⚡ **Efficiency Gains**: How HROM achieves true computational speedups in non-linear simulations.

### Key Files in `RomTutorial_part7`:
- **[RomApp_Tutorial_7.pptx](file:///home/kratos/Kratos_ROM_Tutorial/RomTutorial_part7/RomApp_Tutorial_7.pptx)**: Detailed lecture slides on HROM theory and mathematical formulations.

---

## 🧠 Part 8: Neural Network Enhanced ROMs
**Part 8** introduces advanced reconstruction techniques using **Artificial Neural Networks (ANNs)**. By moving beyond linear POD decoders, we can better capture non-linearities and improve the accuracy of the reduced model.

### What we cover in this part:
- 🤖 **ANN-Enhanced Decoders**: Configuring the `RomManager` to use neural networks for basis reconstruction (`ann_enhanced` decoder type).
- 🧬 **Hyperparameter Tuning**: Defining layers, batch sizes, epochs, and learning rate strategies for the ANN.
- 🎯 **Advanced Fit**: Training the ANN-ROM on specific parameter sets and evaluating its performance against linear methods.

### Key Files in `RomTutorial_part8`:
- **[ROM folder](file:///home/kratos/Kratos_ROM_Tutorial/RomTutorial_part8/ROM/)**: Implementation of the ANN-enhanced solver scripts.
- **[RomApp_Tutorial_8.pptx](file:///home/kratos/Kratos_ROM_Tutorial/RomTutorial_part8/RomApp_Tutorial_8.pptx)**: Lecture slides on neural network integration in ROM.

---

## 🏛️ Part 9: Projection & Assembling Strategies
**Part 9** explores different mathematical strategies for projecting the full-order equations onto the reduced basis and assembling the resulting systems. Choosing the right strategy is key to stability and performance.

### What we cover in this part:
- 🔄 **Projection Strategies**: Implementing and comparing **Galerkin**, **Petrov-Galerkin**, and **LSPG (Least-Squares Petrov-Galerkin)** projections.
- 🧩 **Assembling Strategies**: Understanding the difference between **Global** and **Elemental** assembling and their impact on efficiency.
- ⚖️ **Stability & Accuracy**: Evaluating how different combinations of strategies affect the simulation of fluid flows.

### Key Files in `RomTutorial_part9`:
- **[ROM_2 folder](file:///home/kratos/Kratos_ROM_Tutorial/RomTutorial_part9/ROM_2/)**: Scripts for testing different projection and assembly configurations.
- **[RomApp_Tutorial_9.pptx](file:///home/kratos/Kratos_ROM_Tutorial/RomTutorial_part9/RomApp_Tutorial_9.pptx)**: Lecture slides on advanced numerical strategies for ROM.

---

## 🏎️ Part 10: HROM Execution & ECM
**Part 10** is the culmination of the series, where we put the theory into practice and execute a **Hyper-Reduced Order Model (HROM)**. This part demonstrates the full workflow of training the HROM and measuring the speedup achieved through the Empirical Cubature Method.

### What we cover in this part:
- 🛠️ **HROM Configuration**: Finalizing the `RomManager` settings for the HROM stage.
- 📐 **ECM Implementation**: Using the `empirical_cubature` method to select a subset of elements and weights.
- ⚡ **Execution & Performance**: Running `rom_manager.RunHROM()` and validating the results against the full-order simulation.

### Key Files in `RomTutorial_part10`:
- **[ROM folder](file:///home/kratos/Kratos_ROM_Tutorial/RomTutorial_part10/ROM/)**: The final automated script implementing HROM.
- **[RomApp_Tutorial_10.pptx](file:///home/kratos/Kratos_ROM_Tutorial/RomTutorial_part10/RomApp_Tutorial_10.pptx)**: Final lecture slides of the series.
- **[RaulBravo_FIME.pptx](file:///home/kratos/Kratos_ROM_Tutorial/RomTutorial_part10/RaulBravo_FIME.pptx)**: Additional case studies and advanced applications.

---

## 📅 Roadmap
- [x] **Part 1**: Introduction & Snapshots
- [x] **Part 2**: Beam Simulation & Snapshot Manager
- [x] **Part 3**: The ROM Manager
- [x] **Part 4**: Fluid Dynamics ROM
- [x] **Part 5**: Error Estimation & Databases
- [x] **Part 6**: Custom Simulations & QoIs
- [x] **Part 7**: Hyper-Reduction Fundamentals
- [x] **Part 8**: Neural Network Enhanced ROMs
- [x] **Part 9**: Projection & Assembling Strategies
- [x] **Part 10**: HROM Execution & ECM

---
*Created with ❤️ for the Kratos Community.*