"""
The purpose of this code is to define an object that represents the physical
properties of one gamma-emitting radioisotope.

Attributes include:
Atomic number, Mass number, Symbol, Half life [s], Decay constant [1/s],
list of significant gamma emission energies,
list of significant gamma emission branching ratios.
"""


class Isotope(object):
    def __init__(self, symbol, atomic_number, mass_number, half_life,
                 decay_constant, list_sig_g_e, list_sig_g_b_r):
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.mass_number = mass_number
        self.half_life = half_life
        self.decay_constant = decay_constant
        self.list_sig_g_e = list_sig_g_e
        if type(list_sig_g_b_r != 'list'):
            self.list_sig_g_b_r = list_sig_g_b_r
        else:
            self.list_sig_g_b_r = [0.01*list_sig_g_b_r[i]
                                   for i in range(len(list_sig_g_b_r))]
        return


Ac_223_g_e = [83.55, 98.58, 191.3, 434.2]
Ac_223_b_r = [0.0057, 0.00891, 0.0058, 0.0052]
Actinium_223 = Isotope("Ac", 89, 223, 126, 0.0055, Ac_223_g_e, Ac_223_b_r)
Ac_224_g_e = [84.37, 131.61, 215.98]
Ac_224_b_r = [0.0152, 0.269, 0.523]
Actinium_224 = Isotope("Ac", 89, 224, 10008, 0.000069, Ac_224_g_e, Ac_224_b_r)
Actinium_225 = Isotope("Ac", 89, 225, 864000, 8*10**(-7), 99.91, 0.01)
Ac_226_g_e = [158.18, 186.05, 230.37, 253.73]
Ac_226_b_r = [17.5, 4.8, 27, 5.7]
Actinium_226 = Isotope("Ac", 89, 226, 105732, 6.6E-6, Ac_226_g_e, Ac_226_b_r)
Ac_228_g_e = [338.32, 911.204, 964.766, 968.971]
Ac_228_b_r = [11.27, 25.8, 5, 15.8]
Actinium_228 = Isotope("Ac", 89, 228, 22140, 3.13E-05, Ac_228_g_e, Ac_228_b_r)
Ac_229_g_e = [135.36, 146.345, 164.522, 261.92, 569.1]
Ac_229_b_r = [34, 35, 100, 39, 91]
Actinium_229 = Isotope("Ac", 89, 229, 3762, 1.84E-4, Ac_229_g_e, Ac_229_b_r)
Ac_231_g_e = [185.71, 221.4, 282.47, 307.06]
Ac_231_b_r = [16.4, 16.8, 39, 30.4]
Actinium_231 = Isotope("Ac", 89, 231, 450, 0.00154, Ac_231_g_e, Ac_231_b_r)

Al_28_g_e = [1778.97]
Al_28_b_r = [100]
Aluminum_28 = Isotope("Al", 13, 28, 134.4, 0.00516, Al_28_g_e, Al_28_b_r)
Al_29_g_e = [1293.37]
Al_29_b_r = [90.6]
Aluminum_29 = Isotope("Al", 13, 29, 393.6, 0.00176, Al_29_g_e, Al_29_b_r)

Am_242_g_e = [42.13, 44.54]
Am_242_b_r = ["Unknown", "Unknown"]
Americium_242 = Isotope("Am", 95, 242, 30600, 2.27E-5, Am_242_g_e, Am_242_b_r)
Am_244_g_e = [99.38, 153.86, 743.97, 897.85]
Am_244_b_r = [4.6, 16, 66, 28]
Americium_244 = Isotope("Am", 95, 244, 36360, 1.9E-5, Am_244_g_e, Am_244_b_r)

Sb_122_g_e = [564.119, 692.794]
Sb_122_b_r = [71, 692.794]
Antimony = Isotope("Sb", 51, 122, 235336, 2.944E-6, Sb_122_g_e, Sb_122_b_r)
Sb_124_g_e = [602.73, 645.855, 722.786, 1690.983, 2090.945]
Sb_124_b_r = [98.26, 7.456, 10.81, 47.79, 5.51]
Antimony = Isotope("Sb", 51, 124, 5.2E+6, 1.33E-7, Sb_124_g_e, Sb_124_b_r)

Ar_37_g_e = [2621, 2622]
Ar_37_b_r = [2.8, 5.6]
Argon_37 = Isotope("Ar", 18, 37, 3.03E+6, 2.29E-7, Ar_37_g_e, Ar_37_b_r)
Argon_41 = Isotope("Ar", 18, 41, 6560.4, 0.0001056, 1293.587, 99.1)

As_76_g_e = [559.101, 657.041, 1216.104]
As_76_b_r = [45, 6.2, 3.42]
Arsenic_76 = Isotope("As", 33, 76, 93121.92, 7.44E-6, As_76_g_e, As_76_b_r)

At_210_g_e = [245.31, 1181.39, 1436.7, 1483.39, 1599.7]
At_210_b_r = [79, 99.3, 29, 46.5, 13.4]
Astatine = Isotope("At", 85, 210, 29160, 2.38E-5, At_210_g_e, At_210_b_r)

Ba_131_g_e = [123.81, 216.08, 373.25, 496.33]
Ba_131_b_r = [28.97, 19.66, 14.04, 47]
Barium_131 = Isotope("Ba", 56, 131, 993600, 6.97E-7, Ba_131_g_e, Ba_131_b_r)
Ba_133_g_e = [81, 276.4, 302.85, 356.02, 383.851]
Ba_133_b_r = [34.06, 7.164, 18.33, 62.05, 8.94]
Barium_133 = Isotope("Ba", 56, 133, 3.314E+8, 2.1E-9, Ba_133_g_e, Ba_133_b_r)
Ba_139_g_e = [165.864]
Ba_139_b_r = [23.7]
Barium_139 = Isotope("Ba", 56, 139, 4983.6, 1.4E-4, Ba_139_g_e, Ba_139_b_r)

Bk_247_g_e = [84, 265]
Bk_247_b_r = [40, 30]
Berkelium = Isotope("Bk", 97, 247, 4.352E+10, 1.59E-11, Bk_247_g_e, Bk_247_b_r)

Beryllium_10 = Isotope("Be", 4, 10, 4.762E+9, 1.46E-10, 0, 0)

Bi_210_g_e = [265.832, 304.9]
Bi_210_b_r = ["Unknown", "Unknown"]
Bismuth_210 = Isotope("Bi", 83, 210, 433123.2, 1.6E-6, Bi_210_g_e, Bi_210_b_r)

Bi_214_g_e = [609.31, 1120.29, 1764.49]
Bi_214_b_r = [45.49, 14.91, 1764.49]
Bismuth_214 = Isotope("Bi", 83, 214, 1194, 5.81E-4, Bi_214_g_e, Bi_214_b_r)

