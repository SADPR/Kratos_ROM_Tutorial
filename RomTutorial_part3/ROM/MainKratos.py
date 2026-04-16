import KratosMultiphysics
from KratosMultiphysics.RomApplication.rom_manager import RomManager


def rom_manager_parameters():

    default_settings = KratosMultiphysics.Parameters("""{
        "rom_stages_to_train" : ["ROM"],             // ["ROM","HROM"]
        "rom_stages_to_test" : ["ROM"],              // ["ROM","HROM"]
        "save_gid_output": true,                    // false, true #if true, it must exits previously in the ProjectParameters.json
        "save_vtk_output": true,                    // false, true #if true, it must exits previously in the ProjectParameters.json
        "ROM":{
            "model_part_name": "Structure",                            // This changes depending on the simulation: Structure, FluidModelPart, ThermalPart #TODO: Idenfity it automatically
            "nodal_unknowns": ["DISPLACEMENT_X","DISPLACEMENT_Y"]     // Main unknowns. Snapshots are taken from these
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

    # mu_train = [[20,45,60], [23,46,89], [10,23,45]]
    # rom_manager.Fit(mu_train)
    # mu_test = [[200,300,400], [45,-20,-30]]
    # rom_manager.Test(mu_test)
    # rom_manager.PrintErrors()


    rom_manager.RunFOM([[300,200,500]])
    rom_manager.RunROM([[300,200,500]])