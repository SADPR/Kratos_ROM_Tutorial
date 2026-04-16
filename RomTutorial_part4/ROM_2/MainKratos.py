import KratosMultiphysics
from KratosMultiphysics.RomApplication.rom_manager import RomManager
import json

def rom_manager_parameters():

    default_settings = KratosMultiphysics.Parameters("""{
        "rom_stages_to_train" : ["ROM"],             // ["ROM","HROM"]
        "rom_stages_to_test" : [],              // ["ROM","HROM"]
        "save_gid_output": false,                    // false, true #if true, it must exits previously in the ProjectParameters.json
        "save_vtk_output": false,                    // false, true #if true, it must exits previously in the ProjectParameters.json
        "ROM":{
            "model_part_name": "FluidModelPart",                            // This changes depending on the simulation: Structure, FluidModelPart, ThermalPart #TODO: Idenfity it automatically
            "nodal_unknowns": ["VELOCITY_X","VELOCITY_Y", "PRESSURE"]     // Main unknowns. Snapshots are taken from these
        }
    }""")

    return default_settings



def UpdateMaterialParametersFile(material_parametrs_file_name="FluidMaterials.json", mu=None):
    with open(material_parametrs_file_name, mode="r+") as f:
        data = json.load(f)
        data["properties"][1]["Material"]["Variables"]["DYNAMIC_VISCOSITY"] = mu[0]
        #write to file and save file
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()


if __name__ == "__main__":

    rom_manager = RomManager(general_rom_manager_parameters=rom_manager_parameters(), UpdateMaterialParametersFile=UpdateMaterialParametersFile)

    # mu_train = [[0.004],[0.007],[0.01]]

    # rom_manager.Fit(mu_train)
    # rom_manager.PrintErrors()

    rom_manager.RunFOM([[0.001]])