Boron = Isotope("B", 5, 12, 0.02, 34.66, 3214.83, "Unknown")

Br_80_g_e = [616.6, 666.14]
Br_80_b_r = [7, 1.08]
Bromine_80 = Isotope("Br", 35, 80, 1060.8, 6.53E-4, Br_80_g_e, Br_80_b_r)
Br_82_g_e = [221.48, 554.35, 606.34, 619.11, 698.374, 776.57, 827.828, 1007.6,
             1044, 1317.47, 1474.88]
Br_82_b_r = [2.26, 70.8, 1.2, 43.4, 28.49, 83.5, 24.03, 1.271,
             27.23, 26.48, 16.32]
Bromine_82 = Isotope("Br", 35, 82, 127080, 5.45E-6, Br_82_g_e, Br_82_b_r)

Cadmium_107 = Isotope("Cd", 48, 107, 23400, 2.96E-5, 93.124, 4.8)
Cadmium_109 = Isotope("Cd", 48, 109, 3.997E+7, 1.734E-8, 88.04, 3.61)
Cd_115_g_e = [260.89, 336.24, 492.3, 527.9]
Cd_115_b_r = [1.94, 45.9, 8.03, 27.45]
Cadmium_115 = Isotope("Cd", 48, 115, 192456, 3.6E-6, Cd_115_g_e, Cd_115_b_r)
Cd_117_g_e = [273.35, 344.46, 434.19, 1051.7, 1303.27, 1576.62]
Cd_117_b_r = [28, 17.9, 9.8, 3.79, 18.4, 11.19]
Cadmium_117 = Isotope("Cd", 48, 117, 8964, 7.73E-5, Cd_117_g_e, Cd_117_b_r)

Calcium_45 = Isotope("Ca", 20, 45, 1.405E+7, 4.934E-8, 12.4, 3E-6)
Ca_47_g_e = [489.23, 807.86, 1297.09]
Ca_47_b_r = [6.2, 6.2, 71]
Calcium_47 = Isotope("Ca", 20, 47, 391910, 1.7684E-6, Ca_47_g_e, Ca_47_b_r)
Ca_49_g_e = [3084.4, 4071.9]
Ca_49_b_r = [92, 7]
Calcium_49 = Isotope("Ca", 20, 49, 523.08, 0.001325, Ca_49_g_e, Ca_49_b_r)

Cf_251_g_e = [176.6, 227, 285]
Cf_251_b_r = [17.7, 6.3, 1.4]
Cf_251 = Isotope("Cf", 98, 251, 2.83E+10, 2.45E-11, Cf_251_g_e, Cf_251_b_r)

Cerium_137 = Isotope("Ce", 58, 137, 32400, 2.14E-5, 447.15, 1.8)
Cerium_139 = Isotope("Ce", 58, 139, 1.19E+7, 5.829E-8, 165.864, 80)
Cerium_141 = Isotope("Ce", 58, 141, 2.808E+6, 2.468E-7, 145.44, 48.2)

Cs_134_g_e = [563.25, 569.33, 604.72, 795.86, 801.95]
Cs_134_b_r = [8.35, 15.38, 97.62, 85.53, 8.69]
Caesium_134 = Isotope("Cs", 55, 134, 6.51E+7, 1.065E-8, Cs_134_g_e, Cs_134_b_r)
Cs_136_g_e = [86.36, 153.25, 176.6, 273.65, 340.55, 818.51, 1048.1, 1235.36]
Cs_136_b_r = [5.18, 5.75, 10, 11.1, 42.2, 100, 80, 20]
Caesium_136 = Isotope("Cs", 55, 136, 1.137E+6, 6.1E-7, Cs_136_g_e, Cs_136_b_r)
Caesium_137 = Isotope("Cs", 55, 137, 9.483E+8, 7.31E-10, [661.657], [85.1])
Cs_138_g_e = [408.98, 462.8, 547, 871.8, 1009.78, 1435.8, 2218, 2639.6]
Cs_138_b_r = [4.66, 30.7, 10.76, 5.11, 29.8, 76.3, 15.2, 7.63]
Caesium_138 = Isotope("Cs", 55, 138, 2004.6, 3.46E-4, Cs_138_g_e, Cs_138_b_r)

Cl_38_g_e = [1642.714, 2167.405]
Cl_38_b_r = [31.9, 42.4]
Chlorine_38 = Isotope("Cl", 17, 38, 2235, 3.1E-4, Cl_38_g_e, Cl_38_b_r)

Co_60_g_e = [1173.24, 1332.5]
Co_60_b_r = [99.974, 99.986]
Cobalt_60 = Isotope("Co", 27, 60, 1.66E+8, 4.17E-9, Co_60_g_e, Co_60_b_r)

Copper_64 = Isotope("Cu", 29, 64, 45720, 1.52E-5, 1345.84, 0.473)
Cu_66_g_e = [833.54, 1039.23]
Cu_66_b_r = [0.22, 9]
Copper_66 = Isotope("Cu", 29, 66, 307.2, 0.00225, Cu_66_g_e, Cu_66_b_r)

Cm_249_g_e = [368.76, 560.45, 621.87]
Cm_249_b_r = [0.35, 0.84, 1.5]
Curium_249 = Isotope("Cm", 96, 249, 3849, 1.8E-4, Cm_249_g_e, Cm_249_b_r)

Dy_157_g_e = [182.2, 326.16]
Dy_157_b_r = [1.84, 92]
Dysprosium_157 = Isotope("Dy", 66, 157, 29304, 2.37E-5, Dy_157_g_e, Dy_157_b_r)
Dysprosium_159 = Isotope("Dy", 66, 159, 1.248E+7, 5.556E-8, 58, 2.22)
Dysprosium_165 = Isotope("Dy", 66, 165, 8402.4, 8.25E-5, 94.7, 3.58)

Einsteinium_254 = Isotope("Es", 99, 254, 2.382E+7, 2.91E-8, 63, 2)

Er_163_g_e = [297.88, 436.1, 439.94, 1113.5]
Er_163_b_r = [0.012, 0.0285, 0.0276, 0.049]
Erbium_163 = Isotope("Er", 68, 163, 4500, 1.54E-4, Er_163_g_e, Er_163_b_r)
Erbium_169 = Isotope("Er", 68, 169, 812160, 8.534E-7, 109.78, 0.0013)
Er_171_g_e = [111.621, 116.66, 124.015, 295.9, 308.31, 796.54]
Er_171_b_r = [20.5, 2.3, 9.1, 28.9, 64.4, 0.64]
Erbium_171 = Isotope("Er", 68, 171, 27057.6, 2.56E-5, Er_171_g_e, Er_171_b_r)

