import KratosMultiphysics
from KratosMultiphysics.RomApplication.rom_manager import RomManager
import json
import numpy as np
from matplotlib import pyplot as plt

def MyCustomizeSimulation(cls, global_model, parameters, mu=None):
    # Default function that does nothing special
    class DefaultCustomSimulation(cls):
        def __init__(self, model, project_parameters):
            super().__init__(model, project_parameters)
            self.y_vel_at_point = []

        def Initialize(self):
            super().Initialize()

        def FinalizeSolutionStep(self):
            super().FinalizeSolutionStep()
            node = self._GetSolver().GetComputingModelPart().GetNode(1515)
            self.y_vel_at_point.append(node.GetSolutionStepValue(KratosMultiphysics.VELOCITY_Y, 0))

        def GetFinalData(self):
            return {"vel_y": np.array(self.y_vel_at_point)}

    return DefaultCustomSimulation(global_model, parameters)






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

    rom_manager = RomManager(general_rom_manager_parameters=rom_manager_parameters(), UpdateMaterialParametersFile=UpdateMaterialParametersFile, CustomizeSimulation=MyCustomizeSimulation)

    mu_train = [[0.0066]]
    rom_manager.Fit(mu_train)

    fom = rom_manager.data_base.get_snapshots_matrix_from_database(mu_train, "QoI_FOM", "vel_y" )
    rom = rom_manager.data_base.get_snapshots_matrix_from_database(mu_train, "QoI_ROM", "vel_y" )



    plt.plot(fom, label = 'FOM')
    plt.plot(rom, label = 'ROM')
    plt.legend()
    plt.show()


