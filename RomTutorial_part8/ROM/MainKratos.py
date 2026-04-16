import KratosMultiphysics
from KratosMultiphysics.RomApplication.rom_manager import RomManager
import numpy as np

def rom_manager_parameters():

    default_settings = KratosMultiphysics.Parameters("""{
        "rom_stages_to_train" : ["ROM"],             // ["ROM","HROM"]
        "rom_stages_to_test" : ["ROM"],              // ["ROM","HROM"]
        "type_of_decoder" : "ann_enhanced",               // "linear" "ann_enhanced",  TODO: add "quadratic"
        "save_gid_output": true,                    // false, true #if true, it must exits previously in the ProjectParameters.json
        "save_vtk_output": true,                    // false, true #if true, it must exits previously in the ProjectParameters.json
        "store_nonconverged_fom_solutions": true,
        "ROM":{
            "svd_truncation_tolerance": 0,
            "use_non_converged_sols": true,
            "model_part_name": "Structure",                            // This changes depending on the simulation: Structure, FluidModelPart, ThermalPart #TODO: Idenfity it automatically
            "nodal_unknowns": ["DISPLACEMENT_X","DISPLACEMENT_Y"],     // Main unknowns. Snapshots are taken from these
            "ann_enhanced_settings": {
                "modes":[5,10],
                "layers_size":[200,200],
                "batch_size":2,
                "epochs":800,
                "NN_gradient_regularisation_weight": 0.0,
                "lr_strategy":{
                    "scheduler": "sgdr",
                    "base_lr": 0.001,
                    "additional_params": [1e-4, 10, 400]
                },
                "training":{
                    "retrain_if_exists" : false  // If false only one model will be trained for each the mu_train and NN hyperparameters combination
                },
                "online":{
                    "model_number": 0   // out of the models existing for the same parameters, this is the model that will be lauched
                }
            }
        }
    }""")

    return default_settings



def UpdateProjectParameters(parameters, mu):
    parameters["processes"]["loads_process_list"][0]["Parameters"]["value"].SetDouble(mu[0])
    parameters["processes"]["loads_process_list"][1]["Parameters"]["value"].SetDouble(mu[1])
    parameters["processes"]["loads_process_list"][2]["Parameters"]["value"].SetDouble(mu[2])

    return parameters





if __name__ == "__main__":


    rom_manager = RomManager(general_rom_manager_parameters=rom_manager_parameters(), UpdateProjectParameters=UpdateProjectParameters)

    # mu_train = [[20,45,60], [23,46,89], [10,23,45], [10,23,89]]
    # # rom_manager.Fit(mu_train)
    # # mu_test = [[200,300,400], [45,-20,-30]]
    # # rom_manager.Test(mu_test)
    # # rom_manager.PrintErrors()

    # # snapshots_fom = rom_manager.data_base.get_snapshots_matrix_from_database(mu_train, "FOM")
    # # snapshots_rom = rom_manager.data_base.get_snapshots_matrix_from_database(mu_train, "ROM")
    # # print(snapshots_fom.shape)
    # # print(snapshots_rom.shape)


    # # rom_manager.Fit(mu_train)
    # # rom_manager.PrintErrors()
    # # print(np.linalg.norm(snapshots_fom-snapshots_rom)/np.linalg.norm(snapshots_fom-snapshots_rom))

    # single_snapshots_fom = rom_manager.data_base.get_snapshots_matrix_from_database([[10,23,900]], "FOM")
    # print(single_snapshots_fom.shape)


    # # rom_manager.RunFOM([[300,200,500]])
    # # rom_manager.RunROM([[300,200,500]])


    mu_train = [[200,450,600]]
    rom_manager.Fit(mu_train, [[200,450,600]])
    rom_manager.PrintErrors()