Eu_152_g_e = [121.782, 244.7, 344.28, 778.9, 964.1, 1085.87, 1112.1, 1408]
Eu_152_b_r = [28.58, 7.583, 26.5, 12.942, 14.6, 10.2, 13.64, 21]
Europium_152 = Isotope("Eu", 63, 152, 4.27E+8, 1.62E-9, Eu_152_g_e, Eu_152_b_r)
Eu_154_g_e = [123.1, 247.93, 591.8, 723.3, 756.8, 873.2, 996.3, 1004.7, 1274.4]
Eu_154_b_r = [40.8, 6.95, 5, 20.22, 4.57, 12.27, 10.6, 18.01, 35.2]
Europium_154 = Isotope("Eu", 63, 154, 2.71E+8, 2.56E-9, Eu_154_g_e, Eu_154_b_r)

Fermium_257 = Isotope("Fm", 100, 257, 8.683E+6, 7.983E-8, 241, 11)

Flourine_20 = Isotope("F", 9, 20, 11, 0.063, 1633.6, 100)

Francium_221 = Isotope("Fr", 87, 221, 294, 0.00236, 218.2, 11.6)
Francium_222 = Isotope("Fr", 87, 222, 852, 8.14E-4, 206.17, 50)

Gadolinium_159 = Isotope("Gd", 64, 159, 66528, 1.042E-5, 363.55, 11.4)
Gd_161_g_e = [102.32, 283.55, 314.92, 360.94, 480.12]
Gd_161_b_r = [13.9, 5.95, 22.7, 60.1, 2.68]
Gadolinium_161 = Isotope("Gd", 64, 161, 219.6, 0.0032, Gd_161_g_e, Gd_161_b_r)

Ga_70_g_e = [176.17, 1039.2]
Ga_70_b_r = [0.29, 0.65]
Gallium_70 = Isotope("Ga", 31, 70, 1268.4, 5.5E-4, Ga_70_g_e, Ga_70_b_r)
Ga_72_g_e = [601, 630, 834, 894.3, 1050.73, 1861.1, 2201.7, 2491, 2507.8]
Ga_72_b_r = [5.54, 24.8, 96, 9.88, 6.91, 5.25, 25.9, 7.68, 12.78]
Gallium_72 = Isotope("Ga", 31, 72, 50760, 1.366E-5, Ga_72_g_e, Ga_72_b_r)

Ge_75_g_e = [198.61, 264.66]
Ge_75_b_r = [1.19, 11]
Germanium_75 = Isotope("Ge", 32, 75, 4966.8, 1.4E-4, Ge_75_g_e, Ge_75_b_r)
Ge_77_g_e = [211, 215.5, 264.44, 367.4, 416.33, 558, 631.8, 714.35, 1085.2]
Ge_77_b_r = [30.8, 28.6, 54, 14, 21.8, 16.1, 6.95, 7.17, 6.05]
Germanium_77 = Isotope("Ge", 32, 77, 40680, 1.73E-5, Ge_77_g_e, Ge_77_b_r)

Gold = Isotope('Au', 79, 198, 232848, 2.977E-6, 411.8, 96)

Hf_175_g_e = [89.36, 343.4]
Hf_175_b_r = [2.4, 84]
Hafnium_175 = Isotope("Hf", 72, 175, 6048000, 1.146E-7, Hf_175_g_e, Hf_175_b_r)
Hf_181_g_e = [133, 136.27, 345.92, 482.18]
Hf_181_b_r = [43.3, 5.85, 15.12, 80.5]
Hafnium_181 = Isotope("Hf", 72, 181, 3.75E+6, 1.849E-7, Hf_181_g_e, Hf_181_b_r)

Ho_166_g_e = [80.574, 1379.4, 1581.9, 1662.48]
Ho_166_b_r = [6.71, 0.93, 0.187, 0.12]
Holmium_166 = Isotope("Ho", 67, 166, 96588, 7.18E-6, Ho_166_g_e, Ho_166_b_r)
Ho_167_g_e = [207.8, 237.87, 321.336, 346.55]
Ho_167_b_r = [4.9, 5, 23.5, 56]
Holmium_167 = Isotope("Ho", 67, 167, 11160, 6.21E-5, Ho_167_g_e, Ho_167_b_r)

Indium_113m = Isotope("In", 49, 113, 5968.8, 1.16E-4, 391.69, 64.2)
In_114_g_e = [558.46, 576.1]
In_114_b_r = [0.07, 0.004]
Indium_114 = Isotope("In", 49, 114, 71.9, 0.00964, In_114_g_e, In_114_b_r)
Indium_115m = Isotope("In", 49, 115, 16149.6, 4.3E-5, 336.24, 45.83)
Indium_116 = Isotope("In", 49, 116, 14.1, 0.0492, 1293.56, 1.3)
In_116m_g_e = [138.33, 416.86, 818.718, 1097.33, 1293.56, 1507.67, 2112.312]
In_116m_b_r = [3.29, 27.7, 11.5, 56.2, 84.4, 10, 15.5]
Indium_116m = Isotope("In", 49, 116, 3557.4, 1.95E-4, In_116m_g_e, In_116m_b_r)

I_128_g_e = [442.9, 526.56, 969.46]
I_128_b_r = [17, 1.58, 0.404]
Iodine_128 = Isotope("I", 53, 128, 1500, 4.6E-4, I_128_g_e, I_128_b_r)
I_130_g_e = [418, 536.1, 668.54, 739.48, 1157.47]
I_130_b_r = [34.2, 99, 96, 82, 11.3]
Iodine_130 = Isotope("I", 53, 130, 44496, 1.56E-5, I_130_g_e, I_128_b_r)

Ir_192_g_e = [295.96, 308.46, 316.51, 468.071, 604.41, 612.47]
Ir_192_b_r = [28.67, 30, 82.81, 47.83, 8.23, 5.3]
Iridium_192 = Isotope("Ir", 77, 192, 6.38E+6, 1.086E-7, Ir_192_g_e, Ir_192_b_r)
Ir_194_g_e = [293.55, 328.46, 645.16]
Ir_194_b_r = [2.52, 13.1, 1.18]
Iridium_194 = Isotope("Ir", 77, 194, 71380.8, 9.71E-6, Ir_194_g_e, Ir_194_b_r)

Fe_59_g_e = [142.65, 192.35, 1099.25, 1291.6]
Fe_59_b_r = [1.02, 3.08, 56.5, 43.2]
Iron_59 = Isotope("Fe", 26, 59, 3.845E+6, 1.8E-7, Fe_59_g_e, Fe_59_b_r)
Fe_61_g_e = [120.34, 297.9, 1027.42, 1205.1, 1645.95]
Fe_61_b_r = [5.3, 22.2, 42.7, 44, 7]
Iron_61 = Isotope("Fe", 26, 61, 358.8, 0.00193, Fe_61_g_e, Fe_61_b_r)

