import numpy as np
import matplotlib.pyplot as plt

class Calculate():
    
    def __init__(self):
        pass

    def calculate_required_acid_volume(self):
        mineral_fraction = float(input('Digite a fração de mineral em porcentagem decimal: '))
        porosity = float(input('Digite a porosidade da formação em porcentagem decimal: '))
        well_radius = float(input('Digite o raio do poço (ft): '))
        well_acid_penetration_radius = float(input('Digite o raio de tratamento ácido (ft): '))
        acid_concentration = float(input('Digite a concentração de ácido em porcentagem decimal: '))
        acid_type = input('Digite o tipo de ácido -> \n [1] - HCl \n [2] - HF \n [3] - CH2O2 (Ácido Fórmico) \n -> ')
        mineral_type = input('Digite o mineral a ser dissolvido -> \n [1] - CaCO3 \n [2] - SiO2 \n [3] - CaMg(CO3)2 \n ->')
        
        STOICHIOMETRIC_NUMBER = {
            'acid': 4,
            'mineral': 1,
        }

        ACID_MOLAR_MASS = {
            '1': 36.458,
            '2': 20.01,
            '3': 46.03,
        }

        MINERAL_MOLAR_MASS = {
            '1': 100.0869,
            '2': 60.08,
            '3': 184.4,
        }

        ACID_SPECIFIC_GRAVITY = {
            '1': 1.19,
            '2': 1.15,
            '3': 1.22,
        }

        MINERAL_SPECIFIC_GRAVITY = {
            '1': 2.71,
            '2': 2.22,
            '3': 2.85,
        }

        stoichiometric_fraction = STOICHIOMETRIC_NUMBER['mineral']/STOICHIOMETRIC_NUMBER['acid']
        gravimetric_potential = stoichiometric_fraction*(MINERAL_MOLAR_MASS[mineral_type]/ACID_MOLAR_MASS[acid_type])*acid_concentration
        volumetric_potential = gravimetric_potential*(ACID_SPECIFIC_GRAVITY[acid_type]/MINERAL_SPECIFIC_GRAVITY[mineral_type])
        mineral_volume = np.pi*(well_acid_penetration_radius**2 - well_radius**2)*(1 - porosity)*mineral_fraction
        porous_volume = np.pi*(well_acid_penetration_radius**2 - well_radius**2)*porosity
        required_acid_volume = (mineral_volume/volumetric_potential) + porous_volume + mineral_volume

        print(
            f'Sandstone Acidizing - Required Volume',
            f'\n Gravimetric Potential: {gravimetric_potential}',
            f'\n Volumetric Potentital: {volumetric_potential}',
            f'\n Mineral Volume: {mineral_volume} ft³',
            f'\n Porous Volume: {porous_volume} ft³',
            f'\n Required Acid Volume: {required_acid_volume} ft³'
        )


    def calculate_injection_pump_flow_and_pressure(self):
        formation_permeability = float(input('Digite a permeabilidade da formação (mD): '))
        pay_zone_thickness = float(input('Digite a espessura de pay zone (ft): '))
        reservoir_depth = float(input('Digite a profundidade da pay zone (ft): '))
        acid_relative_density = float(input('Digite a densidade da solução ácida: '))
        acid_viscosity = float(input('Digite a viscosidade da solução ácida (cp): '))
        draining_radius = float(input('Digite o raio de drenagem do ácido (ft): '))
        well_radius = float(input('Digite o raio do poço (ft): '))
        fracture_gradient = float(input('Digite o gradiente de fratura (psi/ft): '))
        reservoir_pressure = float(input('Digite a pressão do reservatório(psi): '))
        injection_tubing_diameter = float(input('Digite o diâmetro do tubing de injeção (in): '))
        skin = float(input('Digite o coeficiente de película: '))
        security_margin = float(input('Digite o fator de segurança (psi): '))
        BHPf = float(input('digite a pressão de teste do fundo do poço (psi): '))


        fracture_pressure = fracture_gradient*reservoir_depth

        maximum_injection_flow = (4.917*10**(-6)*formation_permeability*pay_zone_thickness*(fracture_pressure - reservoir_pressure - security_margin))/(acid_viscosity*(np.log(0.472*draining_radius/well_radius) + skin))
        
        pressure_drop = (518*(acid_relative_density**0.79)*(maximum_injection_flow**1.79)*(acid_viscosity**0.207)*reservoir_depth)/(1000*(injection_tubing_diameter**4.79))
        hydrostatic_pressure = (acid_relative_density*8.3454)*reservoir_depth*0.052

        injection_pressure = BHPf - hydrostatic_pressure + pressure_drop 

        print(
            f'Sandstone Acidizing - Maximum Pump Injection Flow & Pump Pressure',
            f'\n Fracture Pressure: {fracture_pressure} psi',
            f'\n Pressure Drop: {pressure_drop} psi',
            f'\n Hydrostatic Pressure: {hydrostatic_pressure} psi',
            f'\n Maximum Pump Injection Flow: {maximum_injection_flow} bpm',
            f'\n Pump Injection Pressure: {injection_pressure} psi'
        )