Kr_79_g_e = [261.35, 397.54, 606.1]
Kr_79_b_r = [13, 9.3, 8.12]
Krypton_79 = Isotope("Kr", 36, 79, 126144, 5.5E-6, Kr_79_g_e, Kr_79_b_r)
Krypton_81 = Isotope("Kr", 36, 81, 7.22E+12, 9.6E-14, 276, 0.3)
Krypton_83m = Isotope("Kr", 36, 83, 109.8, 0.0063, 9.4, 4.9)
Krypton_85 = Isotope("Kr", 36, 85, 3.392E+8, 2.04E-9, 514, 0.43)
Kr_87_g_e = [402.59, 845.43, 2554.8]
Kr_87_b_r = [49.6, 7.34, 9.2]
Krypton_87 = Isotope("Kr", 36, 87, 4578, 1.51E-4, Kr_87_g_e, Kr_87_b_r)

La_140_g_e = [328.76, 487.02, 815.77, 867.85, 925.19, 95.4]
La_140_b_r = [20.3, 45.5, 23.28, 5.5, 6.9, 95.4]
Lanthanum = Isotope("La", 57, 140, 144987.84, 4.78E-6, La_140_g_e, La_140_b_r)

Pb_203_g_e = [279.2, 401.32]
Pb_203_b_r = [81, 3.35]
Lead_203 = Isotope("Pb", 82, 203, 186742.8, 3.71E-6, Pb_203_g_e, Pb_203_b_r)
Pb_204m_g_e = [374.72, 899.15, 911.78]
Pb_204m_b_r = [89, 99, 90.7]
Lead_204 = Isotope("Pb", 82, 204, 4032, 1.72E-4, Pb_204m_g_e, Pb_204m_b_r)
Lead_210 = Isotope("Pb", 82, 210, 7E9, 9.9E-10, [46.54], [4.3])
Lead_212 = Isotope("Pb", 82, 212, 38304, 1.81E-5, [238.63], [43.6])
Pb_214_g_e = [295.22, 351.93]
Pb_214_b_r = [18.5, 35.6]
Lead_214 = Isotope("Pb", 82, 214, 1608, 4.31E-4, Pb_214_g_e, Pb_214_b_r)

Lu_176_g_e = [88.34, 201.83, 306.78]
Lu_176_b_r = [13.3, 86.5, 94]
Lutetium_176 = Isotope("Lu", 71, 176, 1.2E+18, 5.8E-19, Lu_176_g_e, Lu_176_b_r)
Lutetium_176m = Isotope("Lu", 71, 176, 13104, 5.29E-5, 88.34, 8.9)
Lu_177_g_e = [112.95, 208.37]
Lu_177_b_r = [6.4, 11]
Lutetium_177 = Isotope("Lu", 71, 177, 581818, 1.19E-6, Lu_177_g_e, Lu_176_b_r)

Mg_27_g_e = [843.74, 1014.42]
Mg_27_b_r = [71.8, 28]
Magnesium_27 = Isotope("Mg", 12, 27, 567.6, 0.00122, Mg_27_g_e, Mg_27_b_r)

Manganese_54 = Isotope("Mn", 25, 54, 2.7E+7, 2.57E-8, 834.848, 99.976)
Mn_56_g_e = [846.77, 1820.77, 2113.123]
Mn_56_b_r = [98.9, 27.2, 14.3]
Manganese_56 = Isotope("Mn", 25, 56, 9280.8, 7.47E-5, Mn_56_g_e, Mn_56_b_r)

Md_258_g_e = [71.1, 276.8, 296.7, 367.8, 447.9]
Md_258_b_r = [8, 20.2, 5.4, 100, 37]
Mendelevium_258 = Isotope("Md", 101, 258, 4.45E+6, 1.56E-7, Md_258_g_e,
                          Md_258_b_r)

Hg_195_g_e = [61.46, 180.11, 585.13, 779.8, 1111.04]
Hg_195_b_r = [6.2, 1.9, 1.99, 7, 1.44]
Mercury_195 = Isotope("Hg", 80, 195, 35640, 1.94E-5, Hg_195_g_e, Hg_195_b_r)
Hg_197_g_e = [77.351, 191.437]
Hg_197_b_r = [18.7, 0.0632]
Mercury_197 = Isotope("Hg", 80, 197, 230904, 3.0E-6, Hg_197_g_e, Hg_197_b_r)
Hg_197m_g_e = [130.2, 133.99, 279.01]
Hg_197m_b_r = [0.273, 33, 6]
Mercury_197m = Isotope("Hg", 80, 197, 85680, 8.1E-6, Hg_197m_g_e, Hg_197m_b_r)
Hg_199m_g_e = [158.38, 374.1]
Hg_199m_b_r = [52, 13.8]
Mercury_199m = Isotope("Hg", 80, 199, 2856, 2.43E-4, Hg_199m_g_e, Hg_199m_b_r)
Mercury_203 = Isotope("Hg", 80, 203, 4.03E+6, 1.72E-7, 279.197, 81)
Mercury_205 = Isotope("Hg", 80, 205, 312, 0.0022, 203.75, 2.2)

Mo_93m_g_e = [263.06, 684.67, 1477.13]
Mo_93m_b_r = [56.7, 99.7, 99.1]
Molybdenum_93m = Isotope("Mo", 42, 93, 24660, 2.81E-5, Mo_93m_g_e, Mo_93m_b_r)
Mo_99_g_e = [140.51, 181.06, 739.5, 777.92]
Mo_99_b_r = [89.43, 5.99, 12.13, 4.26]
Molybdenum_99 = Isotope("Mo", 42, 99, 237384, 2.92E-6, Mo_99_g_e, Mo_99_b_r)
Mo_101_g_e = [191.92, 195.93, 408.7, 505.92, 590.1, 695.56, 1012.5]
Mo_101_b_r = [18, 2.77, 1.53, 11.62, 19.2, 6.66, 13]
Molybdenum_101 = Isotope("Mo", 42, 101, 876.6, 2.92E-6, Mo_101_g_e, Mo_101_b_r)

Nd_147_g_e = [91.11, 319.41, 439.9, 531.02]
Nd_147_b_r = [28, 1.95, 1.2, 13.1]
Neodymium_147 = Isotope("Nd", 60, 147, 9.5E+5, 7.3E-7, Nd_147_g_e, Nd_147_b_r)
Nd_151_g_e = [116.8, 138.9, 175.07, 255.68, 423.56, 736.23, 1180.9]
Nd_151_b_r = [39, 7.05, 6.33, 14.8, 5.92, 5.92, 13.3]
Neodymium_151 = Isotope("Nd", 60, 151, 746.4, 9.3E-4, Nd_151_g_e, Nd_151_b_r)

Neon_23 = Isotope("Ne", 10, 23, 37.24, 0.0186, 439.99, 33)

Np_238_g_e = [923.98, 984.45, 1025.87, 1028.54]
Np_238_b_r = [2.86, 27.8, 9.6, 20.3]
Neptunium_238 = Isotope("Np", 93, 238, 182909, 3.79E-6, Np_238_g_e, Np_238_b_r)

Ni_65_g_e = [366.27, 1115.55, 1481.84, 1623.41]
Ni_65_b_r = [4.81, 15.43, 24, 0.498]
Nickel_65 = Isotope('Ni', 28, 65, 9061, 7.65E-5, Ni_65_g_e, Ni_65_b_r)

Nb_92_g_e = [561.03, 934.46]
Nb_92_b_r = [100, 100]
Niobium_92 = Isotope("Nb", 41, 92, 1.09E+15, 6.33E-16, Nb_92_g_e, Nb_92_b_r)
Nb_92m_g_e = [912.73, 934.46]
Nb_92m_b_r = [1.78, 99]
Niobium_92m = Isotope("Nb", 41, 92, 876960, 7.9E-7, Nb_92m_g_e, Nb_92m_b_r)
Nb_94_g_e = [702.622, 871.09]
Nb_94_b_r = [97.9, 100]
Niobium_94 = Isotope("Nb", 41, 94, 6.4E+11, 1.08E-12, Nb_94_g_e, Nb_94_b_r)
Niobium_94m = Isotope("Nb", 41, 94, 375.78, 1.84E-3, 871.09, 0.5)
Niobium_95 = Isotope("Nb", 41, 95, 3.02E+6, 2.29E-7, 765.79, 100)
Nb_95m_g_e = [204.12, 235.7]
Nb_95m_b_r = [2.33, 24.9]
Niobium_95m = Isotope("Nb", 41, 95, 311760, 2.22E-6, Nb_95m_g_e, Nb_95m_b_r)

Os_185_g_e = [592.07, 646.12, 717.32, 874.81, 880.52]
Os_185_b_r = [1.318, 78, 3.94, 6.29, 5.17]
Osmium_185 = Isotope("Os", 76, 185, 8.09E+6, 8.57E-8, Os_185_g_e, Os_185_b_r)
Osmium_186 = Isotope("Os", 76, 186, 6.3E+22, 1.1E-23, 2757.7, 100)
Os_190m_g_e = [186.72, 361.14, 502.53, 616.08]
Os_190m_b_r = [70.2, 94.88, 97.79, 98.62]
Osmium_190m = Isotope("Os", 76, 190, 594, 0.0012, Os_190m_g_e, Os_190m_b_r)
Osmium_191 = Isotope("Os", 76, 191, 1.33E+6, 5.21E-7, 129.41, 29)
Os_193_g_e = [138.94, 280.47, 460.55, 557.43]
Os_193_b_r = [4.27, 1.24, 3.95, 1.3]
Osmium_193 = Isotope("Os", 76, 193, 108396, 6.39E-6, Os_193_g_e, Os_193_b_r)

Pd_109_g_e = [311.4, 415.2, 636.3, 647.3, 781.4]
Pd_109_b_r = [0.032, 0.0107, 0.01, 0.024, 0.011]
Palladium_109 = Isotope("Pd", 46, 109, 49320, 1.47E-5, Pd_109_g_e, Pd_109_b_r)
Palladium_109m = Isotope("Pd", 46, 109, 282, 0.00246, 188.99, 55.9)
Pd_111m_g_e = [172.18, 391.28, 632.76]
Pd_111m_b_r = [34, 1.53, 1.01]
Palladium_111m = Isotope("Pd", 46, 111, 19800, 3.5E-5, Pd_111m_g_e,
                         Pd_111m_b_r)

Pt_191_g_e = [172.18, 351.21, 359.9, 409.44, 538.9]
Pt_191_b_r = [3.52, 3.36, 6, 8, 13.7]
Platinum_191 = Isotope("Pt", 78, 191, 2.42E+5, 2.86E-6, Pt_191_g_e, Pt_191_b_r)
Pt_197_g_e = [77.355, 191.44]
Pt_197_b_r = [17, 3.7]
Platinum_197 = Isotope("Pt", 78, 197, 71604, 9.7E-6, Pt_197_g_e, Pt_191_b_r)
Pt_197m_g_e = [279.01, 346.5]
Pt_197m_b_r = [2.4, 11.1]
Platinum_197m = Isotope("Pt", 78, 197, 5724.6, 1.2E-4, Pt_197m_g_e, Pt_197_b_r)
Pt_199_g_e = [185.77, 317.06, 493.77, 542.99, 714.58]
Pt_199_b_r = [3.32, 4.95, 5.6, 15, 1.84]
Platinum_199 = Isotope("Pt", 78, 199, 1848, 3.8E-4, Pt_199_g_e, Pt_199_b_r)

Pu_243_g_e = [84, 109.2, 356.4, 381.7]
Pu_243_b_r = [23, 0.161, 0.133, 0.56]
Plutonium_243 = Isotope("Pu", 94, 243, 17842, 3.9E-5, Pu_243_g_e, Pu_243_b_r)
Pu_245_g_e = [308.22, 327.43, 376.68, 491.6, 560.13, 630.1, 800, 910.5, 987.6]
Pu_245_b_r = [4.9, 25.4, 3.2, 2.7, 5.4, 2.7, 1.57, 1.39, 1.32]
Plutonium_245 = Isotope("Pu", 94, 245, 37800, 1.81E-5, Pu_245_g_e, Pu_245_b_r)

Potassium_40 = Isotope("K", 19, 40, 4.02E+16, 1.72E-17, [1460.83], [11])
Potassium_42 = Isotope("K", 19, 42, 44496, 1.56E-5, 1524.7, 18)

Praseodymium_142 = Isotope("Pr", 59, 142, 68832, 1.01E-5, 1575.85, 3.7)

Pm_146_g_e = [453.88, 633.08, 735.72, 747.16]
Pm_146_b_r = [65, 2.15, 22.5, 34]
Promethium_146 = Isotope("Pm", 61, 146, 1.74E8, 4E-9, Pm_146_g_e, Pm_146_b_r)
Pm_151_g_e = [167.75, 177.2, 240.1, 275.2, 340.1, 445.68, 717.72]
Pm_151_b_r = [8.3, 3.82, 3.82, 6.8, 23, 4, 4.05]
Promethium_151 = ("Pm", 61, 151, 102240, 6.78E-6, Pm_151_g_e, Pm_151_b_r)

Pa_232_g_e = [150.1, 387.9, 453.7, 515.6, 581.4, 819.2, 866.8, 894.35, 969.3]
Pa_232_b_r = [10.8, 7, 8.61, 5.52, 6, 7.45, 5.81, 19.8, 41.6]
Protactinium_232 = Isotope("Pa", 91, 232, 78453, 6E-6, Pa_232_g_e, Pa_232_b_r)
Pa_234_g_e = [1131.3, 152.72, 227.25, 569.5, 733.4, 880.5, 883.24, 946]
Pa_234_b_r = [18, 6, 5.8, 8.2, 6.9, 6, 9.6, 13.4]
Proactinium_234 = Isotope("Pa", 91, 234, 24120, 2.9E-5, Pa_234_g_e, Pa_234_b_r)

Radium_226 = Isotope("Ra", 88, 226, 5.05E+10, 1.37E-11, 186.21, 3.59)
Ra_227_g_e = [283.7, 300.1, 302.7, 330.1, 407.8, 487]
Ra_227_b_r = [3.1, 4.6, 4.2, 2.7, 2.2, 2.3]
Radium_227 = Isotope("Ra", 88, 227, 2532, 2.7E-4, Ra_227_g_e, Ra_227_b_r)

Radon_222 = Isotope("Rn", 86, 222, 330307.2, 2.1E-6, 511, 0.076)
Rn_223_g_e = [140.9, 416, 491.4, 547, 591.8, 635.2, 648.7, 645]
Rn_223_b_r = [26, 55, 19, 20, 100, 76, 29, 44]
Radon_223 = Isotope("Rn", 86, 223, 1932, 3.6E-4, Rn_223_g_e, Rn_223_b_r)

Rhenium_186 = Isotope("Re", 75, 186, 321261, 2.16E-6, 137.16, 9.42)
Rhenium_188 = Isotope("Re", 75, 188, 61200, 1.13E-05, 155.032, 15.1)
Rhenium_188m = Isotope("Re", 75, 188, 1116, 6.2E-4, 105.87, 10.8)

Rb_82m_g_e = [554.35, 619.11, 698.37, 776.52, 827.83, 1044, 1317.47, 1474.9]
Rb_82m_b_r = [62.4, 37.98, 26.3, 84, 21, 32.1, 23, 15.53]
Rubidium_82m = Isotope("Rb", 37, 82, 23299, 3E-5, Rb_82m_g_e, Rb_82m_b_r)
Rubidium_86 = Isotope("Rb", 37, 86, 1.61E+6, 4.3E-7, 1076.64, 9)
Rubidium_86m = Isotope("Rb", 37, 86, 61.02, 0.011, 556.1, 98)
Rb_88_g_e = [898.042, 1836.063, 2677.892]
Rb_88_b_r = [14.04, 21.4, 1.96]
Rubidium_88 = Isotope("Rb", 37, 88, 1066.88, 6.5E-4, Rb_88_g_e, Rb_88_b_r)

Ru_97_g_e = [215.72, 324.48, 569.31]
Ru_97_b_r = [86, 10.79, 0.863]
Ruthenium_97 = Isotope("Ru", 44, 97, 2.5E+5, 2.77E-6, Ru_97_g_e, Ru_97_b_r)
Ru_103_g_e = [443.8, 497.1, 610.33]
Ru_103_b_r = [3.27, 90.9, 5.75]
Ruthenium_103 = Isotope("Ru", 44, 103, 3.4E+6, 2E-7, Ru_103_g_e, Ru_103_b_r)
Ru_105_g_e = [129.78, 262.83, 316.44, 469.37, 676.36, 724.21]
Ru_105_b_r = [5.68, 6.57, 11.1, 17.5, 15.7, 47]
Ruthenium_105 = Isotope("Ru", 44, 105, 15984, 4.3E-5, Ru_105_g_e, Ru_105_b_r)

Sm_153_g_e = [69.67, 103.18]
Sm_153_b_r = [4.85, 30]
Samarium_153 = Isotope("Sm", 62, 153, 1.65E+5, 4.16E-6, Sm_153_g_e, Sm_153_b_r)
Sm_155_g_e = [104.33, 141.44, 245.77]
Sm_155_b_r = [74.6, 1.98, 3.7]
Samarium_155 = Isotope("Sm", 62, 155, 1338, 5.2E-4, Sm_155_g_e, Sm_155_b_r)

Sc_46_g_e = [889.28, 1120.55]
Sc_46_b_r = [99.98, 99.98]
Scandium_46 = Isotope("Sc", 21, 46, 7.24E+6, 9.57E-8, Sc_46_g_e, Sc_46_b_r)

Se_75_g_e = [121.12, 136, 264.66, 279.54, 400.66]
Se_75_b_r = [17.2, 58.3, 58.9, 25, 11.47]
Selenium_75 = Isotope("Se", 34, 75, 1.03E+7, 6.7E-8, Se_75_g_e, Se_75_b_r)
Se_83_g_e = [224.8, 356.69, 510.17, 718.1, 799.1, 836.52, 866.9, 1064.11, 1299]
Se_83_b_r = [32.7, 70, 43, 15, 14.8, 13, 8.2, 5.5, 5.3]
Selenium_83 = Isotope("Se", 34, 83, 1338, 5.2E-4, Se_83_g_e, Se_83_b_r)

Silicon_31 = Isotope("Si", 14, 31, 9438, 7.34E-5, 1266.12, 0.07)

Ag_108_g_e = [433.94, 618.84, 632.97]
Ag_108_b_r = [0.5, 0.261, 1.76]
Silver_108 = Isotope("Ag", 47, 108, 139.2, 0.005, Ag_108_g_e, Ag_108_b_r)
Ag_108m_g_e = [79.138, 433.84, 614.28, 722.91]
Ag_108m_b_r = [6.63, 90, 89.8, 90.8]
Silver_108m = Isotope("Ag", 47, 108, 1.3E+10, 5E-11, Ag_108m_g_e, Ag_108m_b_r)
Ag_110m_g_e = [657.76, 677.62, 687.01, 706.68, 763.94, 884.69, 937.49, 1384.3]
Ag_110m_b_r = [94, 10.28, 6.39, 16.33, 22.14, 72.2, 34.13, 24.12]
Silver_110m = Isotope("Ag", 47, 110, 2.16E+7, 3.2E-8, Ag_110m_g_e, Ag_110m_b_r)

Na_24_g_e = [1368.63, 2754.03]
Na_24_b_r = [100, 99.94]
Sodium_24 = Isotope("Na", 11, 24, 53856, 1.29E-5, Na_24_g_e, Na_24_b_r)

Strontium_85 = Isotope("Sr", 38, 85, 5.6E+6, 1.24E-7, 514.01, 96)
Sr_85m_g_e = [151.16, 231.67]
Sr_85m_b_r = [12.9, 84.4]
Strontium_85m = Isotope("Sr", 38, 85, 4057.8, 1.7E-4, Sr_85m_g_e, Sr_85m_b_r)
Strontium_87m = Isotope("Sr", 38, 87, 10080, 6.88E-5, 388.53, 81.9)
Strontium_89 = Isotope("Sr", 38, 89, 4.37E+6, 1.59E-7, 908.96, 0.01)
Sr_91_g_e = [620.1, 652.9, 749.8, 925.8, 1024.3]
Sr_91_b_r = [1.77, 8, 23.61, 3.84, 33]
Strontium_91 = Isotope("Sr", 38, 91, 34668, 2E-5, Sr_91_g_e, Sr_91_b_r)

Sulfur_37 = Isotope("S", 16, 37, 303, 2.29E-3, 3103.4, 94)

Ta_182_g_e = [100.11, 152.43, 222.11, 1121.3, 1189.1, 1221.41, 1231.02]
Ta_182_b_r = [14.1, 6.93, 7.49, 34.5, 16.23, 26.98, 11.22]
Tantalum_182 = Isotope("Ta", 73, 182, 9.89E+6, 7.01E-8, Ta_182_g_e, Ta_182_b_r)
Ta_182m2_g_e = [146.78, 171.58, 184.95, 318.36]
Ta_182m2_b_r = [37.2, 49, 24.5, 6.9]
Tantalum_182m2 = Isotope("Ta", 73, 182, 950, 7E-4, Ta_182m2_g_e, Ta_182m2_b_r)
Ta_183_g_e = [99.1, 107.93, 161.35, 244.26, 246.1, 353.99]
Ta_183_b_r = [6.7, 11, 8.9, 8.5, 27, 11.2]
Tantalum_183 = Isotope("Ta", 73, 183, 440640, 1.6E-6, Ta_183_g_e, Ta_183_b_r)

Tc_98_g_e = [652.43, 745.36]
Tc_98_b_r = [100, 102]
Technetium_98 = Isotope("Tc", 43, 98, 1.32E+14, 5.2E-15, Tc_98_g_e, Tc_98_b_r)
Technetium_99m = Isotope("Tc", 43, 99, 21960, 3.2E-5, Tc_98_g_e, Tc_98_b_r)

Te_121_g_e = [470.47, 507.6, 573.14]
Te_121_b_r = [1.41, 17.7, 80.3]
Tellurium_121 = Isotope("Te", 52, 121, 1.45E+6, 4.8E-7, Te_121_g_e, Te_121_b_r)
Te_121m_g_e = [212.19, 1102.15]
Te_121m_b_r = [81, 2.54]
Tellurium_121m = Isotope("Te", 52, 121, 1.3E+7, 5E-8, Te_121m_g_e, Te_121m_b_r)
Tellerium_123m = Isotope("Te", 52, 123, 1.03E+7, 6.7E-8, 159, 84)
Tellerium_127 = Isotope("Te", 52, 127, 33660, 2.1E-5, 417.95, 1)
Te_131_g_e = [149.72, 452.32, 492.66, 602.04, 997.25, 1146.96]
Te_131_b_r = [69, 18.18, 4.83, 4.2, 3.33, 4.95]
Tellerium_131 = Isotope("Te", 52, 131, 1500, 4.6E-4, Te_131_g_e, Te_131_b_r)

Tb_160_g_e = [197.04, 298.58, 879.38, 962.32, 966.17, 1177.96, 1271.88]
Tb_160_b_r = [5.18, 26.13, 30.1, 9.81, 25.1, 14.87, 7.44]
Terbium_160 = Isotope("Tb", 65, 160, 6.26E+6, 1.11E-7, Tb_160_g_e, Tb_160_b_r)

Tl_206m_g_e = [216.32, 247.2, 265.83, 453.28, 457.2, 564.2, 686.3, 1021.5]
Tl_206m_b_r = [74, 8.6, 86, 93, 22, 5.2, 90, 69]
Thallium_206m = Isotope("Tl", 81, 206, 224.4, 3.1E-3, Tl_206m_g_e, Tl_206m_b_r)

Tl_208_g_e = [583.19, 2614.51]
Tl_208_b_r = [30.6, 35.9]
Thallium_208 = Isotope("Tl", 81, 208, 183.18, 0.003784, Tl_208_g_e, Tl_208_b_r)

Th_233_g_e = [86.48, 169.16, 459.22, 669.9, 890.1]
Th_233_b_r = [2.7, 0.34, 1.4, 0.68, 0.14]
Thorium_233 = Isotope("Th", 90, 233, 1338, 5.2E-4, Th_233_g_e, Th_233_b_r)

Thorium_234 = Isotope("Th", 90, 234, 2.08E6, 3.33E-7, [92.58], [5.58])

Thulium_170 = Isotope("Tm", 69, 170, 1.1E+7, 6.23E-8, 84.25, 2.5)
Tm_172_g_e = [181.53, 912.13, 1093.66, 1387.1, 1465.9, 1529.7, 1608.6]
Tm_172_b_r = [2.75, 1.42, 6, 5.6, 4.5, 5.1, 4.14]
Thulium_172 = Isotope("Tm", 69, 172, 228960, 3E-6, Tm_172_g_e, Tm_172_b_r)

Sn_113_g_e = [255.05, 391.7]
Sn_113_b_r = [1.82, 64]
Tin_113 = Isotope("Sn", 50, 113, 9.9E+6, 6.97E-8, Sn_113_g_e, Sn_113_b_r)
Sn_117m_g_e = [156.02, 158.56]
Sn_117m_b_r = [2.11, 86]
Tin_117m = Isotope("Sn", 50, 117, 1.2E+6, 5.9E-7, Sn_117m_g_e, Sn_117m_b_r)
Tin_123 = Isotope("Sn", 50, 123, 1.12E+7, 6.21E-8, 1088.64, 0.6)
Tin_123m = Isotope("Sn", 50, 123, 2403.6, 2.9E-4, 160.33, 86)
Sn_125_g_e = [332.1, 469.9, 822.5, 915.6, 1067.1, 1089.2, 2002.15]
Sn_125_b_r = [1.41, 1.48, 4.28, 4.13, 10, 4.6, 1.92]
Tin_125 = Isotope("Sn", 50, 125, 832896, 8.32E-7, Sn_125_g_e, Sn_125_b_r)
Tin_125m = Isotope("Sn", 50, 125, 571.2, 0.0012, 332.1, 97.2)
Sn_127_g_e = [119.7, 169.2, 262.5, 284.3, 438.2, 491, 806, 823, 1095.6, 1114.3]
Sn_127_b_r = [2.21, 2.06, 2.37, 2.7, 6.2, 5.4, 8.4, 11, 20, 39]
Tin_127 = Isotope("Sn", 50, 127, 7560, 9.2E-5, Sn_127_g_e, Sn_127_b_r)
Sn_127m_g_e = [490.9, 1348, 1564]
Sn_127m_b_r = [90, 4.8, 4]
Tin_127m = Isotope("Sn", 50, 127, 247.8, 2.8E-3, Sn_127_g_e, Sn_127_b_r)

Ti_44_g_e = [67.88, 78.34]
Ti_44_b_r = [94.4, 96]
Titanium_44 = Isotope("Ti", 22, 44, 1.99E+9, 3.5E-10, Ti_44_g_e, Ti_44_b_r)
Ti_51_g_e = [320.08, 608.6, 928.6]
Ti_51_b_r = [93, 1.18, 6.9]
Titanium_51 = Isotope("Ti", 22, 51, 345.6, 2E-3, Ti_51_g_e, Ti_51_b_r)

W_181_g_e = [136.27, 152.32]
W_181_b_r = [0.0311, 0.0083]
Tungsten_181 = Isotope("W", 74, 181, 1.04E+7, 6.62E-8, W_181_g_e, W_181_b_r)
Tungsten_185 = Isotope("W", 74, 185, 6.48E+6, 1.1E-7, 125.36, 0.019)
W_187_g_e = [72, 134.24, 479.53, 551.53, 618.36, 685.77, 772.9]
W_187_b_r = [11.14, 8.85, 21.8, 5.08, 6.28, 27.3, 4.12]
Tungsten_187 = Isotope("W", 74, 187, 85392, 8.11E-6, W_187_g_e, W_187_b_r)

Uranium_234 = Isotope("U", 92, 234, 7.71E+12, 9E-14, 120.9, 0.0342)
U_235_g_e = [109.2, 143.76, 163.36, 185.71, 205.31]
U_235_b_r = [1.54, 10.96, 5.08, 57.2, 5.01]
Uranium_235 = Isotope("U", 92, 235, 2.22E+16, 3.123E-17, U_235_g_e, U_235_b_r)
U_237_g_e = [59.54, 208, 332.36]
U_237_b_r = [34.5, 21.2, 1.2]
Uranium_237 = Isotope("U", 92, 237, 583200, 1.19E-6, U_237_g_e, U_237_b_r)
U_239_g_e = [43.53, 74.66]
U_239_b_r = [4.14, 48]
Uranium_239 = Isotope("U", 92, 239, 1407, 4.9E-4, U_239_g_e, U_239_b_r)

Vanadium_52 = Isotope("V", 23, 52, 224.1, 3.1E-3, 1434.07, 100)

Xe_125_g_e = [54.97, 188.42, 453.8]
Xe_125_b_r = [6.81, 54, 4.7]
Xenon_125 = Isotope("Xe", 54, 125, 60840, 1.14E-5, Xe_125_g_e, Xe_125_b_r)
Xe_127_g_e = [145.25, 172.13, 202.9, 375]
Xe_127_b_r = [4.29, 25.5, 68, 17.2]
Xenon_127 = Isotope("Xe", 54, 127, 3.14E+6, 2.2E-7, Xe_127_g_e, Xe_127_b_r)
Xe_129m_g_e = [39.58, 196.6]
Xe_129m_b_r = [7.5, 4.6]
Xenon_129m = Isotope("Xe", 54, 129, 767232, 9E-7, Xe_129m_g_e, Xe_129m_b_r)
Xenon_131m = Isotope("Xe", 54, 131, 1.02E+6, 6.78E-7, 163.93, 1.91)
Xenon_133 = Isotope("Xe", 54, 133, 452217, 1.53E-6, 81, 38)
Xenon_133m = Isotope("Xe", 54, 133, 189216, 3.66E-6, 233.22, 10)
Xe_135_g_e = [249.77, 608.15]
Xe_135_b_r = [90, 2.9]
Xenon_135 = Isotope("Xe", 54, 135, 32904, 2.1E-5, Xe_135_g_e, Xe_135_b_r)
Xenon_135m = Isotope("Xe", 54, 135, 917.4, 7.56E-4, 526.56, 80.5)
Xenon_137 = Isotope("Xe", 54, 137, 229.1, 3.03E-3, 455.5, 31)

Yb_169_g_e = [63.12, 93.62, 109.8, 130.52, 197.96, 307.74]
Yb_169_b_r = [44.2, 2.61, 17.5, 11.31, 35.8, 10.1]
Ytterbium_169 = Isotope("Yb", 70, 169, 2.77E+6, 2.5E-7, Yb_169_g_e, Yb_169_b_r)
Yb_175_g_e = [113.81, 282.52, 396.33]
Yb_175_b_r = [1.88, 3, 6.4]
Ytterbium_175 = Isotope("Yb", 70, 175, 361584, 1.92E-6, Yb_175_g_e, Yb_175_b_r)
Yb_177_g_e = [121.62, 150.39, 1080.2, 1241.2]
Yb_177_b_r = [3.42, 20.3, 5.6, 3.47]
Ytterbium_177 = Isotope("Yb", 70, 177, 6879.6, 1E-4, Yb_177_g_e, Yb_177_b_r)

Y_90m_g_e = [202.51, 479.17, 681.8, 2319.97]
Y_90m_b_r = [97.3, 90.74, 0.32, 0.0018]
Yttrium_90m = Isotope("Y", 39, 90, 11484, 6E-5, Y_90m_g_e, Y_90m_b_r)

Zinc_65 = Isotope("Zn", 30, 65, 2.11E+7, 3.28E-8, 1115.55, 50.6)
Zinc_69m = Isotope("Zn", 30, 69, 49536, 1.4E-5, 438.63, 94.77)
Zn_71_g_e = [121.5, 389.88, 511.56, 910.27, 1119.7]
Zn_71_b_r = [3, 3.8, 32, 7.8, 2.18]
Zinc_71 = Isotope("Zn", 30, 71, 147, 0.0047, Zn_71_g_e, Zn_71_b_r)
Zn_71m_g_e = [142.6, 386.28, 487.4, 511.6, 596.14, 620.2, 964.64, 1107.5]
Zn_71m_b_r = [5.6, 93, 62, 28.4, 27.9, 57, 4.3, 2]
Zinc_71m = Isotope("Zn", 30, 71, 14256, 4.86E-5, Zn_71m_g_e, Zn_71m_b_r)

Zr_95_g_e = [724.2, 756.73]
Zr_95_b_r = [44.2, 54]
Zirconium_95 = Isotope("Zr", 40, 95, 5.5E+6, 1.25E-7, Zr_95_g_e, Zr_95_b_r)
Zr_97_g_e = [254.2, 355.4, 507.64, 743.36, 1147.97]
Zr_97_b_r = [1.14, 2.1, 5.03, 93, 2.61]
Zirconium_97 = Isotope("Zr", 40, 97, 60876, 1.13E-05, Zr_97_g_e, Zr_97_b_r)
